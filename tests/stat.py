from _brmtest import *

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    pool = []

    pool.append(config( \
        equip=[] ,stat=[25,20,0,25] \
        ))
    pool.append(config( \
        equip=[] ,stat=[30,20,0,25] \
        ))
    pool.append(config( \
        equip=[] ,stat=[25,25,0,25] \
        ))
    pool.append(config( \
        equip=[] ,stat=[25,20,5,25] \
        ))
    pool.append(config( \
        equip=[] ,stat=[25,20,0,30] \
        ))


    #testhaste(pool)
    testn(pool)

if __name__ == '__main__' :
    main()
