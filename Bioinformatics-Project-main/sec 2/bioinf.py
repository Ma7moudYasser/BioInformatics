# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:37:21 2022

@author: Mohamed Elhakim
"""

def GC_Content(seq):
    l=len(seq)
    num_G=seq.count("G")
    num_C=seq.count("C")
    total=num_C+num_G
    return total/l
def Complement(seq):
    dic={"G":"C","C":"G","A":"T","T":"A"}
    s=list(seq)
    for i in range(len(seq)):
        s[i]=str(dic[s[i]])
    s="".join(s)
    return s
def Reverse(seq):
    s=list(seq)
    s=reversed(s)
    s="".join(s)
    return s
def Reverse_Complement(seq):
    seq=Reverse(seq)
    seq=Complement(seq)
    return seq 


file=open("dna1.fasta")
l=[i for i in file]
seq=l[1][0:-1]
l=len(seq)
count=0
for i in range(len(seq)):
    if seq[i]=="G" or seq[i]=="C":
        count+=1
print(count/l)
s=""
for i in range(len(seq)):
    s=seq[i]+s
print(s)
#print("GC Content",GC_Content(s))
# print("Reverse",Reverse(s))

# print("Reverse Complement",Reverse_Complement(s))





