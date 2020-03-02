import itertools
import optparse
def generate(n):
    dic = open('passwords.txt','w')
    words = 'abcdefghijklmnoqprstuvwxyzABCDEFGHIJKLMNOQPRSTUVWXYZ1234567890'
    #print(len(words))
    passwd = itertools.product(words,repeat=n)
    for k in passwd:
        dic.write("".join(k))
        dic.write("".join("\n"))


def main():
    num = ''
    parser = optparse.OptionParser("usage%prog " + "-n <number>")
    parser.add_option("-n", dest="num", type="string", help="input number")
    (options, args) = parser.parse_args()
    if(options.num == None): # must have 1 args
        print(parser.usage)
        exit(0)
    else:
        num = options.num
    generate(int(num))

if __name__ == "__main__":
    main()         
