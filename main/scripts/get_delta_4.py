"""
Script that calculates the delta parameter for random and optimised structures
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


import re
from periodictable import elements


from scipy.spatial import distance
import numpy as np
import math
i=0
arrays_opt = []
arrays_rand = []

with open("./data/start_times", 'r') as fp:
    linees = len(fp.readlines())
    print('Total Number of lines:', linees)
arrays_opt_bl = np.array([])
arrays_rand_bl = np.array([])

delta = 0
with open("./data/xyz_opt_str") as f:
    yourList = []
    for line in f:
        if line != '*\n':
            line = line.strip().split()
            line = [float(x) for x in line]
            yourList.append(line)

        else:
            yourArray = np.array(yourList)
            yourList = []
            arrays_opt.append(yourArray)

#print(arrays_opt[0][:][:])                    #for the first opt str
print("length = ", len(arrays_opt))

print("\n")

with open("./data/xyz_rnd_str") as f2:
    yourList2 = []
    for line in f2:
        if line != '*\n':
            line = line.strip().split()
            line = [float(x) for x in line]
            yourList2.append(line)

        else:
            yourArray2 = np.array(yourList2)
            yourList2 = []
            arrays_rand.append(yourArray2)

#print(arrays_rand[0][:][:])                     #for the first rand str
print("length = ", len(arrays_rand))

structure_dictionary_rand_list = []

for array in arrays_rand:
    structure_dictionary_rand = {'Zn': [],
                            'H': [],
                            'O': []}

    for row in array:
        if round(row[-1]) == 16:
            structure_dictionary_rand['O'].append(row[:3])

        elif round(row[-1])== 65:
            structure_dictionary_rand['Zn'].append(row[:3])

        else:
            structure_dictionary_rand['H'].append(row[:3])

    structure_dictionary_rand['O'] = np.array(structure_dictionary_rand['O'])
    structure_dictionary_rand['Zn'] = np.array(structure_dictionary_rand['Zn'])
    structure_dictionary_rand['H'] = np.array(structure_dictionary_rand['H'])
    structure_dictionary_rand_list.append(structure_dictionary_rand)

#print(structure_dictionary_rand_list[(linees-1)]['Zn'])
#print(structure_dictionary_rand_list[10]['O'][0])
#print(structure_dictionary_rand_list[10]['H'])


zno_r = open("zno_rand_delta", 'w')

oh_r = open("oh_rand_delta", 'w')

znh_r = open("znh_rand_delta", 'w')

znzn_r = open("znzn_rand_delta", 'w')

for i in range((linees-1)):
    for j in range(len(structure_dictionary_rand_list[i]['Zn'])):
            #print(structure_dictionary_rand_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_rand_list[i]['O'])):
                dst=np.linalg.norm(structure_dictionary_rand_list[i]['Zn'][j] - structure_dictionary_rand_list[i]['O'][k])
                arrays_rand_bl=np.append(arrays_rand_bl,dst)
    delta = np.max(arrays_rand_bl[np.nonzero(arrays_rand_bl)]) - np.min(arrays_rand_bl[np.nonzero(arrays_rand_bl)])
    arrays_rand_bl=[]
    print('rand str ' + str(i) + ' Zn-O min-max delta = ' + str(delta))
    zno_r.write(str(delta)+'\n')
    
    
    
for i in range((linees-1)):
    for j in range(len(structure_dictionary_rand_list[i]['Zn'])):
            #print(structure_dictionary_rand_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_rand_list[i]['Zn'])):
                dst=np.linalg.norm(structure_dictionary_rand_list[i]['Zn'][j] - structure_dictionary_rand_list[i]['Zn'][k])
                arrays_rand_bl=np.append(arrays_rand_bl,dst)
    delta = np.max(arrays_rand_bl[np.nonzero(arrays_rand_bl)]) - np.min(arrays_rand_bl[np.nonzero(arrays_rand_bl)])
    arrays_rand_bl=[]
    print('rand str ' + str(i) + ' Zn-Zn min-max delta = ' + str(delta))
    znzn_r.write(str(delta)+'\n')
    
    
for i in range((linees-1)):
    for j in range(len(structure_dictionary_rand_list[i]['Zn'])):
            #print(structure_dictionary_rand_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_rand_list[i]['H'])):
                dst=np.linalg.norm(structure_dictionary_rand_list[i]['Zn'][j] - structure_dictionary_rand_list[i]['H'][k])
                arrays_rand_bl=np.append(arrays_rand_bl,dst)
    delta = np.max(arrays_rand_bl[np.nonzero(arrays_rand_bl)]) - np.min(arrays_rand_bl[np.nonzero(arrays_rand_bl)])
    arrays_rand_bl=[]
    print('rand str ' + str(i) + ' Zn-H min-max delta = ' + str(delta))
    znh_r.write(str(delta)+'\n')
    
    
    
for i in range((linees-1)):
    for j in range(len(structure_dictionary_rand_list[i]['O'])):
            #print(structure_dictionary_rand_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_rand_list[i]['H'])):
                dst=np.linalg.norm(structure_dictionary_rand_list[i]['O'][j] - structure_dictionary_rand_list[i]['H'][k])
                arrays_rand_bl=np.append(arrays_rand_bl,dst)
    delta = np.max(arrays_rand_bl[np.nonzero(arrays_rand_bl)]) - np.min(arrays_rand_bl[np.nonzero(arrays_rand_bl)])
    arrays_rand_bl=[]
    print('rand str ' + str(i) + ' O-H min-max delta = ' + str(delta))
    oh_r.write(str(delta)+'\n')
    

structure_dictionary_opt_list = []

for array in arrays_opt:
    structure_dictionary_opt = {'Zn': [],
                            'H': [],
                            'O': []}

    for row in array:
        if round(row[-1]) == 16:
            structure_dictionary_opt['O'].append(row[:3])

        elif round(row[-1])== 65:
            structure_dictionary_opt['Zn'].append(row[:3])

        else:
            structure_dictionary_opt['H'].append(row[:3])

    structure_dictionary_opt['O'] = np.array(structure_dictionary_opt['O'])
    structure_dictionary_opt['Zn'] = np.array(structure_dictionary_opt['Zn'])
    structure_dictionary_opt['H'] = np.array(structure_dictionary_opt['H'])
    structure_dictionary_opt_list.append(structure_dictionary_opt)

#print(structure_dictionary_opt_list[(linees-1)]['Zn'])
#print(structure_dictionary_opt_list[10]['O'][0])
#print(structure_dictionary_opt_list[10]['H'])


zno_o = open("zno_opt_delta", 'w')

oh_o = open("oh_opt_delta", 'w')

znh_o = open("znh_opt_delta", 'w')

znzn_o = open("znzn_opt_delta", 'w')


for i in range((linees-1)):
    for j in range(len(structure_dictionary_opt_list[i]['Zn'])):
            #print(structure_dictionary_opt_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_opt_list[i]['O'])):
                dst=np.linalg.norm(structure_dictionary_opt_list[i]['Zn'][j] - structure_dictionary_opt_list[i]['O'][k])
                arrays_opt_bl=np.append(arrays_opt_bl,dst)
    delta = np.max(arrays_opt_bl[np.nonzero(arrays_opt_bl)]) - np.min(arrays_opt_bl[np.nonzero(arrays_opt_bl)])
    arrays_opt_bl=[]
    print('opt str ' + str(i) + ' Zn-O min-max delta = ' + str(delta))
    zno_o.write(str(delta)+'\n')
    
    
    
for i in range((linees-1)):
    for j in range(len(structure_dictionary_opt_list[i]['Zn'])):
            #print(structure_dictionary_opt_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_opt_list[i]['Zn'])):
                dst=np.linalg.norm(structure_dictionary_opt_list[i]['Zn'][j] - structure_dictionary_opt_list[i]['Zn'][k])
                arrays_opt_bl=np.append(arrays_opt_bl,dst)
    delta = np.max(arrays_opt_bl[np.nonzero(arrays_opt_bl)]) - np.min(arrays_opt_bl[np.nonzero(arrays_opt_bl)])
    arrays_opt_bl=[]
    print('opt str ' + str(i) + ' Zn-Zn min-max delta = ' + str(delta))
    znzn_o.write(str(delta)+'\n')
    
    
for i in range((linees-1)):
    for j in range(len(structure_dictionary_opt_list[i]['Zn'])):
            #print(structure_dictionary_opt_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_opt_list[i]['H'])):
                dst=np.linalg.norm(structure_dictionary_opt_list[i]['Zn'][j] - structure_dictionary_opt_list[i]['H'][k])
                arrays_opt_bl=np.append(arrays_opt_bl,dst)
    delta = np.max(arrays_opt_bl[np.nonzero(arrays_opt_bl)]) - np.min(arrays_opt_bl[np.nonzero(arrays_opt_bl)])
    arrays_opt_bl=[]
    print('opt str ' + str(i) + ' Zn-H min-max delta = ' + str(delta))
    znh_o.write(str(delta)+'\n')
    
    
    
for i in range((linees-1)):
    for j in range(len(structure_dictionary_opt_list[i]['O'])):
            #print(structure_dictionary_opt_list[i]['Zn'][j])
            for k in range(len(structure_dictionary_opt_list[i]['H'])):
                dst=np.linalg.norm(structure_dictionary_opt_list[i]['O'][j] - structure_dictionary_opt_list[i]['H'][k])
                arrays_opt_bl=np.append(arrays_opt_bl,dst)
    delta = np.max(arrays_opt_bl[np.nonzero(arrays_opt_bl)]) - np.min(arrays_opt_bl[np.nonzero(arrays_opt_bl)])
    arrays_opt_bl=[]
    print('opt str ' + str(i) + ' O-H min-max delta = ' + str(delta))
    oh_o.write(str(delta)+'\n')
