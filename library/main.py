import sys
from PySide6.QtWidgets import QApplication
from app import Notebook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notebook()
    window.show()

    sys.exit(app.exec())