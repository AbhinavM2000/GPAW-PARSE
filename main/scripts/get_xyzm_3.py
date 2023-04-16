"""
Allocates mass to atoms and obtains [x y z m] format for random and optimized for abnv_get_com.py
Copyright (C) 2022  Abhinav M

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""

import numpy
from scipy import ndimage
import re
from periodictable import elements
def get_atomic_masses(filename):
    with open(filename) as f:
        pos_block_found = False
        pos_lines = []
        for line in f:
            if "Positions:" in line:
                pos_block_found = True
                continue
            elif pos_block_found and line.strip():
                atom_name = re.match(r'\s+\d+\s+(\w{1,2})\s+', line)
                if atom_name:
                    pos_lines.append(atom_name.group(1))
                else:
                    break

    # replace the atom names with the atomic masses using the periodictable package
    for i in range(len(pos_lines)):
        pos_lines[i] = elements.symbol(pos_lines[i]).mass
    #end list with -1 to indicate end of list
    pos_lines.append(-1)

    return pos_lines


xyzOptstr = open("./data/xyz_opt_str", 'w')

xyzm = numpy.array([])
with open('./data/pos_Opt_structures') as infile:
    i = 0
    k = 0
    j = get_atomic_masses('./data/bh.py.out')
    for line in infile:
        try:
            if j[k] == -1:
                k = 0
            mass = str(j[k])
            k = k + 1
            xxx = line.split()[2] + ' ' + line.split()[3] + ' ' + line.split()[4] + ' ' + mass + ' \n'
            xyzOptstr.write(str(xxx))
            i = i + 1
        except IndexError:
            xyzOptstr.write("*\n")
            pass
        continue
print(i)

xyzOptrnd = open("./data/xyz_rnd_str", 'w')
with open('./data/pos_Rand_structures') as infile2:
    i = 0
    k = 0
    j = get_atomic_masses('./data/bh.py.out')
    for line in infile2:
        try:
            if j[k] == -1:
                k = 0
            mass = str(j[k])
            k = k + 1
            xxx = line.split()[2] + ' ' + line.split()[3] + ' ' + line.split()[4] + ' ' + mass + ' \n'
            xyzOptrnd.write(str(xxx))
            i = i + 1
        except IndexError:
            xyzOptrnd.write("*\n")
            pass
        continue
