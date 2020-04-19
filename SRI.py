import numpy as np
import matplotlib.pyplot as plt

class SRI:
    def __init__(self, beta, gamma, beta_after,gamma_after, gamma_cllps=0.02, I_threshold=1.,EmeDecDay=100,delta_t=1.,LastDay=1000):
       #beta_after : after    
       self.S_ini=1. 
       self.I_ini=0.00001
       self.R_ini=0.

       S = self.S_ini 
       I = self.I_ini 
       R = self.R_ini 
       self.Dl=list()
       self.Sl=list()
       self.Il=list()
       self.Rl=list()
       for k in range(0,LastDay):
           print('%d %0lf %0lf %0lf %0lf' % (k, S, I, R, S+I+R))
           Spre=S
           Ipre=I
           Rpre=R
           if Ipre>I_threshold:
               gamma=gamma_cllps
           if k>EmeDecDay and Ipre<I_threshold:
               beta=beta_after
               gamma=gamma_after
           R=Rpre+gamma*delta_t*Ipre
           S=Spre-beta*delta_t*Spre*Ipre
           I=Ipre+beta*delta_t*Spre*Ipre-gamma*delta_t*Ipre
           self.Dl.append(k)
           self.Sl.append(S)
           self.Il.append(I)
           self.Rl.append(R)
       self.draw_plt()
       return

    def draw_plt(self):
       print('func::draw_plt called')
       lenD=len(self.Dl)
       lenS=len(self.Sl)
       lenI=len(self.Il)
       lenR=len(self.Rl)
       fig, ax = plt.subplots()
       ax.set_xlabel('days')
       ax.set_ylabel('')
       ax.set_title('SRI model')
       ax.grid()
       ax.plot(self.Dl,self.Sl,color="blue" ,label="S")
       ax.plot(self.Dl,self.Il,color="green",label="I")
       ax.plot(self.Dl,self.Rl,color="red"  ,label="R")
       ax.legend(loc=0)
       fig.tight_layout()
       plt.show()
       print('%d %d %d %d' % (lenD, lenS, lenI, lenR))
       return

case1 = SRI(beta=0.3,gamma=0.07,beta_after=0.20,gamma_after=0.07,EmeDecDay=200,LastDay=200, I_threshold=1.);
case2 = SRI(beta=0.3,gamma=0.07,beta_after=0.20,gamma_after=0.07,EmeDecDay=200,LastDay=200, I_threshold=0.1);
case3 = SRI(beta=0.3,gamma=0.07,beta_after=0.24,gamma_after=0.07,EmeDecDay=35 ,LastDay=200, I_threshold=1.);
case4 = SRI(beta=0.3,gamma=0.07,beta_after=0.15,gamma_after=0.07,EmeDecDay=35 ,LastDay=200, I_threshold=1.);
case5 = SRI(beta=0.3,gamma=0.07,beta_after=0.06,gamma_after=0.07,EmeDecDay=35 ,LastDay=200, I_threshold=1.);
