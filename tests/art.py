from _brmtest import *

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    pool = []

    pool.append(config( \
        iduration=7.5 \
        ))
    pool.append(config( \
        iduration=8.0 \
        ))
    pool.append(config( \
        iduration=8.5 \
        ))
    pool.append(config( \
        iduration=9.0 \
        ))



    #testhaste(pool)
    testhaste(pool)

if __name__ == '__main__' :
    main()
