import pandas as pd
from tqdm import tqdm

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

def get_views(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['views']

def get_mature(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['mature']

def get_life_time(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['life_time']

def get_created_time(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['created_at']

def get_updated_time(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['updated_at']

def get_dead_account(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['dead_account']

def get_language(info,node):
    '''
    获取节点 node 属性
    '''
    return info[node]['language']

def get_link(info,node):
    '''
    获取节点 node 属性
    '''
    if 'link' in info[node]:
        return info[node]['link']
    else:
        return {'NONE',}

def print_mode(info,node):
    '''
    显示节点全部信息（利用 format 或者 f 函数）
    '''
    print('------------------------------------')
    if 'link' in info[node]:
        print('numeric_id: {}\nviews: {}\nmature: {}\nlife_time: {}\ncreated_at: {}\nupdated_at: {}\ndead_account: {}\nlanguage: {}\nlink: {}'.format(info[node]['numeric_id'],info[node]['views'],info[node]['mature'],info[node]['life_time'],info[node]['created_at'],info[node]['updated_at'],info[node]['dead_account'],info[node]['language'],info[node]['link']))
    else:
        print('numeric_id: {}\nviews: {}\nmature: {}\nlife_time: {}\ncreated_at: {}\nupdated_at: {}\ndead_account: {}\nlanguage: {}\nlink: NONE'.format(info[node]['numeric_id'],info[node]['views'],info[node]['mature'],info[node]['life_time'],info[node]['created_at'],info[node]['updated_at'],info[node]['dead_account'],info[node]['language']))
    print('------------------------------------')

def main():
    '''
    测试函数
    '''
    info_path='D:\Project\Python\week4module\large_twitch_features.csv'
    edge_path='D:\Project\Python\week4module\large_twitch_edges1.csv'
    ID=200
    info=init_node(info_path,edge_path)
    print('numeric_id: ',ID)
    print('views: ',get_views(info,ID))
    print('mature: ',get_mature(info,ID))
    print('life_time: ',get_life_time(info,ID))
    print('created_at: ',get_created_time(info,ID))
    print('updated_at: ',get_updated_time(info,ID))
    print('dead_account: ',get_dead_account(info,ID))
    print('language: ',get_language(info,ID))
    print('link: ',get_link(info,ID))
    print()
    ID=700
    print('numeric_id: ',ID)
    print('views: ',get_views(info,ID))
    print('mature: ',get_mature(info,ID))
    print('life_time: ',get_life_time(info,ID))
    print('created_at: ',get_created_time(info,ID))
    print('updated_at: ',get_updated_time(info,ID))
    print('dead_account: ',get_dead_account(info,ID))
    print('language: ',get_language(info,ID))
    print('link: ',get_link(info,ID))

if __name__=='__main__':main()