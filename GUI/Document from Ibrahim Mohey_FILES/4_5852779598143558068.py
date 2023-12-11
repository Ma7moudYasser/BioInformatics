import tkinter
from tkinter import *
import numpy as np
import pandas as pd
import time
top = Tk()
top.config(background='blue')
top.minsize(800,800)
top.title("BIO Tool Box")

label11=Label(text="Please Enter The Sequence", bg = 'blue')
label11.pack()
label11.place(x=10,y=10)
seq_entery=Entry()
seq_entery.pack()
seq_entery.place(x=10,y=40)
def gc():
    seq=seq_entery.get()
    leng=len(seq)

    num_G=seq.count("G")
    num_C=seq.count("C")
    total=num_C+num_G

    allgc=total/leng
    lenlabe5=Label(text="the GC COUNT is" +str(allgc))
    lenlabe5.pack()
    lenlabe5.place(x=20,y=90)
but=Button(text="GC precentage" , command=gc, bg = 'yellow')
but.pack()
but.place(x=30,y=70)

###########################################################################
label11=Label(text="Please Enter The Sequence", bg = 'blue')
label11.pack()
label11.place(x=270,y=10)
com_entery=Entry()
com_entery.pack()
com_entery.place(x=270,y=40)
def Complement():
    seq=com_entery.get()
    dic={"G":"C","C":"G","A":"T","T":"A"}
    s=list(seq)
    for i in range(len(seq)):
        s[i]=str(dic[seq[i]])
    s="".join(s)
    lenlabel2=Label(text="the Compelement is" +str(s))
    lenlabel2.pack()
    lenlabel2.place(x=270,y=100)
but3=Button(text="Complement" , command=Complement, bg = 'yellow')
but3.pack()
but3.place(x=290,y=70)
#################################################
label11=Label(text="Please Enter The Sequence", bg = 'blue')
label11.pack()
label11.place(x=10,y=130)
res_entery=Entry()
res_entery.pack()
res_entery.place(x=10,y=160)
def reverse():
    seq=res_entery.get()
    s=list(seq)
    s=reversed(s)
    s="".join(s)
    lenlabe3=Label(text="the Reverse is: " +str(s))
    lenlabe3.pack()
    lenlabe3.place(x=10,y=220)
but4=Button(text="Reverse" , command=reverse , bg = 'yellow')
but4.pack()
but4.place(x=40,y=190)

#####################################################

label111=Label(text="Please Enter The Sequence", bg = 'blue')
label111.pack()
label111.place(x=10,y=130)
res_entery11=Entry()
res_entery11.pack()
res_entery11.place(x=300,y=120)

def reverseComplement():
    seq=res_entery11.get()
    seq=reverse()
    seq=Complement()
    lenlabe4=Label(text="the ReverseComplement is" + str(seq))
    lenlabe4.pack()
    lenlabe4.place(x = 200, y = 300)
    
but5=Button(text="ReverseComplement" , command=reverseComplement, bg = 'yellow')
but5.pack()
but5.place(x=300,y=150)

############################################################################
T = 'ACGACTC$'
def index():
    l=[]
    for i in range(len(T)):
        l.append(T[i:])
    l2=l.copy()
    l.sort()
    dec={}
    for i in range(len(l)):
        dec[l[i]]=i
    table=[]
    for i in range(len(l)):
        table.append([l2[i],i,dec[l2[i]]])
    
    lenlabel2=Label(text="the INDEX is" +str(table))
    lenlabel2.pack()
    lenlabel2.place(x=40,y=510)
    
but6=Button(text="Indexing" , command=index,  bg = 'silver')
but6.pack()
but6.place(x=100,y=480)
################################################################################

label1=Label(text="Please Enter The sequence", bg = 'blue')
label1.pack()
label1.place(x=10,y=260)
seq_entery=Entry()
seq_entery.pack()
seq_entery.place(x=100,y=290)

label2=Label(text="Please Enter The subsequence", bg = 'blue')
label2.pack()
label2.place(x=10,y=320)
sub_entery=Entry()
sub_entery.pack()
sub_entery.place(x=100,y=350)

def match():
    seq=seq_entery.get()
    sub_seq=sub_entery.get()
    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
    matchlabel=Label(text="the match is" +str(x))
    matchlabel.pack()
    matchlabel.place(x=20,y=410)
def Badchars():
    seq=seq_entery.get()
    sub_seq=sub_entery.get()
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
    badlabel=Label(text="the Bad character is" +str(x))
    badlabel.pack()
    badlabel.place(x=20,y=440)


but7=Button(text="match" , command=match, bg = 'yellow')
but7.pack()
but7.place(x=20,y=400)
but8=Button(text="Bad characters" , command=Badchars, bg = 'yellow')
but8.pack()
but8.place(x=150,y=400)

####################################################################
file=open("dna1.fasta")
l=[i for i in file]
seq=l[1][0:-1]
tag=10
dic={}


    
    
for i in range(0,len(seq)-tag):      
        dic[seq[i:i+tag]]=dic.get(seq[i:i+tag],0)+1

head=['TAG','Count']
df=pd.DataFrame(dic.items(),columns=head)
df.to_csv("tag.csv")

file=open("dna2.fasta")
l=[i for i in file]
seq2=l[1][0:]
dic2={}

    
    
for i in range(0,len(seq2)-tag):
        
        dic2[seq2[i:i+tag]]=dic2.get(seq2[i:i+tag],0)+1

       
       
       
    
def result():
    k=list(dic.keys())
    for i in range(len(k)):
        dic2[k[i]]=(dic2.get(k[i],0)- dic[k[i]])
    d=list(dic2.values())
    Sum=0
    for i in range(len(d)):
        Sum+=d[i]**2
    distance=float(Sum**(0.5))
    re=Label(text="the result is "+str(distance))
    re.pack()
    re.place(x=250,y=250)




btn=Button(text="Distance",command=result , bg = 'yellow')
btn.pack()
btn.place(x=300,y=200)

#######--------------smith-WaterMan Algorithm-----------############################
labelnew=Label(text="Please Enter The sequence1", bg = 'blue')
labelnew.pack()
labelnew.place(x=380,y=260)
seq_entery_new=Entry()
seq_entery_new.pack()
seq_entery_new.place(x=380,y=290)

labelnew2=Label(text="Please Enter The sequence2", bg = 'blue')
labelnew2.pack()
labelnew2.place(x=380,y=320)
seq_entery_new2=Entry()
seq_entery_new2.pack()
seq_entery_new2.place(x=380,y=350)
def smith_waterman(match_score=1, mismatch_score=-1, gap_penalty=-1):
    seq1 = seq_entery_new.get()
    seq2 = seq_entery_new2.get()
    m, n = len(seq1), len(seq2)
    score = [[0 for _ in range(n+1)] for _ in range(m+1)]

    max_score = 0
    max_pos = None
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = score[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
            delete = score[i-1][j] + gap_penalty
            insert = score[i][j-1] + gap_penalty
            score[i][j] = max(0, diag, delete, insert)
            if score[i][j] > max_score:
                max_score = score[i][j]
                max_pos = (i, j)

    align1, align2 = '', ''
    i, j = max_pos
    while score[i][j] > 0:
        if score[i][j] == score[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score):
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif score[i][j] == score[i][j-1] + gap_penalty:
            align1 = '-' + align1
            align2 = seq2[j-1] + align2
            j -= 1
        elif score[i][j] == score[i-1][j] + gap_penalty:
            align1 = seq1[i-1] + align1
            align2 = '-' + align2
            i -= 1

    #return max_score, align1, align2
    re = Label(text = f"Maximum Score{max_score}")
    re.pack()
    re.place(x = 300, y = 450)
    re2 = Label(text = f"Allignment 1{align1}")
    re2.pack()
    re2.place(x = 300, y = 500)
    re3 = Label(text = f"Allighnment 2: {align2}")
    re3.pack()
    re3.place(x = 300 , y = 550)
btnwater = Button(text = "Water-Smith Algorithm", command = smith_waterman, bg = 'yellow' )
btnwater.place(x=380, y = 400)


###----------------------Translation---------------------######






def translation():
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
    re = Label(text = "SF"+ str(sf))
    re.pack()
    re.place(x = 200, y = 300)
    re2 = Label(text = "S" + str(s))
    re2.pack()
    re2.place(x = 400, y = 300)
    s="GCCTCTGGTATGCTTCCCTGCTTGATGATTGCGGAAACCGTAACCCTACAAGGCAGGACGATGCTAGAAAAAACCAAGCAGTTTGTGGAGAATGTGACTGTGGACTATTTACAAAAAATCTGCAACTAATGTTCCGTGCCTGCCGCTGCACCCAAATCCCAAGTTTAGGGTGCG"       
    #re3 = Label(text = "Translation tables"+ str(translation(s)))
    #re3.pack()
    #re3.place(x = 200, y = 150)

labelnew3=Label(text="Please Enter The sequence to table", bg = 'blue')
labelnew3.pack()
labelnew3.place(x=530,y=30)
seq_entery_new3=Entry()
seq_entery_new3.pack()
seq_entery_new3.place(x=550,y=70)

btntrans = Button(text = "Translation Table", command = translation, bg = 'yellow' )
btntrans.pack()
btntrans.place(x=550, y = 100)









top.mainloop()
