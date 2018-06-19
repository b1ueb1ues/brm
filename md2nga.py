import sys
from markdown2 import Markdown
from markdown2 import main as mmain


#md = Markdown()
#print md.convert("## test\#")


def processall(a):
    alt = 1
    print '-------'
    replace = {
        '<p>'   : ''        , '</p>'   : ''         ,
       #'<p>'   : '[quote]' , '</p>'   : '[/quote]' ,
        '<pre>' : ''        , '</pre>' : ''         ,
       #-------------
        '<h1>' : '[h][b][size=150%]' , '</h1>' : '[/size][/b][/h]' , # #
        '<h2>' : '[h][b][size=130%]' , '</h2>' : '[/size][/b][/h]' , # ##
        '<h3>' : '[b][size=120%]'    , '</h3>' : '[/size][/b]'     , # ###
        '<h4>' : '[b][size=110%]'    , '</h4>' : '[/size][/b]'     , # ####
        '<h5>' : '[b][size=100%]'    , '</h5>' : '[/size][/b]'     , # #####
        '<h6>' : '[b][size=100%]'    , '</h6>' : '[/size][/b]'     , # ######
       # # ## ### #### ##### ######
        '<ul>'         : '[list]'         , '</ul>'         : '[/list]'     , # list
        '<ol>'         : '[list]'         , '</ol>'         : '[/list]'     , # list
        '<li>'         : '[*]'            , '</li>'         : ''            ,
       #-------------
        '<table>'      : '[table]'        , '</table>'      : '[/table]'    , # table
        '<thead>'      : ''               , '</thead>'      : ''            ,
        '<th>'         : '[th]'           , '</th>'         : '[/th]'       ,
        '<tbody>'      : ''               , '</tbody>'      : ''            ,
        '<tr>'         : '[tr]'           , '</tr>'         : '[/tr]'       ,
        '<td>'         : '[td]'           , '</td>'         : '[/td]'       ,
       #-------------
        '<strong>'     : '[b][size=110%]' , '</strong>'     : '[/size][/b]' , # **
        '<em>'         : '[color=red]'    , '</em>'         : '[/color]'    , # *
        '<blockquote>' : '[quote]'        , '</blockquote>' : '[/quote]'    , # >
       #'<blockquote>' : '[collapse]'     , '</blockquote>' : '[/collapse]' , # >
        '<code>'       : '[code]'         , '</code>'       : '[/code]'     , # `
        '<strike>'     : '[del]'          , '</strike>'     : '[/del]'      , # ~~
        '<hr />'       : '======'         , '<hr>'          : ''            , # ---

        '__END__' : '__END__'
        }

    if alt :
        replace['<blockquote>'] = '[collapse]'
        replace['</blockquote>'] = '[/collapse]'
        replace['<p>'] = '[quote]'
        replace['</p>'] = '[/quote]'

    for i in replace:
        a = a.replace(i,replace[i])
    print a


def processline(l):
    pass

def main():
    ext = {
            "tables":1,
            "fenced-code-blocks":1,
            "numbering":1,
            #"spoiler":1,
            "strike":1,
            "__END__":0
    }
    if len(sys.argv) >= 2:
        if sys.argv[1] :
            path = sys.argv[1]
    else:
        path = 'b.md'
    a = mmain(path=path,extras=ext)
    processall(a)

if __name__ == "__main__":
    main()

