import itertools
import optparse
def generate(n1,n2):
    dic = open('passwords.txt','w')
    words = 'abcdefghijklmnoqprstuvwxyzABCDEFGHIJKLMNOQPRSTUVWXYZ1234567890'
    for i in range(n1,n2+1):
    #print(len(words))
        passwd = itertools.product(words,repeat=i)
        for k in passwd:
            dic.write("".join(k))
            dic.write("".join("\n"))


def main():
    num = ''
    parser = optparse.OptionParser("usage%prog " + "-b <begin>" + "-s <stop>")
    parser.add_option("-b", dest="num1", type="string", help="input begin number")
    parser.add_option("-s", dest="num2", type="string", help="input stop number")
    (options, args) = parser.parse_args()
    if(options.num1 == None ) | (options.num2 == None) | (options.num1 > options.num2): # must have 2 args  num1 <num2
        print(parser.usage)
        exit(0)
    else:
        num1 = options.num1
        num2 = options.num2
    generate(int(num1),int(num2))

if __name__ == "__main__":
    main()         
