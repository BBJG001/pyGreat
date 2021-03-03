from optparse import OptionParser

usage="show something usefull -- for example: how to use this program"

parser = OptionParser(usage) # 带参的话会把参数变量的内容作为帮助信息输出
parser.add_option("-f","--file",dest="filename",help="read picture from File",metavar="FILE",action = "store",type="string")
parser.add_option("-s","--save",dest="save_mold",help="save image to file or not",default = True)
(options,args)=parser.parse_args()

print(options.filename)
print(options.save_mold)
print(parser.usage)