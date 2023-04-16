import numpy as np
from ase import Atoms
from ase.visualize import view
import periodictable
import pandas as pd
# read the data file and split it into blocks


symbol_to_mass = {
    'H': 1.0,
    'He': 4.0,
    'Li': 6.9,
    'Be': 9.0,
    'B': 10.8,
    'C': 12.0,
    'N': 14.0,
    'O': 16.0,
    'F': 19.0,
    'Ne': 20.2,
    'Na': 23.0,
    'Mg': 24.3,
    'Al': 27.0,
    'Si': 28.1,
    'P': 31.0,
    'S': 32.1,
    'Cl': 35.5,
    'Ar': 39.9,
    'K': 39.1,
    'Ca': 40.1,
    'Sc': 45.0,
    'Ti': 47.9,
    'V': 50.9,
    'Cr': 52.0,
    'Mn': 54.9,
    'Fe': 55.8,
    'Co': 58.9,
    'Ni': 58.7,
    'Cu': 63.5,
    'Zn': 65.4,
    'Ga': 69.7,
    'Ge': 72.6,
    'As': 74.9,
    'Se': 78.0,
    'Br': 79.9,
    'Kr': 83.8,
    'Rb': 85.5,
    'Sr': 87.6,
    'Y': 88.9,
    'Zr': 91.2,
    'Nb': 92.9,
    'Mo': 95.9,
    'Tc': 98.0,
    'Ru': 101.1,
    'Rh': 102.9,
    'Pd': 106.4,
    'Ag': 107.9,
    'Cd': 112.4,
    'In': 114.8,
    'Sn': 118.7,
    'Sb': 121.8,
    'Te': 127.6,
    'I': 126.9,
    'Xe': 131.3,
    'Cs': 132.9,
    'Ba': 137.3,
    'La': 138.9,
    'Ce': 140.1,
    'Pr': 140.9,
    'Nd': 144.2,
    'Pm': 145.0,
    'Sm': 150.4,
    'Eu': 152.0,
    'Gd': 157.3,
    'Tb': 158.9,
    'Dy': 162.5,
    'Ho': 164.9,
    'Er': 167.3,
    'Tm': 168.9,
    'Yb': 173.0,
    'Lu': 175.0,
    'Hf': 178.5,
    'Ta': 180.9,
    'W': 183.8,
    'Re': 186.2,
    'Os': 190.2,
    'Ir': 192.2,
    'Pt': 195.1,
    'Au': 197.0}  # dictionary with symbol to mass values
element_numbers ={
    'H': 1,
    'He': 2,
    'Li': 3,
    'Be': 4,
    'B': 5,
    'C': 6,
    'N': 7,
    'O': 8,
    'F': 9,
    'Ne': 10,
    'Na': 11,
    'Mg': 12,
    'Al': 13,
    'Si': 14,
    'P': 15,
    'S': 16,
    'Cl': 17,
    'Ar': 18,
    'K': 19,
    'Ca': 20,
    'Sc': 21,
    'Ti': 22,
    'V': 23,
    'Cr': 24,
    'Mn': 25,
    'Fe': 26,
    'Co': 27,
    'Ni': 28,
    'Cu': 29,
    'Zn': 30,
    'Ga': 31,
    'Ge': 32,
    'As': 33,
    'Se': 34,
    'Br': 35,
    'Kr': 36,
    'Rb': 37,
    'Sr': 38,
    'Y': 39,
    'Zr': 40,
    'Nb': 41,
    'Mo': 42,
    'Tc': 43,
    'Ru': 44,
    'Rh': 45,
    'Pd': 46,
    'Ag': 47,
    'Cd': 48,
    'In': 49,
    'Sn': 50
}
import pathlib

filename = 'xyz_rnd_str'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename

with open('./data/xyz_rnd_str') as f:
    data = f.read().split('*\n')
    data = [d.strip().split('\n') for d in data if d.strip()]
    # Replace the mass values with the corresponding atomic symbols using the dictionary symbol_to_mass
    for i in range(len(data)):
        for j in range(len(data[i])):
            line_data = data[i][j].split()
            x, y, z, mass = float(line_data[0]), float(line_data[1]), float(line_data[2]), float(line_data[3])
            mass = round(mass, 1) # round off to 1 decimal
            symbol = list(symbol_to_mass.keys())[list(symbol_to_mass.values()).index(mass)]
            data[i][j] = '{} {} {} {}'.format(x, y, z, symbol)

# Loop over the blocks and create ASE Atoms objects
structures = []
for block in data:
    positions = []
    symbols = []
    for line in block[0:]:
        line_data = line.split()
        positions.append([float(line_data[0]), float(line_data[1]), float(line_data[2])])
        symbols.append(line_data[3])
    structures.append(Atoms(symbols=symbols, positions=positions))
import os

# Generate png files using ASE and store them in a folder called images using write function
if not os.path.exists('./data/images/rand'):
    os.makedirs('./data/images/rand')
for i, atoms in enumerate(structures):
    atoms.write('./data/images/rand/{}.png'.format(i))

#repeat same for xyz_opt_str
filename = 'xyz_opt_str'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename

with open('./data/xyz_opt_str') as f:
    data = f.read().split('*\n')
    data = [d.strip().split('\n') for d in data if d.strip()]
    # Replace the mass values with the corresponding atomic symbols using the dictionary symbol_to_mass
    for i in range(len(data)):
        for j in range(len(data[i])):
            line_data = data[i][j].split()
            x, y, z, mass = float(line_data[0]), float(line_data[1]), float(line_data[2]), float(line_data[3])
            mass = round(mass, 1) # round off to 1 decimal
            symbol = list(symbol_to_mass.keys())[list(symbol_to_mass.values()).index(mass)]
            data[i][j] = '{} {} {} {}'.format(x, y, z, symbol)

# Loop over the blocks and create ASE Atoms objects
structures2 = []
for block in data:
    positions = []
    symbols = []
    for line in block[0:]:
        line_data = line.split()
        positions.append([float(line_data[0]), float(line_data[1]), float(line_data[2])])
        symbols.append(line_data[3])
    structures2.append(Atoms(symbols=symbols, positions=positions))
#function to return structure xyz and symbol from structures[] in html format
def get_xyz_str(structures2, i):
    xyz_str = structures2[i].get_positions()
    symbols = structures2[i].get_chemical_symbols()
    xyz_str = np.array(xyz_str)
    xyz_str = np.round(xyz_str, decimals=3)
    xyz_str = np.column_stack((symbols, xyz_str))
    xyz_str = np.array2string(xyz_str, separator=' ', max_line_width=1000000)
    xyz_str = xyz_str.replace('[', '').replace(']', '').replace("'", '')
    return xyz_str

# Generate png files using ASE and store them in a folder called images using write function
if not os.path.exists('./data/images/opt'):
    os.makedirs('./data/images/opt')
for i, atoms in enumerate(structures2):
    atoms.write('./data/images/opt/{}.png'.format(i))

#display data in html table as random structure images, opt structure images, bfsgs, and energies
import os
from IPython.display import HTML
filename = 'opt_energies'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename

#open file to read opt_energies and maxbfgs
with open('./data/opt_energies') as f:
    opt_energies = f.read().splitlines()
filename = 'maxbfgs'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename
with open('./data/maxbfgs') as f:
    maxbfgs = f.read().splitlines()

import os
from IPython.display import HTML

#open file to read opt_energies and maxbfgs
filename = 'opt_energies'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename

#open file to read opt_energies and maxbfgs
with open('./data/opt_energies') as f:
    opt_energies = f.read().splitlines()

filename = 'maxbfgs'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename
with open('./data/maxbfgs') as f:
    maxbfgs = f.read().splitlines()
#find lowest energy and corresponding index and store in min_energy and min_index
min_energy = min(opt_energies)
min_index = opt_energies.index(min_energy)
#generate HTML code

html = """
<style>
table {
  border-collapse: collapse;
  width: 100%;
  max-width: 800px;
  margin: auto;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background-color: #f2f2f2;
}

img {
  display: block;
  margin: auto;
  max-width: 200px;
  max-height: 200px;
  cursor: pointer;
}

.modal {
  display: none; 
  position: fixed; 
  z-index: 1; 
  padding-top: 100px; 
  left: 0;
  top: 0;
  width: 100%;
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.4); 
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  height: 50%; 
  max-width: 800px;
}
.highlight {
			background-color: yellow;
		}
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>

<div id="myModal" class="modal">
    <title>Atom Coordinates:</title>
  <div class="modal-content">
    <span class="close">&times;</span>
    <pre id="xyz-string"></pre>
  </div>
</div>

<table onload="highlightLowestEnergyRow()">
  <caption>COMPARISON OF BASINS : BFGS, ENERGY (click on image to get coordinates)</caption>
  
  <thead>
    <tr>
      <th>ID</th>
      <th>Random Structure</th>
      <th>Optimized Structure</th>
      <th>BFGS taken</th>
      <th>Energy (eV)</th>
    </tr>
  </thead>
  <tbody>
"""

for i in range(len(opt_energies)):
    html += """
    <tr>
    <td>{}</td>
      <td><img src="images/rand/{}.png" onclick="openModal(`{}`)"></td>
      <td><img src="images/opt/{}.png" onclick="openModal(`{}`)"></td>
      <td>{}</td>
      <td>{}</td>
    </tr>
    """.format(i, i, get_xyz_str(structures, i), i, get_xyz_str(structures2, i), maxbfgs[i], opt_energies[i])

html += """
  </tbody>
</table>

<script>
function openModal(xyz) {
  var modal = document.getElementById("myModal");
  var modalContent = document.getElementById("xyz-string");
  modal.style.display = "block";
  modalContent.textContent = xyz;
}

var closeModal = document.getElementsByClassName("close")[0];
closeModal.onclick = function() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
</script>
<script>
		function highlightRow() {
			var table = document.getElementsByTagName("table")[0];
			var rows = table.getElementsByTagName("tr");
			var lowestEnergy = Infinity;
			var lowestEnergyRow = null;
			for (var i = 0; i < rows.length; i++) {
				var energyCell = rows[i].cells[4];
				var energy = parseFloat(energyCell.innerHTML);
				if (energy < lowestEnergy) {
					lowestEnergy = energy;
					lowestEnergyRow = rows[i];
				}
			}
			lowestEnergyRow.classList.add("highlight");
		}
	</script>
    
"""
html += """
  </tbody>
</table>


"""

filename = 'BFGS.html'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename
#write to HTML file
with open('./data/BFGS.html', 'w') as f:
    f.write(html)

#display HTML
HTML(html)


import ase
from ase import Atom, Atoms

# function to get list of atoms in a structure
def get_atoms(structure):
    atoms = []
    for atom in structure:
        atoms.append(atom.symbol)
    return atoms
import numpy as np
from ase import Atom, Atoms



import numpy as np
from ase import Atoms

import numpy as np
from itertools import combinations
from collections import defaultdict
from ase import Atoms
import matplotlib as plt
import numpy as np
from itertools import combinations
from collections import defaultdict
from ase import Atoms

# get all bonds in the structure with ase, atom1-atom2, bond length format
def get_bonds(structure):
    bond_lengths = defaultdict(list)
    for atom1, atom2 in combinations(structure, 2):
        bond_type = '-'.join(sorted([atom1.symbol, atom2.symbol]))
        bond_lengths[bond_type].append(np.linalg.norm(atom1.position - atom2.position))
    return bond_lengths

#calculate average bond length for each bond type
def get_avg_bond_length(bond_lengths):
    avg_bond_lengths = {}
    for bond_type, lengths in bond_lengths.items():
        avg_bond_lengths[bond_type] = np.mean(lengths)
    return avg_bond_lengths

# example usage
bond_lengths = get_bonds(structures[0])
avg_bond_lengths = get_avg_bond_length(bond_lengths)
#print(avg_bond_lengths)
from collections import defaultdict
from itertools import combinations
import numpy as np
import ase.io
import ipywidgets as widgets
from IPython.display import display, HTML
def get_bond_length_table(structure, i):
    # get bond lengths for the structure
    bond_lengths = get_bonds(structure)
    # calculate average bond length for each bond type
    avg_bond_lengths = get_avg_bond_length(bond_lengths)

    # create table HTML
    table_html = f'<div class="table-container">\n'
    table_html += f'<h2 class="table-title">Random structure {i}</h2>\n'
    table_html += f'<div class="image-container"><img src="{os.path.join("images", "rand", f"{i}.png")}" alt="Structure {i}" class="structure-image"></div>\n'
    table_html += '<table class="bond-table">\n'
    table_html += '<caption class="table-caption">Average Bond Lengths (A)</caption>\n'
    table_html += '<thead><tr><th>Bond Type</th><th>Average Length</th></tr></thead>\n'
    table_html += '<tbody>'
    for bond_type, avg_length in avg_bond_lengths.items():
        table_html += f'<tr><td>{bond_type}</td><td>{avg_length:.2f}</td></tr>\n'
    table_html += '</tbody></table>\n'
    table_html += '<hr>\n'
    table_html += '</div>\n'
    return table_html


# generate HTML file for all structures with structure index. Use table format
html_str = '''
<html>
<head>
    <title>Bond Lengths</title>
    <meta charset="UTF-8">
    <style>
        .table-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 20px;
        }
        hr {
  border-top: 2px solid black;
  margin: 10px 0;
}
.bond-table tbody tr {
  border-bottom: 1px solid #ddd;
}

        .structure-image {
            display: block;
            margin: auto;
            height: 200px;
            width: auto;
        }

        .bond-table {
            border-collapse: collapse;
            width: 100%;
        }

        .bond-table th, .bond-table td {
            padding: 10px;
            text-align: center;
        }

        .bond-table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }

        .table-caption {
            font-style: italic;
            font-weight: bold;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
'''

for i in range(len(structures)):
    html_str += get_bond_length_table(structures[i], i)
    html_str += ' '

html_str += '''
</body>
</html>
'''

filename = 'bond_lengths_rand.html'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename

# save HTML to file
with open('./data/bond_lengths_rand.html', 'w') as f:
    f.write(html_str)
#now repeat with structures2 and generate a new HTML file called bond_lengths_opt.html
# generate HTML file for all structures with structure index. Use table format
html_str = '''
<html>
<head>
    <title>Bond Lengths</title>
    <meta charset="UTF-8">
    <style>
        .table-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 20px;
        }
        hr {
  border-top: 2px solid black;
  margin: 10px 0;
}
.bond-table tbody tr {

  border-bottom: 1px solid #ddd;
} 

        .structure-image {
            display: block; 
            margin: auto;
            height: 200px;
            width: auto;
        }

        .bond-table {
            border-collapse: collapse;
            width: 100%;
        }

        .bond-table th, .bond-table td {
            padding: 10px;
            text-align: center; 
        }

        .bond-table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
      
        .table-caption {
            font-style: italic;
            font-weight: bold;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
'''
def get_bond_length_table2(structure, i):
    # get bond lengths for the structure
    bond_lengths = get_bonds(structure)
    # calculate average bond length for each bond type
    avg_bond_lengths = get_avg_bond_length(bond_lengths)

    # create table HTML
    table_html = f'<div class="table-container">\n'
    table_html += f'<h2 class="table-title">Optimized structure {i}</h2>\n'
    table_html += f'<div class="image-container"><img src="{os.path.join("images", "opt", f"{i}.png")}" alt="Structure {i}" class="structure-image"></div>\n'
    table_html += '<table class="bond-table">\n'
    table_html += '<caption class="table-caption">Average Bond Lengths (A)</caption>\n'
    table_html += '<thead><tr><th>Bond Type</th><th>Average Length</th></tr></thead>\n'
    table_html += '<tbody>'
    for bond_type, avg_length in avg_bond_lengths.items():
        table_html += f'<tr><td>{bond_type}</td><td>{avg_length:.2f}</td></tr>\n'
    table_html += '</tbody></table>\n'
    table_html += '<hr>\n'
    table_html += '</div>\n'
    return table_html
for i in range(len(structures2)):
    html_str += get_bond_length_table2(structures2[i], i)
    html_str += ' '

html_str += '''
</body>
</html>

'''
filename = 'bond_lengths_opt.html'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the xyz_rnd_str file
filepath = str(ab.parent) + '/data/' + filename
# save HTML to file
with open('./data/bond_lengths_opt.html', 'w') as f:
    f.write(html_str)

#save bond lengths to a csv file with columns: structure index, bond type, average bond length for structures dictionary
with open('bond_lengths_opt.csv', 'w') as f:
    f.write('structure index,bond type,average bond length,\n')

    for i in range(len(structures2)):
        bond_lengths = get_bonds(structures2[i])
        avg_bond_lengths = get_avg_bond_length(bond_lengths)
        for bond_type, avg_length in avg_bond_lengths.items():
            f.write(f'{i},{bond_type},{avg_length:.2f},\n')
            
#save bond lengths to a csv file with columns: structure index, bond type, average bond length for structures dictionary
with open('bond_lengths_rnd.csv', 'w') as f:
    f.write('structure index,bond type,average bond length,\n')

    for i in range(len(structures)):
        bond_lengths = get_bonds(structures[i])
        avg_bond_lengths = get_avg_bond_length(bond_lengths)
        for bond_type, avg_length in avg_bond_lengths.items():
            f.write(f'{i},{bond_type},{avg_length:.2f},\n')
            
filename = 'opt_energies'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the opt_energies file
filepath = str(ab.parent) + '/data/' + filename

#for each structure index, get the energy from corresponding line in the opt_energies file
energies = []
with open('./data/opt_energies', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        energies.append(float(line[0]))


filename = 'maxbfgs'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the maxbfgs file
filepath = str(ab.parent) + '/data/' + filename

#for each structure index, get the bfgs from corresponding line in the maxbfgs file
bfgs = []
with open('./data/maxbfgs', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        bfgs.append(float(line[0]))


#convert energies list to pandas dataframe
energies_df = pd.DataFrame(energies, columns=['energy'])
# add structure index column
energies_df['structure index'] = energies_df.index
#reorder columns
energies_df = energies_df[['structure index', 'energy']]
#print(energies_df)

#load bond_lengths_opt.csv into pandas dataframe
bond_lengths_df = pd.read_csv('bond_lengths_opt.csv')
#merge bond_lengths_df and energies_df on structure index
merged_df = pd.merge(bond_lengths_df, energies_df, on='structure index')
#eliminate Unnamed: 3 column
merged_df = merged_df.drop(columns=['Unnamed: 3'])
#print(merged_df)
#save merged_df to csv file
merged_df.to_csv('bond_lengths_opt_energies_m.csv', index=False)
#convert bfgs list to pandas dataframe
bfgs_df = pd.DataFrame(bfgs, columns=['bfgs'])
# add structure index column
bfgs_df['structure index'] = bfgs_df.index
#reorder columns
bfgs_df = bfgs_df[['structure index', 'bfgs']]
#print(bfgs_df)

#load bond_lengths_opt_energies_m.csv into pandas dataframe
bond_lengths_opt_energies_df = pd.read_csv('bond_lengths_opt_energies_m.csv')
#merge bond_lengths_opt_energies_df and bfgs_df on structure index
merged_df = pd.merge(bond_lengths_opt_energies_df, bfgs_df, on='structure index')
#eliminate Unnamed: 3 column
#merged_df = merged_df.drop(columns=['Unnamed: 3'])
#print(merged_df)
#save merged_df to csv file
merged_df.to_csv('bond_lengths_opt_energies_bfgs_mm.csv', index=False)








#plot graph between bond length and energy for each bond type from merged_df
#import seaborn
import seaborn as sns


#plot histogram of bond lengths for each bond type from merged_df
g = sns.displot(
    data=merged_df,
    x="average bond length", col="bond type", hue="bond type", kind="kde", fill=True, common_norm=False
)
g.set_axis_labels("Average Bond Length (A)", "frequency")
g.set_titles("{col_name}")
g.savefig('bond_lengths_opt_hist.png')




#save bond lengths to a csv file with columns: structure index, bond type, average bond length for structures dictionary
with open('bond_lengths_rnd.csv', 'w') as f:
    f.write('structure index,bond type,average bond length,\n')

    for i in range(len(structures)):
        bond_lengths = get_bonds(structures[i])
        avg_bond_lengths = get_avg_bond_length(bond_lengths)
        for bond_type, avg_length in avg_bond_lengths.items():
            f.write(f'{i},{bond_type},{avg_length:.2f},\n')
            
filename = 'opt_energies'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the opt_energies file
filepath = str(ab.parent) + '/data/' + filename

#for each structure index, get the energy from corresponding line in the opt_energies file
energies = []
with open('./data/opt_energies', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        energies.append(float(line[0]))


filename = 'maxbfgs'
#find absolute path of current directory
ab= pathlib.Path().absolute()
#filepath is one folder up from current directory and then into the data folder and then into the maxbfgs file
filepath = str(ab.parent) + '/data/' + filename

#for each structure index, get the bfgs from corresponding line in the maxbfgs file
bfgs = []
with open('./data/maxbfgs', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        bfgs.append(float(line[0]))


#convert energies list to pandas dataframe
energies_df = pd.DataFrame(energies, columns=['energy'])
# add structure index column
energies_df['structure index'] = energies_df.index
#reorder columns
energies_df = energies_df[['structure index', 'energy']]
#print(energies_df)

#load bond_lengths_opt.csv into pandas dataframe
bond_lengths_df = pd.read_csv('bond_lengths_rnd.csv')
#merge bond_lengths_df and energies_df on structure index
merged_df = pd.merge(bond_lengths_df, energies_df, on='structure index')
#eliminate Unnamed: 3 column
merged_df = merged_df.drop(columns=['Unnamed: 3'])
#print(merged_df)
#save merged_df to csv file
merged_df.to_csv('bond_lengths_rnd_energies_m.csv', index=False)
#convert bfgs list to pandas dataframe
bfgs_df = pd.DataFrame(bfgs, columns=['bfgs'])
# add structure index column
bfgs_df['structure index'] = bfgs_df.index
#reorder columns
bfgs_df = bfgs_df[['structure index', 'bfgs']]
#print(bfgs_df)

#load bond_lengths_opt_energies_m.csv into pandas dataframe
bond_lengths_opt_energies_df = pd.read_csv('bond_lengths_rnd_energies_m.csv')
#merge bond_lengths_opt_energies_df and bfgs_df on structure index
merged_df = pd.merge(bond_lengths_opt_energies_df, bfgs_df, on='structure index')
#eliminate Unnamed: 3 column
#merged_df = merged_df.drop(columns=['Unnamed: 3'])
#print(merged_df)
#save merged_df to csv file
merged_df.to_csv('bond_lengths_rnd_energies_bfgs_mm.csv', index=False)

#plot graph between bond length and energy for each bond type from merged_df
sns.set_theme(style="darkgrid")
g = sns.relplot(
    data=merged_df,
    x="average bond length", y="energy", col="bond type", style="bond type",
    #kind="scatter", height=4, aspect=.7, facet_kws=dict(sharex=False)
    #use bfgs as heatmap
    kind="scatter", height=4, aspect=0.7, facet_kws=dict(sharex=False), hue="bfgs", palette="ch:r=-.2,d=.3_r"
    #use dots instead of lines
    #kind="scatter", height=4, aspect=1.2, facet_kws=dict(sharex=False)
)
g.set_axis_labels("Average Bond Length (A)", "Energy (eV)")
g.set_titles("{col_name}")
g.savefig('bond_lengths_rnd_energies.png')

g = sns.displot(
    data=merged_df,
    x="average bond length", col="bond type", hue="bond type", kind="kde", fill=True, common_norm=False
)
g.set_axis_labels("Average Bond Length (A)", "frequency")
g.set_titles("{col_name}")
g.savefig('bond_lengths_rnd_hist.png')


#create html file to dsiplay bond_lengths_rnd_hist.png, bond_lengths_rnd_energies.png and bond_lengths_opt_hist.png using <img> tag
import os

html_content = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Bond Length Optimization Plots</title>
    <style>
      body {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        background-color: #f2f2f2;
        margin: 0;
        padding: 0;
        font-size: 18px;
      }

      .container {
        max-width: 1080px;
        margin: 0 auto;
        padding: 20px;
      }

      h1 {
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
      }

      .plot-img {
        display: block;
        margin: 0 auto;
        max-width: 100%;
        cursor: pointer;
      }

      .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.9);
      }

      .modal-content {
        margin: auto;
        display: block;
        max-width: 90%;
        max-height: 90%;
      }

      .close {
        color: #fff;
        position: absolute;
        top: 0;
        right: 25px;
        font-size: 35px;
        font-weight: bold;
        transition: 0.3s;
      }

      .close:hover,
      .close:focus {
        color: #bbb;
        text-decoration: none;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>&#x1F6C8  Click on plots to open and save.</h1>
      <h1><u>Initial (Random) Bond Lengths Histograms</u></h1>
      <img src="bond_lengths_rnd_hist.png" alt="bond lengths histograms" class="plot-img" onclick="showModal(this)">
      <h1><u>Optimized Bond Lengths Histograms</u></h1>
      <img src="bond_lengths_opt_hist.png" alt="bond lengths histograms" class="plot-img" onclick="showModal(this)">
      <h1><u>Initial Bond Lengths vs. Optimized Energy with BFGS Heatmap</u></h1>
      <img src="bond_lengths_rnd_energies.png" alt="bond lengths vs. energy" class="plot-img" onclick="showModal(this)">
    </div>


 <div id="myModal" class="modal" onclick="closeModal(event)">
      <span class="close" onclick="closeModal(event)">&times;</span>
      <img class="modal-content" id="modalImg">
    </div>
    <script>
      function showModal(img) {
        var modal = document.getElementById("myModal");
        var modalImg = document.getElementById("modalImg");
        modal.style.display = "block";
        modalImg.src = img.src;
      }

      function closeModal() {
        var modal = document.getElementById("myModal");
        modal.style.display = "none";
      }
    </script>
  </body>
</html>


"""

with open("plots.html", "w") as f:
    f.write(html_content)



#delete all csv files in one directory above
import os
import glob
os.chdir('..')
files = glob.glob('*.csv')
for f in files:
    os.remove(f)

#delete files znh_rand_delta, znh_opt_delta,oh_rand_delta,oh_opt_delta,zn_rand_delta,zn_opt_delta,zno_rand_delta,zno_opt_delta
import os
import glob
files = glob.glob('znh_rand_delta')
for f in files:
    os.remove(f)

files = glob.glob('znh_opt_delta')
for f in files:
    os.remove(f)

files = glob.glob('oh_rand_delta')
for f in files:
    os.remove(f)

files = glob.glob('oh_opt_delta')
for f in files:
    os.remove(f)

files = glob.glob('zn_rand_delta')
for f in files:
    os.remove(f)

files = glob.glob('zn_opt_delta')
for f in files:
    os.remove(f)

files = glob.glob('zno_rand_delta')
for f in files:
    os.remove(f)

files = glob.glob('zno_opt_delta')
for f in files:
    os.remove(f)

    