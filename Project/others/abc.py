import csv
import math
import numpy as np

def readfile():
    infile = "02.amc"
    outfile = "03.amc"

    delete_list = ["root", "lowerback", "upperback", "thorax", "lowerneck", "upperneck", "head", "rclavicle", "rhumerus",
                   "rradius", "rwrist", "rhand", "rfingers", "rthumb", "lclavicle", "lhumerus", "lradius", "lwrist", "lhand", "lfingers", "lthumb", "rfemur", "rtibia", "rfoot", "rtoes", "lfemur", "ltibia", "lfoot", "ltoes"]
    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()


    with open("03.amc", 'rt') as csvfile:
        data = list(csv.reader(csvfile, delimiter = " "))
    data = data[:30*32] 

    b = []
    for i in data:
        if len(i) != 1:
            for j in i:
                try:
                    if abs(float(j)) > int(abs(float(j))):
                        
                        b = b + [float(j)]
                        
                        
                except:
                    a = 0
                   
    c = np.reshape(b,(32,62))
    print c
    return c
