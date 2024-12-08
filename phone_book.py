from decorator import line_controller

class PhoneBook:

    def __init__(self, data: dict) -> None:
        self.data = data

    
    @line_controller
    def option_show(self, line_number: int) -> dict:
        data = {}
        number = 0

        for key in self.data.keys():

            if number == line_number:
                break

            data[key] = self.data.get(key)
            number += 1
        
        return data


    def filter_numbers(self, starts_with: str) -> dict:
         
        data = {}

        for key in self.data.keys():
            if self.data.get(key).startswith(starts_with):
                data[key] = self.data.get(key)
        
        return data
         

    
    


    

