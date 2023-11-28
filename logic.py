#pyuic6 -x gui.ui -o gui.py

from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)





    '''
    Below is from our Test 10 gui logic, it's only here for notes, delete if don't need
    
    '''
        #example of how to make button below \/
        # self.pushButton_submit.clicked.connect(lambda : self.submit())
        # self.pushButton_clear.clicked.connect(lambda : self.clear())


    #some method examples below \/
    # def submit(self):
    #     try:
    #         food = float(self.input_food.text().strip())
    #         drink = float(self.input_drink.text().strip())
    #         dessert = float(self.input_dessert.text().strip())

    #         tax = .10
    #         tip = .10 #default option

    #         if self.radioButton_tip_10.isChecked():
    #             tip = .10
    #         elif self.radioButton_tip_15.isChecked():
    #             tip = .15
    #         elif self.radioButton_tip_20.isChecked():
    #             tip = .20


    #         meal_total = food + drink + dessert
    #         tax_amount = meal_total * tax
    #         tip_amount = (meal_total + tax_amount) * tip

    #         bill_total = meal_total + tax_amount + tip_amount





    #         # print(f'food: {food}, drink: {drink}, dessert: {dessert}, tax_amount: {tax_amount}, tip_amount: {tip_amount}, bill_total: {bill_total}')
            
    #         self.textBrowser_bill.setText(f"{'SUMMARY' :^40}\n"
    #                                         f"{'Food:' :<40} ${food:.2f}\n"
    #                                         f"{'Drink:' :<40} ${drink:.2f}\n"
    #                                         f"{'Dessert:' :<40} ${dessert:.2f}\n"
    #                                         f"{'Tax:' :<40} ${tax_amount:.2f}\n" 
    #                                         f"{'Tip:' :<40} ${tip_amount:.2f}\n\n"
    #                                         f"{'TOTAL:' :<40} ${bill_total:.2f}")
    #         #for some reason it's not doing string alignment with pyqt text box

    #         # print(f"{'SUMMARY' :^40}\n"
    #         #                                 f"{'Food:' :<40} ${food:.2f}\n"
    #         #                                 f"{'Drink:' :<40} ${drink:.2f}\n"
    #         #                                 f"{'Dessert:' :<40} ${dessert:.2f}\n"
    #         #                                 f"{'Tax:' :<40} ${tax_amount:.2f}\n" 
    #         #                                 f"{'Tip:' :<40} ${tip_amount:.2f}\n\n"
    #         #                                 f"{'TOTAL:' :<40} ${bill_total:.2f}")

    #     except:
    #         self.textBrowser_bill.setText(f"{'Food, drink, and dessert' :^40}\n"
    #                                       f"{'need to be numeric' :^40}\n"
    #                                       f"{'e.g. 10.25 not $10.25' :^40}\n")



    # def clear(self):
    #     self.input_food.clear()
    #     self.input_drink.clear()
    #     self.input_dessert.clear()
    #     self.textBrowser_bill.clear()
    #     self.radioButton_tip_10.setChecked(True)