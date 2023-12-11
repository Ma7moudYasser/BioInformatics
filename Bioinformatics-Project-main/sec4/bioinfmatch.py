# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:37:21 2022

@author: Mohamed Elhakim
"""
import numpy as np
import time

def match(seq,sub_seq):
    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
    return x






def Badchars(seq,sub_seq):
    table=np.zeros([4,len(sub_seq)])     
    row=["C","G","A","T"]
    for i in range (4):
        num=-1
        for j in range (len(sub_seq)):
            if row[i]==sub_seq[j]:
                table[i,j]=-1
                num=-1
            else:
                num+=1
                table[i,j]=num
    x=-1
    i=0
    while(i<len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
        else:
            for j in range(i+len(sub_seq)-1,i-1,-1):
                if seq[j] != sub_seq[int(j-i)]:
                    k=row.index(seq[j])
                    i+=table[k,j-i]
                    break
        i=int(i+1)
    return x
file=open("dna1.fasta")
l=[i for i in file]
p=l[1][0:-1]
t="GCGTCGCTGTGGAG"
print(match(p,t))
print(Badchars(p,t))





