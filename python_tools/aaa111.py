import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRect

class ScreenshotTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('截图工具')

        # 显示截图区域
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border: 2px dashed #000")
        self.label.setFixedSize(0, 0)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 设置布局
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.label)

        # 显示主窗口
        self.show()

    def mousePressEvent(self, event):
        # 记录鼠标按下的起始点
        self.start_point = event.pos()

    def mouseReleaseEvent(self, event):
        # 计算截图区域的矩形
        rect = QRect(self.start_point, event.pos()).normalized()

        # 截取屏幕上的区域
        screenshot = self.grab(rect)

        # 显示截图
        self.label.setPixmap(screenshot)
        self.label.setFixedSize(rect.size())

        # 保存截图
        screenshot.save('screenshot.png')
        print("截图已保存为 screenshot.png")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScreenshotTool()
    sys.exit(app.exec_())
