# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:39:59 2021

@author: isand
"""

from __main__ import vtk, qt, ctk, slicer

#
# HelloPython
#

class MyNewModule:
  def __init__(self, parent):
    parent.title = "PythonModule"
    parent.categories = ["New Categories"]
    parent.dependencies = []
    parent.contributors = ["Sandeep"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    Example of scripted loadable extension for the HelloPython tutorial.
    """
    parent.acknowledgementText = "" # replace with organization, grant and thanks.
    self.parent = parent

#
# qHelloPythonWidget
#

class MyNewModuleWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    # Instantiate and connect widgets ...

    # Collapsible button
    sampleCollapsibleButton = ctk.ctkCollapsibleButton()
    sampleCollapsibleButton.text = "A collapsible button"
    self.layout.addWidget(sampleCollapsibleButton)

    # Layout within the sample collapsible button
    self.sampleFormLayout = qt.QFormLayout(sampleCollapsibleButton)
    #volume selector
    self.formFrame = qt.QFrame(sampleCollapsibleButton)
    #set the layout to horizontal
    self.formFrame.setLayout(qt.QHBoxLayout())
    #add it to the layout
    self.sampleFormLayout.addWidget(self.formFrame)
    
    #create new volume selector
    self.inputSelector = qt.QLabel("input label: ", self.formFrame)
    self.formFrame.layout().addWidget(self.inputSelector)
    
    self.inputSelector = slicer.qMRMLNodeComboBox(self.formFrame)
    #self.inputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode"),"")
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    self.formFrame.layout().addWidget(self.inputSelector)
    
    #a button
    button = qt.QPushButton("Apply")
    button.toolTip = "Crop Volume"
    #button.connect("clicked(bool)",self.setInformationButtonClicled)
    button.connect("clicked(bool)",self.setCropButtonClicked)
    self.formFrame.layout().addWidget(button)
    
    #textfiled
    # self.textfiled = qt.QTextEdit()
    # self.textfiled.setReadOnly(True)
    # self.formFrame.layout().addWidget(self.textfiled)
    
    self.layout.addStretch(1)
    
    
  def setCropButtonClicked(self):
        vol = self.inputSelector.currentNode()
        roi = slicer.vtkMRMLAnnotationROINode()
        roi.Initialize(slicer.mrmlScene)
    
        mainWindow = slicer.util.mainWindow()
        mainWindow.moduleSelector().selectModule('CropVolume')
    
        cropVolumeNode = slicer.vtkMRMLCropVolumeParametersNode()
        cropVolumeNode.SetScene(slicer.mrmlScene)
        cropVolumeNode.SetName('ChangeTracker_CropVolume_node')
        cropVolumeNode.SetIsotropicResampling(True)
        cropVolumeNode.SetSpacingScalingConst(0.5)
        slicer.mrmlScene.AddNode(cropVolumeNode)
    
        cropVolumeNode.SetInputVolumeNodeID(vol.GetID())
        cropVolumeNode.SetROINodeID(roi.GetID())
    
        cropVolumeLogic = slicer.modules.cropvolume.logic()
        cropVolumeLogic.Apply(cropVolumeNode)
    
        #self.delayDisplay('First test passed, closing the scene and running again')
        # test clearing the scene and running a second time
        slicer.mrmlScene.Clear(0)
        # the module will re-add the removed parameters node
        mainWindow.moduleSelector().selectModule('Transforms')
        mainWindow.moduleSelector().selectModule('CropVolume')
        cropVolumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLCropVolumeParametersNode1')
        #vol = SampleData.downloadSample("MRHead")
        roi = slicer.vtkMRMLAnnotationROINode()
        roi.Initialize(slicer.mrmlScene)
        cropVolumeNode.SetInputVolumeNodeID(vol.GetID())
        cropVolumeNode.SetROINodeID(roi.GetID())
        cropVolumeLogic.Apply(cropVolumeNode)
    
        #self.delayDisplay('Test passed')
       
       
    


