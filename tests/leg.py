from _brmtest import *

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    pool = []

    pool.append(config( \
            equip=['4t','ring','waist']\
        ))

    pool.append(config( \
            equip=['4t','ring','wrist']\
        ))
    test2(pool)

    pool = []

    pool.append(config( \
            equip=['4t','ring','waist']\
        ))

    pool.append(config( \
            equip=['4t','wrist','waist']\
        ))

    pool.append(config( \
            equip=['4t','ring','wrist']\
        ))

    #testhaste(pool)
    testhaste(pool,100000)

if __name__ == '__main__' :
    main()
