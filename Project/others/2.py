import csv
import math
import numpy as np

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
print c[0]

file = open("04.amc", "w")
for i in range(32):
    
    file.write(str(i+1) + "\n")
    file.write("root"+ ' ' +str(c[i][0])+ ' ' +str(c[i][1])+ ' ' +str(c[i][2])+ ' ' +str(c[i][3])+ ' ' +str(c[i][4])+ ' ' +str(c[i][5])+ "\n")
    file.write("lowerback"+ ' ' +str(c[i][6])+ ' ' +str(c[i][7])+ ' ' + str(c[i][8])+ "\n")
    file.write("upperback"+ ' ' +str(c[i][9])+ ' ' +str(c[i][10])+ ' ' + str(c[i][11])+ "\n")
    file.write("thorax"+ ' ' +str(c[i][12])+ ' ' +str(c[i][13])+ ' ' + str(c[i][14])+ "\n")
    file.write("lowerneck"+ ' ' +str(c[i][15])+ ' ' +str(c[i][16])+ ' ' + str(c[i][17])+ "\n")
    file.write("upperneck"+ ' ' +str(c[i][18])+ ' ' +str(c[i][19])+ ' ' + str(c[i][20])+ "\n")
    file.write("head"+ ' ' +str(c[i][21])+ ' ' +str(c[i][22])+ ' ' + str(c[i][23])+ "\n")
    file.write("rclavicle"+ ' ' +str(c[i][24])+ ' ' +str(c[i][25])+ "\n")
    file.write("rhumerus"+ ' ' +str(c[i][26])+ ' ' +str(c[i][27])+ ' ' + str(c[i][28])+ "\n")
    file.write("rradius"+ ' ' +str(c[i][29])+ "\n")
    file.write("rwrist"+ ' ' +str(c[i][30])+ "\n")
    file.write("rhand"+ ' ' +str(c[i][31])+ ' ' + str(c[i][32])+ "\n")
    file.write("rfingers"+ ' ' +str(c[i][33])+ "\n")
    file.write("rthumb"+ ' ' +str(c[i][34])+ ' ' + str(c[i][35])+ "\n")
    file.write("lclavicle"+ ' ' +str(c[i][36])+ ' ' + str(c[i][37])+ "\n")
    file.write("lhumerus"+ ' ' +str(c[i][38])+ ' ' +str(c[i][39])+ ' ' + str(c[i][40])+ "\n")
    file.write("lradius"+ ' ' +str(c[i][41])+ "\n")
    file.write("lwrist"+ ' ' +str(c[i][42])+ "\n")
    file.write("lhand"+ ' ' +str(c[i][43])+ ' ' + str(c[i][44])+ "\n")
    file.write("lfingers"+ ' ' +str(c[i][45])+ "\n")
    file.write("lthumb"+ ' ' +str(c[i][46])+ ' ' + str(c[i][47])+ "\n")
    file.write("rfemur"+ ' ' +str(c[i][48])+ ' ' +str(c[i][49])+ ' ' + str(c[i][50])+ "\n")
    file.write("rtibia"+ ' ' +str(c[i][51])+ "\n")
    file.write("rfoot"+ ' ' +str(c[i][52])+ ' ' + str(c[i][53])+ "\n")
    file.write("rtoes"+ ' ' +str(c[i][54])+ "\n")
    file.write("lfemur"+ ' ' +str(c[i][55])+ ' ' +str(c[i][56])+ ' ' + str(c[i][57])+ "\n")
    file.write("ltibia"+ ' ' +str(c[i][58])+ "\n")
    file.write("lfoot"+ ' ' +str(c[i][59])+ ' ' + str(c[i][60])+ "\n")
    file.write("ltoes"+ ' ' +str(c[i][61])+ "\n")

file.close()

 
    
 

