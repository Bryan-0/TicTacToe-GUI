#### Tic Tac Toe Game with GUI!

import sys
import os
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog, QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5.uic import loadUi
from PyQt5 import QtGui

def Start():
    m = TicTacToe()
    m.show()
    return m


class TicTacToe(QDialog):

	def __init__(self):
		super(TicTacToe,self).__init__()
		loadUi('src\\tictactoe.ui', self)
		self.setWindowTitle('Tic Tac Toe Game')
		self.p1 = 'X'
		self.p2 = 'O'
		self.counter = 0
		self.canMark = True

		self.labelTitle.setStyleSheet('color: blue')

		self.pushButton.clicked.connect(self.on_pushButton_clicked)
		self.pushButtonNine.clicked.connect(self.on_pushButtonNine_clicked)
		self.pushButtonEight.clicked.connect(self.on_pushButtonEight_clicked)
		self.pushButtonSeven.clicked.connect(self.on_pushButtonSeven_clicked)
		self.pushButtonSix.clicked.connect(self.on_pushButtonSix_clicked)
		self.pushButtonFive.clicked.connect(self.on_pushButtonFive_clicked)
		self.pushButtonFour.clicked.connect(self.on_pushButtonFour_clicked)
		self.pushButtonThree.clicked.connect(self.on_pushButtonThree_clicked)
		self.pushButtonTwo.clicked.connect(self.on_pushButtonTwo_clicked)
		self.pushButtonOne.clicked.connect(self.on_pushButtonOne_clicked)
		self.pushButton_SwitchX.clicked.connect(self.on_pushButton_SwitchX_clicked)
		self.pushButton_SwitchO.clicked.connect(self.on_pushButton_SwitchO_clicked)


		self.pushButtonOne.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonTwo.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonThree.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonFour.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonFive.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonSix.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonSeven.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonEight.setStyleSheet("QPushButton{background: transparent;}")
		self.pushButtonNine.setStyleSheet("QPushButton{background: transparent;}")

		self.setWindowIcon(QtGui.QIcon('src\\ticicon.ico'))



	@pyqtSlot()
	def on_pushButton_SwitchX_clicked(self):

		if self.p1 == 'O' and self.p2 == 'X':
			self.p1 = 'X'
			self.p2 = 'O'
			self.labelp1.setText('X')
			self.labelp2.setText('O')


	@pyqtSlot()
	def on_pushButton_SwitchO_clicked(self):

		if self.p1 == 'X' and self.p2 == 'O':
			self.p1 = 'O'
			self.p2 = 'X'
			self.labelp1.setText('O')
			self.labelp2.setText('X')


	@pyqtSlot()
	def on_pushButton_clicked(self):
		self.counter = 0
		self.canMark = True
		self.labelResult.setText("")
		self.pushButtonNine.setText("")
		self.pushButtonEight.setText("")
		self.pushButtonSeven.setText("")
		self.pushButtonSix.setText("")
		self.pushButtonFive.setText("")
		self.pushButtonFour.setText("")
		self.pushButtonThree.setText("")
		self.pushButtonTwo.setText("")
		self.pushButtonOne.setText("")


	@pyqtSlot()
	def on_pushButtonNine_clicked(self):
		if self.canMark:
			if len(self.pushButtonNine.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonNine.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonNine.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonEight_clicked(self):
		if self.canMark:

			if len(self.pushButtonEight.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonEight.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonEight.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonSeven_clicked(self):
		if self.canMark:
			if len(self.pushButtonSeven.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonSeven.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonSeven.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonSix_clicked(self):
		if self.canMark:

			if len(self.pushButtonSix.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonSix.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonSix.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonFive_clicked(self):
		if self.canMark:

			if len(self.pushButtonFive.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonFive.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonFive.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonFour_clicked(self):
		if self.canMark:

			if len(self.pushButtonFour.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonFour.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonFour.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonThree_clicked(self):
		if self.canMark:

			if len(self.pushButtonThree.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonThree.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonThree.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonTwo_clicked(self):
		if self.canMark:

			if len(self.pushButtonTwo.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonTwo.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonTwo.setText(self.p2)
					self.checkWin()
					self.counter += 1

	@pyqtSlot()
	def on_pushButtonOne_clicked(self):
		if self.canMark:

			if len(self.pushButtonOne.text()) == 1:
				return False
			else:
				if self.counter % 2 == 0:
					self.pushButtonOne.setText(self.p1)
					self.checkWin()
					self.counter += 1
				elif self.counter % 2 != 0:
					self.pushButtonOne.setText(self.p2)
					self.checkWin()
					self.counter += 1


	def checkWin(self):

		## X Comprobation!

		x_Win = False
		o_Win = False

		if self.pushButtonOne.text() + self.pushButtonTwo.text() + self.pushButtonThree.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonFour.text() + self.pushButtonFive.text() + self.pushButtonSix.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonSeven.text() + self.pushButtonEight.text() + self.pushButtonNine.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonOne.text() + self.pushButtonFour.text() + self.pushButtonSeven.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonTwo.text() + self.pushButtonFive.text() + self.pushButtonEight.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonThree.text() + self.pushButtonSix.text() + self.pushButtonNine.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonOne.text() + self.pushButtonFive.text() + self.pushButtonNine.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		if self.pushButtonThree.text() + self.pushButtonFive.text() + self.pushButtonSeven.text() == 'XXX':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('X Win!')
			x_Win = True
			self.canMark = False

		## O Comprobation!

		if self.pushButtonOne.text() + self.pushButtonTwo.text() + self.pushButtonThree.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonFour.text() + self.pushButtonFive.text() + self.pushButtonSix.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonSeven.text() + self.pushButtonEight.text() + self.pushButtonNine.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonOne.text() + self.pushButtonFour.text() + self.pushButtonSeven.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonTwo.text() + self.pushButtonFive.text() + self.pushButtonEight.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonThree.text() + self.pushButtonSix.text() + self.pushButtonNine.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonOne.text() + self.pushButtonFive.text() + self.pushButtonNine.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.pushButtonThree.text() + self.pushButtonFive.text() + self.pushButtonSeven.text() == 'OOO':
			self.labelResult.setStyleSheet('color: green')
			self.labelResult.setText('O Win!')
			o_Win = True
			self.canMark = False

		if self.counter == 8 and not x_Win and not o_Win:
			self.labelResult.setStyleSheet('color: red')
			self.labelResult.setText('Tied!')



if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	window = Start()

	app.exec_()
