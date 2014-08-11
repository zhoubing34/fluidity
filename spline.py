#!/usr/bin/env python
from math import pow
import pylab


e=[0.1544535825,0.2748526645,0.3625068659,0.412745937,0.4674295763,0.5282583069,0.5772440306,0.6187169157,0.7164262117,0.7931250187,0.8385892222,0.8957380133] 
dedt_k=[11115.5978729463,3824.9074006973,2248.5407453053,1843.3982021721,1387.1490141697,1083.730080291,898.7069155121,744.1679956897,534.9701226336,455.38544496,371.4353697503,329.4397601335]

n=12
n1=n-1
n2=n-2
m=[0.0]*n
b=[0.0]*n
a=[0.0]*n
c=[0.0]*n1
d=[0.0]*n1
h=[0.0]*n1
y=dedt_k

at=[0.0]*n2
bt=[0.0]*n2
ct=[0.0]*n2
dt=[0.0]*n2
mt=[0.0]*n2
bt2=[0.0]*n2
ct2=[0.0]*n2
dt2=[0.0]*n2

for i in range(n1):  
 h[i]=e[i+1]-e[i]


#solve b[1] to b[11] by thomas algrithm
for i in range(n2):
 at[i]=h[i]
 bt[i]=(2.0)*(h[i]+h[i+1])
 ct[i]=h[i+1]
 dt[i]=6*((y[i+2]-y[i+1])/h[i+1]-(y[i+1]-y[i])/h[i])

    
for i in range(n2):
  if i==0:
    ct2[i]=ct[i]/bt[i]
    dt2[i]=dt[i]/bt[i]
  else:
    ct2[i]=ct[i]/(bt[i]-ct2[i-1]*at[i])
    dt2[i]=(dt[i]-dt2[i-1]*at[i])/(bt[i]-ct2[i-1]*at[i])

for i in range(n2-1,-1,-1):
  if i==n2-1:
    mt[i]=dt2[i]
  else:
    mt[i]=(dt2[i]-ct2[i]*mt[i+1])

for i in range(1,n-1):
   m[i]=mt[i-1]

  
#calculate spline coefficient
for i in range(n1):
   a[i]=y[i]
   b[i]=(y[i+1]-y[i])/h[i]-m[i]*(h[i]/(2.0))-(h[i]/6.0)*(m[i+1]-m[i])
   c[i]=m[i]/2.0
   d[i]=(m[i+1]-m[i])/(6*h[i])
a[n-1]=dedt_k[n-1]
b[n-1]=(a[n-1]-a[n-2])/(e[n-1]-e[n-2])

e2=range(0,105,5)
for i in range(len(e2)):
  e2[i]=e2[i]/100.0

  
ek2=[0.0]*len(e2)

k1=0

for k in e2:
 if k<e[0]:
   ek2[k1]=b[0]*((e2[k1]-e[0]))+a[0]
 elif k>e[n-1]:
   ek2[k1]=b[n-1]*((e2[k1]-e[n-1]))+a[n-1]
 else:   
   i=0
   j=n
   while j-i>1:
   
     if (j-i)%2==0:
       
       p=(j-i)/2
     else:
       p=(j-i+1)/2
       
     if k>=e[i+p]:
        i=i+p
     else:
        j=i+p
       
   #if i<n-1:

   ek2[k1]=a[i]+b[i]*((e2[k1]-e[i]))+c[i]*pow((e2[k1]-e[i]),2.0)+d[i]*pow((e2[k1]-e[i]),3.0)
   #else:
     #ek2[k1]=a[i]
 k1=k1+1

print ek2

#pylab.plot(e,dedt_k,color='blue',marker='.',markersize=15)
#pylab.plot(e2,ek2,color='red',lw=2)
#pylab.show()

