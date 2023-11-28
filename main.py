#Project 1
from candidates import *
from logic import *


"""
test

python -m PyQt6.uic.pyuic -o gui.py -x Project1GUI.ui



"""


    

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

    



  
if __name__ == '__main__':
    main()
    