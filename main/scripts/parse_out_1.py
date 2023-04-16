"""
Script extracts position block of random and optimized for abnv_get_xyzm.py
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

#| Usage note : Last entry (BFGS 0 to BFGS X) will be ignored |

#input arg as arguement
import sys
arg = int(float(sys.argv[1])+1)
print("woooooooo"+str(arg))
import linecache as lc

with open("./data/bh.py.out") as big_file:  # scan file to find the positions
    BFGS_Zero_lno = []
    pos_BFGS_Zero_lno = []
    pos_rnd_str_lno = [] # contains bfgs before bfgs 0 value
    BFGS_prev_lno = []
    
    isAfterZero = False

    prevNum = -1
    prev_BFGS = -1
    prev_array_BFGS = [-1,-1] #consecutive BFGS lines 
    for num, string in enumerate(big_file):
        
        if string.startswith("BFGS:"):
            prev_array_BFGS[0] = prev_array_BFGS[1]
            prev_array_BFGS[1] = num

        if string.startswith("Positions:"):

            if isAfterZero:
                pos_BFGS_Zero_lno.append(num + 1)
                isAfterZero = False

            prevNum = num

        if string.startswith("BFGS:    0"):
            BFGS_Zero_lno.append(num + 1)
            
            isAfterZero = True
            
            if prev_array_BFGS[0] != -1: # to skip the first 0 value for prev_num
                BFGS_prev_lno.append(prev_array_BFGS[0] + 1) # do something with first vlaue   
            if len(BFGS_Zero_lno) > 1:
                pos_rnd_str_lno.append(prevNum + 1)

#### read positions and write to resp. files ####
with open("./data/start_times", 'w') as BFGSzeroFile:
    for num in BFGS_Zero_lno:
        line = lc.getline("./data/bh.py.out", num)
        BFGSzeroFile.write(line)

with open("./data/pos_Rand_structures", 'w') as posRndFile:
    for num in pos_BFGS_Zero_lno:
        for i in range(1, int(arg)):
            line = lc.getline("./data/bh.py.out", num + i)
            posRndFile.write(line)
        posRndFile.write("***\n")

with open("./data/pos_Opt_structures", 'w') as posOptFile: # still misses last optimised str, misses copying , deleted last rand,opt str set to fix, actually delted the rand, bc opt was unavailable. #here
    for num in pos_rnd_str_lno:
        for i in range(1, int(arg)):
            line = lc.getline("./data/bh.py.out", num + i)
            posOptFile.write(line)
        posOptFile.write("***\n")
        
        
with open("./data/opt_energies", 'w') as BFGSprevFile:
    for num in BFGS_prev_lno:
        line = lc.getline("./data/bh.py.out", num)
        energy = line.split()[3]
        BFGSprevFile.write(energy + "\n")   
        
        
with open("./data/maxbfgs", 'w') as BFGSprevFile:
    for num in BFGS_prev_lno:
        line = lc.getline("./data/bh.py.out", num)
        energy = line.split()[1]
        BFGSprevFile.write(energy + "\n")   
        





with open('./data/pos_Rand_structures') as f1: #here
    lines = f1.readlines()

with open('./data/pos_Rand_structures', 'w') as f2: #here
    f2.writelines(lines[:-int(arg)])
    
times=[]    
    
print(BFGS_prev_lno)
    
    #Calcuation of time interval
    
#with open("start_times") as time_file:
#    for string2 in time_file:
#             string2 = string2.strip().split()
#             times.append(string2)
#print(times[3])
