import numpy as np
import math
import matplotlib.pyplot as plt
from magpylib.source.magnet import Cylinder
from magpylib.source.current import Circular
from magpylib import Collection 

TURNS = 15
s = 90
LENGTH = 3
CURRENT = 1

# create magnets
s2 = Cylinder(mag=(0,0,500), dim=(3,5))
coil1 = [Circular(curr=CURRENT,dim=LENGTH,pos=[0,0,z]) for z in np.linspace(-3,3,TURNS)]

# create collection 
c1 = Collection(coil1)

xs = np.linspace(0, 0,6)
ys = np.linspace(0, 0,6)
zs = np.linspace(-9, 9, s)
F_POS = np.array([(x,y,z) for x in xs for y in ys for z in zs])

def mag(x):
    return math.sqrt(sum(i**2 for i in x))

B = c1.getB(F_POS)[:s]
mags = [ mag(x) for x in B ]
z_pos = [d for d in zs]
print(mags)


plt.plot(z_pos, mags)
plt.title(f"Strength of Magnetic Field - Solenoid, {TURNS} turns, {LENGTH}cm long, {CURRENT} amp, {s} data points")
plt.xlabel('Displacement from center of air core (cm)')
plt.ylabel(f'Magnetic Field Strength (mT)')

plt.show()
