#!/usr/bin/env python

import warnings
from astroplan import get_IERS_A_or_workaround

warnings.filterwarnings('ignore', category=Warning)
get_IERS_A_or_workaround()

print('Running...')

from GenOutputs import visible_objects
from GenOutputs import star_visualization
from GenOutputs import const_visualization

print('Finding Stars...')

stars, constellations = visible_objects()
out_string = '''The following stars are visible:
{0}

The following constellations are visible:
{1}
'''
output = open('./Outputs/VisibleObjects.txt', 'w')
output.write(out_string.format(stars, constellations))
print('Generating star visualization...')

star_visualization(stars)
print('Generating constellation visualiztion...')

const_visualization(constellations)
print('Done!')
