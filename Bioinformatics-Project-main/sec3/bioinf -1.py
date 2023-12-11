# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:37:21 2022

@author: Mohamed Elhakim
"""
import colorama
from colorama import Fore
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
        s[i]=str(dic[seq[i]])
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
def Translation_Table(seq):
    dic = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
           "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
           "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
           "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
           "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
           "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
           "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "TAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "TAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
           "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "TGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }
    s=""
    sf=""
    flag=0
    for i in range(0,len(seq)-2,3):
        if dic[seq[i:i+3]]=="M":
            flag=1
        elif (dic[seq[i:i+3]]=="*"):
            flag=0
        if flag==1:
            s+=dic[seq[i:i+3]]
        sf+=dic[seq[i:i+3]]
    return sf,s        
s="GCCTCTGGTATGCTTCCCTGCTTGATGATTGCGGAAACCGTAACCCTACAAGGCAGGACGATGCTAGAAAAAACCAAGCAGTTTGTGGAGAATGTGACTGTGGACTATTTACAAAAAATCTGCAACTAATGTTCCGTGCCTGCCGCTGCACCCAAATCCCAAGTTTAGGGTGCG"
# print(len(s))
# print("GC Content",GC_Content(s))
# print("Reverse Complement",Reverse_Complement(s))
print(Translation_Table(s))
