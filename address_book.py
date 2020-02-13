import json


class AddressBook:
    """This class contains methods for creating, updating and performing various operations on an address book"""
    def __init__(self):
        self.data = {}

    def create_file(self):
        """Method creates a new JSON file of an address book"""
        data = {'data': []}
        with open('address.json', 'a+') as f:
            json.dump(data, f, indent=4)
            f.close()
            print("Successfully, we have created a new file")
        self.data = data
        self.operation()

    def open_file(self):
        """Method will open an existing JSON file"""
        while True:
            try:
                with open('address.json', 'r') as new_file:
                    self.data = json.load(new_file)
                break
            except FileNotFoundError:
                print("Sorry,the File not exist")
                self.create_file()

    def sort_by_zip_code(self):
        """Method will sort the address book according to zip codes of areas or city"""
        self.open_file()
        for i in range(len(self.data['data'])):
            for j in range(len(self.data['data']) - i - 1):
                if self.data["data"][j]["ZipCode"] < self.data["data"][j+1]["ZipCode"]:
                    self.data["data"][j], self.data["data"][j+1] = self.data["data"][j+1], self.data["data"][j]
        self.display_address_book()
        self.save()

    def sort_by_name(self):
        """Method will sort the address book according to alphabetical order"""
        self.open_file()
        for number in range(len(self.data['data'])):
            for num in range(len(self.data['data']) - number - 1):
                if self.data["data"][num]["Last_Name"] < self.data["data"][num + 1]["Last_Name"]:
                    self.data["data"][num], self.data["data"][num + 1] = self.data["data"][num + 1], self.data["data"][num]
        self.display_address_book()
        self.save()

    def save(self):
        """Method saves the address book in JSON format"""
        with open('address.json', 'w+') as f:
            json.dump(self.data, f, indent=4)
            f.close()

    def address_details(self):
        """Method takes all the details from the user and creates a list of all the address details"""

        new_user_detail = {}  # It will add individual person details in a dictionary

        self.open_file()

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter the Address: ")
        city = input("Enter the City:  ")
        state = input("Enter the State:  ")
        zip_code = input("Enter the ZipCode:  ")
        phone_number = input("Enter the Phone Number: ")

        if (first_name.isalpha() and last_name.isalpha() and city.isalpha() and state.isalpha()
                and zip_code.isnumeric() and phone_number.isnumeric()):
            new_user_detail['First_Name'] = first_name
            new_user_detail['Last_Name'] = last_name
            new_user_detail['Address'] = address
            new_user_detail['City'] = city
            new_user_detail['State'] = state
            new_user_detail['ZipCode'] = zip_code
            new_user_detail['Phone_Number'] = phone_number

            self.data["data"].append(new_user_detail)

            self.save()
            self.display_address_book()
            self.operation()

        else:
            print("Please Enter correct values: ")
            self.address_details()

    def update_details_in_address_book(self):
        """Method helps the user to update the person's details except person's first and last name"""
        self.open_file()

        if len(self.data['data']) >= 1:
            first_name = input("Enter the First Name of the person for which you want to update the details: ")
            last_name = input("Enter the First Name of the person for which you want to update the details: ")
            for number in range(len(self.data['data'])):
                if (self.data['data'][number]["First_Name"] == first_name
                        and self.data['data'][number]["Last_Name"] == last_name):
                    flag = True
                    if flag:
                        print("1. Address")
                        print("2. City")
                        print("3. State")
                        print("4. ZipCode")
                        print("5. Phone Number")
                        print("6. Quit")
                        choice = int(input("Select any value from 1 to 6 for updating the details: "))

                        if choice == 1:
                            address = input("Enter the address which you want to update: ")
                            self.data['data'][number]["Address"] = address
                            self.display_address_book()
                            self.save()

                        elif choice == 2:
                            city = input("Enter the city name which you want to update: ")
                            self.data['data'][number]["Address"] = city
                            self.display_address_book()
                            self.save()

                        elif choice == 3:
                            state = input("Enter the state name you want to update: ")
                            self.data['data'][number]["Address"] = state
                            self.display_address_book()
                            self.save()

                        elif choice == 4:
                            zip_code = input("Enter the ZipCode which you want to update: ")
                            self.data['data'][number]["Address"] = zip_code
                            self.display_address_book()
                            self.save()

                        elif choice == 5:
                            phone_number = input("Enter the PhoneNumber which you want to update: ")
                            self.data['data'][number]["Address"] = phone_number
                            self.display_address_book()
                            self.save()

                        elif choice == 6:
                            pass

                        else:
                            print("Invalid choice")
                            self.operation()

    def display_address_book(self):
        print(self.data)
        self.operation()

    def operation(self):
        """This method allows the user to perform required activities on the address book
        """
        print("1.Add an address\n"
              "2.Update an address\n"
              "3.Print the list\n"
              "4.Sort by name\n"
              "5.Sort by zip_code\n"
              "6.Create a file\n"
              "7.Exit")

        operate = int(input("Enter operation: "))

        if operate == 1:
            self.address_details()
        elif operate == 2:
            self.update_details_in_address_book()
        elif operate == 3:
            self.display_address_book()
        elif operate == 4:
            self.sort_by_name()
        elif operate == 5:
            self.sort_by_zip_code()
        elif operate == 6:
            self.create_file()
        elif operate == 7:
            pass
        else:
            print("Wrong Input. Try Again!")
            self.operation()


def main():
    address_book = AddressBook()
    address_book.operation()


main()






