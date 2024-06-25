class ContactBook:
    def __init__(self) -> None:
        self.ContactDictionary = {
            "Name": ["Joshua", "Joe", "Ana", "Andrew", "James"],
            "Phone-Number": [
                "(555) 123-4567",
                "(555) 234-5678",
                "(555) 345-6789",
                "(555) 456-7890",
                "(555) 567-8901"
            ],
            "Email": [
                "joshua@example.com",
                "joe@example.com",
                "ana@example.com",
                "andrew@example.com",
                "james@example.com",
            ]
        }
        print("Welcome to your personal Contact Book!")
        print("What would you like to do for today?")
        loop = True
        while loop:
            print("Enter '1' to add new contact.\nEnter '2' to search a contact by name.\nEnter '3' to view all contacts.\nEnter '4' to delete a contact by number.\nEnter '5'  to exit.")
            userInput = input("Enter here: ")
            if userInput == '1':
                self.addContact()
            elif userInput == '2':
                self.searchContact()
            elif userInput == '3':
                self.viewAllContacts()
            elif userInput == '4':
                self.deleteContact()
            elif userInput == '5':
                loop = False

    def addContact(self):
        print("Enter the name.")
        personName = input("Enter here: ")
        print("Enter the phone number")
        personNumber = input("Enter here: ")
        print("Enter the email.")
        personEmail = input("Enter here: ")
        if personName.isalpha() and personNumber.isnumeric():
            self.ContactDictionary["Name"].append(personName)
            self.ContactDictionary["Phone-Number"].append(personNumber)
            self.ContactDictionary["Email"].append(personEmail)
            print(f"{personName.capitalize()}, with phone number ({personNumber}), and ({personEmail}) has been added to the Contact Book!")
        else:
            print("Please check your input!")

    def searchContact(self):
        print("Enter the name of the contact, that you want to search for.")
        searchName = input("Enter here: ")
        indexOfName = self.ContactDictionary.get("Name").index(searchName)
        if searchName in self.ContactDictionary["Name"]:
            contactName, contactNumber, contactEmail = self.ContactDictionary["Name"][indexOfName], self.ContactDictionary[
                "Phone-Number"][indexOfName], self.ContactDictionary["Email"][indexOfName]
            print("Contact name found!")
            print(f"Person's name is: {contactName.capitalize()}, phone number is: {contactNumber}, and email is: {contactEmail}.")
        else:
            print(f"There's no contact named, {searchName}, in the contact book! Please check your input.")

    def viewAllContacts(self):
        for i in range(len(self.ContactDictionary["Name"])):
            print(
                f"Person's name is: {self.ContactDictionary['Name'][i].capitalize()}, phone number is: {self.ContactDictionary['Phone-Number'][i]}, and email is: {self.ContactDictionary['Email'][i]}.")

    def deleteContact(self):
        print("Enter the Name of the contact you want to delete.")
        nameOfContact = input("Enter here: ")
        indexOfContact = self.ContactDictionary.get("Name").index(nameOfContact)
        print(f"Name: {self.ContactDictionary["Name"][indexOfContact]}, phone number is: {self.ContactDictionary["Phone-Number"][indexOfContact]}, and email is: {self.ContactDictionary["Email"][indexOfContact]} has been deleted!")
        del self.ContactDictionary["Name"][indexOfContact], self.ContactDictionary["Phone-Number"][indexOfContact], self.ContactDictionary["Email"][indexOfContact]

        
if __name__ == "__main__":
    ContactBook()
