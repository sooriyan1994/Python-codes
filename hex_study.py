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
fix_line = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fix_line, [4])
load_line = geompy.CreateGroup(Extrusion_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(load_line, [35])
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

###
### PARAVIS component
###

<salome>
  <ServerManagerState version="5.4.1">
    <Proxy servers="16" type="AnimationScene" id="263" group="animation">
      <Property number_of_elements="1" id="263.AnimationTime" name="AnimationTime">
        <Element value="0" index="0"/>
      </Property>
      <Property number_of_elements="1" id="263.Cues" name="Cues">
        <Proxy value="265"/>
        <Domain id="263.Cues.groups" name="groups"/>
      </Property>
      <Property number_of_elements="1" id="263.Duration" name="Duration">
        <Element value="10" index="0"/>
      </Property>
      <Property number_of_elements="1" id="263.EndTime" name="EndTime">
        <Element value="1" index="0"/>
      </Property>
      <Property number_of_elements="1" id="263.FramesPerTimestep" name="FramesPerTimestep">
        <Element value="1" index="0"/>
        <Domain id="263.FramesPerTimestep.range" name="range"/>
      </Property>
      <Property id="263.GoToFirst" name="GoToFirst"/>
      <Property id="263.GoToLast" name="GoToLast"/>
      <Property id="263.GoToNext" name="GoToNext"/>
      <Property id="263.GoToPrevious" name="GoToPrevious"/>
      <Property number_of_elements="1" id="263.LockEndTime" name="LockEndTime">
        <Element value="0" index="0"/>
        <Domain id="263.LockEndTime.bool" name="bool"/>
      </Property>
      <Property number_of_elements="1" id="263.LockStartTime" name="LockStartTime">
        <Element value="0" index="0"/>
        <Domain id="263.LockStartTime.bool" name="bool"/>
      </Property>
      <Property number_of_elements="1" id="263.Loop" name="Loop">
        <Element value="0" index="0"/>
        <Domain id="263.Loop.bool" name="bool"/>
      </Property>
      <Property number_of_elements="1" id="263.NumberOfFrames" name="NumberOfFrames">
        <Element value="10" index="0"/>
        <Domain id="263.NumberOfFrames.range" name="range"/>
      </Property>
      <Property id="263.Play" name="Play"/>
      <Property number_of_elements="1" id="263.PlayMode" name="PlayMode">
        <Element value="0" index="0"/>
        <Domain id="263.PlayMode.enum" name="enum">
          <Entry value="0" text="Sequence"/>
          <Entry value="1" text="Real Time"/>
          <Entry value="2" text="Snap To TimeSteps"/>
        </Domain>
      </Property>
      <Property number_of_elements="1" id="263.StartTime" name="StartTime">
        <Element value="0" index="0"/>
      </Property>
      <Property id="263.Stop" name="Stop"/>
      <Property number_of_elements="1" id="263.TimeKeeper" name="TimeKeeper">
        <Proxy value="259"/>
      </Property>
      <Property id="263.ViewModules" name="ViewModules">
        <Domain id="263.ViewModules.groups" name="groups"/>
      </Property>
    </Proxy>
    <Proxy servers="16" type="TimeAnimationCue" id="265" group="animation">
      <Property number_of_elements="1" id="265.AnimatedDomainName" name="AnimatedDomainName">
        <Element value="" index="0"/>
      </Property>
      <Property number_of_elements="1" id="265.AnimatedElement" name="AnimatedElement">
        <Element value="0" index="0"/>
      </Property>
      <Property number_of_elements="1" id="265.AnimatedPropertyName" name="AnimatedPropertyName">
        <Element value="Time" index="0"/>
      </Property>
      <Property number_of_elements="1" id="265.AnimatedProxy" name="AnimatedProxy">
        <Proxy value="259"/>
        <Domain id="265.AnimatedProxy.groups" name="groups"/>
      </Property>
      <Property number_of_elements="1" id="265.Enabled" name="Enabled">
        <Element value="1" index="0"/>
        <Domain id="265.Enabled.bool" name="bool"/>
      </Property>
      <Property number_of_elements="1" id="265.EndTime" name="EndTime">
        <Element value="1" index="0"/>
      </Property>
      <Property id="265.KeyFrames" name="KeyFrames">
        <Domain id="265.KeyFrames.groups" name="groups"/>
      </Property>
      <Property id="265.LastAddedKeyFrameIndex" name="LastAddedKeyFrameIndex"/>
      <Property number_of_elements="1" id="265.StartTime" name="StartTime">
        <Element value="0" index="0"/>
      </Property>
      <Property number_of_elements="1" id="265.TimeMode" name="TimeMode">
        <Element value="0" index="0"/>
        <Domain id="265.TimeMode.enum" name="enum">
          <Entry value="0" text="Normalized"/>
          <Entry value="1" text="Relative"/>
        </Domain>
      </Property>
      <Property number_of_elements="1" id="265.UseAnimationTime" name="UseAnimationTime">
        <Element value="1" index="0"/>
        <Domain id="265.UseAnimationTime.bool" name="bool"/>
      </Property>
    </Proxy>
    <Proxy servers="16" type="ViewLayout" id="4798" group="misc">
      <Property number_of_elements="2" id="4798.PreviewMode" name="PreviewMode">
        <Element value="0" index="0"/>
        <Element value="0" index="1"/>
      </Property>
      <Property number_of_elements="3" id="4798.SeparatorColor" name="SeparatorColor">
        <Element value="0.937" index="0"/>
        <Element value="0.922" index="1"/>
        <Element value="0.906" index="2"/>
        <Domain id="4798.SeparatorColor.range" name="range"/>
      </Property>
      <Property number_of_elements="1" id="4798.SeparatorWidth" name="SeparatorWidth">
        <Element value="1" index="0"/>
        <Domain id="4798.SeparatorWidth.range" name="range"/>
      </Property>
      <Layout number_of_elements="1">
        <Item direction="0" view="0" fraction="0.5"/>
      </Layout>
    </Proxy>
    <Proxy servers="16" type="TimeKeeper" id="259" group="misc">
      <Property id="259.SuppressedTimeSources" name="SuppressedTimeSources"/>
      <Property number_of_elements="1" id="259.Time" name="Time">
        <Element value="0" index="0"/>
        <Domain id="259.Time.range" name="range"/>
      </Property>
      <Property number_of_elements="1" id="259.TimeLabel" name="TimeLabel">
        <Element value="Time" index="0"/>
      </Property>
      <Property number_of_elements="2" id="259.TimeRange" name="TimeRange">
        <Element value="0" index="0"/>
        <Element value="0" index="1"/>
      </Property>
      <Property id="259.TimeSources" name="TimeSources"/>
      <Property id="259.TimestepValues" name="TimestepValues"/>
      <Property id="259.Views" name="Views"/>
    </Proxy>
    <ProxyCollection name="animation">
      <Item id="263" name="AnimationScene1"/>
      <Item id="265" name="TimeAnimationCue1"/>
    </ProxyCollection>
    <ProxyCollection name="layouts">
      <Item id="4798" name="Layout #1"/>
    </ProxyCollection>
    <ProxyCollection name="timekeeper">
      <Item id="259" name="TimeKeeper1"/>
    </ProxyCollection>
    <CustomProxyDefinitions/>
    <Links/>
  </ServerManagerState>
  <InteractiveViewLinks/>
</salome>
###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Extrusion_1)
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
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
isDone = Mesh_1.Compute()
fix_line_1 = Mesh_1.GroupOnGeom(fix_line,'fix_line',SMESH.EDGE)
load_line_1 = Mesh_1.GroupOnGeom(load_line,'load_line',SMESH.EDGE)
fix_line_2 = Mesh_1.GroupOnGeom(fix_line,'fix_line',SMESH.NODE)
load_line_2 = Mesh_1.GroupOnGeom(load_line,'load_line',SMESH.NODE)
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'/home/u1449908/Salome_files/hex_mesh.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'
([Mesh_1_1], status) = smesh.CreateMeshesFromMED(r'/home/u1449908/Salome_files/hex_mesh.med')
[ load_line_3, fix_line_3, fix_line_4, load_line_4 ] = Mesh_1_1.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Mesh_1_1.GetMesh(), 'Mesh_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(load_line_4, 'load_line')
smesh.SetName(fix_line_4, 'fix_line')
smesh.SetName(fix_line_2, 'fix_line')
smesh.SetName(load_line_2, 'load_line')
smesh.SetName(load_line_3, 'load_line')
smesh.SetName(fix_line_3, 'fix_line')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(load_line_1, 'load_line')
smesh.SetName(fix_line_1, 'fix_line')

###
### ASTERSTUDY component
###

{
  "minor": 10, 
  "history": {
    "cases": [
      {
        "stages": [
          1
        ], 
        "name": "CurrentCase"
      }
    ], 
    "stages": [
      {
        "files": [
          {
            "handle": 20, 
            "attr": 1, 
            "filename": "/home/u1449908/Salome_files/hex_mesh.med"
          }
        ], 
        "text": "mesh = LIRE_MAILLAGE(FORMAT='MED', UNITE=20)\n\nmodel = AFFE_MODELE(AFFE=_F(MODELISATION=('DKT', ), PHENOMENE='MECANIQUE', TOUT='OUI'), MAILLAGE=mesh)\n\nAluminum = DEFI_MATERIAU(ELAS=_F(E=70000.0, NU=0.3))\n\nfieldmat = AFFE_MATERIAU(AFFE=_F(MATER=(Aluminum, ), TOUT='OUI'), MODELE=model)", 
        "uid": 1, 
        "name": "Stage_1", 
        "result": {
          "resstate": 1, 
          "job": {}
        }
      }
    ], 
    "aster": "stable", 
    "versionMinor": 6, 
    "versionMajor": 13
  }
}
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
