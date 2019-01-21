from threading import Thread
import time
import requests
import datetime
import os
import sys
from urllib import parse
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
    def __init__(self,n,filenames):
        self.nodes=n
        self.partfile=list(filenames)
        self.completed=[0 for x in range(n)]
        self.threads=[]
        self.parts=[]

    def download(self,url,resume=False):
        if(not resume):
            self.url=url
            self.filename=self.getfilename(url)
            self.getheader()
            self.partition()
            if(self.total==0):
                print("empty")
                return
        print(self.parts)
        for i in range(self.nodes):
            self.threads.append(Thread(target=self.downloadpart,args=(i,resume,)))
            self.threads[-1].start()
        self.threads.append(Thread(target=self.monitor))
        self.threads[-1].start()
        for i in range(self.nodes+1):
            self.threads[i].join()
            print(i,"joined")
        print("after join()")
        if(not self.pause):
            self.joinfiles()
            self.cleanup()
            print("cleaning")
        for i in self.threads:
            del i
        self.threads=[]
        print("returning")
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
        try:
            self.total=int(r.headers['Content-Length'])
        except:
            self.total=-1
        self.contenttype=r.headers['Content-Type']
        try:
            if(r.headers['Accept-Ranges']!='bytes'):
                self.nodes=1
        except:
            self.nodes=1
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
        print(n,headers)
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
                print("paused ",n)
                break
        f.close()
        return

    def joinfiles(self):
        #print("in join")
        f=open(self.filename,'wb')
        for i in range(self.nodes):
            f1=open(self.partfile[i],'rb')
            f.write(f1.read())
            f1.close()
        f.close()
        #print("exit")
        return

    def status(self):
        a="["
        length=20
        per=self.total/length
        for i in range(self.nodes):
            sofar=self.completed[i]
            total=self.parts[i+1]-self.parts[i]+2
            a=a+"-"*int(sofar/per)+" "*int((total-sofar)/per)
        if((len(a)-1)<length):
            a=a+" "*(length-len(a)+1)
        return a+']'
    def tojson(self):
        pass
    def fromjson(self):
        pass
    def monitor(self):
        a=0
        sm=0.1
        prevl=1
        times=0
        #print(self.total)
        while((a<self.total)and(not self.pause)):
            prev=a
            a=sum(self.completed)
            self.avg=sm*self.prevspd+(1-sm)*(self.avg)
            m=(self.status(),(a/self.total)*100,self.speed(a-prev),self.time((self.total-a)//self.avg))
            sys.stdout.write("\r")
            sys.stdout.write(" "*prevl)
            sys.stdout.write("\r")
            prevl=sys.stdout.write("%s %.2f%% speed: %s ETA %s"%m)
            sys.stdout.flush()
            self.prevspd=a-prev
            time.sleep(1)
            times+=1
        if(self.total==-1):
            print("no file size specified")
        print()
        print("size: %s time taken %s"%(self.speed(self.total)[:-4],self.time(times)))

    def time(self,sec):
        return str(datetime.timedelta(seconds=sec))

    def cleanup(self):
        for i in range(self.nodes):
            os.remove(self.partfile[i])

    def speed(self,a):
        if(a<=1024):
            return "%f bytes/sec"%(float(a),)
        elif(a<=(1024*1024)):
            return "%.2f kb/sec"%(a/1024,)
        elif(a<=(1024**3)):
            return "%.2f Mb/sec"%(a/(1024**2),)
        else:
            return "%.2f Gb/sec"%(a/(1024**3),)
    
    def getfilename(self,url):
        return parse.unquote(url[len(url)-url[::-1].index('/'):])

if(__name__=="__main__"):
    d=downloadManager(10,['1.m','2.m','3.m','4.m','5.m','6.m','7.m','8.m','9.m','10.m'])
    d.download(input().strip())