# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.3.0 with dump python functionality
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

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
A = geompy.MakeVertex(0, 0, 0)
listSubShapeIDs = geompy.SubShapeAllIDs(A, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(A, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(A, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(A, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(A, geompy.ShapeType["VERTEX"])
B = geompy.MakeVertex(5, 0, 0)
C = geompy.MakeVertex(10, 8.66, 0)
D = geompy.MakeVertex(20, 8.66, 0)
E = geompy.MakeVertex(25, 0, 0)
F = geompy.MakeVertex(30, 0, 0)
G = geompy.MakeVertex(20, -8.66, 0)
H = geompy.MakeVertex(10, -8.66, 0)
AB = geompy.MakeLineTwoPnt(A, B)
BC = geompy.MakeLineTwoPnt(B, C)
CD = geompy.MakeLineTwoPnt(C, D)
DE = geompy.MakeLineTwoPnt(D, E)
EF = geompy.MakeLineTwoPnt(E, F)
EF_vertex_2 = geompy.GetSubShape(EF, [2])
EG = geompy.MakeLineTwoPnt(EF_vertex_2, G)
GH = geompy.MakeLineTwoPnt(G, H)
AB_vertex_3 = geompy.GetSubShape(AB, [3])
HB = geompy.MakeLineTwoPnt(H, AB_vertex_3)
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(HB, geompy.ShapeType["VERTEX"])
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
geompy.addToStudyInFather( EF, EF_vertex_2, 'EF:vertex_2' )
geompy.addToStudy( EG, 'EG' )
geompy.addToStudy( GH, 'GH' )
geompy.addToStudyInFather( AB, AB_vertex_3, 'AB:vertex_3' )
geompy.addToStudy( HB, 'HB' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
