from _brmtest import *
import copy
import os
import sys


def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    basearg = {'equip':[] ,'stat':[20,10,5,20], 'talent':['ht','light'], 'iduration':7, 'noisb':1, 'prate':0.5,'mode':'gd', \
            'ver':'ptr'
            }
    pool = []
    pool.append(brm(**basearg))
    stattotal = 2000
    statindex =  sys.argv[1] 
    if statindex == '0' :
        teststatwide(pool,statindex=0,offset=1,start=10,stop=10+stattotal/72.0)
    elif statindex == '1':
        teststatwide(pool,statindex=1,offset=72.0/68,start=0,stop=stattotal/68.0)
    elif statindex == '2':
        teststatwide(pool,statindex=2,offset=72.0/85,start=0,stop=stattotal/85.0)
    elif statindex == '3' :
        teststatwide(pool,statindex=3,offset=1,start=8,stop=8+stattotal/72.0)
    return

    teststatwide(pool,statindex=statindex,offset=1)
    teststatwide(pool,statindex=1,offset=72.0/68)
    teststatwide(pool,statindex=2,offset=72.0/85)
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
