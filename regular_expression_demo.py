import re
from datetime import date


class RegularExpression:
    def __init__(self):
        pass

    def replace(self, first_name=None, last_name=None):
        my_string = '''Hello <<name>>, We have your full name as <<full name>> in our system. 
        Your contact number is 91­xxxxxxxxxx.Please,let us know in case of any clarification. 
        Thank you BridgeLabz 01/01/2016'''

        d = date.today().strftime("%d/%m/%y")
        while True:
            first_name = str(input("Enter the user first name: "))
            if not re.match("^[a-zA-Z]*$", first_name):
                print("Please enter characters only")
            else:
                break

        while True:
            last_name = input("Enter the user last name: ")
            if not re.match("^[a-zA-Z]*$",last_name):
                print("Please enter characters only")
            else:
                break

        while True:
            mobile_number = input("Enter the Mobile Number: ")
            if not re.match("^[0-9]*$",mobile_number):
                print("Please enter numbers only")
            else:
                break
        mobile = '91-'+mobile_number
        full_name = first_name +' '+last_name
        data = [first_name, full_name, mobile, d]
        pattern = ['<<name>>', '<<full name>>', '91­xxxxxxxxxx', '01/01/2016']
        for i in range(4):
            my_string = re.sub(pattern[i], data[i], my_string)
        print(my_string)


obj = RegularExpression()
obj.replace()
