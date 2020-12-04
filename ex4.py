import sys
import os
import subprocess as sp

command = ""
file_name = ""
for i in range(len(sys.argv)-1):
    aux = sys.argv[i+1]
    command = command + " " + aux
    file_name = file_name + aux[:-4] + "_"
    print(file_name)
container_command = "python3"+" "+"ex2.py"+command

sp.run(container_command, shell = True)

file_ex3 = file_name[:-1]+".mp4"

ex3_command = "python3"+" "+"ex3.py"+" "+file_ex3

sp.run(ex3_command, shell=True)
