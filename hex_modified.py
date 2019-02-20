import numpy as np
from parameters import edge_length

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

#FUSING AND EXTRUSION
Fuse_1 = geompy.MakeFuseList([AB, BC, CD, DE, EF, EG, GH, HB], True, True)
Extrusion_1 = geompy.MakePrismVecH(Fuse_1, OZ, 10)

#CREATING A GROUP ~ helps in boundary conditions
fix_line = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fix_line, [4])
load_line = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(load_line, [35])

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
geompy.addToStudy( Fuse_1, 'Fuse_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudyInFather( Extrusion_1, fix_line, 'fix_line' )
geompy.addToStudyInFather( Extrusion_1, load_line, 'load_line' )

###MESH MODULE

#INTIALISING
import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

#CREATING A STUDY AND MESHING A PART
smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Extrusion_1)

#Specifying the mesh hypothesis and the mesh type
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)

#MESH PARAMETERS
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 3.5 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( 0.1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetMinSize( 1 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = Mesh_1.Compute() #MESHING

#Creating Groups on Geometry after meshing
fix_line_1 = Mesh_1.GroupOnGeom(fix_line,'fix_line',SMESH.EDGE)
load_line_1 = Mesh_1.GroupOnGeom(load_line,'load_line',SMESH.EDGE)
fix_line_2 = Mesh_1.GroupOnGeom(fix_line,'fix_line',SMESH.NODE)
load_line_2 = Mesh_1.GroupOnGeom(load_line,'load_line',SMESH.NODE)
smesh.SetName(Mesh_1, 'hex_mesh')

try:
  Mesh_1.ExportMED( r'/home/u1449908/Salome_files/hex_mesh.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'

###WHATS THIS??????????????????????????
([Mesh_1_1], status) = smesh.CreateMeshesFromMED(r'/home/u1449908/Salome_files/hex_mesh.med')
[ load_line_3, fix_line_3, fix_line_4, load_line_4 ] = Mesh_1_1.GetGroups()

###THIS TOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!
## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(load_line_1, 'load_line')
smesh.SetName(fix_line_1, 'fix_line')
smesh.SetName(Mesh_1.GetMesh(), 'hex_mesh')
smesh.SetName(load_line_2, 'load_line')
smesh.SetName(fix_line_2, 'fix_line')


#FOR GUI
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)


