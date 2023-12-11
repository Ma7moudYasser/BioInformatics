# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:27:39 2022

@author: Mohamed Elhakim
"""
import pandas as pd
file=open("dna1.fasta")
l=[i for i in file]
seq=l[1][0:-1]
seq="ATGTGTG"
tag=3
dic={}
for i in range(0,len(seq)-tag):
    dic[seq[i:i+tag]]=dic.get(seq[i:i+tag],0)+1
  
file=open("dna2.fasta")
l=[i for i in file]
seq2=l[1][0:]
seq2="CATGTG"
dic2={}
for i in range(0,len(seq2)-tag):
    dic2[seq2[i:i+tag]]=dic2.get(seq2[i:i+tag],0)+1
k=list(dic.keys())
for i in range(len(k)):
    dic2[k[i]]=(dic2.get(k[i],0)-dic[k[i]])
d=list(dic2.values())
Sum=0
for i in range(len(d)):
    Sum+=d[i]**2
distance=Sum**(0.5)
print("distance between two dna sequences = ",distance)