class brm:
	st = 0 #stagger
	_stbuff = 0 #staggerdebufftime
	_stbase = 0.4 #stagger base rate
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

		this.brewcdbase = this._brewcdbase/(1 + this.hast)
		this.brewcdtotal = this.brewcdbase * 2 
		this.kegcdbase = this._kegcdbase/(1 + this.hast)

		this.energyregen = this._energyregen*(1 + this.hast)
#	}

	def tick(this):
		clock += 1
#	dmg
		if this._stbuff > 0:
			this.dmgtaken += this.st/this._stbuff
			this.st -= this.st/this._stbuff
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
		this._stbuff -= 1
		this.ironbuff -= 1
		if this.ironbuff == 0 :
			this.strate = this.stbase
#	energy
		this.energy += this.energyregen
		if this.energy > 100 :
			this.energy = 100

#	}

	def iron(this):
		if this.brewcd > this.brewcdtotal :
			print clock,'> e:ironbrew no stack'
			return
		if ironbuff < 0:
			ironbuff = this.ironlen
		else :
			this.ironbuff += this.ironlen
		this.strate = this.stbase + 40
#	}

	def pury(this):
		if this.brewcd > this.brewcdtotal :
			print clock,'> e:purybrew no stack'
			return 
		this.dmgavoid += this.st * this.prrate
		this.st -= this.st * this.prrate
#	}

	def takedmg(this,times=1,dmg=100):
		this.dmgtotal += dmg
		this.dmgtaken += dmg * (1 - this.strate)
		this.st += dmg * this.strate
#	}

	def palm(this):
		if this.energy < 25:
			print this.clock,'> e:palm no energy'
			return
		this.energy -= 25
		this.brewcd -= 1
		if this.brewcd < 0:
			this.brewcd = 0
		this.blackcd -= 1
		if this.blackcd < 0:
			this.blackcd = 0

	def keg(this):
		if kegcd != 0 :
			print this.clock,'> e:keg no cd'
			return
		if this.energy < 40:
			print this.clock,'> e:keg no energy'
			return
		this.energy -= 40
		this.brewcd -= 4
		if this.brewcd < 0:
			this.brewcd = 0
		this.blackcd -= 4
		if this.blackcd < 0:
			this.blackcd = 0

def main():


#}



if __name__ == '__main__':
	main()
