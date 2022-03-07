#   Aurthor : : Unusual Boyee
#   Date    : : 2022/03/08
#   Concept : : No double writing in file.
#   Mail    : : voperatingsystem@gmail.com
#   Country : : Nepal
'''
    This file is consider as only one program
    Which helps you to write in file line by line by not adding double line
'''
import os
import sys
def funcion1():
    while 1:# we have to be in while loop for taking input
        main_file=open(sys.argv[1],"r")
        marked=0 # we have to mark as the input is in file line already exist
        scanned=input(":- ")
        if not scanned: # to exit if not entered any and pressed return key 
            exit()
        for i in main_file: # we have to check every line of file to compare the line string 
            if i.rstrip("\n")==scanned: # if .rstip is not given it will compare '\n' as with the file line.
                marked=1
        if marked==0: # if marked is zero then we gonna keep input in line
            open(sys.argv[1],"a").writelines("%s\n" % scanned)

#   sys.argv[1] gives file name provided in cmdline
if os.path.isfile(sys.argv[1])==False:
    main_file=open(sys.argv[1],"w")
    funcion1()
else:
    funcion1()
"""
        if main_file.readline()==scanned:
            continue
        else:
            open(sys.argv[1],"a").writelines("%s\n" % scanned)
"""
