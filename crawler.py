# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crawler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request as req
from bs4 import BeautifulSoup
header = {"電影版":"https://www.ptt.cc/bbs/movie/index.html", "研究所版":"https://www.ptt.cc/bbs/graduate/index.html"}



class Ui_pttcrawler(object):
    def setupUi(self, pttcrawler):
        pttcrawler.setObjectName("pttcrawler")
        pttcrawler.resize(520, 458)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        pttcrawler.setFont(font)
        pttcrawler.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(85, 85, 127);\n"
"}")
        self.webcrawler = QtWidgets.QWidget(pttcrawler)
        self.webcrawler.setObjectName("webcrawler")
        self.output = QtWidgets.QTextEdit(self.webcrawler)
        self.output.setGeometry(QtCore.QRect(10, 10, 501, 211))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setLineWidth(2)
        self.output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.output.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.output.setDocumentTitle("")
        self.output.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.output.setReadOnly(False)
        self.output.setPlaceholderText("")
        self.output.setObjectName("output")
        
        
        self.webcombo = QtWidgets.QComboBox(self.webcrawler)
        self.webcombo.setGeometry(QtCore.QRect(10, 270, 261, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.webcombo.setFont(font)
        self.webcombo.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.webcombo.setObjectName("webcombo")
        self.webcombo.addItem("電影版")
        self.webcombo.addItem("研究所版")
        
        
        
        self.label = QtWidgets.QLabel(self.webcrawler)
        self.label.setGeometry(QtCore.QRect(20, 240, 231, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.webcrawler)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 241, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        
        self.nameinput = QtWidgets.QLineEdit(self.webcrawler)
        self.nameinput.setGeometry(QtCore.QRect(10, 360, 261, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.nameinput.setFont(font)
        self.nameinput.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.nameinput.setInputMask("")
        self.nameinput.setObjectName("nameinput")
        
        
        self.pagenumber = QtWidgets.QSpinBox(self.webcrawler)
        self.pagenumber.setGeometry(QtCore.QRect(290, 270, 211, 51))
        self.pagenumber.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pagenumber.setAlignment(QtCore.Qt.AlignCenter)
        self.pagenumber.setMinimum(1)
        self.pagenumber.setMaximum(50)
        self.pagenumber.setProperty("value", 10)
        self.pagenumber.setObjectName("pagenumber")
        
        
        self.label_3 = QtWidgets.QLabel(self.webcrawler)
        self.label_3.setGeometry(QtCore.QRect(310, 240, 171, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        
        self.pressButton = QtWidgets.QPushButton(self.webcrawler, clicked = lambda: self.press_it(header[self.webcombo.currentText()], self.nameinput.text(), self.pagenumber.value()))
        self.pressButton.setGeometry(QtCore.QRect(290, 360, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pressButton.setFont(font)
        self.pressButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pressButton.setObjectName("pressButton")
        pttcrawler.setCentralWidget(self.webcrawler)

        self.retranslateUi(pttcrawler)
        QtCore.QMetaObject.connectSlotsByName(pttcrawler)
    
        
    def getData(self, url):
        request = req.Request(url, headers = {
                "cookie":"over18=1",
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        })
        
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        
        root = BeautifulSoup(data, "html.parser") 
        titles = root.find_all("div",class_="title")
        for title in titles:
            if title.a != None: 
                self.output.append(title.a.string)
        nextlink = root.find("a", string = "‹ 上頁")
        return nextlink["href"]

    def get(self, url,papercount = 0,author=""):
        url = url
        request = req.Request(url,headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        })
        
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        root = BeautifulSoup(data, "html.parser")
        titles = root.find_all("div", class_ = "author")
        for title in titles:
            name = title.string
            if name == author:
                papercount = papercount +1
        nextpage = root.find("a",string = "‹ 上頁").get("href")
        return nextpage,papercount
    
    def press_it(self, url, user_name, page):
        if user_name == "":
            self.output.setText("")
            pageURL = url
            count = 0
            while count < page:
                pageURL = "https://www.ptt.cc"+self.getData(pageURL)
                count+=1
        else:
            urlname = url
            number = 0
            total = 0
            count = 0
            while count<page:
                urlname,number = self.get(urlname, author = user_name)
                urlname = "https://www.ptt.cc"+urlname
                total = total+number
                count+=1
            # print("{} 總共發了 {} 篇文.".format(user_name,total))
            print(total)
            self.output.setText(f"{user_name}總共發了{total}篇文!")
    
    
    def retranslateUi(self, pttcrawler):
        _translate = QtCore.QCoreApplication.translate
        pttcrawler.setWindowTitle(_translate("pttcrawler", "MainWindow"))
        self.label.setText(_translate("pttcrawler", "選擇要爬取的版"))
        self.label_2.setText(_translate("pttcrawler", "輸入用戶名字"))
        self.pagenumber.setSuffix(_translate("pttcrawler", "頁"))
        self.pagenumber.setPrefix(_translate("pttcrawler", "連續爬取"))
        self.label_3.setText(_translate("pttcrawler", "設定爬取頁數"))
        self.pressButton.setText(_translate("pttcrawler", "開始爬取"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pttcrawler = QtWidgets.QMainWindow()
    ui = Ui_pttcrawler()
    ui.setupUi(pttcrawler)
    pttcrawler.show()
    sys.exit(app.exec_())

