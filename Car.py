import datetime

class Car:
    def __init__(self, entry_time = datetime(0,0,0), exit_time = datetime(0,0,0), ticket_number = 0):
        self._entry_time = entry_time
        self._exit_time = exit_time
        self._ticket_number = ticket_number
    
    def get_entry_time(self):
        return self._entry_time
    
    def get_exit_time(self):
        return self._exit_time
    
    def get_ticket_number(self):
        return self._ticket_number
    
    def set_entry_time(self, value):
        self._entry_time = value
        
    def set_exit_time(self, value):
        self._exit_time = value
    
    def set_ticket_number(self, value):
        self._ticket_number = value
    