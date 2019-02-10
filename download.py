from PyQt5.QtCore import QThread
from threading import Thread
import time
import requests
import datetime
import os
import sys
from urllib import parse
from monitor import monitor
class downloadManager:
    filename=''
    url=''
    contenttype=''
    parts=[]
    partfile=[]
    completed=[]
    threads=[]
    nodes=0
    total=0
    avg=1
    prevspd=1
    pause=False
    def __init__(self,n,filenames,gui=None):
        self.nodes=n
        self.partfile=list(filenames)
        self.completed=[0 for x in range(n)]
        self.threads=[]
        self.parts=[]
        self.gui=gui
        self.monitor=monitor(self,(self.gui==None))
        self.monitor.progressChange.connect(self.updateProgress)

    def updateProgress(self,a):
        self.gui.ui.progressBar.setValue(int(a))
    def download(self,url,resume=False):
        if(not resume):
            self.url=url
            self.getheader()
            if(self.filename==''):
                self.filename=self.getfilename(url)
            self.partition()
            if(self.total==0):
                print("empty")
                return
        #print(self.parts)
        for i in range(self.nodes):
            self.threads.append(Thread(target=self.downloadpart,args=(i,resume,)))
            self.threads[-1].start()
        self.monitor.start()
        for i in range(self.nodes):
            self.threads[i].join()
            #print(i,"joined")
        #print("after join()")
        if(not self.pause):
            self.joinfiles()
            self.cleanup()
            #print("cleaning")
        for i in self.threads:
            del i
        self.threads=[]
        #print("returning")
        return
    
    def partition(self):
        if(self.total==-1):
            self.parts.append(-1)
            return
        if(self.total==0):
            return
        per=self.total//(self.nodes)
        for i in range(0,self.total+1,per):
            self.parts.append(i)
        self.parts.pop()
        self.parts.append(self.total)
    
    def getheader(self):
        r=requests.head(self.url)
        #print(r.headers)
        self.total=int(r.headers.get('Content-Length',-1))
        self.contenttype=r.headers['Content-Type']
        if(r.headers.get('Accept-Ranges',0)!='bytes'):
            self.nodes=1
        contentname=r.headers.get('Content-Disposition',False)
        if(contentname):
            fil=contentname.find('filename="')
            if(fil==-1):
                return
            self.filename=contentname[fil:contentname.find('"',fil+1)]
        return
        #print(self.nodes)

    def downloadpart(self,n,resume=False):
        if(self.parts[n]==-1):
            headers={}
        else:
            headers={'Range':'bytes={}-{}'}
            if(self.parts[n+1]==self.parts[-1]):
                headers['Range']=headers['Range'].format(self.parts[n]+self.completed[n],self.parts[n+1])
            else:
                headers['Range']=headers['Range'].format(self.parts[n]+self.completed[n],self.parts[n+1]-1)
        #print(n,headers)
        req=requests.get(self.url,stream=True,headers=headers)
        if(not resume):
            f=open(self.partfile[n],'wb')
        else:
            f=open(self.partfile[n],'ab')
        for chunk in req.iter_content(chunk_size=64):
            if(chunk):
                f.write(chunk)
                self.completed[n]+=len(chunk)
            if(self.pause):
                #print("paused ",n)
                req.close()
                break
        f.close()
        return

    def joinfiles(self):
        #print("in join")
        f=open(self.filename,'wb')
        for i in range(self.nodes):
            f1=open(self.partfile[i],'rb')
            f.write(f1.read())
            self.monitor.progressChange.emit(int((i+1)/self.nodes))
            f1.close()
        f.close()
        #print("exit")
        return

    def cleanup(self):
        for i in range(self.nodes):
            os.remove(self.partfile[i])
    
    def getfilename(self,url):
        url=parse.urlparse(url).path
        filename=parse.unquote(url[len(url)-url[::-1].index('/'):])
        if(filename==''):
            filename='noidea'
        return filename

if(__name__=="__main__"):
    d=downloadManager(10,['1.m','2.m','3.m','4.m','5.m','6.m','7.m','8.m','9.m','10.m'])
    d.download(input().strip())