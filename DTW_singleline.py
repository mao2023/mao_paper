# -*- coding: UTF-8 -*-
# from dtw import dtw
import numpy as np
import math
import pandas as pd


def dis_abs(x, y):
    dis = math.sqrt(sum([(a - b)**2 for (a,b) in zip(x,y)])) 
    return dis

def estimate_twf(A,B,dis_func=dis_abs):
    
    N_A = len(A)
    N_B = len(B)
    D = np.zeros([N_A,N_B])
    D[0,0] = dis_func(A[0],B[0])
    
    # 
    for i in range(1,N_A):
        D[i,0] = D[i-1,0]+dis_func(A[i],B[0])
    # 
    for j in range(1,N_B):
        D[0,j] = D[0,j-1]+dis_func(A[0],B[j])
    # 
    for i in range(1,N_A):
        for j in range(1,N_B):        
            D[i,j] = dis_func(A[i],B[j])+min(D[i-1,j],D[i,j-1],D[i-1,j-1])
            

    i = 0  
    j = 0  
    count =0
    d = np.zeros(max(N_A,N_B)*3)
    path = []
    path.append((0,0))
    while True:
        if i<(N_A-1) and j<(N_B-1):
            m = min(D[i+1, j],D[i, j+1],D[i+1,j+1])
            if m == D[i+1,j+1]:
                d[count] = D[i+1,j+1]-D[i,j]
                i = i+1
                j = j+1
                count = count+1
                path.append((i,j))
                
            elif m == D[i,j+1]:
                d[count] = D[i,j+1] - D[i,j]
                j = j+1
                count = count+1
                path.append((i,j))
    
            elif m == D[i+1, j]:
                d[count] = D[i+1,j] - D[i,j]
                i = i+1 
                count = count+1
                path.append((i,j))
                   
        elif i == (N_A-1) and j == (N_B-1):            
            d[count] = D[i,j]
            count = count+1
            path.append((i,j))
            break
        
        elif i == (N_A-1):
            d[count] = D[i,j+1]-D[i,j]
            j = j+1
            count = count+1
            path.append((i,j))
        
        elif j == (N_B-1): 
            d[count] = D[i+1,j] -D[i,j]
            i = i+1
            count = count+1
            path.append((i,j))    
    #mean = np.sum(d) / count
    return path,D[-1][-1],count
    
if __name__=="__main__":
        lujing_a = "G:\\vscode\\morphing\\1.13\\xls\\b.xls"
        df_a = pd.read_excel(lujing_a, usecols=[0,1],names=None)  # coordinate, usecols=[0,1]
        a = df_a.values.tolist()
        
        lujing_b = "G:\\vscode\\morphing\\1.13\\xls\\a.xls"
        df_b = pd.read_excel(lujing_b, usecols=[0,1],names=None)  # coordinate, usecols=[0,1]
        b = df_b.values.tolist()

        path,dtw,count = estimate_twf(a,b,dis_func=dis_abs)     
        print(dtw)  #dtw_distance
        print(count) #k
        print(path)  #warping path
        
        
