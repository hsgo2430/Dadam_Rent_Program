# -*- coding: utf-8 -*-
import sqlite3

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 1004)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.personInformationFrame = QtWidgets.QFrame(self.centralwidget)
        self.personInformationFrame.setGeometry(QtCore.QRect(30, 190, 271, 451))
        self.personInformationFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.personInformationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personInformationFrame.setLineWidth(3)
        self.personInformationFrame.setObjectName("personInformationFrame")

        self.formFrame = QtWidgets.QFrame(self.personInformationFrame)
        self.formFrame.setGeometry(QtCore.QRect(10, 40, 251, 391))
        self.formFrame.setObjectName("formFrame")

        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(-1, -1, -1, 1)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")

        self.nameTv = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.nameTv.setFont(font)
        self.nameTv.setObjectName("nameTv")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameTv)

        self.nameEditText = QtWidgets.QTextEdit(self.formFrame)
        self.nameEditText.setBaseSize(QtCore.QSize(127, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.nameEditText.setFont(font)
        self.nameEditText.setObjectName("nameEditText")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEditText)

        self.studentIdTv = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.studentIdTv.setFont(font)
        self.studentIdTv.setObjectName("studentIdTv")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.studentIdTv)

        self.studentIdEditText = QtWidgets.QTextEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.studentIdEditText.setFont(font)
        self.studentIdEditText.setObjectName("studentIdEditText")
        self.studentIdEditText.setPlainText("")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.studentIdEditText)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.statusTv = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.statusTv.setFont(font)
        self.statusTv.setObjectName("statusTv")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.statusTv)
        self.statusComboBox = QtWidgets.QComboBox(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.statusComboBox.setFont(font)
        self.statusComboBox.setObjectName("statusComboBox")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.statusComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.majorTv = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.majorTv.setFont(font)
        self.majorTv.setObjectName("majorTv")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.majorTv)
        self.majorComboBox = QtWidgets.QComboBox(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.majorComboBox.setFont(font)
        self.majorComboBox.setObjectName("majorComboBox")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.majorComboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.majorComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.phoneNumberTv = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.phoneNumberTv.setFont(font)
        self.phoneNumberTv.setObjectName("phoneNumberTv")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.phoneNumberTv)
        self.phoneNumberEditText = QtWidgets.QTextEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.phoneNumberEditText.setFont(font)
        self.phoneNumberEditText.setObjectName("phoneNumberEditText")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.phoneNumberEditText)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label = QtWidgets.QLabel(self.personInformationFrame)
        self.label.setGeometry(QtCore.QRect(90, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(330, 190, 831, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.formFrame_4 = QtWidgets.QFrame(self.frame)
        self.formFrame_4.setGeometry(QtCore.QRect(20, 40, 331, 511))
        self.formFrame_4.setObjectName("formFrame_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formFrame_4)
        self.formLayout_4.setObjectName("formLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_4.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.YesLicenseTv = QtWidgets.QLabel(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.YesLicenseTv.setFont(font)
        self.YesLicenseTv.setObjectName("YesLicenseTv")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.YesLicenseTv)
        self.YesLicenseEditText = QtWidgets.QTextEdit(self.formFrame_4)
        self.YesLicenseEditText.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.YesLicenseEditText.setFont(font)
        self.YesLicenseEditText.setObjectName("YesLicenseEditText")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.YesLicenseEditText)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_4.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.detailedClassificationTv = QtWidgets.QLabel(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.detailedClassificationTv.setFont(font)
        self.detailedClassificationTv.setObjectName("detailedClassificationTv")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.detailedClassificationTv)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_4.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.ingredientTv = QtWidgets.QLabel(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.ingredientTv.setFont(font)
        self.ingredientTv.setObjectName("ingredientTv")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ingredientTv)
        self.firstIngredientEditText = QtWidgets.QTextEdit(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.firstIngredientEditText.setFont(font)
        self.firstIngredientEditText.setObjectName("firstIngredientEditText")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.firstIngredientEditText)
        self.secondIngredientEditText = QtWidgets.QTextEdit(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.secondIngredientEditText.setFont(font)
        self.secondIngredientEditText.setObjectName("secondIngredientEditText")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.secondIngredientEditText)
        self.thirdIngredientEditText = QtWidgets.QTextEdit(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.thirdIngredientEditText.setFont(font)
        self.thirdIngredientEditText.setObjectName("thirdIngredientEditText")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.thirdIngredientEditText)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_4.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.purposeTv = QtWidgets.QLabel(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.purposeTv.setFont(font)
        self.purposeTv.setObjectName("purposeTv")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.purposeTv)
        self.purposeEditText = QtWidgets.QTextEdit(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.purposeEditText.setFont(font)
        self.purposeEditText.setObjectName("purposeEditText")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.purposeEditText)
        self.noLicenseComboBox = QtWidgets.QComboBox(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.noLicenseComboBox.setFont(font)
        self.noLicenseComboBox.setObjectName("noLicenseComboBox")
        self.noLicenseComboBox.addItem("")
        self.noLicenseComboBox.setItemText(0, "")
        self.noLicenseComboBox.addItem("")
        self.noLicenseComboBox.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.noLicenseComboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.noLicenseTv = QtWidgets.QLabel(self.formFrame_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.noLicenseTv.setFont(font)
        self.noLicenseTv.setObjectName("noLicenseTv")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.noLicenseTv)
        self.checkLincenseBtn = QtWidgets.QPushButton(self.frame)
        self.checkLincenseBtn.setGeometry(QtCore.QRect(360, 130, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.checkLincenseBtn.setFont(font)
        self.checkLincenseBtn.setObjectName("checkLincenseBtn")
        self.checkLincenseBtn.clicked.connect(self.check_licenses)

        self.checkLicenseTable = QtWidgets.QTableWidget(self.frame)
        self.checkLicenseTable.setGeometry(QtCore.QRect(360, 230, 461, 311))
        self.checkLicenseTable.setObjectName("checkLicenseTable")
        self.checkLicenseTable.setColumnCount(3)
        self.checkLicenseTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        item.setFont(font)
        self.checkLicenseTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        item.setFont(font)
        self.checkLicenseTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        item.setFont(font)
        self.checkLicenseTable.setHorizontalHeaderItem(2, item)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(330, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formFrame_5 = QtWidgets.QFrame(self.centralwidget)
        self.formFrame_5.setGeometry(QtCore.QRect(760, 790, 231, 121))
        self.formFrame_5.setObjectName("formFrame_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formFrame_5)
        self.formLayout_5.setObjectName("formLayout_5")
        self.applyNumberTv = QtWidgets.QLabel(self.formFrame_5)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.applyNumberTv.setFont(font)
        self.applyNumberTv.setObjectName("applyNumberTv")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.applyNumberTv)
        self.textEdit = QtWidgets.QTextEdit(self.formFrame_5)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.receptionistEditText = QtWidgets.QTextEdit(self.formFrame_5)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.receptionistEditText.setFont(font)
        self.receptionistEditText.setObjectName("receptionistEditText")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.receptionistEditText)
        self.receptionistTv = QtWidgets.QLabel(self.formFrame_5)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.receptionistTv.setFont(font)
        self.receptionistTv.setObjectName("receptionistTv")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.receptionistTv)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_5.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        self.applyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.applyBtn.setGeometry(QtCore.QRect(1030, 810, 121, 81))
        self.applyBtn.setObjectName("applyBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 651, 151))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/hsgo2/Dadam/Dadam_Rent_Program/dadamImage/dadam.png"))
        #이미지 경로 설정
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.setup_table_widget()
        # 셀 더블클릭 시그널에 슬롯 연결
        self.checkLicenseTable.cellDoubleClicked.connect(self.apply_license)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameTv.setText(_translate("MainWindow", "이름"))

        self.studentIdTv.setText(_translate("MainWindow", "학번"))

        self.statusTv.setText(_translate("MainWindow", "신분"))
        self.statusComboBox.setItemText(0, _translate("MainWindow", "학부생"))
        self.statusComboBox.setItemText(1, _translate("MainWindow", "대학원생"))
        self.statusComboBox.setItemText(2, _translate("MainWindow", "교직원"))
        self.majorTv.setText(_translate("MainWindow", "학부"))
        self.majorComboBox.setItemText(0, _translate("MainWindow", "기계"))
        self.majorComboBox.setItemText(1, _translate("MainWindow", "디자인건축"))
        self.majorComboBox.setItemText(2, _translate("MainWindow", "메카"))
        self.majorComboBox.setItemText(3, _translate("MainWindow", "산경"))
        self.majorComboBox.setItemText(4, _translate("MainWindow", "에신화"))
        self.majorComboBox.setItemText(5, _translate("MainWindow", "전전통"))
        self.majorComboBox.setItemText(6, _translate("MainWindow", "컴퓨터"))
        self.majorComboBox.setItemText(7, _translate("MainWindow", "기타"))
        self.phoneNumberTv.setText(_translate("MainWindow", "연락처"))
        self.label.setText(_translate("MainWindow", "신청자 정보"))
        self.YesLicenseTv.setText(_translate("MainWindow", "장비(라이센스 O)"))
        self.detailedClassificationTv.setText(_translate("MainWindow", "사용분류"))
        self.ingredientTv.setText(_translate("MainWindow", "공구 및 재료"))
        self.purposeTv.setText(_translate("MainWindow", "사용 목적"))
        self.noLicenseComboBox.setItemText(1, _translate("MainWindow", "인두기"))
        self.noLicenseComboBox.setItemText(2, _translate("MainWindow", "오실로스코프"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "수업"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "공학설계"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "산학연"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "졸업설계"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "개인"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "동아리"))
        self.noLicenseTv.setText(_translate("MainWindow", "장비(라이센스 X)"))
        self.checkLincenseBtn.setText(_translate("MainWindow", "라이센스확인"))
        item = self.checkLicenseTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "장비명"))
        item = self.checkLicenseTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "취득날"))
        item = self.checkLicenseTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "신청"))
        self.label_6.setText(_translate("MainWindow", "대여 장비 정보"))
        self.applyNumberTv.setText(_translate("MainWindow", "신청번호"))
        self.receptionistTv.setText(_translate("MainWindow", "접수자"))
        self.applyBtn.setText(_translate("MainWindow", "신청하기"))

    def setup_table_widget(self):
        # 열 크기 조정 모드 설정
        self.checkLicenseTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        # 각 열의 너비 설정
        self.checkLicenseTable.setColumnWidth(0, 160)  # 장비명 열
        self.checkLicenseTable.setColumnWidth(1, 160)  # 취득날짜 열
        self.checkLicenseTable.setColumnWidth(2, 98)  # 신청 열

    def check_licenses(self):
        try:
            student_id = self.studentIdEditText.toPlainText()

            if student_id == "":
                QMessageBox.critical(None, '오류', '학번을 입력해 주세요.')
            else:
                conn = sqlite3.connect('../db/license.db')
                cursor = conn.cursor()

                # 장비 정보 조회
                cursor.execute('SELECT 구분, 날짜 FROM license WHERE 학번 = ?', (student_id,))
                rows = cursor.fetchall()
                conn.close()

                if len(rows) != 0:
                    self.checkLicenseTable.setRowCount(len(rows))
                    for row_index, row_data in enumerate(rows):
                        for col_index, col_data in enumerate(row_data):
                            item = QTableWidgetItem(str(col_data))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 읽기 전용으로 설정
                            self.checkLicenseTable.setItem(row_index, col_index, item)
                        apply_item = QTableWidgetItem("신청")
                        apply_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        apply_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 읽기 전용으로 설정
                        self.checkLicenseTable.setItem(row_index, 2, apply_item)
                else:
                    self.checkLicenseTable.clearContents()
                    QMessageBox.critical(None, '오류', '보유한 K-License가 없습니다.')
        except Exception as e:
            QMessageBox.critical(None, '오류', f'라이센스를 조회하는 중 오류가 발생했습니다: {str(e)}')

    def apply_license(self, row, column):
        try:
            if column == 2:  # 신청 열이 클릭되었을 때
                equipment_name = self.checkLicenseTable.item(row, 0).text()
                self.YesLicenseEditText.setPlainText(equipment_name)
                print(f'equipment_name은 {equipment_name}')

        except Exception as e:
            QMessageBox.critical(None, '오류', f'라이센스를 신청하는 중 오류가 발생했습니다: {str(e)}')