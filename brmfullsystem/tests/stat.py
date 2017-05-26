from _brmtest import *
import copy

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    basearg = {'equip':['4t19','ring','waist'] ,'stat':[26,30,7,28],'talent':['ht','black'],'prate':0.44,'mode':'gd', \
            'ver':'ptr'
            }
    #compare5stat(basearg)
    pool = []
    pool.append(brm(**basearg))
    teststat(pool,statindex=1)
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
