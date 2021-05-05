import numpy as np
import random


def laplace(epsilon):
	return np.random.laplace(loc=0.0,scale = epsilon)

# dat rn a  dictionory of values/names to a discreet set.
def empricaldistro(data):
	total = len(data.keys())
	empricaldistro = {}
	for dataum in data.keys():
		empricaldistro[data[dataum]] = empricaldistro[data[dataum]] + 1/total if data[dataum] in empricaldistro	else 1/total
	return empricaldistro

# dat rn a  dictionory of values/names to a discreet set.
def uniformdistro(data):
	total = len(data.keys())
	uniformdistro = {}
	for dataum in data.keys():
		uniformdistro[data[dataum]] = 1/total
	return uniformdistro

# query is a function 
#distro is a distribution dictionary
def evalquery(query,distro):
	return sum([query(i)*distro[i] for i in distro.keys()])


def mistake(query, distro, trueDistro):
	return abs(evalquery(query,distro) - evalquery(query,trueDistro))

def signofmistake(query, distro, trueDistro)
	return 1 if evalquery(query,distro) - evalquery(query,trueDistro) > 0 else -1

#Qt is a list of queries chosen at time t
#Distrot is the list of distribtutions over daatset chosen at time t
#trueDistro is the distribution 
def regret(Qt,Distrot,trueDistro):
	return sum([mistake(Qt[i],Distrot[i],trueDistro) for i in range(len(Qt))])
