import tkinter as tk
from tkinter import simpledialog, messagebox
import os


class HomeworkApp:
    def __init__(self, master):
        self.master = master
        self.master.title("(Naweedullah) Homework Management App")
        self.master.geometry("400x300")

        # Create buttons for homework options
        self.homework_buttons = []
        for i in range(1, 4):
            button = tk.Button(master, text=f"Homework {i}", command=lambda i=i: self.open_homework_window(i),bg="yellow")
            button.pack(pady=10)
            self.homework_buttons.append(button)

        # Create delete button
        self.delete_button = tk.Button(master, text="Delete Homework", command=self.delete_homework,bg="gray")
        self.delete_button.pack(pady=10)

        # Load existing homework if any
        self.load_homework()

    def load_homework(self):
        """Load saved homework from files."""
        for i in range(1, 4):
            filename = f'homework{i}.txt'
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    content = file.read()
                    setattr(self, f'homework{i}_content', content)
            else:
                setattr(self, f'homework{i}_content', "")

    def open_homework_window(self, hw_number):
        """Open a new window to edit homework."""
        hw_content = getattr(self, f'homework{hw_number}_content')

        hw_window = tk.Toplevel(self.master)
        hw_window.title(f"Edit Homework {hw_number}")

        text_frame = tk.Frame(hw_window)
        text_frame.pack(padx=10, pady=10)

        # Create a large text area for writing code
        self.text_area = tk.Text(text_frame, width=100, height=30)
        self.text_area.insert(tk.END, hw_content)
        self.text_area.pack()

        save_button = tk.Button(hw_window, text="Save", command=lambda: self.save_homework(hw_number),bg="red")
        save_button.pack(pady=5)

    def save_homework(self, hw_number):
        """Save homework content to a file."""
        content = self.text_area.get("1.0", tk.END).strip()

        with open(f'homework{hw_number}.txt', 'w') as file:
            file.write(content)

        setattr(self, f'homework{hw_number}_content', content)  # Update in-memory content

    def delete_homework(self):
        """Delete selected homework after password verification."""

        password = simpledialog.askstring("Password", "Enter password to delete homework:")

        if password == "your_password":  # Replace 'your_password' with your actual password.
            hw_number = simpledialog.askinteger("Delete Homework", "Enter Homework Number (1-3):")

            if hw_number in [1, 2, 3]:
                os.remove(f'homework{hw_number}.txt')
                setattr(self, f'homework{hw_number}_content', "")  # Clear in-memory content
                messagebox.showinfo("Success", f"Homework {hw_number} deleted.")
            else:
                messagebox.showerror("Error", "Invalid Homework Number.")


# Main execution block
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeworkApp(root)
    root.mainloop()