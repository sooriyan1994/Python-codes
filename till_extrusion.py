# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/u1449908/Salome_files')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

geomObj_1 = geompy.MakeVertex(0, 0, 0)
geomObj_2 = geompy.MakeVertex(5, 0, 0)
geomObj_3 = geompy.MakeVertex(10, 8.660254037844386, 0)
geomObj_4 = geompy.MakeVertex(20, 8.660254037844386, 0)
geomObj_5 = geompy.MakeVertex(25, 0, 0)
geomObj_6 = geompy.MakeVertex(30, 0, 0)
geomObj_7 = geompy.MakeVertex(20, -8.660254037844386, 0)
geomObj_8 = geompy.MakeVertex(10, -8.660254037844386, 0)
geomObj_9 = geompy.MakeLineTwoPnt(geomObj_1, geomObj_2)
geomObj_10 = geompy.MakeLineTwoPnt(geomObj_2, geomObj_3)
geomObj_11 = geompy.MakeLineTwoPnt(geomObj_3, geomObj_4)
geomObj_12 = geompy.MakeLineTwoPnt(geomObj_4, geomObj_5)
geomObj_13 = geompy.MakeLineTwoPnt(geomObj_5, geomObj_6)
geomObj_14 = geompy.MakeLineTwoPnt(geomObj_5, geomObj_7)
geomObj_15 = geompy.MakeLineTwoPnt(geomObj_7, geomObj_8)
geomObj_16 = geompy.MakeLineTwoPnt(geomObj_8, geomObj_2)
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
A = geompy.MakeVertex(0, 0, 0)
B = geompy.MakeVertex(5, 0, 0)
C = geompy.MakeVertex(10, 8.660254037844386, 0)
D = geompy.MakeVertex(20, 8.660254037844386, 0)
E = geompy.MakeVertex(25, 0, 0)
F = geompy.MakeVertex(30, 0, 0)
G = geompy.MakeVertex(20, -8.660254037844386, 0)
H = geompy.MakeVertex(10, -8.660254037844386, 0)
AB = geompy.MakeLineTwoPnt(A, B)
BC = geompy.MakeLineTwoPnt(B, C)
CD = geompy.MakeLineTwoPnt(C, D)
DE = geompy.MakeLineTwoPnt(D, E)
EF = geompy.MakeLineTwoPnt(E, F)
EG = geompy.MakeLineTwoPnt(E, G)
GH = geompy.MakeLineTwoPnt(G, H)
HB = geompy.MakeLineTwoPnt(H, B)
Fuse_1 = geompy.MakeFuseList([AB, BC, CD, DE, EF, EG, GH, HB], True, True)
Extrusion_1 = geompy.MakePrismVecH(Fuse_1, OZ, 10)
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


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
