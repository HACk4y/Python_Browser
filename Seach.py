import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        

#navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
# Back_Btn      
      
        Back_Btn = QAction("Back",self)   
        Back_Btn.triggered.connect(self.browser.back)
        navbar.addAction(Back_Btn)

# Forward_Btn    
        Forward_Btn = QAction("Forward",self)   
        Forward_Btn.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_Btn)
        
# Reload_Btn
        Reload_Btn = QAction("Reload",self)   
        Reload_Btn.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_Btn)
        
#  Home_Btn
        Home_Btn = QAction("Home",self)   
        Home_Btn.triggered.connect(self.navigate_home)
        navbar.addAction(Home_Btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.Navigate_url)
        navbar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_url)
        
# Home DEF       
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
       
# URL SEACH   
    def Navigate_url(self):
         url= self.url_bar.text()
         self.browser.setUrl(QUrl(url))
         
# update_url
    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
        
        
        
        
App = QApplication(sys.argv)
QApplication.setApplicationName("Browser")
window = MainWindow()
App.exec_()