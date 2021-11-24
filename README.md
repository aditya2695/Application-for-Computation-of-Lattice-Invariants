
# Application for Computation of Lattice Invariants

## Problem

This project aims to develop a web application that can be used to compare 2-dimensional or 3-dimensional lattices by providing lattice parameters as a set of cell lengths and angles thereby providing a platform to calculate the isometry invariants and visualize the similarity distance between lattices. 

Moreover, this project also aims to provide an interface to upload crystallographic datasets like CIF files and compare the uploaded files and visualize the invariant distance. The application allows users to upload data files and perform hierarchical clustering between the lattices from the uploaded files. The resulting clustering output was visualized graphically in the form of a dendrogram. This dendrogram can be used to assess the similarity between lattices. 

## DataSet
In this project, we have used Crystallographic data from CCDC database and Materials project website. 

This data is in the form of CIF files.Also, manual data entry have been used.


## Setup
This part includes the the basic setup used to run the application.

Libraries used in the application are:
•	NumPy\
•	Matplotlib\
•	SciPy\
•	Gemmi \
•	Pymatgen

<ul>
        <li > 1.Django installation
        <li>   pip install Django
        <li>2.	NumPy installation 
        <li>    pip install numpy
        <li>3.	SciPy installation
        <li>    pip install scipy
        <li>4.	Gemmi installation
        <li>    pip install gemmi
        <li>5.	Pymatgen installation
        <li>	    pip install pymatgen
        <li>6. Matplotlib installation
        <li>    pip install matplotlib
</ul>

## Testing

1. Extract the zip folder 
2. To run the application, go to the base directory containing the file ‘manage.py’ 
3. Execute python manage.py runserver.
4. The application runs by default on port 8000.
5. The URL http://127.0.0.1:8000/lattice/home takes you to the   application home screen.

<div>
<img src="https://drive.google.com/file/d/1Iy8Ry0D8AYYuh4kYjlxFcQRz6nl22BuF/view?usp=sharing">
</div>


