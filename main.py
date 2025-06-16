import sys
import os
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QFrame,
    QPushButton,
    QFileDialog,
    QApplication
)
from PyQt5.QtGui import QGuiApplication, QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QRect
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SnippingTool(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        self.showFullScreen()
        self.setWindowOpacity(0.3)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        self.currX = 0;
        self.currY = 0;

        screenshot = QGuiApplication.primaryScreen().grabWindow(0)
        screenshot.save("screenshot.png", "png")


    def snip(self):
        img = Image.open("screenshot.png")
        x1, x2 = sorted([self.x1, self.x2])
        y1, y2 = sorted([self.y1, self.y2])
        print(x1)
        crop_box = (x1, y1, x2, y2)
        cropped_img = img.crop(crop_box)
        cropped_img.save("snip.png")
    

    def keyPressEvent(self, event):
        self.close()
        QApplication.quit()
    
    def mousePressEvent(self, event):
        point = event.globalPos()
        self.x1 = point.x()
        self.y1 = point.y()
    
    def mouseMoveEvent(self, event):
        currPoint = event.pos()
        self.currX = currPoint.x()
        self.currY = currPoint.y()
        self.update()
    
        
    def paintEvent(self, event):
        painter = QPainter(self) 
        pen = QPen(Qt.green, 5)
        painter.setPen(pen)
        painter.drawLine(self.x1,self.y1, self.currX, self.y1) #horizontal line 1
        painter.drawLine(self.x1,self.y1, self.x1, self.currY) #vertical line 1
        painter.drawLine(self.x1,self.currY, self.currX, self.currY) #horizontal line 2
        painter.drawLine(self.currX,self.y1, self.currX, self.currY) #horizontal line 2

        #drawing the reactangle here (completely transparent)
        painter.setCompositionMode(QPainter.CompositionMode_Clear)
        tempRect = QRect(self.x1, self.y1, self.currX - self.x1, self.currY - self.y1).normalized()
        painter.fillRect(tempRect, Qt.transparent)

    
    def mouseReleaseEvent(self, event):
        point = event.globalPos()
        self.x2 = point.x()
        self.y2 = point.y()
        self.snip()
        self.close()
        self.reverseImageSearch()
        QApplication.quit()
    

    def reverseImageSearch(self):
        d = webdriver.Chrome(executable_path="chromedriver.exe")

        #going to google images
        d.get("https://images.google.com/")

        #clicking the camera icon (to upload the image)
        search_by_image_btn = d.find_element(By.CLASS_NAME, "Gdd5U")
        search_by_image_btn.click()
        time.sleep(1)#wont work without this for some reason

        #clicking the "upload image" section
        upload_tab = d.find_element(By.CLASS_NAME, 'cB9M7')
        upload_tab.click()

        upload_input = d.find_element(By.NAME, "encoded_image")

        abs_path = os.path.abspath("snip.png")
        upload_input.send_keys(abs_path)

        time.sleep(30) #fix later



    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    snipping_app = SnippingTool()
    snipping_app.show()
    sys.exit(app.exec_());