# -*- coding: utf-8 -*-
import json
import string
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import operator
import unicodedata
from time import time
start_time=time()
punctuation = list(string.punctuation)
frecdict={}
stop =punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my'
,'your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from',
'new','la','but']
f=open('tweet_data.json', 'r')
termf=open('term_frequencies.txt','w')
linelist=f.readlines()
for l in linelist:
     # read only the first tweet/line
    tweet = json.loads(l) # load it as Python dict
    print tweet.keys()
    created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
    stri=tweet['text']#tweet
    stri=stri.lower()
    L=stri.split(" ")
    for i in L:
        if(i in frecdict):
            frecdict[i]+=1
        else:
            if(not(i in stop)):

                frecdict[i]=1
for u in range(0,20):

    term=max(frecdict.iteritems(), key=operator.itemgetter(1))[0]
    amount=frecdict[max(frecdict.iteritems(), key=operator.itemgetter(1))[0]]
    unicodedata.normalize('NFKD', term).encode('ascii','ignore')
    term=str(term)
    amount=str(amount)
    if(u==0):
        t1=term;
    if(u==1):
        t2=term;
    if(u==2):
        t3=term;
    if(u==3):
        t4=term;
    if(u==4):
        t5=term;
    writestr="(\'"+term+"\', "+amount+")\n"
    termf.write(writestr)
    del frecdict[max(frecdict.iteritems(), key=operator.itemgetter(1))[0]]
td1 = [[0 for x in range(60)] for x in range(24)]
td2 = [[0 for x in range(60)] for x in range(24)]
td3 = [[0 for x in range(60)] for x in range(24)]
td4 = [[0 for x in range(60)] for x in range(24)]
td5 = [[0 for x in range(60)] for x in range(24)]
for l in linelist:
     # read only the first tweet/line
    tweet = json.loads(l) # load it as Python dict
    print tweet.keys()
    created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
    stri=tweet['text']#tweet
    date=tweet["created_at"];#date-time in ISO format
    dt=datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format
    stri=stri.lower()
    L=stri.split(" ")
    for i in L:
        if(i==t1):
            if(td1[dt.hour][dt.minute] is None):
                td1[dt.hour][dt.minute]=1
            else:
                td1[dt.hour][dt.minute]+=1
        if(i==t2):
            if(td2[dt.hour][dt.minute] is None):
                td2[dt.hour][dt.minute]=1
            else:
                td2[dt.hour][dt.minute]+=1
        if(i==t3):
            if(td3[dt.hour][dt.minute] is None):
                td3[dt.hour][dt.minute]=1
            else:
                td3[dt.hour][dt.minute]+=1
        if(i==t4):
            if(td4[dt.hour][dt.minute] is None):
                td4[dt.hour][dt.minute]=1
            else:
                td4[dt.hour][dt.minute]+=1
        if(i==t5):
            if(td5[dt.hour][dt.minute] is None):
                td5[dt.hour][dt.minute]=1
            else:
                td5[dt.hour][dt.minute]+=1
fdtwstr=""
for y in range(0,24):
    for x in range(0,60):
        if((not(td1[y][x] is None))and(td1[y][x]!=0)):
            ys=str(y)
            xs=str(x)
            if(y<10):
                ys="0"+str(y)
            if(x<10):
                xs="0"+str(x)
            fdtwstr=fdtwstr+t1+" 2015-11-23 "+ys+":"+xs+":00 "+str(td1[y][x])+"\n"
for y in range(0,24):
    for x in range(0,60):
        if((not(td2[y][x] is None))and(td2[y][x]!=0)):
            ys=str(y)
            xs=str(x)
            if(y<10):
                ys="0"+str(y)
            if(x<10):
                xs="0"+str(x)
            fdtwstr=fdtwstr+t2+" 2015-11-23 "+ys+":"+xs+":00 "+str(td2[y][x])+"\n"
for y in range(0,24):
    for x in range(0,60):
        if((not(td3[y][x] is None))and(td3[y][x]!=0)):
            ys=str(y)
            xs=str(x)
            if(y<10):
                ys="0"+str(y)
            if(x<10):
                xs="0"+str(x)
            fdtwstr=fdtwstr+t3+" 2015-11-23 "+ys+":"+xs+":00 "+str(td3[y][x])+"\n"
for y in range(0,24):
    for x in range(0,60):
        if((not(td4[y][x] is None))and(td4[y][x]!=0)):
            ys=str(y)
            xs=str(x)
            if(y<10):
                ys="0"+str(y)
            if(x<10):
                xs="0"+str(x)
            fdtwstr=fdtwstr+t4+" 2015-11-23 "+ys+":"+xs+":00 "+str(td4[y][x])+"\n"
for y in range(9,11):
    for x in range(0,60):
        if((not(td5[y][x] is None))and(td5[y][x]!=0)):
            ys=str(y)
            xs=str(x)
            if(y<10):
                ys="0"+str(y)
            if(x<10):
                xs="0"+str(x)
            fdtwstr=fdtwstr+t5+" 2015-11-23 "+ys+":"+xs+":00 "+str(td5[y][x])+"\n"
tfotf=open('term frequencies overtime.txt','w')
tfotf.write(fdtwstr)
end_time=time()
elapsed=end_time-start_time
print(elapsed)
#Saving a plot figure as image
#fig=plt.figure()
#x=np.linspace(0,10,30)
#y=x*x;
#plt.plot(x,y)
#plt.savefig('sample_plot.png')
#plt.show()
