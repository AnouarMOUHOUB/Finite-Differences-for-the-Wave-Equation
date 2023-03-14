import numpy as np
import math
import matplotlib.pyplot as plt
#Test case 1
def f(x,y):
    return np.exp(-(x**2 + y**2) )


c = 1
#longueur et largeur du canal
Lx = 10
Ly = 10
# nombre de noeud suivant x et y 
Nx = 30
Ny = 30
#le pas de maillage suivant x et y
dx = 2*Lx/(Nx-1)
dy = 2*Ly/(Ny-1)
# maillage et condition initiale
x= np.zeros((Nx,Ny))
y= np.zeros((Nx,Ny))
u= np.zeros((Nx,Ny))
un_1 = np.zeros((Nx,Ny))

for i in range(Nx):
    for j in range(Ny):
        x[i,j] = i*dx
        y[i,j] = j*dy
        u[i,j] = f(x[i,j], y[i,j])
        un_1[i,j] = f(x[i,j], y[i,j])

CFL = 0.8
dt = min(CFL*dx/c, CFL*dy/c)

lamda1 = c*dt/dx
lamda2 = c*dt/dy


t=0
T = 8
unew = np.zeros((Nx,Ny))
while(t < T):
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            unew[i,j] = 2*u[i,j] - un_1[i,j] + (lamda1**2)*(u[i-1,j]- 2*u[i,j]+ u[i+1,j]) \
                                        + (lamda2**2)*(u[i,j-1]- 2*u[i,j]+ u[i,j+1])
        # les conditions aux limites
    unew[0,:] = 1 #bord sud
    unew[:,Ny-1] = 1
    unew[:,0] =1
    unew[Nx-1,:] = 1 
    
        
    t = t + dt
    u = unew.copy()
    un_1 = un_1.copy()
    plt.title('time-{}'.format(int(t)))
    plt.contourf(x,y,u,30)
    plt.colorbar()
    plt.show()
