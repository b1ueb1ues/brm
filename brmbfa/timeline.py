
class Timeline(object):
    'timeline for every 0.001s'
    def __init__(this):
        this._now = 0
        this.precessor = []
        pass

    def run(this,time=600):
        _time = time * 1000
        for i in range(_time):
            this.process()
            this._now += 1

    def process(this):
        for i in this.processor:
            i.process(this._now)
        
