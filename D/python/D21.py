import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy.random import random, uniform, rand, choice
import scipy as sp


def update_derivative(x, x_dot, K, ω):
    for i in range(len(x_dot)):
        x_dot[i] = ω[i]
        for j in range(len(x)):
            x_dot[i] += K[i,j] * np.sin(x[j] - x[i]) 

def integration_step(dt, x, x_dot, K, ω):
    update_derivative(x, x_dot, K, ω)
    x += x_dot * dt


# T: measure-times ( t_j )
# X: matrix ( x_i(t_j) )
def simulation(dt, tmax, x, K, ω, T): 
    # Allocate some space
    X     = np.zeros( (len(x), len(T)) )
    x_dot = np.zeros( len(x) ) 
    # Conduct the simulation
    j = 0 # index for the time
    for t in np.arange(0, tmax + dt, dt):
        integration_step(dt, x, x_dot, K, ω)
        if j < len(T) and t >= T[j]:
            X[:,j]     = x
            T[j]       = t
            j += 1
    return X


def adjacency_matrix(dim):
    K = np.zeros( (dim, dim) )
    # Need an altered p: 1/2 of the entries shall be 0, but
    # we have as condition that the diagonal is 0 too.
    p = (dim*dim/2) / (dim*dim - dim)
    for i in range(dim):
        for j in range(dim):
            if i == j: continue
            if random() <= p:
                K[i,j] = uniform(0.2, 1.0)
    return K


def reconstruct_matrix(X, ω, T):
    N = len(ω)
    M = len(T) - 2
    X_dot = ( X[:, 2:] - X[:, 0:-2] ) / ( T[2:] - T[:-2] )
    y = np.zeros( (N, M) )
    for i in range(N):
        y[i,:] = X_dot[i,:] - ω[i]
    z = np.zeros( (N, N, X_dot.shape[1]) )
    for i in range(N):
        for j in range(N):
                z[i,j,:] = np.sin( X[j,1:-1] - X[i,1:-1] )

    K = np.zeros( (N, N) )
    for i in range(N):
        K[i,:] = np.dot(y[i,:], np.linalg.pinv(z[i,:,:]))
    return K


def trial(Tstart=0.0, Tend=2, N=5, M=100, dt=0.01):
    # get the K matrix
    K = adjacency_matrix(N)
    # random initial conditions
    x = rand(N)
    ω = choice( [-1, 1], N )

    # M+2 since we need more sample points
    # in order to calculate the derivatives
    T = np.linspace(Tstart, Tend, M+2)

    X = simulation(dt, Tend, x, K, ω, T)
    K_ = reconstruct_matrix(X,ω,T)
    return K, K_


def take_measures(measures, trials=500, Tstart=0.0, Tend=2., N=5, M=100, dt=0.01):
    qual = np.zeros(len(measures))
    for i in range(trials):
        K, K_ = trial(Tstart=Tstart, Tend=Tend, N=N, M=M, dt=dt)
        K_[K_ < 0.05] = 0.
        K_[K_ > 1.05] = 1.
        qual += np.array( [ measure(K, K_) for measure in measures ] )
    return qual / trials


def mean_difference(K, K_):    return np.abs((K - K_)).mean()
def maximum_difference(K, K_): return np.max(np.abs(K - K_))
def Q_95(K, K_): 
    J_max = max(np.max(K), np.max(K_))
    # Temporary variable
    R     = 0.05 - np.abs(K - K_)/(2*J_max)
    Q     = 1/K.size * (R >= 0).sum()
    return Q


measures = [mean_difference, maximum_difference, Q_95]


#N = 12
#M = 200
#Tend = 4

#print(take_measures(measures, N=N, M=M, Tend=Tend))


# Dependency on M
#results1 = {}
#results2 = {}
#results3 = {}
#for N in [5, 10, 12]:
    #print("N = ", N)
    #for Tend in [1.0, 2.0, 3.0, 4.0, 5.0]:
        #print("  Tend = ", Tend)
        #M = np.array(list(range(50, 251, 10)))
        #vals = [ take_measures(measures, N=N, M=m, Tend=Tend) for m in M ]
        #results1[(N, Tend)] = np.array( [val[0] for val in vals] )
        #results2[(N, Tend)] = np.array( [val[1] for val in vals] )
        #results3[(N, Tend)] = np.array( [val[2] for val in vals] )
