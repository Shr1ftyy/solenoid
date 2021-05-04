import numpy as np
import math
import matplotlib.pyplot as plt
from magpylib.source.magnet import Cylinder
from magpylib.source.current import Circular
from magpylib import Collection 

# create magnets
s2 = Cylinder(mag=(0,0,500), dim=(3,5))
coil1 = [Circular(curr=1,dim=3,pos=[0,0,z]) for z in np.linspace(-3,3,15)]

# create collection
c1 = Collection(coil1)

s = 90
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
plt.title(f"Strength of Magnetic Field - Solenoid, 15 turns, 3cm long, 1 amp")
plt.xlabel('Displacement from center of air core (cm)')
plt.ylabel(f'Magnetic Field Strength (mT)')

plt.show()
