from _brmtest import *
import copy
import os
import sys


def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    basearg = {'equip':['2t20','4t19','ring','waist'] ,'stat':[25,25,5,25],'talent':['ht','black'],'prate':0.44,'mode':'gd', \
            'ver':'ptr'
            }
    pool = []
    pool.append(brm(**basearg))
    statindex =  sys.argv[1] 
    if statindex == '0' :
        teststatwide(pool,statindex=0,offset=1)
    elif statindex == '1':
        teststatwide(pool,statindex=1,offset=400.0/375)
    elif statindex == '2':
        teststatwide(pool,statindex=2,offset=400.0/475)
    elif statindex == '3' :
        teststatwide(pool,statindex=3,offset=1)
    return

    teststatwide(pool,statindex=statindex,offset=1)
    teststatwide(pool,statindex=1,offset=400.0/375)
    teststatwide(pool,statindex=2,offset=400.0/475)
    teststatwide(pool,statindex=3,offset=1)
    return

def comparesinglestat(basearg,statindex):
    base = brm(**basearg)

    pool = []
    pool.append(base)
    teststat(pool,statindex=statindex)

def compare5stat(basearg):
    base = brm(**basearg)
    
    pool = []
    tmp = copy.deepcopy(basearg)
    tmp['stat'][0] += 5
    pool.append(brm(**tmp))

    tmp = copy.deepcopy(basearg)
    tmp['stat'][1] += 5.0*400/375
    pool.append(brm(**tmp))

    tmp = copy.deepcopy(basearg)
    tmp['stat'][2] += 5.0*400/475
    pool.append(brm(**tmp))

    tmp = copy.deepcopy(basearg)
    tmp['stat'][3] += 5
    pool.append(brm(**tmp))

    testn(pool,basebrm=base)

if __name__ == '__main__' :
    main()
