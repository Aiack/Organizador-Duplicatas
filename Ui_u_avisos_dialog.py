# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jhelison\Documents\Python\PYQT\Gerenciador de boletos\Modelos\u_avisos_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(898, 616)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_duplicatas = QtWidgets.QWidget()
        self.tab_duplicatas.setObjectName("tab_duplicatas")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_duplicatas)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.tab_duplicatas)
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget_duplicatas_vencidas = QtWidgets.QTableWidget(self.verticalGroupBox_2)
        self.tableWidget_duplicatas_vencidas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_duplicatas_vencidas.setObjectName("tableWidget_duplicatas_vencidas")
        self.tableWidget_duplicatas_vencidas.setColumnCount(0)
        self.tableWidget_duplicatas_vencidas.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_duplicatas_vencidas)
        self.verticalLayout_3.addWidget(self.verticalGroupBox_2)
        self.verticalGroupBox_3 = QtWidgets.QGroupBox(self.tab_duplicatas)
        self.verticalGroupBox_3.setObjectName("verticalGroupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_duplicata_com_alerta = QtWidgets.QTableWidget(self.verticalGroupBox_3)
        self.tableWidget_duplicata_com_alerta.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_duplicata_com_alerta.setObjectName("tableWidget_duplicata_com_alerta")
        self.tableWidget_duplicata_com_alerta.setColumnCount(0)
        self.tableWidget_duplicata_com_alerta.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget_duplicata_com_alerta)
        self.verticalLayout_3.addWidget(self.verticalGroupBox_3)
        self.label_3 = QtWidgets.QLabel(self.tab_duplicatas)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tabWidget.addTab(self.tab_duplicatas, "")
        self.tab_notas_fiscais = QtWidgets.QWidget()
        self.tab_notas_fiscais.setObjectName("tab_notas_fiscais")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_notas_fiscais)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalGroupBox_4 = QtWidgets.QGroupBox(self.tab_notas_fiscais)
        self.verticalGroupBox_4.setObjectName("verticalGroupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_notas_fiscais_com_vencimento = QtWidgets.QTableWidget(self.verticalGroupBox_4)
        self.tableWidget_notas_fiscais_com_vencimento.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_notas_fiscais_com_vencimento.setObjectName("tableWidget_notas_fiscais_com_vencimento")
        self.tableWidget_notas_fiscais_com_vencimento.setColumnCount(0)
        self.tableWidget_notas_fiscais_com_vencimento.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_notas_fiscais_com_vencimento)
        self.verticalLayout_8.addWidget(self.verticalGroupBox_4)
        self.verticalGroupBox_5 = QtWidgets.QGroupBox(self.tab_notas_fiscais)
        self.verticalGroupBox_5.setObjectName("verticalGroupBox_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalGroupBox_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget_notas_fiscais_com_alertas = QtWidgets.QTableWidget(self.verticalGroupBox_5)
        self.tableWidget_notas_fiscais_com_alertas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_notas_fiscais_com_alertas.setObjectName("tableWidget_notas_fiscais_com_alertas")
        self.tableWidget_notas_fiscais_com_alertas.setColumnCount(0)
        self.tableWidget_notas_fiscais_com_alertas.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget_notas_fiscais_com_alertas)
        self.verticalLayout_8.addWidget(self.verticalGroupBox_5)
        self.label_4 = QtWidgets.QLabel(self.tab_notas_fiscais)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.tabWidget.addTab(self.tab_notas_fiscais, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "AVISOS"))
        self.verticalGroupBox_2.setTitle(_translate("Dialog", "Duplicatas Vencidas"))
        self.verticalGroupBox_3.setTitle(_translate("Dialog", "Duplicatas com Alerta Proximo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_duplicatas), _translate("Dialog", "Duplicatas"))
        self.verticalGroupBox_4.setTitle(_translate("Dialog", "Notas Fiscais não recebidas com vencimentos proximos"))
        self.verticalGroupBox_5.setTitle(_translate("Dialog", "Notas Fiscais com alertas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_notas_fiscais), _translate("Dialog", "Notas Fiscais"))
