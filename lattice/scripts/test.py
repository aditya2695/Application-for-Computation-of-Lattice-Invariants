import numpy as np
from . import lattice_sim_2d
from . import lattice_sim_3d
from pymatgen import core
from os.path import isfile
import os
from os import listdir
from ntpath import join
import ase.io
import numpy as np
import amd

np.set_printoptions(precision=5, suppress=True)

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



# 8 C15 H18 O6 Rh2 AACRHC
# Crysal angles: 86.84 103.93 85.14
# Crysal lengths: 11.365 8.98 8.950000000000001

# 9 C8 H16 B1 F4 O10 Ru2 AACRUB
# Crysal angles: 90.0 97.19 90.0
# Crysal lengths: 14.246 6.904 17.687

def dot_product_angle(v1,v2):

    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        print("Zero magnitude vector!")
    else:
        vector_dot_product = np.dot(v1,v2)
        arccos = np.arccos(vector_dot_product / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        angle = np.degrees(arccos)
        return angle
    return 0


def gen_cellParams(cell):


    v1=cell[0]
    v2=cell[1]
    v3=cell[2]
    alpha = dot_product_angle(v3,v2)
    beta = dot_product_angle(v1,v3)
    gamma = dot_product_angle(v1,v2)

    a=np.linalg.norm(v1)
    b=np.linalg.norm(v2)
    c=np.linalg.norm(v3)
    a,b,c

    cell_params={'a':a,'b':b,'c':c,'alpha':alpha,'beta':beta,'gamma':gamma}

    return cell_params



def genCIF_to_Lattice(pathA,pathB):

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # path = os.path.join(BASE_DIR, 'media')

    # print(path)

    # files = [f for f in listdir(path) if isfile(join(path, f))]

    # print('fg:',files)

    # pathA  = join(path, str(files[0]))
    # pathB  = join(path, str(files[1]))

    print(pathA)
    print(pathB)    


    # blockA = ase.io.cif.parse_cif(pathA)
    # blockB = ase.io.cif.parse_cif(pathB)

    atomsA = ase.io.read(pathA)             # returns one atoms object
    atomsB = ase.io.read(pathB) 


    cellA = atomsA.get_cell().array  
    cellB = atomsB.get_cell().array  

    print(cellA,cellB)

    cell_paramsA=gen_cellParams(cellA)
    cell_paramsB=gen_cellParams(cellB)


    print(cell_paramsA,cell_paramsB)

    return cell_paramsA,cell_paramsB




def getMediaFiles():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mypath = os.path.join(BASE_DIR, 'media') 

    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    return files

def generate_art_Data():

    lat1=[]
    lat2=[]

   
    x=np.random.random()
    y=np.random.random()

    lat1.append([x,0])
    lat1.append([0,y])

    x=np.random.random()
    y=np.random.random()
    
    lat2.append([x,0])
    lat2.append([0,y])

    return lat1,lat2

def gen3D_latVectors():
    alpha, beta, gamma = 86.84, 103.93, 85.14
    a,b,c =  11.365, 8.98, 8.950000000000001
    lat1 = core.lattice.Lattice.from_parameters(a,b,c, alpha, beta, gamma) 
    lat_vecs1 = [list(i) for i in lat1.get_niggli_reduced_lattice().matrix]
    alpha, beta, gamma = 90.0, 97.19, 90.0
    a,b,c = 14.246, 6.904, 17.687

    lat2 = core.lattice.Lattice.from_parameters(a,b,c, alpha, beta, gamma) 
    lat_vecs2 = [list(i) for i in lat2.get_niggli_reduced_lattice().matrix]

    return lat_vecs1,lat_vecs2

def lattice2d_compute(lat_a,lat_b):

    lat1=[]
    lat2=[]

    lat1.append([lat_a['a'],0])
    lat1.append([lat_a['b']*np.cos(lat_a['angle']* np.pi/180)-lat_a['a'],
                 lat_a['b']*np.sin(lat_a['angle']* np.pi/180)])

    lat2.append([lat_b['a'],0])
    lat2.append([lat_b['b']*np.cos(lat_b['angle']* np.pi/180)-lat_b['a'],
                 lat_b['b']*np.sin(lat_b['angle']* np.pi/180)])


    lat_1  = lattice_sim_2d.Lattice_2d(lat1)
    lat_2  = lattice_sim_2d.Lattice_2d(lat2)

    pairdists_min2d = lattice_sim_2d.isodist_2d(lat_1, lat_2, dtype = 2, reflect = False)
    print('2d dist:',pairdists_min2d,'\n')

    return round(pairdists_min2d,2)


def lattice3d_compute(lattice1,latttice2):


    lat1 = core.lattice.Lattice.from_parameters(lattice1['a'],lattice1['b'],lattice1['c'], lattice1['alpha'], lattice1['beta'], lattice1['gamma']) 
    lat_vecs1 = [list(i) for i in lat1.get_niggli_reduced_lattice().matrix]

    lat2 = core.lattice.Lattice.from_parameters(latttice2['a'],latttice2['b'],latttice2['c'], latttice2['alpha'], latttice2['beta'], latttice2['gamma']) 
    lat_vecs2 = [list(i) for i in lat2.get_niggli_reduced_lattice().matrix]

    lat_1  = lattice_sim_3d.Lattice_3d(lat_vecs1)
    lat_2  = lattice_sim_3d.Lattice_3d(lat_vecs2)

    pairdists_min3d = lattice_sim_3d.lattice_3d_distance(lat_1, lat_2, dtype = 2, iso = False)

    print('3d val:',pairdists_min3d)

    return  round(pairdists_min3d,2)

def handle_uploaded_file(f):
    with open('media/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def main():

    """
    2d lattice
    """
    # lat1=[[8.98,0],[0,11.365]]
    # lat2=[[6.904,0],[0,14.246]]

    lat1,lat2 = generate_art_Data()
    

    lat_1  = lattice_sim_2d.Lattice_2d(lat1)
    lat_2  = lattice_sim_2d.Lattice_2d(lat2)

    pairdists_min2d = lattice_sim_2d.isodist_2d(lat_1, lat_2, dtype = 2, reflect = False)
    print('2d dist:',pairdists_min2d,'\n')
    
    """
    3d lattice
    """
    # lat1=[[8.98,0,0],[0,11.365,0],[0,0,11.365]]
    # lat2=[[6.904,0],[0,14.246],[0,0,14.246]]

    lat1,lat2 = gen3D_latVectors()
    lat_1  = lattice_sim_3d.Lattice_3d(lat1)
    lat_2  = lattice_sim_3d.Lattice_3d(lat2)

    print(lat_1,lat_2)
    pairdists_min3d = lattice_sim_3d.lattice_3d_distance(lat_1, lat_2, dtype = 2, iso = False)

    print(pairdists_min3d)
 
    return [pairdists_min2d,pairdists_min3d]

def test():
    return np.random.randint(100)

main()