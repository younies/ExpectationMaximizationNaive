#!/usr/bin/python

"""
This program for calculating the expectation maximization
"""


import os
import sys
import subprocess
import re
import scipy.stats
import numpy
# The input data

Xs = [35, 41, 21, 20, 17, 55, 12, 33, 15, 18, 4, 51, 17, 46]
K = 2 #number of clusters

# 1- initialize the parameter

PIs = [1.0/K] * K # set all PI's equally in the first
N 	= len(Xs) # number of data points
Ms 	= Xs[0:K] # choose random data points as means
SDs = [1.0] * K # set all standard deviations as one

C = [1] + [0] *(K-1) # all of them the same cluster in the begining
Cs = [C] * N ## assign clusters randomly



## calculating assigning clusters

def assignCluster(Xi):
	denominator = 0.0;
	for i in range(K):
		denominator += scipy.stats.norm(Ms[i], SDs[i]).pdf(Xi) * PIs[i]

	##choose the cluster
	value = -1.0
	c = 0
	for i in range(K):
		tempValue = (scipy.stats.norm(Ms[i], SDs[i]).pdf(Xi) * PIs[i]) / denominator
		if(tempValue > value):
			value = tempValue
			c = i
	C = [0] * K
	C[c] = 1
	return C


def uopdatePI_Means(newCs):
	for Pi in range(K):
		Ni = 0
		Mi = []
		for j in range(N):
			if( newCs[j][Pi] == 1 ):
				Ni += 1
				Mi.append(Xs[j])
		PIs[Pi] = Ni/ float(N)
		if(Ni != 0):
			Ms[Pi] = numpy.mean(Mi)
			SDs[Pi] = numpy.std(Mi)
		else:
			print ("error")


##Step two repeat until converge

while True:
	print (PIs)
	print (Ms)
	print (SDs)
	newCs = []
	for Xi in Xs:
		newCs.append(assignCluster(Xi))
	uopdatePI_Means(newCs)

	if(newCs == Cs):
		print ("Converged")
		print (PIs)
		print (Ms)
		print (SDs)
		break
	else:
		Cs = newCs


for i in range(K):
	print("Cluster " + str(i+1))

	for j in range(N):
		if(Cs[j][i] == 1):
			print(Xs[j])

	print("#####")


	