#pyuic6 -x gui.ui -o gui.py

from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Voting Menu')

        #hiding frames to be displayed
        self.voting_frame.hide()
        self.total_votes_frame.hide()

        #From the home frame, 
        # #vote_for_button takes you to voting frame
        # #total_votes_button takes you to total votes frame
        self.vote_for_button.clicked.connect(lambda : self.display_voting_frame())
        self.total_votes_button.clicked.connect(lambda : self.display_total_votes_frame())

        #getting back to home button from voting frame or total votes frame
        self.push_button_home.clicked.connect(lambda : self.display_home_frame())
        self.push_button_home2.clicked.connect(lambda : self.display_home_frame())

        #submitting a vote on the voting frame
        self.push_button_submit.clicked.connect(lambda : self.voter_submit_button())


        #creating a new CSV (this will delete the previous save!!)
        #will only remember votes per session
        self.create_csv()
    
    def display_total_votes_frame(self) -> None:
        '''
        displays total votes frame, hides home frame
        
        :return: None
        '''
        self.total_votes_frame.show()
        self.home_frame.hide()
        self.total_vote_label.setText(self.count_total_votes())

    def display_voting_frame(self) -> None:
        '''
        displays voting frame, hides home frame
        
        :return: None
        '''
        self.home_frame.hide()
        self.voting_frame.show()

    def display_home_frame(self) -> None:
        '''
        displays home frame, hides others frames

        :return: None
        '''
        self.clear_voter_choices()
        self.home_frame.show()
        self.voting_frame.hide()
        self.total_votes_frame.hide()




    def get_radio_input(self) -> str:
        '''
        function gets input from radio button, if none is selected then returns "Nothing selected"
        possible choice for radio buttons: 'Kanye', 'Drake', 'Nothing selected'

        :return: candidate_choice
        '''
        candidate_choice = "Nothing selected"
        if self.candidate1_radio.isChecked():
            candidate_choice = 'Kanye'
            # print(candidate_choice)
        elif self.candidate2_radio.isChecked():
            candidate_choice = 'Drake'
            # print(candidate_choice)
        return candidate_choice


    def get_user_input(self) -> str:
        '''
        takes string from line_edit_NUID and returns it


        :return: student_ID: str
        '''
        student_ID = self.line_edit_NUID.text()
        return student_ID


    def clear_voter_choices(self) -> None:
        '''
        clears all voting options, clears NUID textbox, clears radio buttons, clears invalid messages
        
        :return: None
        '''
        #clearing NUID text box
        self.line_edit_NUID.clear()
        #clearing Invalid messages
        self.validNUID_label.clear()
        #clearing radio buttons
        for radioButton in [self.candidate1_radio, self.candidate2_radio]:
            radioButton.setAutoExclusive(False)
            radioButton.setChecked(False)
            radioButton.setAutoExclusive(True)


    def create_csv(self) -> None:
        '''
        Creates a CSV with the header: NUID, Candidate

        a new CSV is created every time program is run, deleting the previous votes
        :return: None
        '''
        with open('output.csv', 'w', newline='') as csv_output_file:
            csv_output_writer = csv.writer(csv_output_file)
            csv_output_writer.writerow(["NUID", "Candidate_Choice"])



    def NUID_isvalid(self, user_NUID: str) -> bool:
        '''
        makes sure NUID is valid: 8 numbers, and not been used in output.csv
        
        :return: True if NUID is valid, False if NUID is NOT valid
        '''
        user_NUID = user_NUID.strip()
        print(user_NUID)
        if user_NUID == '':
            self.validNUID_label.setText('Please enter a NUID')

        if len(user_NUID) != 8:
            self.validNUID_label.setText('NUID needs to be 8 characters long')
            return False
        
        if not user_NUID.isnumeric():
            self.validNUID_label.setText('NUID needs to be 8 numbers')
            return False
        
        #checking if NUID has been used
        with open('output.csv', 'r') as csv_file:

            for line in csv_file:
                line = line.strip()
                line = line.split(',')
                if line[0] == user_NUID:
                    # print("NUID ALREADY USED")
                    self.validNUID_label.setText('NUID has already been used')
                    return False


        return True





    def append_csv(self, user_NUID: str, candidate_choice: str) -> None:
        '''
        takes params and outputs to csv file, in the form ['user_NUID', 'candidate_choice']

        :param user_NUID: a valid UNID as a str
        :param candidate_choice: a valid radio choice, either 'Kanye' or 'Drake'
        :return: None
        '''
        with open('output.csv', 'a') as csv_output_file:
            writer = csv.writer(csv_output_file)
            writer.writerow([user_NUID, candidate_choice])


    def voter_submit_button(self) -> bool:
        '''
        gets user NUID and candidate radio option,
        checks if NUID is valid with .NUID_isvalid method,
        checks if radio option is NOT 'Nothing selected'
        
        if all checks are good, then append to CSV

        :return: True if submit was successful, and False if submit was unsuccessful
        '''
        user_NUID = self.get_user_input()
        user_candidate_choice = self.get_radio_input()

        self.clear_voter_choices()


        if self.NUID_isvalid(user_NUID) == False:
            return False


        if user_candidate_choice == "Nothing selected":
            self.validNUID_label.setText('Please select a candidate')
            return False
        

        #set label
        self.validNUID_label.setText('Vote has been submitted!')
        self.append_csv(user_NUID, user_candidate_choice)
        return True



    def count_total_votes(self) -> str:
        '''
        counts all votes for each candidate 
        
        :return: f string which states total votes for each candidate
        '''
        with open('output.csv', 'r') as csv_file:
            votes_for_kanye = 0
            votes_for_drake = 0
            
            header_line = True
            for line in csv_file:
                if header_line == True:
                    header_line = False
                    continue
                
                line = line.strip()
                line = line.split(',')
                
                if line[1] == 'Kanye':
                    votes_for_kanye += 1
                
                if line[1] == 'Drake':
                    votes_for_drake += 1
            
            return f'Votes for Kanye {votes_for_kanye}\nVotes for Drake: {votes_for_drake}'
