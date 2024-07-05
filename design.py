# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1006, 828)
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 30, 941, 201))
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 310, 461, 211))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 441, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.edit_d_firstname = QLineEdit(self.widget)
        self.edit_d_firstname.setObjectName(u"edit_d_firstname")

        self.horizontalLayout_4.addWidget(self.edit_d_firstname)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.edit_d_lastname = QLineEdit(self.widget)
        self.edit_d_lastname.setObjectName(u"edit_d_lastname")

        self.horizontalLayout_4.addWidget(self.edit_d_lastname)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.widget1 = QWidget(self.groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 20, 234, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.edit_d_country = QLineEdit(self.widget1)
        self.edit_d_country.setObjectName(u"edit_d_country")

        self.horizontalLayout_6.addWidget(self.edit_d_country)

        self.widget2 = QWidget(self.groupBox)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 120, 441, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.widget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.edit_d_address = QLineEdit(self.widget2)
        self.edit_d_address.setObjectName(u"edit_d_address")

        self.horizontalLayout_7.addWidget(self.edit_d_address)

        self.widget3 = QWidget(self.groupBox)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 170, 441, 26))
        self.horizontalLayout_11 = QHBoxLayout(self.widget3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.widget3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.edit_d_city = QLineEdit(self.widget3)
        self.edit_d_city.setObjectName(u"edit_d_city")

        self.horizontalLayout_8.addWidget(self.edit_d_city)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.widget3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.edit_d_state = QLineEdit(self.widget3)
        self.edit_d_state.setObjectName(u"edit_d_state")

        self.horizontalLayout_9.addWidget(self.edit_d_state)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.widget3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.edit_d_zipcode = QLineEdit(self.widget3)
        self.edit_d_zipcode.setObjectName(u"edit_d_zipcode")

        self.horizontalLayout_10.addWidget(self.edit_d_zipcode)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(510, 310, 471, 211))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 170, 441, 26))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.edit_b_city = QLineEdit(self.layoutWidget)
        self.edit_b_city.setObjectName(u"edit_b_city")

        self.horizontalLayout_13.addWidget(self.edit_b_city)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.edit_b_state = QLineEdit(self.layoutWidget)
        self.edit_b_state.setObjectName(u"edit_b_state")

        self.horizontalLayout_14.addWidget(self.edit_b_state)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.edit_b_zipcode = QLineEdit(self.layoutWidget)
        self.edit_b_zipcode.setObjectName(u"edit_b_zipcode")

        self.horizontalLayout_15.addWidget(self.edit_b_zipcode)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 1)
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 70, 441, 26))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.edit_b_firstname = QLineEdit(self.layoutWidget_2)
        self.edit_b_firstname.setObjectName(u"edit_b_firstname")

        self.horizontalLayout_18.addWidget(self.edit_b_firstname)

        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.edit_b_lastname = QLineEdit(self.layoutWidget_2)
        self.edit_b_lastname.setObjectName(u"edit_b_lastname")

        self.horizontalLayout_18.addWidget(self.edit_b_lastname)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_18)

        self.layoutWidget_3 = QWidget(self.groupBox_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 20, 234, 24))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.edit_b_country = QLineEdit(self.layoutWidget_3)
        self.edit_b_country.setObjectName(u"edit_b_country")

        self.horizontalLayout_19.addWidget(self.edit_b_country)

        self.layoutWidget_4 = QWidget(self.groupBox_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 120, 441, 24))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget_4)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.edit_b_address = QLineEdit(self.layoutWidget_4)
        self.edit_b_address.setObjectName(u"edit_b_address")

        self.horizontalLayout_20.addWidget(self.edit_b_address)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 530, 951, 101))
        self.widget4 = QWidget(self.groupBox_3)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(20, 20, 391, 24))
        self.horizontalLayout_23 = QHBoxLayout(self.widget4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget4)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_23.addWidget(self.label_18)

        self.edit_credit_number = QLineEdit(self.widget4)
        self.edit_credit_number.setObjectName(u"edit_credit_number")

        self.horizontalLayout_23.addWidget(self.edit_credit_number)

        self.widget5 = QWidget(self.groupBox_3)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(480, 20, 331, 24))
        self.horizontalLayout_25 = QHBoxLayout(self.widget5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget5)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_25.addWidget(self.label_19)

        self.edit_credit_expiry = QLineEdit(self.widget5)
        self.edit_credit_expiry.setObjectName(u"edit_credit_expiry")

        self.horizontalLayout_25.addWidget(self.edit_credit_expiry)

        self.widget6 = QWidget(self.groupBox_3)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(480, 60, 331, 24))
        self.horizontalLayout_26 = QHBoxLayout(self.widget6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget6)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_26.addWidget(self.label_20)

        self.edit_credit_code = QLineEdit(self.widget6)
        self.edit_credit_code.setObjectName(u"edit_credit_code")

        self.horizontalLayout_26.addWidget(self.edit_credit_code)

        self.widget7 = QWidget(self.groupBox_3)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(20, 60, 391, 24))
        self.horizontalLayout_24 = QHBoxLayout(self.widget7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget7)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_24.addWidget(self.label_21)

        self.edit_credit_name = QLineEdit(self.widget7)
        self.edit_credit_name.setObjectName(u"edit_credit_name")

        self.horizontalLayout_24.addWidget(self.edit_credit_name)

        self.btn_start = QPushButton(Form)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(890, 640, 93, 28))
        self.text_log = QTextEdit(Form)
        self.text_log.setObjectName(u"text_log")
        self.text_log.setGeometry(QRect(30, 640, 841, 141))
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 790, 841, 23))
        self.progressBar.setValue(24)
        self.widget8 = QWidget(Form)
        self.widget8.setObjectName(u"widget8")
        self.widget8.setGeometry(QRect(30, 240, 941, 30))
        self.horizontalLayout_21 = QHBoxLayout(self.widget8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget8)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edit_product = QLineEdit(self.widget8)
        self.edit_product.setObjectName(u"edit_product")

        self.horizontalLayout.addWidget(self.edit_product)


        self.horizontalLayout_21.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.edit_quantity = QLineEdit(self.widget8)
        self.edit_quantity.setObjectName(u"edit_quantity")

        self.horizontalLayout_2.addWidget(self.edit_quantity)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_2)

        self.but_add = QPushButton(self.widget8)
        self.but_add.setObjectName(u"but_add")

        self.horizontalLayout_21.addWidget(self.but_add)

        self.but_delete = QPushButton(self.widget8)
        self.but_delete.setObjectName(u"but_delete")

        self.horizontalLayout_21.addWidget(self.but_delete)

        self.horizontalLayout_21.setStretch(0, 2)
        self.widget9 = QWidget(Form)
        self.widget9.setObjectName(u"widget9")
        self.widget9.setGeometry(QRect(30, 280, 381, 24))
        self.horizontalLayout_22 = QHBoxLayout(self.widget9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget9)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_22.addWidget(self.label_3)

        self.edit_email = QLineEdit(self.widget9)
        self.edit_email.setObjectName(u"edit_email")

        self.horizontalLayout_22.addWidget(self.edit_email)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Shopify Bot", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Product URL", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Quantity", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"asgweg", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem4 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"1234123", None));
        ___qtablewidgetitem5 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"5", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Delivery Address", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Firstname", None))
#if QT_CONFIG(statustip)
        self.edit_d_firstname.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Lastname", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Country/Region", None))
#if QT_CONFIG(tooltip)
        self.edit_d_country.setToolTip(QCoreApplication.translate("Form", u"US, Mexico, Canada", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Address", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"City", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"State", None))
#if QT_CONFIG(tooltip)
        self.edit_d_state.setToolTip(QCoreApplication.translate("Form", u"Abbreviation e.g(CA)", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"Zipcode", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Billing Address", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"City", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"State", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Zipcode", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Firstname", None))
#if QT_CONFIG(statustip)
        self.edit_b_firstname.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_15.setText(QCoreApplication.translate("Form", u"Lastname", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Country/Region", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Address", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Credit Card", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Card Number", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Expiration Date", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Security Code", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Name on Card", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.label.setText(QCoreApplication.translate("Form", u"Product URL", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.but_add.setText(QCoreApplication.translate("Form", u"Add", None))
        self.but_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
    # retranslateUi

