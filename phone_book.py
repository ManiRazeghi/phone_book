
class PhoneBook:

    def __init__(self, data: dict) -> None:
        self.data = data
    

    def option_show(self, line_number: int) -> dict:
        data = {}
        number = 0

        for key in self.data.keys():

            if number == line_number:
                break

            data[key] = self.data.get(key)
            number += 1
        
        return data
    
