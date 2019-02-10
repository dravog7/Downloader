# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 208)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.filenameLabel = QtWidgets.QLabel(Dialog)
        self.filenameLabel.setObjectName("filenameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.filenameLabel)
        self.filenameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.filenameLineEdit.setObjectName("filenameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filenameLineEdit)
        self.uRLLabel = QtWidgets.QLabel(Dialog)
        self.uRLLabel.setObjectName("uRLLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uRLLabel)
        self.uRLLineEdit = QtWidgets.QLineEdit(Dialog)
        self.uRLLineEdit.setEnabled(False)
        self.uRLLineEdit.setText("")
        self.uRLLineEdit.setObjectName("uRLLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uRLLineEdit)
        self.speedLabel = QtWidgets.QLabel(Dialog)
        self.speedLabel.setObjectName("speedLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.speedLabel)
        self.speed = QtWidgets.QLabel(Dialog)
        self.speed.setText("")
        self.speed.setObjectName("speed")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.speed)
        self.totalSizeLabel = QtWidgets.QLabel(Dialog)
        self.totalSizeLabel.setObjectName("totalSizeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.totalSizeLabel)
        self.total = QtWidgets.QLabel(Dialog)
        self.total.setText("")
        self.total.setObjectName("total")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.total)
        self.completedLabel = QtWidgets.QLabel(Dialog)
        self.completedLabel.setObjectName("completedLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.completedLabel)
        self.completed = QtWidgets.QLabel(Dialog)
        self.completed.setText("")
        self.completed.setObjectName("completed")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.completed)
        self.statusLabel = QtWidgets.QLabel(Dialog)
        self.statusLabel.setObjectName("statusLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.statusLabel)
        self.Status = QtWidgets.QLabel(Dialog)
        self.Status.setObjectName("Status")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Status)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Download"))
        self.filenameLabel.setText(_translate("Dialog", "Filename:"))
        self.uRLLabel.setText(_translate("Dialog", "URL:"))
        self.speedLabel.setText(_translate("Dialog", "Speed:"))
        self.totalSizeLabel.setText(_translate("Dialog", "Total Size:"))
        self.completedLabel.setText(_translate("Dialog", "Completed:"))
        self.statusLabel.setText(_translate("Dialog", "Status"))
        self.Status.setText(_translate("Dialog", "Downloading"))
        self.progressBar.setFormat(_translate("Dialog", "%p%"))

