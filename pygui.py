#Install the following libraries before running the code [PyQt5, matplotlib, simphony]

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from simphony.libraries import siepic
from simphony.simulation import Detector, Laser, Simulation


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
#adjust the dimension of the window
        
        MainWindow.resize(743, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Creating the first combo box
        self.comp_1 = QtWidgets.QComboBox(self.centralwidget)
        #set its size and other prefrences
        self.comp_1.setGeometry(QtCore.QRect(20, 90, 101, 41))
        self.comp_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comp_1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #naming and assigneing number of values will be later altered
        self.comp_1.setObjectName("comp_1")
        self.comp_1.addItem("")
        self.comp_1.addItem("")
        self.comp_1.addItem("")
        self.comp_1.addItem("")
        self.comp_1.addItem("")
        self.comp_1.addItem("")
        
        self.comp_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comp_2.setGeometry(QtCore.QRect(140, 90, 101, 41))
        self.comp_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comp_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comp_2.setObjectName("comp_2")
        self.comp_2.addItem("")
        self.comp_2.addItem("")
        self.comp_2.addItem("")
        self.comp_2.addItem("")
        self.comp_2.addItem("")
        self.comp_2.addItem("")
        
        self.comp_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comp_3.setGeometry(QtCore.QRect(260, 90, 101, 41))
        self.comp_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comp_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comp_3.setObjectName("comp_3")
        self.comp_3.addItem("")
        self.comp_3.addItem("")
        self.comp_3.addItem("")
        self.comp_3.addItem("")
        self.comp_3.addItem("")
        self.comp_3.addItem("")
        
        self.comp_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comp_4.setGeometry(QtCore.QRect(380, 90, 101, 41))
        self.comp_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comp_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comp_4.setObjectName("comp_4")
        self.comp_4.addItem("")
        self.comp_4.addItem("")
        self.comp_4.addItem("")
        self.comp_4.addItem("")
        self.comp_4.addItem("")
        self.comp_4.addItem("")
        
        self.comp_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comp_5.setGeometry(QtCore.QRect(500, 90, 101, 41))
        self.comp_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comp_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comp_5.setObjectName("comp_5")
        self.comp_5.addItem("")
        self.comp_5.addItem("")
        self.comp_5.addItem("")
        self.comp_5.addItem("")
        self.comp_5.addItem("")
        self.comp_5.addItem("")
        
        self.comp_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comp_6.setGeometry(QtCore.QRect(620, 90, 101, 41))
        self.comp_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comp_6.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comp_6.setObjectName("comp_6")
        self.comp_6.addItem("")
        self.comp_6.addItem("")
        self.comp_6.addItem("")
        self.comp_6.addItem("")
        self.comp_6.addItem("")
        self.comp_6.addItem("")

        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(490, 210, 171, 23))
        self.error_label.setObjectName("error_label")
        #Creating a spin box to input the value for the long wavelength
        #setting the min and max values
        self.wg_long = QtWidgets.QSpinBox(self.centralwidget)
        self.wg_long.setGeometry(QtCore.QRect(170, 150, 61, 31))
        self.wg_long.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wg_long.setMinimum(1)
        self.wg_long.setMaximum(9999)
        self.wg_long.setObjectName("wg_long")
        
        #Creating a spin box to input the value for the short wavelength
        self.wg_short = QtWidgets.QSpinBox(self.centralwidget)
        self.wg_short.setGeometry(QtCore.QRect(410, 150, 61, 31))
        self.wg_short.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wg_short.setMinimum(1)
        self.wg_short.setMaximum(9999)
        self.wg_short.setObjectName("wg_short")
        
        #Creating a spin box to input the value for the Power 
        self.power = QtWidgets.QSpinBox(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(630, 150, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power.sizePolicy().hasHeightForWidth())
        self.power.setSizePolicy(sizePolicy)
        self.power.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.power.setMinimum(0)
        self.power.setMaximum(9999)
        self.power.setObjectName("power")

        #Creating a Push button to start initiate the coding process
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(280, 210, 171, 23))
        self.run.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.run.setObjectName("run")
        #assign the function (Value) to the button when clicked 
        self.run.clicked.connect(self.value)

        #these are just static labels for instructions on the screen
        self.Illustration = QtWidgets.QLabel(self.centralwidget)
        self.Illustration.setGeometry(QtCore.QRect(65, 240, 621, 171))
        self.Illustration.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Illustration.setPixmap(QtGui.QPixmap("Illustration.png"))
        self.Illustration.setScaledContents(False)
        self.Illustration.setObjectName("Illustration")

        self.thero = QtWidgets.QLabel(self.centralwidget)
        self.thero.setGeometry(QtCore.QRect(140, 440, 200, 200))
        self.thero.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.thero.setScaledContents(True)
        self.thero.setObjectName("thero")

        self.noise = QtWidgets.QLabel(self.centralwidget)
        self.noise.setGeometry(QtCore.QRect(370, 440, 200, 200))
        self.noise.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.noise.setScaledContents(True)
        self.noise.setObjectName("noise")


        self.static_label = QtWidgets.QLabel(self.centralwidget)
        self.static_label.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.static_label.setObjectName("static_label")
        
        self.static_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.static_label_2.setGeometry(QtCore.QRect(150, 60, 81, 20))
        self.static_label_2.setObjectName("static_label_2")
        
        self.static_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.static_label_3.setGeometry(QtCore.QRect(270, 60, 91, 20))
        self.static_label_3.setObjectName("static_label_3")
        
        self.static_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.static_label_4.setGeometry(QtCore.QRect(380, 60, 101, 20))
        self.static_label_4.setObjectName("static_label_4")
        
        self.static_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.static_label_5.setGeometry(QtCore.QRect(510, 60, 81, 20))
        self.static_label_5.setObjectName("static_label_5")
        
        self.static_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.static_label_6.setGeometry(QtCore.QRect(630, 60, 91, 20))
        self.static_label_6.setObjectName("static_label_6")
        
        self.main_txt = QtWidgets.QLabel(self.centralwidget)
        self.main_txt.setGeometry(QtCore.QRect(20, 20, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.main_txt.setFont(font)
        self.main_txt.setObjectName("main_txt")
        
        self.therm_label= QtWidgets.QLabel(self.centralwidget)
        self.therm_label.setGeometry((QtCore.QRect(140, 420, 311, 21)))
        self.therm_label.setFont(font)
        self.therm_label.setObjectName("therm_label")
        
        self.noises_label= QtWidgets.QLabel(self.centralwidget)
        self.noises_label.setGeometry((QtCore.QRect(370, 420, 311, 21)))
        self.noises_label.setFont(font)
        self.noises_label.setObjectName("noises_label")

        
        self.wgl_label = QtWidgets.QLabel(self.centralwidget)
        self.wgl_label.setGeometry(QtCore.QRect(20, 150, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wgl_label.setFont(font)
        self.wgl_label.setObjectName("wgl_label")
        self.wgs_label = QtWidgets.QLabel(self.centralwidget)
        self.wgs_label.setGeometry(QtCore.QRect(250, 150, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wgs_label.setFont(font)
        self.wgs_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wgs_label.setObjectName("wgs_label")
        
        self.power_label = QtWidgets.QLabel(self.centralwidget)
        self.power_label.setGeometry(QtCore.QRect(500, 150, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.power_label.setFont(font)
        self.power_label.setObjectName("power_label")
        
        #For fitting the text in the screen 
        MainWindow.setCentralWidget(self.centralwidget)
        # calling the function that translates the blank spaces in the combo boxes to values we desire
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.comp_1.currentIndex()==2:
            print(self.comp_1.currentIndex)
    def value(self):
        content = [int(self.comp_1.currentIndex()),int(self.comp_2.currentIndex()),int(self.comp_3.currentIndex()), int(self.comp_4.currentIndex()),int(self.comp_5.currentIndex()),int(self.comp_6.currentIndex())]
        spiners=[int(self.wg_long.value()), int(self.wg_short.value()), int(self.power.value())]
        wg_long_m=int(spiners[0])*1e-6
        wg_short_m=int(spiners[1])*1e-6
        if content[0]==1:
            gc_input = siepic.GratingCoupler()
            _translate = QtCore.QCoreApplication.translate
            self.error_label.setText(_translate("MainWindow", ""))
            if content[1]==3 and content[2]==5 and content[3]==4 and content[4]==2:
                y_splitter = siepic.YBranch()
                wg_long = siepic.Waveguide(length=wg_long_m)
                wg_short = siepic.Waveguide(length=wg_short_m)
                y_splitter["pin1"].connect(gc_input["pin1"])
                y_splitter.connect(wg_long)
                y_splitter["pin3"].connect(wg_short)
                y_recombiner = siepic.YBranch()
                gc_output = siepic.GratingCoupler()
                y_recombiner.multiconnect(gc_output, wg_short, wg_long)
                _translate = QtCore.QCoreApplication.translate
                self.error_label.setText(_translate("MainWindow",""))
                theoretical = None
            

                watt=int(spiners[2])*1e-3
                with Simulation() as sim:
                    l = Laser(power=watt)
                    l.wlsweep(1500e-9, 1600e-9)
                    l.connect(gc_input)
                    Detector().connect(gc_output)
                    theoretical = sim.sample()
                plt.plot(sim.freqs, theoretical[:, 0, 0])
                plt.title("Theoritically")
                plt.tight_layout()
                #fig, ax=plt.subplots(nrows=1, ncols=1)
                plt.show()
                plt.savefig("Theor.png")


                 #if we specify multiple samples, noise gets added to the simulation
                with Simulation() as sim:
                    l = Laser(power=watt)
                    l.wlsweep(1500e-9, 1600e-9)
                    l.connect(gc_input)
                    Detector().connect(gc_output)
                    # we get 101 samples even though we only use 3 because
                    # filtering requires at least 21 samples and the results
                    # get better with more samples and 101 isn't much slower
                    # than 21
                    noisy = sim.sample(101)
                plt.plot(sim.freqs, noisy[:, 0, 0], label="Noisy 1")
                plt.plot(sim.freqs, noisy[:, 0, 1], label="Noisy 2")
                plt.plot(sim.freqs, noisy[:, 0, 2], label="Noisy 3")
                plt.plot(sim.freqs, theoretical[:, 0, 0], "k", label="Theoretical")
                plt.legend()
                plt.title("Noises")
                plt.tight_layout()
                plt.show()
                plt.savefig("noise.png")
                self.noise.setPixmap(QtGui.QPixmap("noise.png"))
                self.thero.setPixmap(QtGui.QPixmap("Theor.png"))
                self.therm_label.setText("Theoritically:")
                self.noises_label.setText("With noises:")
            else:
                _translate = QtCore.QCoreApplication.translate
                self.error_label.setText(_translate("MainWindow", "There is something wrong with the connection!\nPlease, check the circuit components\' order."))
                self.error_label.adjustSize()
        else:    
            _translate = QtCore.QCoreApplication.translate
            self.error_label.setText(_translate("MainWindow", "Circut should start with \'GC (input)\'"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comp_1.setItemText(0, _translate("MainWindow", "None"))
        self.comp_1.setItemText(1, _translate("MainWindow", "GC (input)"))
        self.comp_1.setItemText(2, _translate("MainWindow", "GC (output)"))
        self.comp_1.setItemText(3, _translate("MainWindow", "Y splitter"))
        self.comp_1.setItemText(4, _translate("MainWindow", "Y combiner"))
        self.comp_1.setItemText(5, _translate("MainWindow", "Wavequide"))
        self.run.setText(_translate("MainWindow", "RUN!", "Run the code"))
        self.static_label.setText(_translate("MainWindow", "First Component"))
        self.static_label_2.setText(_translate("MainWindow", "Second Component"))
        self.static_label_3.setText(_translate("MainWindow", "Third component"))
        self.static_label_4.setText(_translate("MainWindow", "Fourth component"))
        self.static_label_5.setText(_translate("MainWindow", "Fifth component"))
        self.static_label_6.setText(_translate("MainWindow", "Sixth component"))
        self.main_txt.setText(_translate("MainWindow", "Mach-Zehnder Interferometer Simulator"))
        self.wgl_label.setText(_translate("MainWindow", "Waveguide Long [e-6 m] :"))
        self.wgs_label.setText(_translate("MainWindow", "Waveguide Short [e-6 m] :"))
        self.power_label.setText(_translate("MainWindow", "Laser Power [e-3 W] :"))
        self.comp_2.setItemText(0, _translate("MainWindow", "None"))
        self.comp_2.setItemText(1, _translate("MainWindow", "GC (input)"))
        self.comp_2.setItemText(2, _translate("MainWindow", "GC (output)"))
        self.comp_2.setItemText(3, _translate("MainWindow", "Y splitter"))
        self.comp_2.setItemText(4, _translate("MainWindow", "Y combiner"))
        self.comp_2.setItemText(5, _translate("MainWindow", "Wavequide"))
        self.comp_3.setItemText(0, _translate("MainWindow", "None"))
        self.comp_3.setItemText(1, _translate("MainWindow", "GC (input)"))
        self.comp_3.setItemText(2, _translate("MainWindow", "GC (output)"))
        self.comp_3.setItemText(3, _translate("MainWindow", "Y splitter"))
        self.comp_3.setItemText(4, _translate("MainWindow", "Y combiner"))
        self.comp_3.setItemText(5, _translate("MainWindow", "Wavequide"))
        self.comp_4.setItemText(0, _translate("MainWindow", "None"))
        self.comp_4.setItemText(1, _translate("MainWindow", "GC (input)"))
        self.comp_4.setItemText(2, _translate("MainWindow", "GC (output)"))
        self.comp_4.setItemText(3, _translate("MainWindow", "Y splitter"))
        self.comp_4.setItemText(4, _translate("MainWindow", "Y combiner"))
        self.comp_4.setItemText(5, _translate("MainWindow", "Wavequide"))
        self.comp_5.setItemText(0, _translate("MainWindow", "None"))
        self.comp_5.setItemText(1, _translate("MainWindow", "GC (input)"))
        self.comp_5.setItemText(2, _translate("MainWindow", "GC (output)"))
        self.comp_5.setItemText(3, _translate("MainWindow", "Y splitter"))
        self.comp_5.setItemText(4, _translate("MainWindow", "Y combiner"))
        self.comp_5.setItemText(5, _translate("MainWindow", "Wavequide"))
        self.comp_6.setItemText(0, _translate("MainWindow", "None"))
        self.comp_6.setItemText(1, _translate("MainWindow", "GC (input)"))
        self.comp_6.setItemText(2, _translate("MainWindow", "GC (output)"))
        self.comp_6.setItemText(3, _translate("MainWindow", "Y splitter"))
        self.comp_6.setItemText(4, _translate("MainWindow", "Y combiner"))
        self.comp_6.setItemText(5, _translate("MainWindow", "Wavequide"))

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()    
    
    sys.exit(app.exec_())
