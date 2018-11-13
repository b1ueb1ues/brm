import adv
import wep.wand
from core.log import *
from adv.maribelle import *
import al



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
    'x4': ["s1", "s2"],
    'x3': ["s1", "s2"],
    'x2': ["s1", "s2"],
    'x1': ["s1", "s2"],
    'x0': ["s1", "s2"],
    } )

conf['al'] = al

a = Maribelle(conf).run()
logcat()
