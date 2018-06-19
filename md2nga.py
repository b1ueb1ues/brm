import sys
from markdown2 import Markdown
from markdown2 import main as mmain


#md = Markdown()
#print md.convert("## test\#")


def processall(a):
    print '-------'
    replace = {
        '<p>'   : '', '</p>'   : '',
        '<pre>' : '', '</pre>' : '',

        '<h1>'         : '[h][size=150%]' , '</h1>'         : '[/size][/h]' , # #
        '<h2>'         : ''               , '</h2>'         : ''            , # ##
        '<h3>'         : ''               , '</h3>'         : ''            , # ###
        '<h4>'         : ''               , '</h4>'         : ''            , # ####
        '<h5>'         : ''               , '</h5>'         : ''            , # #####
        '<h6>'         : ''               , '</h6>'         : ''            , # ######
        '<strong>'     : '[b][size=110%]' , '</strong>'     : '[/b][/size]' , # **
        '<em>'         : '[color=red]'    , '</em>'         : '[/color]'    , # *
        '<blockquote>' : '[quote]'        , '</blockquote>' : '[/quote]'    , # >
        '<code>'       : '[code]'         , '</code>'       : '[/code]'     , # `
        '<ul>'         : '[list]'         , '</ul>'         : '[/list]'     , # -
        '<li>'         : '[*]'            , '</li>'         : ''            , # -
        '<table>'      : '[table]'        , '</table>'      : '[/table]'    ,
        '<tr>'         : '[tr]'           , '</tr>'         : '[/tr]'       ,
        '<td>'         : '[td]'           , '</td>'         : '[/td]'       ,

        '__END__' : '__END__'
        }
    for i in replace:
        a = a.replace(i,replace[i])
    print a

test = {
        }

def processline(l):
    pass

def main():
    ext = {
            "tables":1,
            #"fenced-code-blocks":1,
            "__END__":0
    }
    a = mmain(path='b.md',extras=ext)
    print a
    processall(a)

if __name__ == "__main__":
    main()

