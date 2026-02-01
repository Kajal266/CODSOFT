contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']}")

def search_contact():
    key = input("Enter name or phone to search: ").strip()
    found = False

    for name, info in contacts.items():
        if key.lower() in name.lower() or key == info["phone"]:
            print("\nContact Found")
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ").strip()

    if name in contacts:
        print("Leave field empty to keep old value.")
        phone = input("New phone number: ").strip()
        email = input("New email: ").strip()
        address = input("New address: ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def show_menu():
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

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
        print("Exiting Contact Management System.")
        break
    else:
        print("Invalid choice. Try again.")
