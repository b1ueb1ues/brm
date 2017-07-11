# wow brewmaster simcs by b1ueb1ues

How to run
=====
python brmfullsystem/run.py

Arguments
=====
There is no arg parse now

Edit run.py directly and run again

class initial 
======
### stat=[25,25,0,25] 
percent of crit, haste, versatility(dmg/heal), mastery

### equip=['ring']  
available: 'ring', 'waist', 'wrist','chest' (unstable), '2t19', '4t19', '2t20', '4t20'

'ring','waist','wrist','chest' means 'Jewel of the Lost Abbey', 'Gai Plin's Soothing Sash', 'Anvil-Hardened Wristwraps', 'Sal'salabim's Lost Tunic'

equip=['ring','waist','wrist'] is legal, but you can't equip this in game.

(We think ['4t19','2t20','ring','waist'] is BIS when consider about survival)

### prate=0.44
you purifying brew rate(without talent)
use this to test relic 

### isbduration=9
use this to test relic (Chinese researchers approve that 9.5s ISB is better than 7% BOF when consider of survival)

### facepalm = 0.4
use this to test relic 

### hotblooded = 0.04
use this to test relic 


### mode='normal'
####available:

'normal' or 'n': 8m raw phydmg per 2sec (can be dodge)

'god' : 15m raw phydmg per 1.5sec (can be dodge, brewmaster die sometimes)

'gd' : 5.5m raw phydmg per 1.2sec (can be dodge)

'creep': 2m raw phydmg per 0.3sec (can be dodge)

'light': 4m raw phydmg per 1.5sec (can be dodge)

'mix': 4m raw phydmg per 1.5sec (can be dodge) and 3m raw magicdmg per 2.5sec

'star': 5m magicdmg per 2.5sec





