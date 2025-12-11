from collections import defaultdict


class ContactBook:
    """
    A simple contact management system that supports
    adding, editing, viewing, and deleting contacts.
    """

    def __init__(self):
        """Initialize the contact storage using a dictionary."""
        self.contacts = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: str = None) -> None:
        """
        Add a new contact to the contact book.

        Parameters:
            name (str): Contact's full name.
            phone (str): Phone number.
            email (str, optional): Email address. Defaults to None.
        """
        if name not in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email}
            print("Contact added successfully.")
        else:
            print("Contact already exists.")

    def edit_contact(self, name: str, phone: str = None, email: str = None) -> None:
        """
        Modify an existing contact's information.

        Parameters:
            name (str): Contact's name.
            phone (str, optional): New phone number.
            email (str, optional): New email address.
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def view_contacts(self) -> None:
        """Display all saved contacts."""
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n--- Contact List ---")
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-------------------------")

    def delete_contact(self, name: str) -> None:
        """
        Delete a contact by name.

        Parameters:
            name (str): The contact name to delete.
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def get_valid_name(self) -> str:
        """
        Continuously prompt the user for a valid name.
        Only alphabetic characters and spaces are allowed.

        Returns:
            str: A valid name entered by the user.
        """
        while True:
            name = input("Enter contact name: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            if all(c.isalpha() or c.isspace() for c in name):
                return name

            print("Name must contain letters only.")

    def get_valid_phone(self) -> str:
        """
        Continuously prompt the user for a valid 11-digit phone number.

        Returns:
            str: A valid phone number.
        """
        while True:
            phone = input("Enter contact phone number: ").strip()

            if not phone:
                print("Phone number cannot be empty.")
                continue

            if not phone.isdigit():
                print("Phone number must contain digits only.")
                continue

            if len(phone) != 11:
                print("Phone number must be 11 digits.")
                continue

            return phone


def main():
    """Run the main menu loop for the contact book application."""
    book = ContactBook()

    while True:
        print("\n=========== Contact Book ===========")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Quit")
        print("====================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = book.get_valid_name()
            phone = book.get_valid_phone()
            email = input("Enter contact email (optional): ").strip() or None
            book.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter the contact name to edit: ").strip()
            new_phone = input("New phone (leave empty to skip): ").strip()
            new_email = input("New email (leave empty to skip): ").strip()

            book.edit_contact(
                name,
                new_phone if new_phone else None,
                new_email if new_email else None,
            )

        elif choice == "3":
            book.view_contacts()

        elif choice == "4":
            name = input("Enter the contact name to delete: ").strip()
            book.delete_contact(name)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
