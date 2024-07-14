length = 180
beam = 20
draft = 6
displacement = 10000
shaftCount = 2
speed = 30
def blockCoefficient():
	volume = length*beam*draft
	return displacement/volume