import download
from threading import Thread
from time import sleep
t=int(input())
for _ in range(t):
    url=input().strip()
    filename=input().strip()
    d=download.downloadManager(10,['1.m','2.m','3.m','4.m','5.m','6.m','7.m','8.m','9.m','10.m'])
    a=Thread(target=d.download,args=(url,filename))
    a.start()
    sleep(5)
    print('pause!')
    d.pause=True
    a.join()
    sleep(5)
    d.pause=False
    a=Thread(target=d.download,args=(url,filename))
    a.start()
    a.join()
    del d
