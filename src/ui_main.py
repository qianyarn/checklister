# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 603)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 641, 534))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setMinimumSize(QtCore.QSize(561, 0))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.SpeciesSelection = QtWidgets.QWidget()
        self.SpeciesSelection.setObjectName("SpeciesSelection")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.SpeciesSelection)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(self.SpeciesSelection)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.butDeleteAll = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDeleteAll.sizePolicy().hasHeightForWidth())
        self.butDeleteAll.setSizePolicy(sizePolicy)
        self.butDeleteAll.setObjectName("butDeleteAll")
        self.gridLayout_2.addWidget(self.butDeleteAll, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineOutputFilename = QtWidgets.QLineEdit(self.frame)
        self.lineOutputFilename.setText("")
        self.lineOutputFilename.setObjectName("lineOutputFilename")
        self.gridLayout_2.addWidget(self.lineOutputFilename, 1, 3, 1, 4)
        self.lineSlist = QtWidgets.QLineEdit(self.frame)
        self.lineSlist.setObjectName("lineSlist")
        self.gridLayout_2.addWidget(self.lineSlist, 2, 3, 1, 4)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabSelect = QtWidgets.QWidget()
        self.tabSelect.setObjectName("tabSelect")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tabSelect)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineSpecies = QtWidgets.QLineEdit(self.tabSelect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineSpecies.sizePolicy().hasHeightForWidth())
        self.lineSpecies.setSizePolicy(sizePolicy)
        self.lineSpecies.setBaseSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(False)
        self.lineSpecies.setFont(font)
        self.lineSpecies.setAutoFillBackground(False)
        self.lineSpecies.setObjectName("lineSpecies")
        self.gridLayout_9.addWidget(self.lineSpecies, 1, 0, 1, 1)
        self.butAddToTree = QtWidgets.QPushButton(self.tabSelect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butAddToTree.sizePolicy().hasHeightForWidth())
        self.butAddToTree.setSizePolicy(sizePolicy)
        self.butAddToTree.setObjectName("butAddToTree")
        self.gridLayout_9.addWidget(self.butAddToTree, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tabSelect)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tabSelect, "")
        self.tabMerge = QtWidgets.QWidget()
        self.tabMerge.setObjectName("tabMerge")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tabMerge)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 461, 71))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineMergeChecklists = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineMergeChecklists.setObjectName("lineMergeChecklists")
        self.gridLayout_5.addWidget(self.lineMergeChecklists, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        self.butMergeChecklists = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.butMergeChecklists.setObjectName("butMergeChecklists")
        self.gridLayout_5.addWidget(self.butMergeChecklists, 2, 1, 1, 1)
        self.butMerge = QtWidgets.QPushButton(self.tabMerge)
        self.butMerge.setGeometry(QtCore.QRect(480, 410, 99, 32))
        self.butMerge.setObjectName("butMerge")
        self.tabWidget_2.addTab(self.tabMerge, "")
        self.tabCompare = QtWidgets.QWidget()
        self.tabCompare.setObjectName("tabCompare")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabCompare)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineChecklistA = QtWidgets.QLineEdit(self.tabCompare)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineChecklistA.sizePolicy().hasHeightForWidth())
        self.lineChecklistA.setSizePolicy(sizePolicy)
        self.lineChecklistA.setObjectName("lineChecklistA")
        self.gridLayout_6.addWidget(self.lineChecklistA, 1, 0, 1, 1)
        self.butCheckASelect = QtWidgets.QPushButton(self.tabCompare)
        self.butCheckASelect.setObjectName("butCheckASelect")
        self.gridLayout_6.addWidget(self.butCheckASelect, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tabCompare)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.butCheckBSelect = QtWidgets.QPushButton(self.tabCompare)
        self.butCheckBSelect.setObjectName("butCheckBSelect")
        self.gridLayout_6.addWidget(self.butCheckBSelect, 1, 5, 1, 1)
        self.butCompare = QtWidgets.QPushButton(self.tabCompare)
        self.butCompare.setObjectName("butCompare")
        self.gridLayout_6.addWidget(self.butCompare, 3, 1, 1, 1)
        self.comboABDifference = QtWidgets.QComboBox(self.tabCompare)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboABDifference.sizePolicy().hasHeightForWidth())
        self.comboABDifference.setSizePolicy(sizePolicy)
        self.comboABDifference.setObjectName("comboABDifference")
        self.comboABDifference.addItem("")
        self.comboABDifference.addItem("")
        self.comboABDifference.addItem("")
        self.comboABDifference.addItem("")
        self.gridLayout_6.addWidget(self.comboABDifference, 3, 0, 1, 1)
        self.lineChecklistB = QtWidgets.QLineEdit(self.tabCompare)
        self.lineChecklistB.setObjectName("lineChecklistB")
        self.gridLayout_6.addWidget(self.lineChecklistB, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tabCompare)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 2, 1, 1)
        self.tabWidget_2.addTab(self.tabCompare, "")
        self.tabCombine = QtWidgets.QWidget()
        self.tabCombine.setObjectName("tabCombine")
        self.label_11 = QtWidgets.QLabel(self.tabCombine)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 338, 27))
        self.label_11.setObjectName("label_11")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabCombine)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 441, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineCombineChecklists = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineCombineChecklists.setObjectName("lineCombineChecklists")
        self.horizontalLayout.addWidget(self.lineCombineChecklists)
        self.butCombineChecklists = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.butCombineChecklists.setObjectName("butCombineChecklists")
        self.horizontalLayout.addWidget(self.butCombineChecklists)
        self.tabWidget_2.addTab(self.tabCombine, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 441, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineExcelFilePath = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineExcelFilePath.setText("")
        self.lineExcelFilePath.setObjectName("lineExcelFilePath")
        self.gridLayout_3.addWidget(self.lineExcelFilePath, 0, 0, 1, 1)
        self.butSelectExcel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.butSelectExcel.setObjectName("butSelectExcel")
        self.gridLayout_3.addWidget(self.butSelectExcel, 0, 1, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 70, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.lineExcelColnum = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineExcelColnum.setObjectName("lineExcelColnum")
        self.horizontalLayout_2.addWidget(self.lineExcelColnum)
        self.butFormatName = QtWidgets.QPushButton(self.tab_3)
        self.butFormatName.setGeometry(QtCore.QRect(360, 80, 131, 32))
        self.butFormatName.setObjectName("butFormatName")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 201, 39))
        self.label_12.setObjectName("label_12")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(210, 70, 121, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 3, 0, 1, 8)
        self.butDeleteSelection = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDeleteSelection.sizePolicy().hasHeightForWidth())
        self.butDeleteSelection.setSizePolicy(sizePolicy)
        self.butDeleteSelection.setObjectName("butDeleteSelection")
        self.gridLayout_2.addWidget(self.butDeleteSelection, 7, 0, 1, 1)
        self.butSelectOutput = QtWidgets.QPushButton(self.frame)
        self.butSelectOutput.setObjectName("butSelectOutput")
        self.gridLayout_2.addWidget(self.butSelectOutput, 1, 7, 1, 1)
        self.butGenerateSp = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butGenerateSp.sizePolicy().hasHeightForWidth())
        self.butGenerateSp.setSizePolicy(sizePolicy)
        self.butGenerateSp.setStyleSheet("")
        self.butGenerateSp.setObjectName("butGenerateSp")
        self.gridLayout_2.addWidget(self.butGenerateSp, 7, 7, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeWidget.setIndentation(10)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(60)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(5)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.treeWidget, 4, 0, 3, 8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 7, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 7, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.butSlist = QtWidgets.QPushButton(self.frame)
        self.butSlist.setObjectName("butSlist")
        self.gridLayout_2.addWidget(self.butSlist, 2, 7, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.SpeciesSelection, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.comboDBselect = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboDBselect.sizePolicy().hasHeightForWidth())
        self.comboDBselect.setSizePolicy(sizePolicy)
        self.comboDBselect.setObjectName("comboDBselect")
        self.comboDBselect.addItem("")
        self.comboDBselect.addItem("")
        self.comboDBselect.addItem("")
        self.comboDBselect.addItem("")
        self.gridLayout_8.addWidget(self.comboDBselect, 0, 0, 1, 1)
        self.butUpdateDB = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butUpdateDB.sizePolicy().hasHeightForWidth())
        self.butUpdateDB.setSizePolicy(sizePolicy)
        self.butUpdateDB.setObjectName("butUpdateDB")
        self.gridLayout_8.addWidget(self.butUpdateDB, 0, 1, 1, 1)
        self.comboDBselect.raise_()
        self.butUpdateDB.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.About)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.About)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 569, 447))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_11.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.About, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "checklister: a species checklist generator"))
        self.butDeleteAll.setText(_translate("MainWindow", "Delete all"))
        self.label_2.setText(_translate("MainWindow", "Export File"))
        self.lineSpecies.setToolTip(_translate("MainWindow", "<html><head/><body><p>Input species name. Type part of common names/epithets/family to list similar names. </p><p>You can press enter or return to add it to the checklist.</p></body></html>"))
        self.butAddToTree.setText(_translate("MainWindow", "Add species"))
        self.label_5.setText(_translate("MainWindow", "Common name / scientific name"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSelect), _translate("MainWindow", "Select species"))
        self.label_9.setText(_translate("MainWindow", "To be merged checklists"))
        self.butMergeChecklists.setText(_translate("MainWindow", "Select file ..."))
        self.butMerge.setText(_translate("MainWindow", "Merge"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabMerge), _translate("MainWindow", "Merge"))
        self.butCheckASelect.setText(_translate("MainWindow", "Select file ..."))
        self.label.setText(_translate("MainWindow", "Checklist A"))
        self.butCheckBSelect.setText(_translate("MainWindow", "Select file ..."))
        self.butCompare.setText(_translate("MainWindow", "Compare"))
        self.comboABDifference.setItemText(0, _translate("MainWindow", "A differ B (A - B)"))
        self.comboABDifference.setItemText(1, _translate("MainWindow", "B differ A (B - A)"))
        self.comboABDifference.setItemText(2, _translate("MainWindow", "A intersects B (A ∩ B )"))
        self.comboABDifference.setItemText(3, _translate("MainWindow", "A union B (A ∪ B)"))
        self.label_8.setText(_translate("MainWindow", "Checklist B"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabCompare), _translate("MainWindow", "Compare"))
        self.label_11.setText(_translate("MainWindow", "To be combined checklists"))
        self.butCombineChecklists.setText(_translate("MainWindow", "Select file ..."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabCombine), _translate("MainWindow", "Combine"))
        self.butSelectExcel.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select export checklist file. Supported file formats: Microsoft Word 2007 (.docx), Open document format (.odt), markdown (.md). Default is docx and markdown.</p></body></html>"))
        self.butSelectExcel.setText(_translate("MainWindow", "Select file ..."))
        self.label_10.setText(_translate("MainWindow", "Column number"))
        self.lineExcelColnum.setText(_translate("MainWindow", "1"))
        self.butFormatName.setText(_translate("MainWindow", "Format"))
        self.label_12.setText(_translate("MainWindow", "Choose file to format names:"))
        self.checkBox.setText(_translate("MainWindow", "with header"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Format"))
        self.butDeleteSelection.setText(_translate("MainWindow", "Delete selected"))
        self.butSelectOutput.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select export checklist file. Supported file formats: Microsoft Word 2007 (.docx), Open document format (.odt), markdown (.md). Default is docx and markdown.</p></body></html>"))
        self.butSelectOutput.setText(_translate("MainWindow", "Select file ..."))
        self.butGenerateSp.setText(_translate("MainWindow", "Export"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Family"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "FullNameWithAuthors"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Common name"))
        self.label_4.setText(_translate("MainWindow", "Batch Export"))
        self.butSlist.setText(_translate("MainWindow", "Select file ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SpeciesSelection), _translate("MainWindow", "Species Selection"))
        self.comboDBselect.setItemText(0, _translate("MainWindow", "Vascular plants of Taiwan (APG IV)"))
        self.comboDBselect.setItemText(1, _translate("MainWindow", "Vascular plants of Taiwan (Flora of Taiwan 2nd Edi.)"))
        self.comboDBselect.setItemText(2, _translate("MainWindow", "Bird list of Taiwan (2014)"))
        self.comboDBselect.setItemText(3, _translate("MainWindow", "Plants of Japan (Ylist)"))
        self.butUpdateDB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Update the checklist database</p></body></html>"))
        self.butUpdateDB.setText(_translate("MainWindow", "Update DB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Databases"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">checklister: </span>a species checklist generator</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Official Website: http://github.com/TaiBON/checklister</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author:  Cheng-Tao Lin mutolisp@mail.ncyu.edu.tw; mutolisp@gmail.com</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Department of Biological Resources, National Chiayi University</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contribution is welcome! </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">License</span>: GPL v 3</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://github.com/TaiBON/checklister/blob/master/LICENSE</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("MainWindow", "About"))
