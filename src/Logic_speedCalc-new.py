import math 
import Data_Ship as ship



def calcFormFactor(): #k1
	Cstern #stern shape adjuster (GIVEN VALUE)
	c13= 1 +0.003*Cstern #stern thingy
	k1 = c13*(0.93+C12*math.pow(B/Lr, 0.92497)*math.pow(0.95-Cp, -0.521448))
	return k1



def total_resistance():
	Rf #friction resistance
	k1 = calcFormFactor() #form factor adjuster
	Rapp #appendage resistance
	Rw #wave resistance
	Rb #bulbous bow resistance
	Rtr #resitance of transom stern
	Ra #model-ship correlation resistance ?
	return Rf*(1+k1)+Rapp+Rw+R_B+R_TR+R_A



if __name__ == "__main__":
    print(calcKWforSpeed())