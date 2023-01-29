import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

#Define forces
k = 1
b = 4
F = lambda x: -k*x-b*(x**3)

#Initialize data
x_ec = []
v_ec = []
t_ec = []

#Set up Euler-Cromer


