import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def _init_(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Contact dictionary to store contact information
        self.contacts = {}

        # GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Grid layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.address_label.grid(row=2, column=0, padx=10, pady=5)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)

        self.email_label.grid(row=3, column=0, padx=10, pady=5)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()

        if name and phone:
            self.contacts[name] = {"Phone": phone, "Address": address, "Email": email}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone are required.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{name}: {details['Phone']}" for name, details in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            matches = [f"{name}: {details['Phone']}" for name, details in self.contacts.items()
                       if search_term.lower() in name.lower() or search_term in details['Phone']]
            if matches:
                result = "\n".join(matches)
                messagebox.showinfo("Search Results", result)
            else:
                messagebox.showinfo("Search Results", "No matching contacts.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        if name in self.contacts:
            new_phone = simpledialog.askstring("Update Contact", "Enter the new phone number:")
            new_address = simpledialog.askstring("Update Contact", "Enter the new address:")
            new_email = simpledialog.askstring("Update Contact", "Enter the new email:")

            self.contacts[name] = {"Phone": new_phone, "Address": new_address, "Email": new_email}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")


if _name_ == "_main_":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
