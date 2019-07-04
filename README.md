# PCA

## Project Title:  Motion compression by PCA and Kernel PCA

## Introduction
Principal component analysis (PCA) is a popular tool for linear dimensionality reduction and data compression. Kernel PCA is the nonlinear form of PCA, which is able to exploit more complicated structure of high-dimensional features (Krzanowski, 2000). In this report, we first review the mathematics of PCA and kernel PCA. Then we focus on the compression for motion data using both PCA and kernel PCA, and for kernel PCA we also tried linear kernel and polynomial kernel. By plotting the principal components, we clearly see that PCA and linear-kernel-PCA  have exactly the same pattern; and polynomial-kernel-PCA have similar pattern with PCA and fits the data better. We also imports the decompressed motion data to blender.

## Getting Started

## Prerequisites
	numpy, matplotlib, scipy, csv, sklearn

## Installing
	install numpy: pip install numpy
	install matplotlib: brew install pkg-config
						pip install matplotlib
	install scipy: pip install scipy
	csv: csv is part of python's standard library so you do not need to install it
	install sklearn: pip install -U scikit-learn

## Running the tests
	First, open the folder OriginalMotions.
	For the 02_06.amc, 09_12.amc, 49_04.amc and 55_02.amc files: 
	Run pyhton2 plot_1.py
	for running each file, you should change some parameters.

	For example, if you would like to run 02_06.amc, 
	change the Numframes = 2235
	infle = "OriginalMotions/02_06.amc"
	read_fileName = "DecompressedMotions/02_06_NPCA.amc" #Normal PCA
	Then go to the Kernel PCA operations, 
	delete the hash symbol of #kpca = KernelPCA(kernel="linear", fit_inverse_transform=True),
	and add hash symbols on other Kernel PCA operations
	or
	read_fileName = "DecompressedMotions/02_06_PPCA.amc" #Polynomial Kernel PCA
	Then go to the Kernel PCA operations, 
	delete the hash symbol of #kpca = KernelPCA(kernel="poly", fit_inverse_transform=True),
	and add hash symbols on other Kernel PCA operations
	or 
	read_fileName = "DecompressedMotions/02_06_rbf.amc"  #rbf Kernel PCA
	Then go to the Kernel PCA operations, 
	delete the hash symbol of #kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True)
	and add hash symbols on other Kernel PCA operations


	For the 02_06_edit.amc, 02_06_orig.amc, 09_12_edit.amc, 09_12_orig.amc, 49_04_edit.amc, 49_04_orig.amc, 55_02_edit.amc, 55_02_orig.amc files:
	Run python2 plot_2.py
	for running each file, you should change some parameters.

	For example, if you would like to run 55_02_edit.amc,
	change the Numframes = 2180
	infile = "OriginalMotions/55_02_edit.amc" 
	read_fileName = "DecompressedMotions/55_02_edit_NPCA.amc" #Normal PCA
	Then go to the Kernel PCA operations, 
	delete the hash symbols of 
	#kpca = KernelPCA(kernel="linear", fit_inverse_transform=True)
	#plotName = "linear"
	and add hash symbols on other Kernel PCA operations
	or
	read_fileName = "DecompressedMotions/55_02_edit_PPCA.amc" #Polynomial Kernel PCA
	Then go to the Kernel PCA operations, 
	delete the hash symbols of 
	#kpca = KernelPCA(kernel="poly", fit_inverse_transform=True)
	#plotName = "poly"
	and add hash symbols on other Kernel PCA operations
	or 
	read_fileName = "DecompressedMotions/55_02_rbf.amc"  #rbf Kernel PCA
	Then go to the Kernel PCA operations, 
	delete the hash symbols of 
	#kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True)
	#plotName = "rbf"
	and add hash symbols on other Kernel PCA operations

## Contributor
  Shuaiqun Pan
  Ruiyu Meng
  
