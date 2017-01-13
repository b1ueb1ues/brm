#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

from brmbase import *



def main():
    b = brmbase()
    print b
    for i in range(10):
        b.iron(15)
        b.pury()
    print b.getavoid()

#} main


if __name__ == "__main__" :
    main()
