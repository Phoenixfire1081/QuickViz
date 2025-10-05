# Port of lic_internal.pyx
# All Cython elements were removed
# Numba is used for acceleration

import numpy as np
from numba import jit

@jit(nopython = True, cache = True)
def void _advance(vx, vy, x, y, fx, fy, w, h):
    if vx>=0:
        tx = (1-fx[0])/vx
    else:
        tx = -fx[0]/vx
    if vy>=0:
        ty = (1-fy[0])/vy
    else:
        ty = -fy[0]/vy
    if tx<ty:
        if vx>=0:
            x[0]+=1
            fx[0]=0
        else:
            x[0]-=1
            fx[0]=1
        fy[0]+=tx*vy
    else:
        if vy>=0:
            y[0]+=1
            fy[0]=0
        else:
            y[0]-=1
            fy[0]=1
        fx[0]+=ty*vx
    if x[0]>=w:
        x[0]=w-1 # FIXME: other boundary conditions?
    if x[0]<0:
        x[0]=0 # FIXME: other boundary conditions?
    if y[0]<0:
        y[0]=0 # FIXME: other boundary conditions?
    if y[0]>=h:
        y[0]=h-1 # FIXME: other boundary conditions?


#np.ndarray[float, ndim=2] 
@jit(nopython = True, cache = True)
def line_integral_convolution(vectors, texture, kernel):

    h = vectors.shape[0]
    w = vectors.shape[1]
    t = vectors.shape[2]
    kernellen = kernel.shape[0]
    if t!=2:
        raise ValueError("Vectors must have two components (not %d)" % t)
    result = np.zeros((h,w),dtype=np.float32)

    for i in range(h):
        for j in range(w):
            x = j
            y = i
            fx = 0.5
            fy = 0.5
            
            k = kernellen//2
            #print i, j, k, x, y
            result[i,j] += kernel[k]*texture[x,y]
            while k<kernellen-1:
                _advance(vectors[y,x,0],vectors[y,x,1],
                        x, y, fx, fy, w, h)
                k+=1
                #print i, j, k, x, y
                result[i,j] += kernel[k]*texture[x,y]

            x = j
            y = i
            fx = 0.5
            fy = 0.5
            
            while k>0:
                _advance(-vectors[y,x,0],-vectors[y,x,1],
                        x, y, fx, fy, w, h)
                k-=1
                #print i, j, k, x, y
                result[i,j] += kernel[k]*texture[x,y]
                    
    return result

