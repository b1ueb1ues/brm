import sys
if len(sys.argv) == 2:
    fname = sys.argv[1]
else:
    fname = 'a.md'
fin = open(fname,'r')
fout = open(fname +'.txt','w')

for line in fin :
    space = line.find(' ')
    prefix = line[0:space]
    if prefix == '===':
        dline = '[h]' + line[space:-1] + '[/h]\n'
    elif prefix == '#':
        dline = '[size=150%]' + line[space:-1] + '[/size]\n'
    elif prefix == '##':
        dline = '[size=150%]' + line[space:-1] + '[/size]\n'
    elif prefix == '###':
        dline = '[size=130%]' + line[space:-1] + '[/size]\n'
    elif prefix == '####':
        dline = '[size=120%]' + line[space:-1] + '[/size]\n'
    elif prefix == '#####':
        dline = '[size=110%]' + line[space:-1] + '[/size]\n'
    else:
        dline = line
    fout.write(dline)
