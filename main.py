# treelist_visualization
import os
import numpy as np
import matplotlib.pyplot as plt

def import_fortran_dat_file(filename, cell_nums):
    from scipy.io import FortranFile
    (nx,ny,nz) = cell_nums
    arr =  FortranFile(filename,'r','uint32').read_ints('float32').T.reshape(nz,ny,nx)
    return arr

rhof = import_fortran_dat_file('treesrhof.dat',[10,10,16])

plt.figure(1)
plt.imshow(rhof[0,:,:],origin='lower')
plt.colorbar()
plt.savefig('surface.png')
print('Surface')

plt.figure(2)
plt.imshow(rhof[5,:,:],origin='lower')
plt.colorbar()
plt.savefig('midstory.png')
print('Midstory')

plt.figure(3)
plt.imshow(rhof[10,:,:],origin='lower')
plt.colorbar()
plt.savefig('canopy.png')
print('Canopy')