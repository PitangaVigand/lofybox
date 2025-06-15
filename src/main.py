from PySide6.QtWidgets import QApplication
from src.timer import LofyBoxWindow
import sys
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LofyBoxWindow()
    window.setWindowIcon(QIcon("assets/lofybox.ico"))

    window.show()
    sys.exit(app.exec())
