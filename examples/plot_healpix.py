"""
Healpix Plot
============

Create a healpix map of your final population

This example shows how you can use the :meth:`~kicker.pop.Population.plot_map` function in 
:class:`~kicker.pop.Population` class to create a healpix map after
running your population. Try increasing ``n_binaries`` or ``nside`` to see a higher resolution plot with more
data. Also feel free to turn ``with_timing`` back on.
"""

import kicker
import matplotlib.pyplot as plt
p = kicker.pop.Population(100)
p.create_population(with_timing=False)

p.plot_map(nside=32, norm="linear", show=False)
plt.show()
