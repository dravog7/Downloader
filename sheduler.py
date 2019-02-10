import download
from threading import Thread
from time import sleep
from gui import App
import sys
from PyQt5.QtWidgets import QApplication
app=QApplication(sys.argv)
url=input().strip()
q=App()
q.show()
d=download.downloadManager(10,['1.m','2.m','3.m','4.m','5.m','6.m','7.m','8.m','9.m','10.m'],q)
a=Thread(target=d.download,args=(url,))
a.start()
sys.exit(app.exec_())