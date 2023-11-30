from candidates import *
from logic import *


"""
Project 1, voting menu

python3 -m PyQt6.uic.pyuic -o gui.py -x Project1GUI.ui
"""

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()




  
if __name__ == '__main__':
    main()
    