# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addEditCoffeeForm(object):
    def setupUi(self, addEditCoffeeForm):
        addEditCoffeeForm.setObjectName("addEditCoffeeForm")
        addEditCoffeeForm.resize(788, 206)
        self.add = QtWidgets.QPushButton(parent=addEditCoffeeForm)
        self.add.setGeometry(QtCore.QRect(120, 70, 151, 61))
        self.add.setObjectName("add")
        self.change = QtWidgets.QPushButton(parent=addEditCoffeeForm)
        self.change.setGeometry(QtCore.QRect(510, 70, 151, 61))
        self.change.setObjectName("change")

        self.retranslateUi(addEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(addEditCoffeeForm)

    def retranslateUi(self, addEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        addEditCoffeeForm.setWindowTitle(_translate("addEditCoffeeForm", "Dialog"))
        self.add.setText(_translate("addEditCoffeeForm", "Добавить"))
        self.change.setText(_translate("addEditCoffeeForm", "Изменить"))
