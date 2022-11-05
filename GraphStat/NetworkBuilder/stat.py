from tqdm import tqdm
import pickle

def get_node_number(node_info):
    '''
    计算节点数
    '''
    node=set()
    for each in tqdm(node_info,desc='getting node_number...'):
        node.add(each)
        if 'link' in node_info[each]:
            node.add(link for link in node_info[each]['link'])
    return len(node)

def get_edge_number(node_info):
    '''
    计算边数
    '''
    edge=set()
    for each in tqdm(node_info,desc='getting edge_number...'):
        if 'link' in node_info[each]['link']:
            for link in node_info[each]['link']:
                edge.add(set(each,link))
        else:
            continue
    return len(edge)

def cal_average_dgree(node_info):
    '''
    计算网络中的平均度
    '''
    dgrees=0
    node_number=0
    for each in tqdm(node_info,desc='calculating average_dgree...'):
        if 'link' in node_info[each]:
            dgrees+=len(node_info[each]['link'])
        node_number+=1
    return dgrees/node_number

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

def cal_attr_distribution(node_info,attr):
    '''
    计算attr属性的分布
    返回attr与频数的字典
    '''
    v={}
    for each in node_info:
        if node_info[each][attr] not in v:
            v.update({node_info[each][attr]:1})
        else:
            v[node_info[each][attr]]+=1
    return v

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
    print('node_number: ')
    print(get_node_number(node))
    print('edge_number: ')
    print(get_edge_number(node))
    print('average_degree: ')
    print(cal_average_dgree(node))
    print('degree_distribution: ')
    print(cal_dgree_distribution(node))
    print('views_distribution: ')
    print(cal_attr_distribution(node,'views'))



if __name__=='__main__':
    main()