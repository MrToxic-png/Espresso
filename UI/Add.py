# Form implementation generated from reading ui file 'Add.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 479)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 20, 441, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.power = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.power.setObjectName("power")
        self.verticalLayout.addWidget(self.power)
        self.type = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.taste = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.taste.setObjectName("taste")
        self.verticalLayout.addWidget(self.taste)
        self.price = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.volume = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.volume.setObjectName("volume")
        self.verticalLayout.addWidget(self.volume)
        self.add = QtWidgets.QPushButton(parent=Dialog)
        self.add.setGeometry(QtCore.QRect(430, 400, 101, 41))
        self.add.setObjectName("add")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 111, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "название сорта"))
        self.label_2.setText(_translate("Dialog", "степень обжарки"))
        self.label_3.setText(_translate("Dialog", "молотый/в зернах"))
        self.label_4.setText(_translate("Dialog", "объем упаковки"))
        self.label_5.setText(_translate("Dialog", "описание вкуса"))
        self.label_6.setText(_translate("Dialog", "цена"))
