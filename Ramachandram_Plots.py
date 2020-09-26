## ./Scripts/UCSF_bootcamp/Ramachandram_project  pdb files should be stored here
## python 3.8

import sys ## used to take arguments from the commandline
import numpy as np  ## used to do math ie cross product, dot pruduct etc.
import matplotlib.pyplot as plt  ## used to make the plot

"""
Torsion is a fucntion that does the math to find the psi and phi angles
"""
def torsion (p1,p2,p3,p4):
	v1 = np.subtract (p2,p1)  ## this makes three vectors from the four points
	v2 = np.subtract (p3,p2)
	v3 = np.subtract (p4,p3)
	norm_v1 = v1/(np.linalg.norm (v1)) ## this normiliza all vectors
	norm_v2 = v2/(np.linalg.norm (v2))
	norm_v3 = v3/(np.linalg.norm (v3))
	cross_v1_v2 = np.cross (norm_v1, norm_v2)  ## makes a vector perpindicular between two vectors
	cross_v2_v3 = np.cross (norm_v2,norm_v3)  ## the angle between these two vectos is equal to the angle between vector 1 and 3
	m = np.cross (cross_v1_v2, norm_v2)  ## in order to make a right trangle I have to make this vector to solve angle
	x = np.dot (cross_v1_v2, cross_v2_v3)
	y = np.dot (m, cross_v2_v3)
	angle = -(np.arctan2 (y, x))*(180/np.pi)  ## arctan is used becasue it is more reailable than arccos as angles are closer to +/- 180
	return angle

def read_pdb(pdb_file):
	"""
	Open a PDB file as an argument in the commandline given that the PDB file is in Ramachandram_project directory 
	Within that file strip information that are ATOM and put it into a list
	"""
	file = []
	with open (pdb_file, 'r') as pdb:    ## opens the whole file line by line and stores it as a list and then closes file
		for line in pdb.readlines ():
			if line [0:4] == 'ATOM': ## takes the list from file and only take lines that have the word ATOM
				file.append (line)  ## for the word ATOM in pdb its columns 1-6 however python starts at 0 and the actual word ATOM is four letters the rest is spaces
	"""
	Next part goes through all the ATOM lines and takes the x,y,z coordinates from alph carbon, nitrogen, and carbon,
	takes the x,y,z coordinates puts them into a list and then places them into a dictionary
	"""
	CA = {}
	C = {}
	N = {}
	pos_ca = []
	pos_n = []
	pos_c = []
	for cor in file:
		if cor [21:22] not in N.keys(): ## Because everything starts with N, looks at keys in dictionary, this block makes dictionaries based on chain
			CA [cor [21:22]] = []
			C [cor [21:22]] = []
			N [cor [21:22]] = []
			x = cor [30:38]  
			y = cor [38:46] ## If key does not exist make sure to take the points from this line
			z = cor [46:54]
			pos_n = cor [23:26] ## this is here to make sure if there is more than one angle at a position, that we only take one angle ex pdb 5eil postion 51
			points = [float(x.strip()), float(y.strip()), float (z.strip())]  ## .strip remove all white spaces, and make sure everything is a float to do math
			N[cor[21:22]].append (points)
		elif cor [12:16] == ' CA ' and cor [23:26] != pos_ca: ## this is here to make sure if there is more than one angle at a position, that we only take one angle ex pdb 5eil postion 51
			x = cor [30:38]
			y = cor [38:46]
			z = cor [46:54]
			pos_ca = cor [23:26]
			points = [float(x.strip()), float(y.strip()), float (z.strip())]  ### this takes the coordinates removes spaces and makes them into floats
			CA[cor[21:22]].append(points)
		elif cor [12:16] == ' N  ' and cor [23:26] != pos_n:
			x = cor [30:38]
			y = cor [38:46]
			z = cor [46:54]
			pos_n = cor [23:26]
			points = [float(x.strip()), float(y.strip()), float (z.strip())]
			N[cor[21:22]].append (points)
		elif cor [12:16] == ' C  ' and cor [23:26] != pos_c:
			x = cor [30:38]
			y = cor [38:46]
			z = cor [46:54]
			pos_c = cor [23:26]
			points = [float(x.strip()), float(y.strip()), float (z.strip())]
			C[cor[21:22]].append (points)

	"""
	Have three dictionaries CA C and N. Each key in dictionary is a different chain (A, B, C ...). First call the keys, then in each index in each key call the 
	xyz coordinatest from each dictionary and find the torsion angles. Store the torsion angles either psi or phi
	"""

	psi = []
	phi = []

	for i in N.keys ():
		for xyz in range (len (N[i])): ## rememeber that it ends with the last point
			if xyz+2 == len (N[i]) :  ## i need this break becasue if I go outside of sequnce I need to end it before it fails
				break
			else:
				angle_for_psi = torsion(N[i][xyz+1], CA[i][xyz+1], C[i][xyz+1], N[i][xyz+2])  ### The first postion [0] can only have a psi angle at CA but not a phi. So skip the first CA
				psi.append (angle_for_psi)
				angle_for_phi = torsion(C[i][xyz],N[i][xyz+1], CA[i][xyz+1], C[i][xyz+1])
				phi.append (angle_for_phi)

	print ('this is psi \n', psi)
	print ('this is phi \n', phi)
	plt.plot (phi, psi, '.')  ## plot x, y and have data points as points
	plt.title (sys.argv [1]) ## make the title of the plot the PDB file name
	plt.xlabel ('phi')
	plt.ylabel ('psi')
	plt.ylim (-181,181)
	plt.xlim (-181,181)
	plt.yticks ((-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180))
	plt.xticks ((-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180))
	plt.arrow (-180,0,360,0) ## make an arrow so the graph looks like the x and y axis are clearly labled
	plt.arrow (0,-180,0,360)
	plt.grid() ## show gride lines at each tick
	plt.show () ## show the plot, remeber that program will continue to run until the graph is closed



read_pdb (sys.argv [1])  ## sys.argv [1] takes whatever comes after the script as an argument in the commandline ie. the pdb file in this dictory is used in this program