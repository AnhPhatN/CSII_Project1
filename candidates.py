
#Abstract class
class Candidate:
    def __init__(self, first_name: str, last_name: str):
        self.__candidate_first_name = first_name
        self.__candidate_last_name = last_name
        self.__total_votes = 0

    
    def __str__(self) -> str:
        return f'First Name = {self.get_first_name()}, Last Name = {self.get_last_name()}, Total Votes = {self.get_total_votes()}'


    #Getters
    def get_first_name(self):
        return self.__candidate_first_name
    
    def get_last_name(self):
        return self.__candidate_last_name
    
    def get_total_votes(self):
        return self.__total_votes


    #Setters
    def set_first_name(self, value: str) -> bool:
        '''
        
        :return: True if successful, False if unsuccessful
        '''
        value = value.strip()
        if value.isalpha():
            self.__candidate_first_name = value
            return True
        
        return False

    def set_last_name(self, value: str) -> bool:
        '''
        
        :return: True if successful, False if unsuccessful
        '''
        value = value.strip()
        if value.isalpha():
            self.__candidate_last_name = value
            return True
        
        return False

    def set_total_votes(self, value: int) -> bool:
        '''
        
        :return: True if successful, False if unsuccessful
        '''
        if isinstance(value, int):
            if value < 0:
                return False
            self.__total_votes = value
            return True
            
        return False





class PresidentialCandidate(Candidate):
    def __init__(self, first_name: str, last_name: str, pol_party: str):
        super().__init__(first_name, last_name)
        self.__candidate_pol_party = pol_party

    def __str__(self) -> str:
        return f'First Name = {self.get_first_name()}, Last Name = {self.get_last_name()}, Total Votes = {self.get_total_votes()}, Political Party = {self.get_pol_party()}'


    #Getters
    def get_pol_party(self):
        return self.__candidate_pol_party


    #Setters
    def set_pol_party(self, value: str) -> bool:
        '''
        

        :return: True if successful, False if unsuccessful
        '''
        value = value.strip()
        if value.isalpha():
            self.__candidate_pol_party = value
            return True
        
        return False
