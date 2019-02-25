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
sys.path.insert( 0, r'/home/u1449908/Salome_files/new_hex')

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
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
fix_line = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fix_line, [4])
load_line = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(load_line, [35])
geompy.DifferenceIDs(fix_line, [4])
geompy.UnionIDs(fix_line, [49])
geompy.DifferenceIDs(load_line, [35])
geompy.UnionIDs(load_line, [28])
Group_1 = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [19, 26, 2, 54, 12, 47, 40, 33])
Group_2 = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Group_2, [28, 52, 56, 32, 53, 14, 21, 46, 57, 11, 25, 45, 42, 31, 10, 49, 18, 39, 17, 7, 4, 38, 35, 24])
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
geompy.addToStudyInFather( Extrusion_1, Group_1, 'Group_1' )
geompy.addToStudyInFather( Extrusion_1, Group_2, 'Group_2' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
hex_mesh = smesh.Mesh(Extrusion_1)
NETGEN_2D_1 = hex_mesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_Parameters_2D = NETGEN_2D_1.Parameters()
NETGEN_Parameters_2D.SetMaxSize( 3.5 )
NETGEN_Parameters_2D.SetSecondOrder( 0 )
NETGEN_Parameters_2D.SetOptimize( 1 )
NETGEN_Parameters_2D.SetFineness( 2 )
NETGEN_Parameters_2D.SetMinSize( 0 )
NETGEN_Parameters_2D.SetUseSurfaceCurvature( 1 )
NETGEN_Parameters_2D.SetFuseEdges( 1 )
NETGEN_Parameters_2D.SetQuadAllowed( 0 )
isDone = hex_mesh.Compute()
fix_line_1 = hex_mesh.GroupOnGeom(fix_line,'fix_line',SMESH.EDGE)
load_line_1 = hex_mesh.GroupOnGeom(load_line,'load_line',SMESH.EDGE)
smesh.SetName(hex_mesh, 'hex_mesh')
try:
  hex_mesh.ExportMED( r'/home/u1449908/Salome_files/new_hex/hex_mesh.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'
smesh.SetName(hex_mesh, 'hex_mesh')
try:
  hex_mesh.ExportMED( r'/home/u1449908/Salome_files/new_hex/hex_mesh.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'
Group_2_1 = hex_mesh.GroupOnGeom(Group_2,'Group_2',SMESH.EDGE)
Group_1_1 = hex_mesh.GroupOnGeom(Group_1,'Group_1',SMESH.FACE)
smesh.SetName(hex_mesh, 'hex_mesh')
try:
  hex_mesh.ExportMED( r'/home/u1449908/Salome_files/new_hex/hex_mesh.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(NETGEN_2D_1.GetAlgorithm(), 'NETGEN_2D_1')
smesh.SetName(NETGEN_Parameters_2D, 'NETGEN_Parameters_2D')
smesh.SetName(Group_1_1, 'Group_1')
smesh.SetName(hex_mesh.GetMesh(), 'hex_mesh')
smesh.SetName(fix_line_1, 'fix_line')
smesh.SetName(Group_2_1, 'Group_2')
smesh.SetName(load_line_1, 'load_line')

###
### ASTERSTUDY component
###

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
mEDReader1 = MEDReader(FileName='/home/u1449908/Salome_files/new_hex/hex_new.rmed')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [933, 668]

# show data in view
mEDReader1Display = Show(mEDReader1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'reslin__DEPL'))

# rescale color and/or opacity maps used to include current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__DEPL'
reslin__DEPLLUT = GetColorTransferFunction('reslin__DEPL')

# get opacity transfer function/opacity map for 'reslin__DEPL'
reslin__DEPLPWF = GetOpacityTransferFunction('reslin__DEPL')

# hide color bar/color legend
mEDReader1Display.SetScalarBarVisibility(renderView1, False)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'reslin__DEPL', '0'))

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'reslin__DEPL', '1'))

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'reslin__DEPL', '2'))

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'reslin__DEPL', '0'))

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'reslin__DEPL', '-1'))

# destroy renderView1
Delete(renderView1)
del renderView1

# get layout
layout1 = GetLayoutByName("Layout #1")

RemoveLayout(layout1)

CreateLayout('Layout #1')

# create a new 'MED Reader'
mEDReader2 = MEDReader(FileName='/home/u1449908/Salome_files/new_hex/hex_new.rmed')

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [933, 678]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.Background = [0.32, 0.34, 0.43]

# get layout
layout1_1 = GetLayout()

# place view in the layout
layout1_1.AssignView(0, renderView1)

# show data in view
mEDReader2Display = Show(mEDReader2, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# split cell
layout1_1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# split cell
layout1_1.SplitVertical(2, 0.5)

# close an empty frame
layout1_1.Collapse(6)

# set active view
SetActiveView(renderView1)

# set scalar coloring
ColorBy(mEDReader2Display, ('POINTS', 'reslin__DEPL'))

# rescale color and/or opacity maps used to include current data range
mEDReader2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
mEDReader2Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on mEDReader2Display
mEDReader2Display.ColorMode = 'Multiply'

# Properties modified on mEDReader2Display
mEDReader2Display.ColorMode = 'Blend'

# Properties modified on mEDReader2Display
mEDReader2Display.StreamingRequestSize = 4

# Properties modified on mEDReader2Display
mEDReader2Display.Specular = 0.03

# Properties modified on mEDReader2Display
mEDReader2Display.Specular = 0.06

# Properties modified on mEDReader2Display
mEDReader2Display.Specular = 0.09

# Properties modified on mEDReader2Display
mEDReader2Display.Specular = 0.12

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader2Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader2Display.RescaleTransferFunctionToDataRange(False, True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [18.582202312664343, -44.808713981058425, -48.20726480279154]
renderView1.CameraFocalPoint = [14.999999999999996, -5.660988864929221e-16, 5.0000000000000036]
renderView1.CameraViewUp = [-0.6018128199845153, -0.6303750574617769, 0.4903556022238828]
renderView1.CameraParallelScale = 18.027756377319946


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
