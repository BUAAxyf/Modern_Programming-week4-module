import pandas as pd
from tqdm import tqdm
import pickle
import os
import sys
import networkx as nx

def init_graph(node_info):
    '''
    构建网络
    '''
    G=nx.Graph()
    for each in tqdm(node_info,desc='loading node_info...'):
        if 'link' not in node_info[each]:
            continue
        for link in node_info[each]['link']:
            G.add_edge(each,link)
    return G

def save(data,file_name):
    '''
    序列化信息
    '''
    file_path=str(sys.argv[0])[:-len(os.path.basename(sys.argv[0]))]+file_name#文件路径
    f=open(file_path,'wb')
    pickle.dump(data,f,0)
    f.close
    return file_path

def load(file_path): 
    '''
    将序列化信息加载至内存
    '''
    f=open(file_path,'rb')
    data=pickle.load(f)
    f.close()
    print(file_path,' loaded √')
    return data

def init_node(info_path,edge_path):
    '''
    从数据文件中加载所有节点及其属性
    返回字典,key 为节点的 ID,值为该节点对应的各属性值(字典)
    '''
    df_info=pd.read_csv(info_path,encoding='utf8')
    node_info=df_info.to_dict(orient='index')
    df_edges=pd.read_csv(edge_path,encoding='utf8')
    for index,edge in tqdm(df_edges.iterrows(),desc='loading edges...'):
        edge1=int(edge['numeric_id_1'])
        edge2=int(edge['numeric_id_2'])
        if 'link' not in node_info[edge1]:
            node_info[edge1].update({'link':{edge2,}})
        else:
            node_info[edge1]['link'].add(edge2)
        if 'link' not in node_info[edge2]:
            node_info[edge2].update({'link':{edge1,}})
        else:
            node_info[edge2]['link'].add(edge1)
    return node_info

def main():
    '''
    测试函数
    '''
    node=load('d:/Project/Python/week4module/GraphStat/NetworkBuilder/storage_node.txt')
    graph=load('D:/Project/Python/week4module/GraphStat/NetworkBuilder/storage_graph.txt')
    print()

if __name__=='__main__': main()