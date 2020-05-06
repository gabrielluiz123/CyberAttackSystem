import sys
import os
import socket
from main import *
from Choice import *
from DoS import *
from Pass import *
from SQL import *
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='sitedjango',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()


class Attack(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ipBtn.clicked.connect(self.ipChoice)
        self.pinga = None

    def ipChoice(self):
        self.pinga = self.ping()

        if not self.pinga:
            self.ipLabel.setText(f'Não foi possível se conectar ao IP: {self.inputIP.text()}')
        else:
            attack.close()
            choice.show()

    def ping(self):
        import os, platform

        if platform.system().lower() == "windows":
            ping_str = "-n 1"
        else:
            ping_str = "-c 1"

        resposta = os.system("ping " + ping_str + " " + self.inputIP.text())
        cmd = "ping -n 1 " + self.inputIP.text()
        r = "".join(os.popen(cmd).readlines())
        r = r.encode('ascii', 'ignore').decode('ascii')
        ping_split = r.split("\n")
        if resposta == 0:
            return f'{ping_split[4]} \n{ping_split[5]} {ping_split[6].strip()} \n Latências após ataque: {ping_split[8]}'
        else:
            return False


class Choice(QMainWindow, Ui_ChoiceWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChoice.clicked.connect(self.choiceAttack)
        self.btnBack.clicked.connect(self.backAttack)
        self.btnClose.clicked.connect(self.closeAttack)

    def closeAttack(self):
        choice.close()

    def backAttack(self):
        choice.close()
        attack.show()

    def choiceAttack(self):
        if self.inputChoice.text() == '1':
            choice.close()
            dos.show()
        elif self.inputChoice.text() == '2':
            choice.close()
            passw.show()
        elif self.inputChoice.text() == '3':
            choice.close()
            sql.show()
        else:
            print("Escolha uma opção válida!!")


class Sql(QMainWindow, Ui_Sql_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSQLVoltar.clicked.connect(self.backSql)
        self.btnChoiceSQL.clicked.connect(self.choiceSql)

    def backSql(self):
        sql.close()
        choice.show()

    def choiceSql(self):
        cursor.execute('SELECT * FROM contatos_categoria')
        self.resultado1 = cursor.fetchall()
        self.resultado1 = len(self.resultado1)

        if int(self.inputSQL.text()) == 1:
            pass
        elif int(self.inputSQL.text()) == 2:
            pass


class Password(QMainWindow, Ui_Pass_Window):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnVoltarPass.clicked.connect(self.backPass)
        self.btnChoicePass.clicked.connect(self.choicePass)

    def backPass(self):
        passw.close()
        choice.show()

    def choicePass(self):
        pass


class Dos(QMainWindow, Ui_Dos_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnDoSVoltar.clicked.connect(self.backDos)
        self.btnDoSChoice.clicked.connect(self.choiceDos)

    def backDos(self):
        dos.close()
        choice.show()

    def choiceDos(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    attack = Attack()
    choice = Choice()
    passw = Password()
    sql = Sql()
    dos = Dos()
    attack.show()
    qt.exec()
