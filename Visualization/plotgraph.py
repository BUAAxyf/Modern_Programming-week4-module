import networkx as nx
import matplotlib.pyplot as plt
import pickle
from tqdm import tqdm

def plot_ego(G,node):
    '''
    （附加：使用 networkx 库中的布局算法可视化结构，
    注意避免结构太大，复杂可能导致绘制失败，或者杂乱。）
    绘制节点的局部网络（找一些度大小合适的节点尝试。）
    '''
    G_neighbor=nx.ego_graph(G,node)
    nx.draw(G_neighbor,with_labels=True)
    plt.show()
    return 1

def cal_dgree_distribution(node_info):
    '''
    计算网络的度分布
    返回度与频数的字典
    '''
    dgrees={}
    for each in node_info:
        if 'link' in node_info[each]:
            dgree=len(node_info[each]['link'])
            if dgree not in dgrees:
                dgrees.update({dgree:1})
            else:
                dgrees[dgree]+=1
    return dgrees

def plotdgree_distribution(node):
    '''
    （观察度分布的形态）
    度的分布图
    '''
    dgree=cal_dgree_distribution(node)
    '''x=sorted(dgree.keys())
    y=[dgree[key] for key in tqdm(x,desc='loading y...')]
    plt.bar(x,y)
    plt.xlabel('degree')
    plt.ylabel('distribution')
    plt.xlim(0,max(x))#尺度自适应
    plt.ylim(0,max(y))
    plt.show()
    return 1'''
    x=dgree.keys()
    plt.hist(x,512)
    plt.xlabel('degree')
    plt.ylabel('distribution')
    plt.show()
    return 1


def load(file_path): 
    '''
    将网络加载至内存
    '''
    f=open(file_path,'rb')
    data=pickle.load(f)
    f.close()
    print(file_path,' loaded √')
    return data

def main():
    '''
    测试函数
    '''
    node=load('d:/Project/Python/week4module/GraphStat/NetworkBuilder/storage_node.txt')
    plotdgree_distribution(node)

if __name__=='__main__': main()