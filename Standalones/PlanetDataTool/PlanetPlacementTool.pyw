from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Axes, Figure
import sys
from matplotlib.patches import Ellipse
import os, lxml.etree as et
from math import sqrt
import pickle,math
def validate_datapath(config):
    while config.dataPath == None or not config.dataPath.endswith(('DATA', 'Data', 'data')):
        msg = QMessageBox()
        msg.setWindowTitle('Error!')
        msg.setText('Point To a Vaild EaW Mod Data Folder!')
        msg.exec_()
        directory = str(QFileDialog.getExistingDirectory())
        if directory.endswith(('DATA', 'Data', 'data')):
            config.dataPath = directory
def loadFile(filename):
    file = open(filename, 'rb')
    obj = file.read().decode('utf-32')
    print(obj)
    obj = obj.replace('%20',' ')
    file.close()
    return obj
def pickleLoad(filename):
    file = open(filename, 'rb')
    obj = pickle.load(file)
    file.close()
    return obj
def serialize(obj, fileName):
    file = open(fileName, 'wb')
    obj = pickle.dump(obj, file)
    file.close()
def encode(obj, fileName):
    file = open(fileName, 'wb')
    file.write(str(obj).encode('utf-32'))
    file.close()

class Planet:
    def __init__(self, xml_entry, fileLocation, logfile):
        self.fileLocation = fileLocation
        self.entry = xml_entry
        self.planet_owners = {}
        self.name = self.get_planet_name(logfile)
        self.text_key = self.get_text_key(logfile)
        self.model_name = self.get_model_name(logfile)
        self.land_map = self.get_land_map(logfile)
        self.space_map = self.get_space_map(logfile)
        self.x, self.y = self.get_position(logfile)
        self.terrain_index = self.get_terrain_index(logfile)
        self.land_structures = self.get_land_structures(logfile)
        self.galactic_model = self.get_galactic_model(logfile)
        self.destroyed_model = self.get_destroyed_model(logfile)
        self.additional_pop = self.get_additional_pop(logfile)
        self.land_accessible = self.get_planet_accessbile(logfile)
    def get_model_name(self, logfile):
        for child in self.entry:
            if child.tag == 'Galactic_Model_Name': 
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed to return string for Galactic_Model_Name in planet {self.name}')
                    logfile.flush()
                    return 0
    def get_terrain_index(self,logfile):
        logfile.write(f'Getting Terrain Index for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Zoomed_Terrain_Index':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Zoomed_Terrain_Index of planet {self.name}\n')
                    logfile.flush()
                    return 0
    def get_land_structures(self,logfile):
        logfile.write(f'Getting Land Slots for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Special_Structures_Land':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Special_Structures_Land of planet {self.name}\n')
                    logfile.flush()
                    return 3
    def get_galactic_model(self,logfile):
        logfile.write(f'Getting Galactic Model for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Galactic_Model_Name':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Galactic_Model_Name of planet {self.name}\n')
                    logfile.flush()
                    return 'W_planet_Temperate01.alo'
    def get_destroyed_model(self,logfile):
        logfile.write(f'Getting Destroyed Model for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Destroyed_Galactic_Model_Name':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Destroyed_Galactic_Model_Name of planet {self.name}\n')
                    logfile.flush()
                    return 'W_planet_Asteroids.alo'
    def get_additional_pop(self,logfile):
        logfile.write(f'Getting Additional Population Capacity for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Additional_Population_Capacity':
                try:
                    return int(child.text)
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Additional_Population_Capacity of planet {self.name}\n')
                    logfile.flush()
                    return 50
    def get_planet_accessbile(self,logfile):
        logfile.write(f'Getting Surface Accessilbe for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Planet_Surface_Accessible':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Planet_Surface_Accessible of planet {self.name}\n')
                    logfile.flush()
                    return 'Yes'
    def get_text_key(self,logfile):
        logfile.write(f'Getting Text ID for planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Text_ID':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Text_ID of planet {self.name}\n')
                    logfile.flush()
                    sys.exit()
    def distanceTo(self, target):
        return sqrt((self.x - target.x)**2 + (self.y - target.y)**2)
    def get_planet_name(self,logfile) -> str:
        logfile.write(f'Getting Planet Name\n')
        return self.entry.get('Name')
    def get_land_map(self,logfile) -> str:
        logfile.write(f'Getting Land Map For Planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Land_Tactical_Map':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Land Map Name of planet {self.name}\n')
                    logfile.flush()
                    sys.exit()
    def get_space_map(self,logfile) -> str:
        logfile.write(f'Getting Space Map For Planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Space_Tactical_Map':
                try:
                    return child.text
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return string for Space Map Name of planet {self.name}\n')
                    logfile.flush()
                    sys.exit()
    def get_position(self,logfile):
        logfile.write(f'Getting Galactic Position For Planet {self.name}\n')
        for child in self.entry:
            if child.tag == 'Galactic_Position':     
                entry = child.text     
                entry = entry.replace(',',' ')
                entry = entry.split()
                try:
                    return float(entry[0]), float(entry[1])
                except:
                    logfile.write(f'CRITICAL ERROR Failed To Return float for galactic position of planet {self.name}\n')
                    logfile.flush()
                    sys.exit()
        return 0,0
    def reset_position(self, logfile):
        self.x, self.y = self.get_position(logfile)







class DraggablePoint:
    lock = None
    def __init__(self, parent, x=0.1, y=0.1, size=25):
        self.parent = parent
        self.point = Ellipse((x, y), size, size, fc='r', alpha=0.5, edgecolor='r')
        self.x = x
        self.y = y

        parent.mapCanvas.figure.axes[0].add_patch(self.point)
        self.press = None
        self.background = None
    def remove(self):
        self.point.remove()

class EditPlanetWindow:
    def __init__(self, planets,parent):
        if os.path.isfile('pointSize'):
            try:
                self.size = float(pickleLoad('pointSize'))
            except:
                self.size = float(25)
        else:
            self.size = float(25)
        self.parent = parent
        self.mainWindow = QMainWindow()
        self.planets = planets
        self.dialogWindow = QSplitter(self.mainWindow)
        self.mainWindow.setCentralWidget(self.dialogWindow)
        self.mainWindow.setWindowTitle("Edit Planet")
        self.x = 0
        self.y = 0
        font = QFont()
        font.setPointSize(10)
        self.mainWindow.setWindowTitle("Planet Placement Tool")
       

        self.__quitAction: QAction = QAction("Quit", self.mainWindow)
        self.__quitAction.triggered.connect(sys.exit)
        self.saveAction = QAction("Save To File", self.mainWindow)
        self.setDataFolderAction = QAction("Set Data Folder", self.mainWindow)
        self.setPointSizeAction = QAction("Set Point Size", self.mainWindow)
        self.setPointSizeAction.triggered.connect(self.change_point_size)

        self.MenuBar = QMenuBar()

        self.MenuBar.addAction(self.__quitAction)
        self.MenuBar.addAction(self.saveAction)
        self.MenuBar.addAction(self.setDataFolderAction)
        self.MenuBar.addAction(self.setPointSizeAction)
        self.mainWindow.setMenuBar(self.MenuBar)
        self.leftSideWidget = QWidget()
        self.LeftSideLayout = QVBoxLayout()
        self.leftSideWidget.setLayout(self.LeftSideLayout)
        self.planetSelection = QComboBox()
        self.ModelNameLayout = QVBoxLayout()
        self.modelNameSublayout = QHBoxLayout()
        self.ModelNameLabel = QLabel()
        self.ModelNameLabel.setFont(font)
        self.ModelNameLabel.setText("Model Name:")
        self.PlanetModelName = QLineEdit()
        self.PlanetModelName.setEnabled(False)

        self.SetModel = QToolButton()
        self.SetModel.setText("...")
        self.SetModel.clicked.connect(self.set_model)
        self.ModelNameLayout.addWidget(self.ModelNameLabel)
        self.modelNameSublayout.addWidget(self.PlanetModelName)
        self.modelNameSublayout.addWidget(self.SetModel)
        self.ModelNameLayout.addLayout(self.modelNameSublayout)



        self.positionLayout = QVBoxLayout()
        self.currentPositionlabel = QLabel()
        self.currentPositionlabel.setFont(font)
        self.currentPositionlabel.setText("Current Position:")
        self.positionLayout.addWidget(self.currentPositionlabel)



        self.xLayout = QHBoxLayout()
        self.xLabel = QLabel()
        self.xLabel.setFont(font)
        self.xLabel.setText("X:")

        self.XPosition = QLineEdit()

        self.xLayout.addWidget(self.xLabel)
        self.xLayout.addWidget(self.XPosition)
        self.changeX = QToolButton()
        self.changeX.setText("...")
        self.xLayout.addWidget(self.changeX)



        self.yLayout = QHBoxLayout()
        self.yLabel = QLabel()
        self.yLabel.setFont(font)
        self.yLabel.setText("Y:")

        self.yPosition = QLineEdit()

        self.yLayout.addWidget(self.yLabel)
        self.yLayout.addWidget(self.yPosition)
        self.changeY = QToolButton()
        self.yLayout.addWidget(self.changeY)
        self.changeY.setText("...")

        self.positionLayout.addLayout(self.xLayout)
        self.positionLayout.addLayout(self.yLayout)

        self.resetPosition = QPushButton()
        self.resetPosition.setText('Reset Planet Position')


        self.XPosition.setEnabled(False)
        self.yPosition.setEnabled(False)




        self.SpaceMapLayout = QVBoxLayout()

        self.SpaceMapLabel = QLabel()
        self.SpaceMapLabel.setFont(font)
        self.SpaceMapLabel.setText("Space Tactical Map:")
        self.SpaceMapSubLayout = QHBoxLayout()
        self.SpaceMap = QLineEdit()
        self.SpaceMap.setEnabled(False)

        self.changeSpaceLayout = QToolButton()
        self.changeSpaceLayout.setText("...")
        self.changeSpaceLayout.clicked.connect(self.set_space_map)
        self.SpaceMapLayout.addWidget(self.SpaceMapLabel)
        self.SpaceMapSubLayout.addWidget(self.SpaceMap)
        self.SpaceMapSubLayout.addWidget(self.changeSpaceLayout)
        self.SpaceMapLayout.addLayout(self.SpaceMapSubLayout)
        self.LandMapLayout = QVBoxLayout()

        self.LandMapLabel = QLabel()
        self.LandMapLabel.setFont(font)
        self.LandMapLabel.setText("Land Tactical Map:")
        self.LandMapSubLayout = QHBoxLayout()
        self.LandMap = QLineEdit()
        self.LandMap.setEnabled(False)
        self.changeLandLayout = QToolButton()
        self.changeLandLayout.setText("...")
        self.changeLandLayout.clicked.connect(self.set_land_map)
        self.LandMapLayout.addWidget(self.LandMapLabel)
        self.LandMapSubLayout.addWidget(self.LandMap)
        self.LandMapSubLayout.addWidget(self.changeLandLayout)
        self.LandMapLayout.addLayout(self.LandMapSubLayout)


        self.LeftSideLayout.addWidget(self.planetSelection)
        self.LeftSideLayout.addItem(QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.LeftSideLayout.addLayout(self.ModelNameLayout)
        self.LeftSideLayout.addItem(QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.LeftSideLayout.addLayout(self.SpaceMapLayout)
        self.LeftSideLayout.addLayout(self.LandMapLayout)
        self.LeftSideLayout.addItem(QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.LeftSideLayout.addLayout(self.positionLayout)
        self.LeftSideLayout.addItem(QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.LeftSideLayout.addWidget(self.resetPosition)
        self.LeftSideLayout.addItem(QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.HideGridButton = QPushButton()
        self.HideGridButton.setText("Show Grid")
        self.LeftSideLayout.addWidget(self.HideGridButton)
        self.LeftSideLayout.addItem(QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.HideGridButton.clicked.connect(self.toggle_grid)
        self.dialogWindow.addWidget(self.leftSideWidget)
        self.dialogWindow.setFixedSize(900, 540)


        self.mapWidget: QWidget = QWidget()
        self.mapWidget.setLayout(QVBoxLayout())
        self.mapCanvas: FigureCanvas = FigureCanvas(Figure())
        self.mapCanvas.mpl_connect('pick_event', self.__planetSelect)
        self.mapCanvas.mpl_connect('motion_notify_event', self.__planetHover)
        self.navbar = NavigationToolbar(self.mapCanvas, self.dialogWindow)
        self.mapWidget.layout().addWidget(self.navbar)
        self.mapWidget.layout().addWidget(self.mapCanvas)
        self.axes: Axes = self.mapCanvas.figure.add_subplot(111, aspect = "equal")
        self.axes.set_xlim(-600,700)
        self.axes.set_ylim(-600,850)
        self.__annotate = self.axes.annotate("", xy = (0,0), xytext = (10, 10), textcoords = "offset points", bbox = dict(boxstyle="round", fc="w"), arrowprops = dict(arrowstyle="->"))
        self.__annotate.set_visible(False)
        self.__planetNames = []
        self.__planetsScatter = None
        self.selected_planet = None
        self.times = 0
        self.dialogWindow.addWidget(self.mapWidget)
    def change_point_size(self):
        size = QInputDialog.getInt(self.mapWidget, "Enter Planet Movement Point Size", "Enter Planet Movement Point Size", self.size, 0, 100, 1)
        if size[1] != False:
            planet_name = self.planetSelection.currentText()
            if planet_name in [x.name for x in self.planets]:
                planet_index = [x.name for x in self.planets].index(planet_name)
            serialize(size[0],'pointSize')
            self.size = float(size[0])
            self.plotSelectedPlanet(self.planets[planet_index],size=self.size)
    def toggle_grid(self):
        if self.HideGridButton.text() == 'Show Grid':
            self.axes.grid(True)
            self.HideGridButton.setText("Hide Grid")
            self.mapCanvas.draw()
        else:
            self.axes.grid(False)
            self.HideGridButton.setText("Show Grid")
            self.mapCanvas.draw()
    def on_index_changed(self):
        planet_name = self.planetSelection.currentText()
        if planet_name in [x.name for x in self.planets]:
            planet_index = [x.name for x in self.planets].index(planet_name)
        self.plotGalaxy(self.planets)
        self.plotSelectedPlanet(self.planets[planet_index])
        planet = self.planets[planet_index]
        self.PlanetModelName.setText(planet.model_name)

        self.LandMap.setText(planet.land_map)
        self.SpaceMap.setText(planet.space_map)
        self.XPosition.setText(str(planet.x))
        self.yPosition.setText(str(planet.y))
    def show(self):
        
        planet_name = self.planetSelection.currentText()
        if planet_name in [x.name for x in self.planets]:
            planet_index = [x.name for x in self.planets].index(planet_name)
        planet = self.planets[planet_index]
        self.plotGalaxy(self.planets)
        self.plotSelectedPlanet(self.planets[planet_index])
        self.planetSelection.currentIndexChanged.connect(self.on_index_changed)
        self.resetPosition.clicked.connect(self.reset_position)
        self.PlanetModelName.setText(planet.model_name)
        self.LandMap.setText(planet.land_map)
        self.SpaceMap.setText(planet.space_map)
        self.XPosition.setText(str(planet.x))
        self.yPosition.setText(str(planet.y))
        self.mainWindow.show()
    def reset_position(self):
        planet_name = self.planetSelection.currentText()
        if planet_name in [x.name for x in self.planets]:
            planet_index = [x.name for x in self.planets].index(planet_name)
        self.plotSelectedPlanet(self.planets[planet_index])
        planet = self.planets[planet_index]
        planet.reset_position(self.parent.logfile)
        self.XPosition.setText(str(planet.x))
        self.yPosition.setText(str(planet.y))
        self.plotSelectedPlanet(self.planets[planet_index])
        self.parent.save_to_cache()
    def plotSelectedPlanet(self, planet, size=25):
        # del(self.list_points[:])
        self.x = planet.x 
        self.y = planet.y
        if self.selected_planet != None:
            self.selected_planet.point.remove()
        self.selected_planet = DraggablePoint(self, planet.x, planet.y,self.size)
        self.connect()
        self.mapCanvas.draw()
    def plotGalaxy(self, allPlanets) -> None:
        '''Plots all planets as alpha = 0.1, then overlays all selected planets and trade routes'''
        self.axes.clear()

        #Has to be set again here for the planet hover labels to work
        self.__annotate = self.axes.annotate("", xy = (0,0), xytext = (10, 10), textcoords = "offset points", bbox = dict(boxstyle="round", fc="w"), arrowprops = dict(arrowstyle="->"))
        self.__annotate.set_visible(False)

        self.__planetNames = []

        x = []
        y = []

        for planet in allPlanets:
            if planet.name != self.planetSelection.currentText():
                x.append(planet.x)
                y.append(planet.y)
                self.__planetNames.append(planet.name)
            else:
                x.append(0)
                y.append(0)
                self.__planetNames.append("Dummy Planet")

        self.__planetsScatter = self.axes.scatter(x, y, c = 'b', alpha = 0.1,picker = 5)
        self.mapCanvas.draw_idle()
        self.times = self.times +1
    def set_model(self):
        directory = str(QFileDialog.getOpenFileName())
        if not directory.lower().endswith('.alo'):
            pass
        else:
            self.PlanetModelName.setText(directory)
        self.parent.save_to_cache()
    def set_land_map(self):
        directory = str(QFileDialog.getOpenFileName())
        if not directory.lower().endswith('.ted'):
            pass
        else:
            self.LandMap.setText(directory)
        self.parent.save_to_cache()
    def set_space_map(self):
        directory = str(QFileDialog.getOpenFileName())
        if not directory.lower().endswith('.ted'):
            pass
        else:
            self.SpaceMap.setText(directory)
        self.parent.save_to_cache()
    def __planetSelect(self, event) -> None:
        '''Event handler for selecting a planet on the map'''
        planet_index = event.ind
        planet_name = self.planets[planet_index[0]].name
        self.planetSelection.setCurrentIndex(planet_index[0])
    def __planetHover(self, event) -> None:
        '''Handler for hovering on a planet in the plot'''
        visible = self.__annotate.get_visible()

        if event.inaxes == self.axes:
            contains, ind = self.__planetsScatter.contains(event)

            if contains:
                pos = self.__planetsScatter.get_offsets()[ind["ind"][0]]
                self.__annotate.xy = pos
                text = "{}".format(" ".join([self.__planetNames[n] for n in ind["ind"]]))
                self.__annotate.set_text(text)
                self.__annotate.set_visible(True)

                self.mapCanvas.draw_idle()
            else:
                if visible:
                    self.__annotate.set_visible(False)

                    self.mapCanvas.draw_idle()
    def connect(self):
        self.cidpress = self.selected_planet.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.selected_planet.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.selected_planet.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
    def on_press(self, event):

        if event.inaxes != self.selected_planet.point.axes: return
        if DraggablePoint.lock is not None: return
        contains, attrd = self.selected_planet.point.contains(event)
        if not contains: return
        self.press = (self.selected_planet.point.center), event.xdata, event.ydata
        DraggablePoint.lock = self

        canvas = self.selected_planet.point.figure.canvas
        axes = self.selected_planet.point.axes
        self.selected_planet.point.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.selected_planet.point.axes.bbox)

        axes.draw_artist(self.selected_planet.point)

        canvas.blit(axes.bbox)

    def on_motion(self, event):

        if DraggablePoint.lock is not self:
            return
        if event.inaxes != self.selected_planet.point.axes: return
        self.selected_planet.point.center, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.selected_planet.point.center = (self.selected_planet.point.center[0]+dx, self.selected_planet.point.center[1]+dy)

        canvas = self.selected_planet.point.figure.canvas
        axes = self.selected_planet.point.axes
        # restore the background region
        canvas.restore_region(self.background)

        # redraw just the current rectangle
        axes.draw_artist(self.selected_planet.point)

        self.x = self.selected_planet.point.center[0]
        self.y = self.selected_planet.point.center[1]
        self.XPosition.setText(str(self.x))
        self.yPosition.setText(str(self.y))
        # blit just the redrawn area
        canvas.blit(axes.bbox)


    def on_release(self, event):

        'on release we reset the press data'
        if DraggablePoint.lock is not self:
            return

        self.press = None
        DraggablePoint.lock = None

        # turn off the rect animation property and reset the background
        self.selected_planet.point.set_animated(False)

        self.background = None

        # redraw the full figure
        self.selected_planet.point.figure.canvas.draw()

        self.x = self.selected_planet.point.center[0]
        self.y = self.selected_planet.point.center[1]
        self.XPosition.setText(str(self.x))
        self.yPosition.setText(str(self.y))
        self.parent.save_to_cache()
    def hide(self):
        self.dialogWindow.accept()


def validate_datapath(dataPath):
    while dataPath == None or not dataPath.endswith(('DATA', 'Data', 'data')):
        msg = QMessageBox()
        msg.setWindowTitle('Error!')
        msg.setText('Point To a Vaild EaW Mod Data Folder!')
        msg.exec_()
        directory = str(QFileDialog.getExistingDirectory())
        if directory.endswith(('DATA', 'Data', 'data')):
            return True

class PlanetPlacementTool:
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        self.logfile = open('logfile.txt', 'w')
        if os.path.isfile('dataPath'):
            try:
                self.mod_dir = loadFile('dataPath')
            except:
                self.mod_dir = self.get_mod_dir()
        else:
            self.mod_dir = self.get_mod_dir()
        self.mod_dir = self.mod_dir.replace('%20',' ')
        print(self.mod_dir)
        self.planetFiles =[]
        self.planets = []
        self.set_planets()
        self.window = EditPlanetWindow(self.planets, self)
        for planet in self.planets:
            self.window.planetSelection.addItem(planet.name)
        self.window.show()
        self.window.setDataFolderAction.triggered.connect(self.set_data_path)
        self.window.saveAction.triggered.connect(self.save_to_file)
        self.window.changeX.clicked.connect(self.change_x_coord)
        self.window.changeY.clicked.connect(self.change_y_coord)
        sys.exit(app.exec_())
    def change_x_coord(self):
        integer, ok = QInputDialog().getInt(None, "Enter New Planet X Coordinate",
                                     "Enter New Planet X Coordinate")
        if ok:
            planet_name = self.window.planetSelection.currentText()
            if planet_name in [x.name for x in self.planets]:
                planet_index = [x.name for x in self.planets].index(planet_name)
            
            self.window.XPosition.setText(str(integer))

            
            self.save_to_cache()
            self.window.plotSelectedPlanet(self.planets[planet_index])
    def change_y_coord(self):
        integer, ok = QInputDialog().getInt(None, "Enter New Planet Y Coordinate",
                                     "Enter New Planet Y Coordinate")
        if ok:
            planet_name = self.window.planetSelection.currentText()
            if planet_name in [x.name for x in self.planets]:
                planet_index = [x.name for x in self.planets].index(planet_name)
            
            self.window.YPosition.setText(str(integer))

            
            self.save_to_cache()
            self.window.plotSelectedPlanet(self.planets[planet_index])
    def set_data_path(self):
        dataPath = str(QFileDialog.getExistingDirectory())
        validate_datapath(dataPath)
        if dataPath == self.mod_dir:
            return
        dataPath=dataPath.replace('%20',' ')
        encode(dataPath, 'dataPath')
        self.mod_dir = dataPath
        self.set_planets()
        self.window.planets = self.planets
        self.window.planetSelection.currentIndexChanged.disconnect(self.window.on_index_changed)

        self.window.planetSelection.clear()
        for planet in self.planets:
            self.window.planetSelection.addItem(planet.name)
        planet_name = self.window.planetSelection.currentText()
        if planet_name in [x.name for x in self.planets]:
            planet_index = [x.name for x in self.planets].index(planet_name)
        planet = self.planets[planet_index]
        self.window.plotGalaxy(self.planets)
        self.window.plotSelectedPlanet(self.planets[planet_index])
        self.window.PlanetModelName.setText(planet.model_name)
        self.window.LandMap.setText(planet.land_map)
        self.window.SpaceMap.setText(planet.space_map)
        self.window.XPosition.setText(str(planet.x))
        self.window.yPosition.setText(str(planet.y))
        self.window.planetSelection.currentIndexChanged.connect(self.window.on_index_changed)
    def get_mod_dir(self):
        dataPath = str(QFileDialog.getExistingDirectory())
        validate_datapath(dataPath)
        encode(dataPath, 'dataPath')
        return dataPath
    def set_planets(self):
        game_object_files = []
        self.planets = []
        if os.path.isdir('xml'):
            xmlPath = '/xml'
        else:
            xmlPath = '/XML'
        gameObjectFiles = et.parse(self.mod_dir+xmlPath+'/gameobjectfiles.xml')
        for child in gameObjectFiles.getroot():
            if child.tag == 'File':
                game_object_files.append(self.mod_dir+xmlPath+'/'+child.text)
        for file in game_object_files:
            try:
                root = et.parse(file).getroot()
            except:
                continue
            if root.tag == 'Planets':
                self.planetFiles.append(os.path.abspath(file))
            for child in root:
                if child.tag == 'Planet':
                    if child.get('Name') != 'Galaxy_Core_Art_Model':
                        self.planets.append(Planet(child, file, self.logfile))
                        if not file in self.planetFiles:
                            self.planetFiles.append(file)
    def save_to_cache(self):
        planet = self.planets[self.window.planetSelection.currentIndex()]
        print(planet.name)
        if self.window.PlanetModelName.text() != planet.get_model_name(self.logfile):
            planet.model_name = self.window.PlanetModelName.text()
        if self.window.SpaceMap.text() != planet.get_space_map(self.logfile):
            planet.space_map = self.window.SpaceMap.text()
        if self.window.LandMap.text() != planet.get_land_map(self.logfile):
            planet.land_map = self.window.LandMap.text()
        if self.window.XPosition.text() != planet.x:
            planet.x = math.floor(float(self.window.XPosition.text()))
        if self.window.yPosition.text() != planet.y:
            planet.y = math.floor(float(self.window.yPosition.text()))
        print(planet.x)
        print(planet.y)
    def save_to_file(self):
        for file in self.planetFiles:
            try:
                xml = et.parse(file)
            except:
                continue
            for child in xml.getroot():
                if child.tag == 'Planet':
                    if child.get('Name') in [x.name for x in self.planets]:
                        planet_index = [x.name for x in self.planets].index(child.get('Name'))
                        planet = self.planets[planet_index]
                        for elem in child:
                            if elem.tag == 'Land_Tactical_Map':
                                if planet.land_map != elem.text:
                                    elem.text = planet.land_map
                            if elem.tag == 'Space_Tactical_Map':
                                if planet.space_map != elem.text:
                                    elem.text = planet.space_map
                            if elem.tag == 'Galactic_Position':
                                galPosition = str(planet.x)
                                galPosition = galPosition + ", "
                                galPosition = galPosition + str(planet.y)
                                galPosition = galPosition + ", 10.0"
                                if galPosition != elem.text:
                                    elem.text = galPosition
            tree= et.ElementTree(xml.getroot())
            tree.write(file,xml_declaration=True, encoding='UTF-8')
            #writeFile.write()
            
PlanetPlacementTool()