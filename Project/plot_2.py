"""
==========
Kernel PCA vs PCA
==========

This example shows PCA and Kernel PCA in motion compression  

"""
print(__doc__)

# Authors: Mathieu Blondel
#          Andreas Mueller
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
import csv
import math


from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles

#change some parameters before running each amc file
Numframes = 2180
infile = "OriginalMotions/55_02_edit.amc" # motion file to be read
read_fileName = "DecompressedMotions/55_02_edit_NPCA.amc" 
NumComponentsForNormalPCA = 10;
#############################################readfile
def writefile(c ): 
    print "writing..."   
    
    file = open(read_fileName, "w")
    for i in range(Numframes):
        
        file.write(str(i+1) + "\n")
        file.write("root"+ ' ' +str(c[i][0])+ ' ' +str(c[i][1])+ ' ' +str(c[i][2])+ ' ' +str(c[i][3])+ ' ' +str(c[i][4])+ ' ' +str(c[i][5])+ "\n")
        file.write("lhipjoint"+ ' ' +str(c[i][6])+ ' ' +str(c[i][7])+ ' ' + str(c[i][8])+ "\n")
        file.write("lfemur"+ ' ' +str(c[i][9])+ ' ' +str(c[i][10])+ ' ' + str(c[i][11])+ "\n")
        file.write("ltibia"+ ' ' +str(c[i][12])+ ' ' +str(c[i][13])+ ' ' + str(c[i][14])+ "\n")
        file.write("lfoot"+ ' ' +str(c[i][15])+ ' ' +str(c[i][16])+ ' ' + str(c[i][17])+ "\n")
        file.write("ltoes"+ ' ' +str(c[i][18])+ ' ' +str(c[i][19])+ ' ' + str(c[i][20])+ "\n")
        file.write("rhipjoint"+ ' ' +str(c[i][21])+ ' ' +str(c[i][22])+ ' ' + str(c[i][23])+ "\n")
        file.write("rfemur"+ ' ' +str(c[i][24])+ ' ' +str(c[i][25])+ ' ' + str(c[i][26])+ "\n")
        file.write("rtibia"+ ' ' +str(c[i][27])+ ' ' +str(c[i][28])+ ' ' + str(c[i][29])+ "\n")
        file.write("rfoot"+ ' ' +str(c[i][30])+ ' ' +str(c[i][31])+ ' ' + str(c[i][32])+ "\n")
        file.write("rtoes"+ ' ' +str(c[i][33])+ ' ' +str(c[i][34])+ ' ' + str(c[i][35])+ "\n")
        file.write("lowerback"+ ' ' +str(c[i][36])+ ' ' +str(c[i][37])+ ' ' + str(c[i][38])+ "\n")
        file.write("upperback"+ ' ' +str(c[i][39])+ ' ' +str(c[i][40])+ ' ' + str(c[i][41])+ "\n")
        file.write("thorax"+ ' ' +str(c[i][42])+ ' ' +str(c[i][43])+ ' ' + str(c[i][44])+ "\n")
        file.write("lowerneck"+ ' ' +str(c[i][45])+ ' ' +str(c[i][46])+ ' ' + str(c[i][47])+ "\n")
        file.write("upperneck"+ ' ' +str(c[i][48])+ ' ' +str(c[i][49])+ ' ' + str(c[i][50])+ "\n")
        file.write("head"+ ' ' +str(c[i][51])+ ' ' +str(c[i][52])+ ' ' + str(c[i][53])+ "\n")
        file.write("lclavicle"+ ' ' +str(c[i][54])+ ' ' +str(c[i][55])+ ' ' + str(c[i][56])+ "\n")
        file.write("lhumerus"+ ' ' +str(c[i][57])+ ' ' +str(c[i][58])+ ' ' + str(c[i][59])+ "\n")
        file.write("lradius"+ ' ' +str(c[i][60])+ ' ' +str(c[i][61])+ ' ' + str(c[i][62])+ "\n")
        file.write("lwrist"+ ' ' +str(c[i][63])+ ' ' +str(c[i][64])+ ' ' + str(c[i][65])+ "\n")
        file.write("lhand"+ ' ' +str(c[i][66])+ ' ' +str(c[i][67])+ ' ' + str(c[i][68])+ "\n")
        file.write("lfingers"+ ' ' +str(c[i][69])+ ' ' +str(c[i][70])+ ' ' + str(c[i][71])+ "\n")
        file.write("lthumb"+ ' ' +str(c[i][72])+ ' ' +str(c[i][73])+ ' ' + str(c[i][74])+ "\n")
        file.write("rclavicle"+ ' ' +str(c[i][75])+ ' ' +str(c[i][76])+ ' ' + str(c[i][77])+ "\n")
        file.write("rhumerus"+ ' ' +str(c[i][78])+ ' ' +str(c[i][79])+ ' ' + str(c[i][80])+ "\n")
        file.write("rradius"+ ' ' +str(c[i][81])+ ' ' +str(c[i][82])+ ' ' + str(c[i][83])+ "\n")
        file.write("rwrist"+ ' ' +str(c[i][84])+ ' ' +str(c[i][85])+ ' ' + str(c[i][86])+ "\n")
        file.write("rhand"+ ' ' +str(c[i][87])+ ' ' +str(c[i][88])+ ' ' + str(c[i][89])+ "\n")
        file.write("rfingers"+ ' ' +str(c[i][90])+ ' ' +str(c[i][91])+ ' ' + str(c[i][92])+ "\n")
        file.write("rthumb"+ ' '+str(c[i][93])+ ' ' +str(c[i][94])+ ' ' + str(c[i][95])+ "\n")

    file.close()

    print "done for writing"

def readfile():
    print "reading ... "
    
    outfile = "others/03.amc" # the median motion file (no use for the result)

    delete_list = [":FULLY-SPECIFIED", ":DEGREES", "root", "lhipjoint", "lfemur", "ltibia", "lfoot", "ltoes", "rhipjoint", "rfemur", "rtibia",
                   "rfoot", "rtoes", "lowerback", "upperback", "thorax", "lowerneck", "upperneck", "head", "lclavicle", "lhumerus", "lradius", "lwrist", "lhand", "lfingers", "lthumb", "rclavicle", "rhumerus", "rradius", "rwrist", "rhand", "rfingers", "rthumb"]   
    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()

    #Numframes = 2000
    with open(outfile, 'rt') as csvfile:
        data = list(csv.reader(csvfile, delimiter = " "))
    data = data[:32*Numframes] 

    b = []
    for i in data:
        if len(i) != 1:
            for j in i:
                try:
                    if abs(float(j)) >= int(abs(float(j))):
                        
                        b = b + [float(j)]
                        
                        
                except:
                    a = 0
    print np.shape(b)               
    c = np.reshape(b,(Numframes,96))

    print "done for reading"
    return c
################################################ Data compression and decompression

a=readfile()
print a.shape

print "compressing ... "

np.random.seed(0)
X, y = make_circles(n_samples=400, factor=.3, noise=.05)
X = a
###############Kernel PCA operations
#note for gamma: (gamma: default Kernel coefficient for rbf, poly and sigmoid kernels)

# kernel 1: linear kernel others
kpca = KernelPCA(kernel="linear", fit_inverse_transform=True)
plotName = "linear"

# kernel 2: polynomial kernel (default degree 3)
#kpca = KernelPCA(kernel="poly", fit_inverse_transform=True)
#plotName = "poly"

# kernel 3: rbf kernel
#kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True)
#plotName = "rbf"

# kernel 4: cosine kernel
#kpca = KernelPCA(kernel="cosine", fit_inverse_transform=True)
#plotName = "cosine"

X_kpca = kpca.fit_transform(X)
X_Kernel_back = kpca.inverse_transform(X_kpca)

###############Normal PCA operations
#pca = PCA(n_components = 20)
pca = PCA()
X_pca = pca.fit_transform(X)
X_Normal_back = pca.inverse_transform(X_pca)
#inverse_transform
############### Plot Original data

plt.figure("Compare" + plotName + " kpca with PCA")
plt.subplot(2, 2, 1, aspect='equal')
plt.title("Original space")
reds = y == 0
blues = y == 1

plt.scatter(X[:, 0], X[:, 1], c="red",
            s=20, edgecolor='k')
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")


##############Projection by PCA
plt.subplot(2, 2, 2, aspect='equal')
plt.scatter(X_pca[:, 0], X_pca[:, 1], c="red",
            s=20, edgecolor='k')
plt.title("Projection by PCA")
plt.xlabel("1st principal component")
plt.ylabel("2nd component")

###############Projection by KernelPCA
plt.subplot(2, 2, 3, aspect='equal')

plt.scatter(X_kpca[:, 0], X_kpca[:, 1], c="blue",
            s=20, edgecolor='k')
plt.title("Projection by KPCA")
plt.xlabel("1st principal component in space induced by $\phi$")
plt.ylabel("2nd component")

################Inverse transform by KernelPCA
plt.subplot(2, 2, 4, aspect='equal')
plt.scatter(X_Kernel_back[:, 0], X_Kernel_back[:, 1], c="blue",
            s=20, edgecolor='k')
plt.title("The data after inverse transform")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")

plt.subplots_adjust(0.02, 0.10, 0.98, 0.94, 0.04, 0.35)

print "done compressing. "
#####################################################write it out
writefile(X_Kernel_back)
#writefile(X_Normal_back)
################Analyze kernelpca pca 

plt.show()


