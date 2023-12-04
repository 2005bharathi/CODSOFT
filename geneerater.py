import tkinter as tk
import random
import string

class PasswordGenerator:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Generator")

        # GUI components
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_entry = tk.Entry(root)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.result_label = tk.Label(root, text="Your Password will appear here.")

        # Grid layout
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                raise ValueError("Invalid length")

            # Characters to use for generating the password
            characters = string.ascii_letters + string.digits + string.punctuation

            # Generate password
            generated_password = ''.join(random.choice(characters) for _ in range(password_length))

            # Display the generated password
            self.result_label.config(text=f"Generated Password: {generated_password}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid password length.")

if __name__ == "_main_":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
