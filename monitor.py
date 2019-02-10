from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtCore import QCoreApplication
import datetime
import sys
translate=QCoreApplication.translate
class monitor(QThread):
    progressChange=pyqtSignal(int)
    def __init__(self,download,noconsole=False):
        QThread.__init__(self)
        self.download=download
        self.noconsole=noconsole
    
    def __del__(self):
        self.wait()
    
    def status(self):
        a="["
        length=20
        per=self.download.total/length
        for i in range(self.download.nodes):
            sofar=self.download.completed[i]
            total=self.download.parts[i+1]-self.download.parts[i]+2
            a=a+"-"*int(sofar/per)+" "*int((total-sofar)/per)
        if((len(a)-1)<length):
            a=a+" "*(length-len(a)+1)
        return a+']'
    def run(self):
        self.download.gui.ui.Status.setText("Downloading...")
        self.download.gui.ui.filenameLineEdit.setText(translate("Dialog",self.download.filename))
        self.download.gui.ui.uRLLineEdit.setText(translate("Dialog",self.download.url))
        total=self.speed(self.download.total)[:-4]
        self.download.gui.ui.total.setText(translate("Dialog",total))
        a=0
        sm=0.1
        prevl=1
        times=0
        #print(self.download.total)
        while((a<self.download.total)and(not self.download.pause)):
            self.guiupdate()
            prev=a
            a=sum(self.download.completed)
            self.download.avg=sm*self.download.prevspd+(1-sm)*(self.download.avg)
            m=(self.status(),(a/self.download.total)*100,self.speed(a-prev),self.time((self.download.total-a)//self.download.avg))
            if(not self.noconsole):
                sys.stdout.write("\r"+(" "*prevl)+"\r")
                prevl=sys.stdout.write("%s %.2f%% speed: %s ETA %s"%m)
                sys.stdout.flush()
            self.download.prevspd=a-prev
            self.sleep(1)
            times+=1
            
        if(not self.noconsole):
            if(self.download.total==-1):
                print("no file size specified")
            print()
            print("size: %s time taken %s"%(self.speed(self.download.total)[:-4],self.time(times)))
            
    
    def guiupdate(self):
        speed=self.speed(self.download.prevspd)
        self.download.gui.ui.speed.setText(translate("Dialog",speed))
        completed=sum(self.download.completed)
        self.download.gui.ui.completed.setText(translate("Dialog",self.speed(completed)[:-4]))
        percent=(completed/self.download.total)*100
        self.progressChange.emit(int(percent))

    def time(self,sec):
        return str(datetime.timedelta(seconds=sec))

    def speed(self,a):
        if(a<=1024):
            return "%f bytes/sec"%(float(a),)
        elif(a<=(1024*1024)):
            return "%.2f kb/sec"%(a/1024,)
        elif(a<=(1024**3)):
            return "%.2f Mb/sec"%(a/(1024**2),)
        else:
            return "%.2f Gb/sec"%(a/(1024**3),)
