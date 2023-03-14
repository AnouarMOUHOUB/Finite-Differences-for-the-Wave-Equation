import numpy as np
import math
import matplotlib.pyplot as plt
#Test case 1
def f(x):
    return np.exp(-x**2)


c = 1
L = 10
# maillage et condition initiale
N = 100
x= np.linspace(-L,L,N)
u= np.zeros(N)
un_1 = np.zeros(N)
for i in range(N):
    u[i] = f(x[i])
    un_1[i] = f(x[i])
#tracé de la condition initiale
#plt.plot(x,u,'-b')
#plt.grid()

#le pas de maillage
dx = 2*L/(N-1)
# temps final des simulations
Tf = 9
#initialisation de temps:
t= 0
# Nombre de CFL tel que (0<CFL<=1)
CFL = 1
#calcul du pas du temps pour avoir la stabilité 
dt = CFL*dx/c
lamda = c*dt/dx
unew= np.zeros(N)
#boucle principale en temps
#On descritise notre interval en (N-1) sous interval 
while (t < Tf):
    for i in range(1,N-1):
        unew[i] = 2*u[i]-un_1[i]+(lamda**2)*(u[i+1]- 2*u[i] + u[i-1]) 
        un_1[i]= u[i]
        #conditions aux limites
    unew[0] = 0
    unew[N-1] = 0
    t = t + dt
    un_1 = un_1.copy()
    u = unew.copy()
    #plt.plot(x, u, '-r')
    #plt.grid()
    #plt.pause(0.5)




#Test case 2

c = 1
L = 1
k=3
def f(x):
    return np.cos((2*k*np.pi*x)/(2*L))


# maillage et condition initiale
N = 100
x= np.linspace(-L,L,N)
u= np.zeros(N)
un_1 = np.zeros(N)
for i in range(N):
    u[i] = f(x[i])
    un_1[i] = f(x[i])
#tracé de la condition initiale
plt.plot(x,u,'-b')
plt.grid()

#le pas de maillage
dx = 2*L/(N-1)
# temps final des simulations
T = 4*L/(2*k+1)*c
Tf = 2*T/3
#initialisation de temps:
t= 0
# Nombre de CFL tel que (0<CFL<=1)
CFL = 0.3
#calcul du pas du temps pour avoir la stabilité 
dt = CFL*dx/c
lamda = c*dt/dx
unew= np.zeros(N)
#boucle principale en temps
#On descritise notre interval en (N-1) sous interval 
while (t < Tf):
    for i in range(1,N-1):
        unew[i] = 2*u[i]-un_1[i]+(lamda**2)*(u[i+1]- 2*u[i] + u[i-1]) 
        un_1[i]= u[i]
        #conditions aux limites
    unew[0] = 0
    unew[N-1] = 0
    t = t + dt
    u = unew.copy()
    un_1 = un_1.copy()
    plt.plot(x, u, '-b')
    plt.title('time-{}'.format(t))
    plt.grid()
    plt.pause(3)







