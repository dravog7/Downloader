# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProgressDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(557, 240)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.TimeLeftLabel = QtWidgets.QLabel(Dialog)
        self.TimeLeftLabel.setObjectName("TimeLeftLabel")
        self.gridLayout.addWidget(self.TimeLeftLabel, 6, 0, 1, 1)
        self.Abort = QtWidgets.QPushButton(Dialog)
        self.Abort.setObjectName("Abort")
        self.gridLayout.addWidget(self.Abort, 9, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 4)
        self.uRLLineEdit = QtWidgets.QLineEdit(Dialog)
        self.uRLLineEdit.setEnabled(False)
        self.uRLLineEdit.setText("")
        self.uRLLineEdit.setObjectName("uRLLineEdit")
        self.gridLayout.addWidget(self.uRLLineEdit, 1, 1, 1, 3)
        self.Pause = QtWidgets.QPushButton(Dialog)
        self.Pause.setObjectName("Pause")
        self.gridLayout.addWidget(self.Pause, 9, 0, 1, 1)
        self.Apply = QtWidgets.QPushButton(Dialog)
        self.Apply.setObjectName("Apply")
        self.gridLayout.addWidget(self.Apply, 9, 1, 1, 1)
        self.total = QtWidgets.QLabel(Dialog)
        self.total.setText("")
        self.total.setObjectName("total")
        self.gridLayout.addWidget(self.total, 3, 1, 1, 1)
        self.speedLabel = QtWidgets.QLabel(Dialog)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout.addWidget(self.speedLabel, 2, 0, 1, 1)
        self.uRLLabel = QtWidgets.QLabel(Dialog)
        self.uRLLabel.setObjectName("uRLLabel")
        self.gridLayout.addWidget(self.uRLLabel, 1, 0, 1, 1)
        self.speed = QtWidgets.QLabel(Dialog)
        self.speed.setText("")
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 2, 1, 1, 1)
        self.totalSizeLabel = QtWidgets.QLabel(Dialog)
        self.totalSizeLabel.setObjectName("totalSizeLabel")
        self.gridLayout.addWidget(self.totalSizeLabel, 3, 0, 1, 1)
        self.filenameLabel = QtWidgets.QLabel(Dialog)
        self.filenameLabel.setObjectName("filenameLabel")
        self.gridLayout.addWidget(self.filenameLabel, 0, 0, 1, 1)
        self.filenameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.filenameLineEdit.setObjectName("filenameLineEdit")
        self.gridLayout.addWidget(self.filenameLineEdit, 0, 1, 1, 3)
        self.TimeLeft = QtWidgets.QLabel(Dialog)
        self.TimeLeft.setText("")
        self.TimeLeft.setObjectName("TimeLeft")
        self.gridLayout.addWidget(self.TimeLeft, 6, 1, 1, 1)
        self.completedLabel = QtWidgets.QLabel(Dialog)
        self.completedLabel.setObjectName("completedLabel")
        self.gridLayout.addWidget(self.completedLabel, 3, 2, 1, 1)
        self.completed = QtWidgets.QLabel(Dialog)
        self.completed.setText("")
        self.completed.setObjectName("completed")
        self.gridLayout.addWidget(self.completed, 3, 3, 1, 1)
        self.TimeElapsed = QtWidgets.QLabel(Dialog)
        self.TimeElapsed.setText("")
        self.TimeElapsed.setObjectName("TimeElapsed")
        self.gridLayout.addWidget(self.TimeElapsed, 6, 3, 1, 1)
        self.TimeElapsedLabel = QtWidgets.QLabel(Dialog)
        self.TimeElapsedLabel.setObjectName("TimeElapsedLabel")
        self.gridLayout.addWidget(self.TimeElapsedLabel, 6, 2, 1, 1)
        self.statusLabel = QtWidgets.QLabel(Dialog)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 7, 0, 1, 1)
        self.Status = QtWidgets.QLabel(Dialog)
        self.Status.setObjectName("Status")
        self.gridLayout.addWidget(self.Status, 7, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Download"))
        self.TimeLeftLabel.setText(_translate("Dialog", "Time Left:"))
        self.Abort.setText(_translate("Dialog", "Abort"))
        self.progressBar.setFormat(_translate("Dialog", "%p%"))
        self.Pause.setText(_translate("Dialog", "Pause"))
        self.Apply.setText(_translate("Dialog", "Apply"))
        self.speedLabel.setText(_translate("Dialog", "Speed:"))
        self.uRLLabel.setText(_translate("Dialog", "URL:"))
        self.totalSizeLabel.setText(_translate("Dialog", "Total Size:"))
        self.filenameLabel.setText(_translate("Dialog", "Filename:"))
        self.completedLabel.setText(_translate("Dialog", "Completed:"))
        self.TimeElapsedLabel.setText(_translate("Dialog", "Time Elapsed:"))
        self.statusLabel.setText(_translate("Dialog", "Status:"))
        self.Status.setText(_translate("Dialog", "Downloading"))

