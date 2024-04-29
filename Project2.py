# Project 2
# Name: Laci Trull
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. MAKE YOUR LIFE EASIER AND ENABLE WORDWRAP! VIEW -> WORD WRAP.
#
# The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
import datetime as dt

# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("Welcome to the Contact List Program")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above.
# The program will run until the user selects option 0 to quit.
# The program will be implemented in a file called Project2.py.
# The program will use the following functions:

# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts.
# The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday.
# The function will take one parameter, the name of the csv file.
# The function will display an error message if the file does not exist.
# The function will display a message if the file exists and the contacts were imported successfully. 
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.
def import_csv(file):
    try:
        with open(file, 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip the first line
            contacts = {}
            for row in reader:
                contacts[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')} # Add contact to dictionary
            print("Contacts imported successfully")
            return contacts
    except FileNotFoundError:
        print("File does not exist") # Display error message
        return {}

# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]
def add_contact(name, phone, email, birthday, contacts):
    if name in contacts:
        print("Contact already exists") # Display error message
        return False
    else:
        contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': dt.datetime.strptime(birthday, '%m/%d/%Y')} # Add contact to dictionary
        print("Contact added")
        return True

# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries.
# You can unpack the dictionary into a list of dictionaries.
# Like in Lab 11 and then use the tabulate library to display the contacts in a table format.
# This is optional and not required. You can use string formatting to display the contacts in a table format.
def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts") # Display message if there are no contacts
    else:
        print("Name\tPhone\tEmail\tBirthday")
        for key, value in contacts.items():
            print(f"{key}\t{value['Phone']}\t{value['Email']}\t{value['Birthday'].strftime('%m/%d/%Y')}") # Display contacts in table format

# delete_contact(id) - This function will delete a contact from the dictionary.
# The function will take one parameter, the name of the contact to delete.
# The function will return True if the contact was deleted and False if the contact was not deleted.
# The function will display an error message if the contact does not exist.
def delete_contact(name, contacts):
    if name in contacts:
        del contacts[name]
        print("Contact deleted") # Display message if contact was deleted
        return True
    else:
        print("Contact does not exist") # Display error message
        return False
    
# next_birthday() - This function will display the next birthday. The function will take no parameters.
# The function will return nothing. The function will display a message if there are no contacts in the dictionary.
# The function will display a message if there are no birthdays in the next 30 days.
# The function will display the next birthday and name if there is a birthday in the next 30 days.
# Use string formatting to display the next birthday.
# The birthdays should be sorted in consecutive order.
# The birthday dates should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue.
# 1: you could replace all the years with the current year.
# 2: you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.
def next_birthday(contacts):
    if len(contacts) == 0: # Display message if there are no contacts
        print("No contacts")
    else:
        today = dt.datetime.today()
        next_birthday = None
        for key, value in contacts.items():
            birthday = value['Birthday']
            birthday = birthday.replace(year=today.year) # Replace year with current year
            if birthday < today:
                birthday = birthday.replace(year=today.year + 1)
            if next_birthday is None or birthday < next_birthday: # Find next birthday
                next_birthday = birthday
                next_name = key
        if (next_birthday - today).days <= 30:
            print(f"Next Birthday: {next_name} on {next_birthday.strftime('%m/%d/%Y')}") # Display next birthday
        else:
            print("No birthdays in the next 30 days") # Display message if there are no birthdays in the next 30 days

# save_csv() - This function will save the contacts to the csv file.
# Prompt the user to enter a filename to save the contacts to.
# If the file exists, overwrite the file. If the file does not exist, create the file.
# The function will return True if the contacts were saved and False if the contacts were not saved.
def save_csv(contacts):
    filename = input("Enter a filename to save the contacts to: ") # Prompt user to enter filename
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday']) 
            for key, value in contacts.items():
                writer.writerow([key, value['Phone'], value['Email'], value['Birthday'].strftime('%m/%d/%Y')]) # Write contacts to csv file
            print("Contacts saved") # Display message if contacts were saved
            return True
    except:
        print("Contacts not saved") # Display error message
        return False

# The main function will be used to run the program.
# The main function will use a while loop to display the menu and get the user's choice.
# The main function will call the appropriate function based on the user's choice.
# The main function will also call the save_csv function to save the contacts to the csv file before the program ends.
def main():
    contacts = import_csv('contacts.csv') 
    while True:
        print("\n1. Add contact\n2. View contacts\n3. Delete contact\n4. Save contacts to csv file\n5. Next Birthday\n0. Quit") # Display menu
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            birthday = input("Enter birthday (mm/dd/yyyy): ")
            add_contact(name, phone, email, birthday, contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name, contacts)
        elif choice == '4':
            save_csv(contacts)
        elif choice == '5':
            next_birthday(contacts)
        elif choice == '0':
            save_csv(contacts)
            break
        else:
            print("Invalid choice")
    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?
    names = [name for name in contacts.keys() if name[0].lower() == 'a']
    print(len(names))
    # How many emails are yahoo emails?
    yahoo = [email for email in contacts.values() if email['Email'].endswith('@yahoo.com')]
    print(len(yahoo))
    # How many .org emails are there?
    org = [email for email in contacts.values() if email['Email'].endswith('.org')]
    print(len(org))
    # How many contacts have a birthday in January?
    january = [contact for contact in contacts.values() if contact['Birthday'].month == 1]
    print(len(january))
# Final Note: You will want to utilize code from other labs, homeworks, and projects. The Bank Account Program will be a good resource for the menu and main function. Use try except statements when possible.


if __name__ == "__main__":
    main()
