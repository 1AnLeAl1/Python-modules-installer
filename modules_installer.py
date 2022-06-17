#!/usr/bin/env python3
import sys, os

from PyQt5.QtWidgets import ( QWidget, QLabel, QLineEdit, QMessageBox, QTextEdit, QGridLayout, QApplication, QPushButton )


class Example( QWidget ):

    def __init__( self ):
        super().__init__()

        self.initUI()


    def initUI( self ):

    	text = QLabel( 'Введите название модуля:', self )
    	name_input = QLineEdit( self )
    	qbtn = QPushButton( 'Установить', self )
    	qbtn.clicked.connect( lambda x: self.install(name_input.text()) )
    	
    	grid = QGridLayout()
    	grid.setSpacing( 10 )

    	grid.addWidget( text, 1, 0 )
    	grid.addWidget( name_input, 1, 1 )
    	grid.addWidget( qbtn, 2, 0 )

    	self.setLayout( grid )

    	self.setGeometry( 300, 200, 350, 150 )
    	self.setWindowTitle( 'Python modules installer' )
    	self.show()

    def install( self, name ):

    	wmsg = QMessageBox()
    	wmsg.setIcon(QMessageBox.Warning)
    	wmsg.setText( 'Не выходите из программы до оканчания установки!' )
    	wmsg.setWindowTitle( 'Внимание!' )
    	wmsg.setStandardButtons( QMessageBox.Ok | QMessageBox.Cancel )
    	wmsg.exec_()

    	message = os.system( f"pip install --user {name}" )
    	
    	imsg = QMessageBox()
    	imsg.setIcon( QMessageBox.Information )
    	imsg.setText( 'Установка завершена' )
    	imsg.setWindowTitle( 'Информация' )
    	imsg.setStandardButtons( QMessageBox.Ok | QMessageBox.Cancel )
    	imsg.exec_()

if __name__ == '__main__':

    app = QApplication( sys.argv )
    ex = Example()
    sys.exit( app.exec_() )
