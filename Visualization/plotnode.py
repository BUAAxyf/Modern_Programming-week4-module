'''
绘制图中节点属性的统计结果
'''
from tqdm import tqdm
import matplotlib.pyplot as plt
import pickle

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

def plot_nodes_attr(node_info,attr) :
    '''
    （观察属性的分布形态）
    '''
    '''v=cal_attr_distribution(node_info,attr)
    x=sorted(v.keys())
    y=[v[key] for key in tqdm(x,desc='loading y...')]
    plt.bar(x,y)
    plt.xlabel(attr)
    plt.ylabel('distribution')
    plt.xlim(0,max(x))#尺度自适应
    plt.ylim(0,max(y))
    plt.show()
    return 1'''
    v=cal_attr_distribution(node_info,attr)
    x=v.keys()
    plt.hist(x,512)
    plt.xlabel(attr)
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
    plot_nodes_attr(node,'views')

if __name__=='__main__':
    main()