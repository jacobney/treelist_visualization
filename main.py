# treelist_visualization
import os
import matplotlib.pyplot

f = open('C:/Users/neyja/OneDrive/Documents/Bitvise_SSH/Temp4Servers/toDRG/treesrhof.dat')

filename = os.path.basename('C:/Users/neyja/OneDrive/Documents/Bitvise_SSH/Temp4Servers/toDRG/treesrhof.dat')

def import_fortran_dat_file(filename, cell_nums):
    from scipy.io import FortranFile
    (nx,ny,nz) = cell_nums
    arr =  FortranFile(filename,'r','uint32').read_ints('float32').T.reshape(nz,ny,nx)
    return arr

matplotlib.pyplot.imshow
