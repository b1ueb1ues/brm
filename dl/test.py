import adv
import wep.wand
from core.log import *
from adv.maribelle import *


conf = {}

conf.update( { 
    "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05} 
    } )

al = {
    'sp': [],
    'x5': [],
    'x4': [],
    'x3': [],
    'x2': [],
    'x1': [],
    'x0': [],
    }

al.update( {
    #'sp': ["s1","s2"],
    'x5': ["s1", "s2"],
    'x4': [],
    'x3': ["s1", "s2"],
    'x2': ["s1", "s2"],
    'x1': ["s1", "s2"],
    'x0': ["s1", "s2"],
    } )

conf['al'] = al

def sum_dmg():
    l = logget()
    dmg_sum = {'x':0, 's':0}
    for i in l:
        if i[1] == 'dmg':
            dmg_sum[i[2][0]] += i[3]

    total = 0
    for i in dmg_sum:
        total += dmg_sum[i]
    dmg_sum['total'] = total
    print dmg_sum


Maribelle(conf).run()
logcat(['x','dmg','cast'])
sum_dmg()

logreset()

conf['al'] = {
    'sp': ['s1','s2'],
    'x5': [],
    'x4': [],
    'x3': [],
    'x2': [],
    'x1': [],
    'x0': [],
    }

Maribelle(conf).run()
sum_dmg()

