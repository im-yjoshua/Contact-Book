# Contact Book

This is a simple Contact Book application written in Python. It allows you to add, search, view, and delete contacts through a command-line interface.

## Features

- **Add a new contact**: Allows the user to add a new contact with a name, phone number, and email.
- **Search for a contact by name**: Allows the user to search for a contact by name and view their details.
- **View all contacts**: Displays all contacts in the contact book.
- **Delete a contact by name**: Allows the user to delete a contact by name.
- **Exit**: Exit the Contact Book application.

## Code Analysis

### Class Definition

```python
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
   ```

## Methods

- `addContact`

This method adds a new contact to the Contact Book. It checks if the inputs are valid before adding the contact to the dictionary.

```python 
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
```
- `searchContact`

This method searches for a contact by name and displays the contact details if found.

``` python 
def searchContact(self):
    print("Enter the name of the contact, that you want to search for.")
    searchName = input("Enter here: ")
    if searchName in self.ContactDictionary["Name"]:
        indexOfName = self.ContactDictionary["Name"].index(searchName)
        contactName = self.ContactDictionary["Name"][indexOfName]
        contactNumber = self.ContactDictionary["Phone-Number"][indexOfName]
        contactEmail = self.ContactDictionary["Email"][indexOfName]
        print("Contact name found!")
        print(f"Person's name is: {contactName.capitalize()}, phone number is: {contactNumber}, and email is: {contactEmail}.")
    else:
        print(f"There's no contact named, {searchName}, in the contact book! Please check your input.")

```

- `viewAllContacts`
This method displays all contacts in the Contact Book.

``` python
def viewAllContacts(self):
    for i in range(len(self.ContactDictionary["Name"])):
        print(f"Person's name is: {self.ContactDictionary['Name'][i].capitalize()}, phone number is: {self.ContactDictionary['Phone-Number'][i]}, and email is: {self.ContactDictionary['Email'][i]}.")
```

- `deleteContact`
This method deletes a contact by name and displays a confirmation message.

``` python 
def deleteContact(self):
    print("Enter the Name of the contact you want to delete.")
    nameOfContact = input("Enter here: ")
    if nameOfContact in self.ContactDictionary["Name"]:
        indexOfContact = self.ContactDictionary["Name"].index(nameOfContact)
        contactName = self.ContactDictionary["Name"][indexOfContact]
        contactNumber = self.ContactDictionary["Phone-Number"][indexOfContact]
        contactEmail = self.ContactDictionary["Email"][indexOfContact]
        del self.ContactDictionary["Name"][indexOfContact]
        del self.ContactDictionary["Phone-Number"][indexOfContact]
        del self.ContactDictionary["Email"][indexOfContact]
        print(f"Name: {contactName}, phone number is: {contactNumber}, and email is: {contactEmail} has been deleted!")
    else:
        print(f"No contact named {nameOfContact} found.")
```
## Main Program
The main program initializes the `ContactBook` and starts the command-line interface loop.

``` python 
if __name__ == "__main__":
    ContactBook()
```

# Improvements

- **Input Validation**: Improve input validation to handle various edge cases and incorrect inputs.

- **Phone Number Format Check**: Validate the phone number format properly.

- **Exception Handling**: Add exception handling to avoid program crashes due to unexpected inputs or errors.

- **Persistent Storage**: Implement persistent storage (e.g., save contacts to a file or database) to retain contacts between sessions.

# Conclusion
This Contact Book application provides a simple and effective way to manage contacts through a command-line interface. With further enhancements, it can be made more robust and user-friendly.
