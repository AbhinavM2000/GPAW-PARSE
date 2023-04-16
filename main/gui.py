import tkinter as tk
from tkinter import ttk
import subprocess
import os
import time
#disable buttons until calculations are finished


# Define the function to execute the Python scripts in the background
def execute_scripts(progress_bar, arg):
    scripts = [ './scripts/parse_out_1.py', './scripts/delta_t_2.py', './scripts/get_xyzm_3.py','./scripts/get_delta_4.py','./scripts/profile_1.py','clean.py']
    total_scripts = len(scripts)
    for index, script in enumerate(scripts):
        #update log with message
        log.config(state='normal')
        log.see(tk.END)
        log.insert(tk.END, 'Executing ' + script + '...\n', 'progress')
        log.see(tk.END)
        log.config(state='disabled')
        subprocess.Popen(['python', script, str(arg)]).wait()
        time.sleep(1)
        progress_bar['value'] = (index + 1) / total_scripts * 100
        progress_bar.update()
    #update log with message when finished
    log.config(state='normal')
    log.see(tk.END)
    log.insert(tk.END, 'Data parsed successfully !\n', 'success')
    log.see(tk.END)
    log.config(state='disabled')
#get absolute path of current directory
path = os.path.dirname(os.path.abspath(__file__))
# Define the function to open files based on user input
def open_file(file_name):
    #os.system("xdg-open " + file_name)
    #if file is html, open in browser, use full path
    if file_name.endswith('.html'):
        #os.system("xdg-open " + path + file_name)
        #use startfile for windows
        os.startfile(path + file_name)
    else:
        #os.system("xdg-open " + path + file_name)
        os.startfile(path + file_name)





# Create the main window
root = tk.Tk()
root.title('File Opener')
import tkinter as tk
from tkinter import ttk
import re
#log messages window built in with existing window
log = tk.Text(root, height=5, width=50)
#make log window uneditable by user
log.config(state='normal')
#make log scrollable
log_scroll = tk.Scrollbar(root)
log_scroll.pack(side=tk.RIGHT, fill=tk.Y)
log_scroll.config(command=log.yview)
log.config(yscrollcommand=log_scroll.set)
#make log colourfull, dark green for success, red for error
log.tag_config('error', foreground='red')
log.tag_config('success', foreground='dark green')
log.tag_config('progress', foreground='blue')
#auto scroll to bottom of log window
log.see(tk.END)
def begin_clicked():
    # input box for the user to enter the chemical formula of the molecule
    formula_str = formula.get()

    pattern = r'([A-Z][a-z]*)(\d*)'

    # find all matches in the formula string
    matches = re.findall(pattern, formula_str)

    # initialize a dictionary to store the element counts
    atom_counts = {}

    try:
        # check if formula string is empty or contains spaces
        formula_str = formula.get()
        if not formula_str or any(char.isspace() for char in formula_str):
            #update log with message
            log.config(state='normal')
            log.insert(tk.END, 'Please enter a valid chemical formula.\n', 'error')
            log.see(tk.END)
            log.config(state='disabled')
            raise ValueError('Invalid formula entered.')
            
        #update log with message
        log.config(state='normal')
        log.insert(tk.END, 'Valid formula entered. Beginning calculations...\n', 'success')
        log.see(tk.END)
        log.config(state='disabled')
        # find all matches in the formula string
        matches = re.findall(pattern, formula_str)

        # initialize a dictionary to store the element counts
        atom_counts = {}

        # loop through the matches and add up the element counts
        for symbol, count_str in matches:
            count = int(count_str) if count_str else 1
            if symbol in atom_counts:
                atom_counts[symbol] += count
            else:
                atom_counts[symbol] = count
        # calculate the total number of atoms
        num_atoms = sum(atom_counts.values())

        # display the number of atoms in the GUI
        num_atoms_label.config(text='Number of atoms in the system: ' + str(num_atoms))
        # update log with message
        log.config(state='normal')
        log.insert(tk.END, 'Number of atoms in the system: ' + str(num_atoms) + '\n', 'success')
        log.see(tk.END)
        log.config(state='disabled')
        open_file1.config(state='disabled')
        open_file2.config(state='disabled')
        execute_scripts(progress_bar,num_atoms)
        # Enable the buttons to open the files
        open_file1.config(state='normal')
        open_file2.config(state='normal')
        open_file3.config(state='normal')
    except ValueError as e:
         # display an error message in the GUI
        num_atoms_label.config(text=str(e))
formula_label = tk.Label(root, text='Chemical formula of system:')
formula_label.pack()
# input box for the user to enter the chemical formula of the molecule
formula = tk.Entry(root, width=50)
#text label above the entry box

#pad the top of the entry box
formula.pack(pady=10)
#make formula box bigger
formula.config(font=('Arial', 12))
formula.insert(0, "---- Enter the chemical formula of the system here (e.g. H2O) ----")

formula.pack()
#clear the box when clicked
formula.bind("<Button-1>", lambda e: formula.delete(0, tk.END))
# Create the BEGIN button
begin_button = tk.Button(root, text='BEGIN', command=begin_clicked)
begin_button.pack()

# show the number of atoms in the molecule in the GUI
num_atoms_label = tk.Label(root, text='')
num_atoms_label.pack()

# Create the progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress_bar.pack()
log.pack()

# Create the information buttons 1. BFGS info 2. Structural info, the buttons open html files
open_file1 = tk.Button(root, text='BFGS INFO', command=lambda: open_file('./data/BFGS.html'))
open_file3 = tk.Button(root, text='PLOTS', command=lambda: open_file('./data/plots.html'))
#if clicked on structural info button, open two options: 1. Optimized structures 2. Initial structures
def open_file2_clicked():
    #open small window
    open_file2_window = tk.Toplevel(root)
    open_file2_window.title('Open file')
    open_file2_window.geometry("200x200")
    open_file2_label = tk.Label(open_file2_window, text="Select:", fg="blue", font="Times 15 bold italic")
    open_file2_label.pack()
    open_file2_button1 = tk.Button(open_file2_window, text='Optimized structures', command=lambda: open_file('./data/bond_lengths_opt.html'))
    #make button bigger
    open_file2_button1.config(height=2, width=20)
    open_file2_button1.pack()
    open_file2_button2 = tk.Button(open_file2_window, text='Initial structures', command=lambda: open_file('./data/bond_lengths_rand.html'))
    open_file2_button2.config(height=2, width=20)
    open_file2_button2.pack()
open_file2 = tk.Button(root, text='STRUCTURAL INFO', command=open_file2_clicked)



# Disable the buttons to open the files until the calculations are finished

#info button to display credits, when clicked opens window with credits
def info_clicked():
    info_window = tk.Tk()
    info_window.title('Credits')
    info_window.geometry("500x500")
    info_label = tk.Label(info_window, text="GPAW PARSER 1.0", fg="blue", font="Times 15 bold italic")
    info_label.pack()
    info_label2 = tk.Label(info_window, text="Created by: abnvm1", fg="blue", font="Times 15 bold italic")
    info_label2.pack()

info_button = tk.Button(root, text='INFO', command=info_clicked)



#look for the .out file in the current directory and display its name in the GUI in the info label
out_file = os.listdir("./data")
for file in out_file:
    if file.endswith(".out"):
        out_file = file + " detected in ./data directory.\n"
        break
    else:
        out_file = "No .out file detected in ./data directory.\n"
#update log with message in green color
log.config(state='normal')
log.insert(tk.END, out_file, 'success')
log.see(tk.END)
log.config(state='disabled')


#make window bigger
root.geometry("500x600")
#make the buttons more visible with padding in between
begin_button.pack(pady=10)
open_file1.config(state='disabled')
open_file2.config(state='disabled')
open_file3.config(state='disabled')
open_file1.pack(pady=10)
open_file2.pack(pady=10)
open_file3.pack(pady=10)

progress_bar.pack(pady=10)
#make buttons bigger
begin_button.config(height=2, width=15)
open_file1.config(height=2, width=15)
open_file2.config(height=2, width=15)
open_file3.config(height=2, width=15)
info_button.config(height=2, width=15)
info_button.pack(pady=10)
info = tk.Label(root, text="GPAW PARSER 1.0", fg="blue", font="Times 15 bold italic")
info.pack(pady=1)



#make progress bar bigger
progress_bar.config(length=500)
#make window unresizable
root.resizable(0,0)








# Start the GUI event loop
root.mainloop()
