import rarfile
import optparse
from threading import Thread 

def extractFile(rar,passwd):
    try:
        rar.extractall(pwd=passwd.encode('UTF-8'))
        print ("Password has found :  " + passwd + '\n')
    except Exception as e:
        #print(p)
        pass

def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    (options, args) = parser.parse_args()
    if(options.zname == None ) | (options.dname == None): # must have 2 args
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname  
    rar = rarfile.RarFile(zname)  # zip
    passFile = open(dname)        # open dic
    for line in passFile.readlines():  
        password = line.strip('\n')   # 4 keys in 1 lines
        p = password.split('    ')   # split
        for k in range(0,4):
            t = Thread(target=extractFile,args=(rar, p[k]))  #mulit thread
            t.start()

if __name__ == "__main__":
    main()     
