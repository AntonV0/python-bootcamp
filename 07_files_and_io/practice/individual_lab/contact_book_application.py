"""Individual Lab: Contact Book Application"""
from pathlib import Path


def load_contacts(file_path):
    """Load contacts from a text file."""
    contacts = {}  # Empty dictionary
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Each line in the file is expected to be in the format: name,phone,email
                name, phone, email = line.strip().split(',')
                # Add the contact information to the contacts dictionary with the name as the
                # key and a nested dictionary for phone and email
                contacts[name] = {'phone': phone, 'email': email}
    except FileNotFoundError:
        print("No existing contact book found. Starting with an empty contact book.")
    return contacts


def save_contacts(contacts, file_path):
    """Save contacts to a text file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for name, info in contacts.items():
                # Write each contact's information to the file in the format: name,phone,email
                file.write(f"{name},{info['phone']},{info['email']}\n")
        print("Contacts saved successfully.")
    except IOError:
        print("Error: Could not save contacts to file.")


def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    # Add the new contact information to the contacts dictionary with the name as the key
    # and a nested dictionary for phone and email
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully.")


def display_contacts(contacts):
    """Display all contacts in the contact book."""
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\nContact Book:")
        for name, info in contacts.items():
            print(
                f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        # If the contact is found, retrieve the contact information and display it
        info = contacts[name]
        print(
            f"Contact found - Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"Contact '{name}' not found.")


def main():
    """Run the contact book application."""
    base_dir = Path(__file__).parent  # Get the directory of the current script
    contacts_file = base_dir / 'contacts.txt'  # Define the path in same directory
    contacts = load_contacts(contacts_file)  # Load dictionary of contacts

    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            save_contacts(contacts, contacts_file)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# ? Example output:
# Contact Book Application
# 1. Add Contact
# 2. Display Contacts
# 3. Search Contact
# 4. Save and Exit
# Enter your choice: 2

# Contact Book:
# Name: Anton, Phone: 07123456789, Email: anton@gmail.com
# Name: Bob, Phone: 07111111111, Email: bob@gmail.com
# Name: Charlie, Phone: 07222222222, Email: charlie@gmail.com

# Enter your choice: 1
# Enter contact name: Dave
# Enter contact phone number: 07333333333
# Enter contact email address: dave@gmail.com
# Contact 'Dave' added successfully.

# Enter your choice: 2

# Contact Book:
# Name: Anton, Phone: 07123456789, Email: anton@gmail.com
# Name: Bob, Phone: 07111111111, Email: bob@gmail.com
# Name: Charlie, Phone: 07222222222, Email: charlie@gmail.com
# Name: Dave, Phone: 07333333333, Email: dave@gmail.com

# Enter your choice: 3
# Enter the name of the contact to search: dave
# Contact 'dave' not found.

# Enter your choice: 3
# Enter the name of the contact to search: Dave
# Contact found - Name: Dave, Phone: 07333333333, Email: dave@gmail.com

# Enter your choice: 4
# Contacts saved successfully.

# ? After exiting, the contacts.txt file will contain the following data:
# Anton,07123456789,anton@gmail.com
# Bob,07111111111,bob@gmail.com
# Charlie,07222222222,charlie@gmail.com
# Dave,07333333333,dave@gmail.com
