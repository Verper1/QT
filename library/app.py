from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtSql import QSqlTableModel
from MainWindow import Ui_MainWindow
from EditWindow import Ui_Dialog
from conn import Data


class Notebook(QMainWindow):
    def __init__(self):
        super(Notebook, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.level = ''

        self.ui.pushButton.clicked.connect(self.open_add_note_window)
        self.ui.pushButton_2.clicked.connect(self.open_add_note_window)
        self.ui.pushButton_3.clicked.connect(self.delete_note)
        self.ui.pushButton_5.clicked.connect(self.close)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('notes')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        # self.ui.tableView.setColumnHidden(0, True)
        self.model.setHeaderData(1, Qt.Horizontal, "Название")
        self.model.setHeaderData(2, Qt.Horizontal, "Описание")
        self.model.setHeaderData(3, Qt.Horizontal, "Дата и время")
        self.model.setHeaderData(4, Qt.Horizontal, "Уровень")
        self.ui.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def open_add_note_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()

        if sender.text() == 'Добавить запись':
            self.ui_window.pushButton.clicked.connect(self.add_note)
        else:
            self.ui_window.pushButton.clicked.connect(self.edit_note)

        self.ui_window.pushButton_3.clicked.connect(self.new_window.close)
        self.ui_window.pushButton_2.clicked.connect(self.reset)

    def radiobutton(self):
        if self.ui_window.radioButton.isChecked():
            self.level = 'Высокий'
        elif self.ui_window.radioButton_2.isChecked():
            self.level = 'Средний'
        elif self.ui_window.radioButton_3.isChecked():
            self.level = 'Низкий'

    def reset(self):
        title = self.ui_window.lineEdit.clear()
        description = self.ui_window.lineEdit_2.clear()
        datetime = self.ui_window.dateTimeEdit.clear()


    def add_note(self):
        self.radiobutton()

        title = self.ui_window.lineEdit.text()
        description = self.ui_window.lineEdit_2.text()
        datetime = self.ui_window.dateTimeEdit.text()
        level = self.level

        if not title or not description or not datetime or not level:
            QMessageBox.warning(self.new_window, "Ошибка", "Все поля должны быть заполнены, а также выбран приоритет.")
            return

        self.conn.add_new_note_query(title, description, datetime, level)

        self.view_data()
        self.new_window.close()

    def edit_note(self):
        index = self.ui.tableView.selectedIndexes()

        if not index:
            QMessageBox.warning(self.new_window, "Ошибка", "Пожалуйста, выберите запись для изменения.")
            return  # Доделать

        index = index[0]
        id_ = str(self.ui.tableView.model().data(index))

        self.radiobutton()

        title = self.ui_window.lineEdit.text()
        description = self.ui_window.lineEdit_2.text()
        datetime = self.ui_window.dateTimeEdit.text()
        level = self.level

        if not title or not description or not level:
            QMessageBox.warning(self.new_window, "Ошибка", "Все поля должны быть заполнены, а также выбран приоритет.")
            return

        self.conn.edit_note_query(title, description, datetime, level, id_)

        self.view_data()
        self.new_window.close()

    def delete_note(self):
        self.main_window = QtWidgets.QDialog()
        index = self.ui.tableView.selectedIndexes()

        if not index:
            QMessageBox.warning(self.main_window, "Ошибка", "Пожалуйста, выберите запись для удаления.")
            return

        index = index[0]
        id_ = str(self.ui.tableView.model().data(index))

        self.conn.delete_note_query(id_)

        self.view_data()
