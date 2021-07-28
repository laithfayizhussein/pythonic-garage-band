from abc import abstractmethod

class Band ():

    band_array = []

    def __init__(self , name ):
       self.name = name 
       Band.band_array.append(self)
    member_array = []

    def add_members(self,name_member):
        self.name_member = name_member

    def play_solos(self):
        result = ''
        for i in Band.member_array:
            result += f"{i.play_solos()}"
        return result 

    @classmethod
    def list_of(cls):
        return cls.member_array

    def __repr__ (self):
        return f"to show {self.name} not true "

    def __str__(self):
        return f"welcome in {self.name} our member {Band.member_array}"
    
