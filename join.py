def joinfiles(m):
    #print("in join")
    f=open(m['filename'],'wb')
    for i in range(m['nodes']):
        f1=open(m['partfile'][i],'rb')
        f.write(f1.read())
        f1.close()
    f.close()
    #print("exit")
    return

m={'filename':'a.mkv','nodes':10,'partfile':['1.m','2.m','3.m','4.m','5.m','6.m','7.m','8.m','9.m','10.m']}
joinfiles(m)