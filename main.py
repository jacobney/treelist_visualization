# treelist_visualization
import os
import numpy as np
import matplotlib.pyplot as plt

#f = open('C:/Users/neyja/OneDrive/Documents/Bitvise_SSH/Temp4Servers/toDRG/treesrhof.dat')
filename = os.path.basename('C:/Users/neyja/OneDrive/Documents/Bitvise_SSH/Temp4Servers/toDRG/treesrhof.dat')
# filename for working directory: 'treesrhof.dat'

def import_fortran_dat_file(filename, cell_nums):
    from scipy.io import FortranFile
    (nx,ny,nz) = cell_nums
    arr =  FortranFile(filename,'r','uint32').read_ints('float32').T.reshape(nz,ny,nx)
    return arr

'''
matplotlib.pyplot.imshow

with open('test.txt') as f:
    lines = f.readlines()
'''

rhof = import_fortran_dat_file('treesrhof.dat',[400,400,26])

print ('Test 1')
plt.figure(1)
plt.imshow(rhof[0,:,:],origin='lower')
plt.colorbar()
plt.savefig('surf.png')


plt.figure(2)
plt.imshow(rhof[5,:,:],origin='lower')
plt.savefig('canop.png')
plt.colorbar()
print ('Test 2')