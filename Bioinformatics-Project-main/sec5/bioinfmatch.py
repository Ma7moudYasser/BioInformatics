# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:37:21 2022

@author: Mohamed Elhakim
"""
import numpy as np
import bisect

def IndexSorted(seq,ln):
    index = []
    for i in range(len(seq)-ln+1):
        index.append((seq[i:i+ln], i))
    index.sort() 
    return index
def query(t,p,index):
    keys = [r[0] for r in index]
    st = bisect.bisect_left(keys,p[:len(keys[0])])
    
    en = bisect.bisect(keys,p[:len(keys[0])])
    hits = index[st:en] 
    print(hits)
    l=[h[1] for h in hits ]
    offsets=[]
    for i in l:
        if t[i:i+len(p)]==p:
            offsets.append(i)
    return offsets
        













file=open("dna1.fasta")
l=[i for i in file]
t=l[1][0:-1]
p="AAG"
ln=3
# table=[]
# for i in range(len(t)-ln+1):
#     table.append([t[i:i+ln],i])
# for  i in range(len(table)):
#     if p[0:ln]==table[i][0]:
#         index=table[i][1]
#         if t[index:index+len(p)]==p:
#             print(i)
# print(t[151:151+len(p)])
index=IndexSorted(t,ln)
print(query(t,p,index))









