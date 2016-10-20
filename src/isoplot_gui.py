# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'isoplot_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(980, 642)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 10, 261, 571))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.plot_treeWidget = QtGui.QTreeWidget(self.groupBox_2)
        self.plot_treeWidget.setObjectName(_fromUtf8("plot_treeWidget"))
        self.plot_treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_4.addWidget(self.plot_treeWidget)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.btn_run_plotfcn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_run_plotfcn.setObjectName(_fromUtf8("btn_run_plotfcn"))
        self.verticalLayout.addWidget(self.btn_run_plotfcn)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 341, 551))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.data_treeWidget = QtGui.QTreeWidget(self.groupBox)
        self.data_treeWidget.setObjectName(_fromUtf8("data_treeWidget"))
        self.data_treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_3.addWidget(self.data_treeWidget)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.groupBox.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Data_File = QtGui.QAction(MainWindow)
        self.actionOpen_Data_File.setObjectName(_fromUtf8("actionOpen_Data_File"))
        self.actionSet_default_directory = QtGui.QAction(MainWindow)
        self.actionSet_default_directory.setObjectName(_fromUtf8("actionSet_default_directory"))
        self.actionAdd_plotting_module = QtGui.QAction(MainWindow)
        self.actionAdd_plotting_module.setObjectName(_fromUtf8("actionAdd_plotting_module"))
        self.actionReset_User_Settings = QtGui.QAction(MainWindow)
        self.actionReset_User_Settings.setObjectName(_fromUtf8("actionReset_User_Settings"))
        self.actionAdd_loading_module = QtGui.QAction(MainWindow)
        self.actionAdd_loading_module.setObjectName(_fromUtf8("actionAdd_loading_module"))
        self.menuSettings.addAction(self.actionSet_default_directory)
        self.menuSettings.addAction(self.actionAdd_plotting_module)
        self.menuSettings.addAction(self.actionAdd_loading_module)
        self.menuSettings.addAction(self.actionReset_User_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Plot Functions", None))
        self.btn_run_plotfcn.setText(_translate("MainWindow", "Run", None))
        self.groupBox.setTitle(_translate("MainWindow", "Data", None))
        self.pushButton_2.setText(_translate("MainWindow", "Plot 1", None))
        self.pushButton_3.setText(_translate("MainWindow", "Plot2", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.actionOpen_Data_File.setText(_translate("MainWindow", "Open Data File", None))
        self.actionSet_default_directory.setText(_translate("MainWindow", "Set default directory", None))
        self.actionAdd_plotting_module.setText(_translate("MainWindow", "Add plotting module", None))
        self.actionReset_User_Settings.setText(_translate("MainWindow", "Reset User Settings", None))
        self.actionAdd_loading_module.setText(_translate("MainWindow", "Add loading module", None))

