from timeline import *


g_log = []
def log(t, name, amount, misc=""):
    g_log.append([now(), t, name, amount, misc])

def logcat(filter=None):
    if filter == None :
        for i in g_log:
            if type(i[3]) == float:
                print "%-8.3f: %-8s\t, %-16s\t, %-8.4f\t, %s"%(i[0],i[1],i[2],i[3],i[4])
            elif type(i[3]) == int:
                print "%-8.3f: %-8s\t, %-16s\t, %-8d\t, %s"%(i[0],i[1],i[2],i[3],i[4])
    else :
        for i in g_log:
            for j in filter :
                if i[1] == j:
                    if type(i[3]) == float:
                        print "%-8.3f: %-8s\t, %-16s\t, %-8.4f\t, %s"%(i[0],i[1],i[2],i[3],i[4])
                    elif type(i[3]) == int:
                        print "%-8.3f: %-8s\t, %-16s\t, %-8d\t, %s"%(i[0],i[1],i[2],i[3],i[4])


def logget():
    return g_log

def logreset():
    global g_log
    g_log = []

