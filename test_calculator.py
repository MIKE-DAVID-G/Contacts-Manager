
class Contacts:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    @classmethod
    def get_contacts(cls):
        name = input("What' your name? ").strip().title()
        phone_number = input("Whats your phone number? ")
        while True:
            email = input("What's your email address? ").strip()
            if "@" in email:
                break
            print("Invalid email. Try again.")
        return cls(name,phone_number,email)
    
def main():
     # menue here
    while True:
     print("\n\n1. Add Contact")
     print("2. View Contacts")
     print("3. Delete Contacts")
     print("4. Exit ")

     choice = input("Choose an option: ")

     if choice == "1":
        contact = Contacts.get_contacts()
         # saving info to contacts.txt
        with open("contacts.txt" ,"a") as file:
            file.write(f"{contact.name} - {contact.phone_number} - {contact.email}\n")
            print("You have added a contact")

     elif choice == "2":
        ## veiwing contacts in store
        try:
            with open("contacts.txt") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No contacts found yet.")
     elif choice == "3":
         del_contact  = input("What contact would you like to delete? ").strip().title()
         contact_ = []
         with open("contacts.txt") as file:
             for line in file:
                 contact_.append(line.strip().split("-"))
         updated_contact = []
         for contact in contact_:
             if contact[0].strip() != del_contact:
                 updated_contact.append(contact)
         with open("contacts.txt","w") as file:
             for contact in updated_contact:
                file.write(f"{contact[0]} - {contact[1]} - {contact[2]}\n")
         print(f"You have sucesfully deleted a {del_contact}")
             

     elif choice == "4":
        print("Goodbye")
        break

if __name__ == "__main__":
    main()