# -*- coding: utf-8 -*-
# Muß mit Anaconda-Python 2.7 starten!!!!!
# Beispielprogramm nach dem Wikipedia-Artikel zu Mayavi <https://en.wikipedia.org/wiki/MayaVi>

import numpy as np
from mayavi import mlab
from scipy.special import sph_harm

# Mit diesem Werten kann gespielt werden:
l = 3
m = 0
# --------------------------------------

theta_ld = np.linspace(0, np.pi, 91)
phi_ld = np.linspace(0, 2*np.pi, 181)

theta_2d, phi_2d = np.meshgrid(theta_ld, phi_ld)
xyz_2d = np.array([np.sin(theta_2d)*np.sin(phi_2d),
                   np.sin(theta_2d) * np.cos(phi_2d),
                   np.cos(theta_2d)])

Y_lm = sph_harm(m, l, phi_2d, theta_2d)
r = abs(Y_lm.real)*xyz_2d

mlab.figure(size = (700, 830))
mlab.mesh(r[0], r[1], r[2], scalars = Y_lm.real, colormap = "cool")
mlab.view(azimuth = 0, elevation = 75, distance = 2.4, roll = -50)
mlab.savefig("images/Y_%i_%i.jpg" % (l, m))

mlab.show()

print("I did it, Babe!")
