# encoding:utf-8

dodge_base = 0.1253
mastery = 0.2119
        
a = ""\
+ "列出0.2119精通,0.1253基础躲闪所有可能出现的情况\n"\
+ "\n- 直接躲闪\n"\
+ "几率: dodge_base\n"\
+ "\n- 命中, 躲闪\n"\
+ "几率: (1-dodge_base)*(dodge_base+0.2119) = %f\n"\
        %( (1-dodge_base)*(dodge_base+0.2119) )\
+ "\n- 命中*2, 躲闪\n"\
+ "几率: (1-dodge_base)*(1-dodge_base-0.2119)*(dodge_base+0.2119*2) = %f\n"\
        %( (1-dodge_base)*(1-dodge_base-0.2119)*(dodge_base+0.2119*2) )\
+ "\n- 命中*3, 躲闪\n"\
+ "几率: (1-dodge_base)*(1-dodge_base-0.2119)*(1-dodge_base-0.2119*2)*(dodge_base+0.2119*3) = %f\n"\
        %( (1-dodge_base)*(1-dodge_base-0.2119)*(1-dodge_base-0.2119*2)*(dodge_base+0.2119*3) )\
+ "\n- 命中*4, 躲闪\n"\
+ "几率: (1-dodge_base)*(1-dodge_base-0.2119)*(1-dodge_base-0.2119*2)*(1-dodge_base-0.2119*3)*(dodge_base+0.2119*4) = %f\n"\
        %( (1-dodge_base)*(1-dodge_base-0.2119)*(1-dodge_base-0.2119*2)*(1-dodge_base-0.2119*3)*(dodge_base+0.2119*4) )\
+ "\n- 命中*5, 躲闪\n"\
+ "几率: (1-dodge_base)*(1-dodge_base-0.2119)*(1-dodge_base-0.2119*2)*(1-dodge_base-0.2119*3)*(1-dodge_base-0.2119*4)*(dodge_base+0.2119*5) = %f\n"\
        %( (1-dodge_base)*(1-dodge_base-0.2119)*(1-dodge_base-0.2119*2)*(1-dodge_base-0.2119*3)*(1-dodge_base-0.2119*4)*(dodge_base+0.2119*5) )\
+ "\n- 命中*6\n"\
+ "几率: 不可能\n"\

a = a.replace("dodge_base","%.4f"%dodge_base)
print a
