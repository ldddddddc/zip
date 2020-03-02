'''
fp = open('/root/Documents/GFSJ/zip/password/password1.txt')
passwd = fp.readlines()
print (passwd[0])
n=9
ln = int(n/4)
col = int(n%4)
print(ln)
print ('\n')
print (col)
Keys = passwd[ln-1]
key = Keys.split('    ')
print (key[col-1])
'''
#encoding=utf-8
import optparse
def FindKey(num,file):
    #dic = open('findkeys.txt','w')
    ln = (int(num)-1)/4
    col = (int(num)-1)%4
    passwords = file.readlines()
    Keys = passwords[ln]
    key = Keys.split('    ')
    #dic.write("".join(key[col]))
    #dic.write("".join("\n"))
    print (key[col])

def main():
    parser = optparse.OptionParser("usage%prog " + "-n <numbers> -d <dictionary>")
    parser.add_option("-n", dest="numbers", type="string", help="specify number")
    parser.add_option("-d", dest="pfile", type="string", help="specify dictionary file")
    (options, args) = parser.parse_args()
    if(options.numbers == None ) | (options.pfile == None): # must have 2 args
        print(parser.usage)
        exit(0)
    else:
        numbers = options.numbers
        file = open(options.pfile)    

    FindKey(numbers,file)     
if __name__ == "__main__":
    main()     