class Spell(object):
    charged = 0
    def __init__(this, sp=None, ac=None):
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
    def charge(this,sp):
        this.charged += sp

    def check(this):
        if this.charged >= sp:
            return 1
        else:
            return 0

    def cast(this):
        if not check():
            return 0
        else:
            this.charged = 0
            this.ac()

    def ac(this):
        pass
