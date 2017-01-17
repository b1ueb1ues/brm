class brm:
	def reset():
		st = 0 #stagger
		_stbase = 0.35 #stagger base rate
		_prbase = 0.5 #purify base rate
		stbase = 0 #stagger base rate +talent 
		prbase = 0 #purify base rate +talent 
		strate = 0
		prrate = 0
		clock = 0
		dmgtaken = 0
		dmgtotal = 0
		dmgavoid = 0
#state
		energy = 100
		energyregen = 0
		_energyregen = 10
#changable talent or hast
		hast = 0.15
		ironlen = 8
		tolerance = 0
		elusive = 0
		light = 0
		black = 0
#cd base
		_brewcdbase = 21
		_kegcdbase = 8
		blackcdbase = 90
		brewcdbase = 0
		brewcdtotal = 0
		kegcdbase = 0
#cost
		kegcost = 40
		palmcost = 25
#buff and cd 
		ironbuff = 0
		brewcd = 0
		blackcd = 0

	def init(this):
		this.stbase = this._stbase + this.tolerance * 0.10
		this.prbase = this._prbase + this.elusive * 0.15
		this.strate = this.stbase
		this.prrate = this.stbase

		this.brewcdbase = (this._brewcdbase - this.light * 3)/(1 + this.hast)
		this.brewcdtotal = this.brewcdbase * (3 + this.light)
		this.kegcdbase = this._kegcdbase/(1 + this.hast)

		this.energyregen = this._energyregen*(1 + this.hast)
#	}

	def tick(this):
		clock += 1
#	dmg
		this.dmgtaken += this.st/10
		this.st -= this.st/10
#	cds
		this.brewcd -= 1
		if this.brewcd < 0 :
			this.brewcd = 0

		this.blackcd -= 1
		if this.blackcd < 0 :
			this.blackcd = 0

		this.kegcd -= 1
		if this.kegcd < 0 :
			kegcd = 0
#	buff
		this.ironbuff -= 1
		if this.ironbuff == 0 :
			this.strate = this.stbase
#	energy
		this.energy += this.energyregen
		if this.energy > 100 :
			this.energy = 100

#	}

	def iron():
		this.ironbuff += this.ironlen
		this.strate = this.stbase + 40
#	}

	def pury():
		dmgavoid += st * strate
		st -= st * strate
#	}

	@staticmethod
	def takedmg(times=1,dmg=100):
		dmgtotal += dmg

		dmgtaken += dmg * (1 - strate)

#	}

brm.takedmg(1,100)
