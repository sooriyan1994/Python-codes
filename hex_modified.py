import numpy as np
#from parameters import edge_length

a = 10

#SALOME INITIALIZATION
import sys
import salome

salome.salome_init()
theStudy = salome.myStudy #Creating a study

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/u1449908/Salome_files')

#GEOM component

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

geompy = geomBuilder.New(theStudy)

#Make the coordinate system
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

#POINTS OF Hexagonal Core Sandwich RCU 
A = geompy.MakeVertex(0, 0, 0)
B = geompy.MakeVertex(a/2, 0, 0)
C = geompy.MakeVertex(a, np.sqrt(3)*a/2, 0)
D = geompy.MakeVertex(2*a, np.sqrt(3)*a/2, 0)
E = geompy.MakeVertex(2.5*a, 0, 0)
F = geompy.MakeVertex(3*a, 0, 0)
G = geompy.MakeVertex(2*a, -np.sqrt(3)*a/2, 0)
H = geompy.MakeVertex(a, -np.sqrt(3)*a/2, 0)

#Joining the points by lines
AB = geompy.MakeLineTwoPnt(A, B)
BC = geompy.MakeLineTwoPnt(B, C)
CD = geompy.MakeLineTwoPnt(C, D)
DE = geompy.MakeLineTwoPnt(D, E)
EF = geompy.MakeLineTwoPnt(E, F)
EG = geompy.MakeLineTwoPnt(E, G)
GH = geompy.MakeLineTwoPnt(G, H)
HB = geompy.MakeLineTwoPnt(H, B)

Extrusion_1 = geompy.MakePrismVecH(AB, OZ, 10)
Extrusion_2 = geompy.MakePrismVecH(BC, OZ, 10)
Extrusion_3 = geompy.MakePrismVecH(CD, OZ, 10)
Extrusion_4 = geompy.MakePrismVecH(DE, OZ, 10)
Extrusion_5 = geompy.MakePrismVecH(EF, OZ, 10)
Extrusion_6 = geompy.MakePrismVecH(EG, OZ, 10)
Extrusion_7 = geompy.MakePrismVecH(GH, OZ, 10)
Extrusion_8 = geompy.MakePrismVecH(HB, OZ, 10)

#Adding all the points and line to the study
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( A, 'A' )
geompy.addToStudy( B, 'B' )
geompy.addToStudy( C, 'C' )
geompy.addToStudy( D, 'D' )
geompy.addToStudy( E, 'E' )
geompy.addToStudy( F, 'F' )
geompy.addToStudy( G, 'G' )
geompy.addToStudy( H, 'H' )
geompy.addToStudy( AB, 'AB' )
geompy.addToStudy( BC, 'BC' )
geompy.addToStudy( CD, 'CD' )
geompy.addToStudy( DE, 'DE' )
geompy.addToStudy( EF, 'EF' )
geompy.addToStudy( EG, 'EG' )
geompy.addToStudy( GH, 'GH' )
geompy.addToStudy( HB, 'HB' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Extrusion_2, 'Extrusion_2' )
geompy.addToStudy( Extrusion_3, 'Extrusion_3' )
geompy.addToStudy( Extrusion_4, 'Extrusion_4' )
geompy.addToStudy( Extrusion_5, 'Extrusion_5' )
geompy.addToStudy( Extrusion_6, 'Extrusion_6' )
geompy.addToStudy( Extrusion_7, 'Extrusion_7' )
geompy.addToStudy( Extrusion_8, 'Extrusion_8' )

#FOR GUI
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)


