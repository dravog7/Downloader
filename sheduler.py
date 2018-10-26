import download
t=int(input())
for _ in range(t):
    url=input().strip()
    filename=input().strip()
    d=download.downloadManager(10,['1.m','2.m','3.m','4.m','5.m','6.m','7.m','8.m','9.m','10.m'])
    d.download(url,filename)
    #print("got out for %d"%(_,))
    del d
