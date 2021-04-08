from __main__ import vtk, qt, ctk, slicer

#
# HelloPython
#

class HelloPython:
  def __init__(self, parent):
    parent.title = "Hello Slicer-Python"
    parent.categories = ["My New Categories"]
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

class HelloPythonWidget:
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

    # HelloWorld button
    # (Insert Section A text here)
    helloWorldButton = qt.QPushButton("Hello World")
    helloWorldButton.toolTip = "Print 'Hello world' in standard ouput."
    self.sampleFormLayout.addWidget(helloWorldButton)
    helloWorldButton.connect('clicked(bool)',self.onHelloWorldButtonClicked())
    # (be sure to match indentation of the rest of this 
    # code)

    # Add vertical spacer
    self.layout.addStretch(1)

    # Set local var as instance attribute
    self.helloWorldButton = helloWorldButton

  def onHelloWorldButtonClicked(self):
    print("Hello World !")
    # (Insert Section B text here)
    # (be sure to match indentation of the rest of this 
    # code)
    qt.QMessageBox.information(
     slicer.util.mainWindow(),
      'Slicer Python','Hello World!')


