class Contact:
  def __init__(self, name, phone, email, address):
      self.name = name
      self.phone = phone
      self.email = email
      self.address = address

class ContactManager:
  def __init__(self):
      self.contacts = []

  def add_contact(self, name, phone, email, address):
      new_contact = Contact(name, phone, email, address)
      self.contacts.append(new_contact)
      print("Contact added successfully.")

  def view_contacts(self):
      if not self.contacts:
          print("No contacts available.")
          return
      print("\nContact List:")
      for i, contact in enumerate(self.contacts):
          print(f"{i+1}. {contact.name} - {contact.phone}")

  def search_contact(self, search_term):
      results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
      if not results:
          print("No contacts found.")
          return
      print("\nSearch Results:")
      for contact in results:
          print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n")

  def update_contact(self, search_term):
      for contact in self.contacts:
          if search_term.lower() in contact.name.lower() or search_term in contact.phone:
              print(f"Updating contact: {contact.name}")
              contact.name = input("Enter new name: ")
              contact.phone = input("Enter new phone number: ")
              contact.email = input("Enter new email: ")
              contact.address = input("Enter new address: ")
              print("Contact updated successfully.")
              return
      print("Contact not found.")

  def delete_contact(self, search_term):
      for contact in self.contacts:
          if search_term.lower() in contact.name.lower() or search_term in contact.phone:
              self.contacts.remove(contact)
              print("Contact deleted successfully.")
              return
      print("Contact not found.")

def main():
  manager = ContactManager()
  while True:
      print("\nContact Management System")
      print("1. Add Contact")
      print("2. View Contact List")
      print("3. Search Contact")
      print("4. Update Contact")
      print("5. Delete Contact")
      print("6. Exit")

      choice = input("Enter your choice (1-6): ")

      if choice == '1':
          name = input("Enter name: ")
          phone = input("Enter phone number: ")
          email = input("Enter email: ")
          address = input("Enter address: ")
          manager.add_contact(name, phone, email, address)
      elif choice == '2':
          manager.view_contacts()
      elif choice == '3':
          search_term = input("Enter name or phone number to search: ")
          manager.search_contact(search_term)
      elif choice == '4':
          search_term = input("Enter name or phone number to update: ")
          manager.update_contact(search_term)
      elif choice == '5':
          search_term = input("Enter name or phone number to delete: ")
          manager.delete_contact(search_term)
      elif choice == '6':
          print("Exiting the Contact Management System. Goodbye!")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
  main()
