contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        details = contacts[name]
        print("Phone:", details["Phone"])
        print("Email:", details["Email"])
        print("Address:", details["Address"])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name]["Phone"] = input("Enter new phone: ")
        contacts[name]["Email"] = input("Enter new email: ")
        contacts[name]["Address"] = input("Enter new address: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Try again.")
