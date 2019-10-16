import numpy as np
import pandas as pd
import networkx as nx

import matplotlib.pyplot as plt



def transform_output_to_graph(df):
    G=nx.DiGraph()
    
    G.add_nodes_from(df['tail'])
    G.add_nodes_from(df['head'])
    
    for i in range(df.shape[0]):
        G.add_edge(df['tail'].values[i],df['head'].values[i], f=np.around(df['flow'].values[i],2))
    
    return G


def get_nodes_pos():
    pos=dict()
    pos[0]=(-1,0)
    pos[1]=(1,0)
    pos[2]=(1,-3)
    pos[3]=(2,2)
    pos[4]=(3,2)
    pos[5]=(2,-1)
    pos[6]=(3,-1)
    pos[7]=(4,-1/2)
    pos[8]=(2,-4)
    pos[9]=(-1,-3)
    pos[10]=(-2,2)
    pos[11]=(-3,2)
    pos[12]=(-2,-1)
    pos[13]=(-3,-1)
    pos[14]=(-4,-1/2)
    pos[15]=(-2,-4)
    return pos


def check_flow_balance(G):
    checksum_dict=dict()
    for n in nx.nodes(G):
        checksum=0
        for i in nx.all_neighbors(G,n):
            if G.has_edge(n,i):
                checksum+=G.get_edge_data(n,i)['f']
            if G.has_edge(i,n):
                checksum-=G.get_edge_data(i,n)['f']
        checksum_dict[n]=checksum
    return checksum_dict



def cost_path(df,paths):
    costs=[]
    for p in paths:
        c_tmp=0
        for i in range(len(p)-1):
            o=p[i]
            d=p[i+1]
            c_tmp=c_tmp+df[np.logical_and(df['tail']==o, df['head']==d)]['actualCost'].values[0]
        costs.append(c_tmp)
    return costs



def flow_on_edges(df,edges):
    flows=[]
    for e in edges:
        o = e[0]
        d = e[1]
        flows.append(df[np.logical_and(df['tail']==o, df['head']==d)]['flow'].values[0])
    return flows
        
