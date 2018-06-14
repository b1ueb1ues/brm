import sys
from markdown2 import Markdown
from markdown2 import main as mmain


#md = Markdown()
#print md.convert("## test\#")

def main():
    a = mmain(path='b.md')
    print a

if __name__ == "__main__":
    main()

