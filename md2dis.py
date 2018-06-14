
import sys


def process(fin, fout):
    dline = ''
    isline = 0
    isseg = 0
    
    linehead = []
    seghead = []
    flag = []
    for line in fin :
        space = line.find(' ')
        prefix = line[0:space]
        if prefix == '[h':
            lineflag.append('[/h]')
            dline += '[h]' + line[space:-1] 
        elif prefix == '#':
            lineflag.append('[/size]')
            dline += '[size=150%]' + line[space:-1] 
        elif prefix == '##':
            lineflag.append('[/size]')
            dline += '[size=130%]' + line[space:-1] 
        elif prefix == '###':
            lineflag.append('[/size]')
            dline += '[size=120%]' + line[space:-1] 
        elif prefix == '####':
            lineflag.append('[/size]')
            dline += '[size=110%]' + line[space:-1] 
        elif prefix == '#####':
            lineflag.append('[/size]')
            dline += '[size=110%]' + line[space:-1] 
        else:
            dline += line
        while len(lineflag):
            lineflag
        fout.write(dline)

strongtag = ['[size=110%][b]','[/b][/size]']
quotetag = ['[quote]','[/quote]']
def processtag(tag,contentin,contentout):


def main():
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = 'a.md'
    fin = open(fname,'r')
    fout = open(fname +'.txt','w')
    process(fin,fout)

if __name__ == "__main__":
    main()
