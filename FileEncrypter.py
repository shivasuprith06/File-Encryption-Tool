import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tqdm import tqdm
import os

class EncryptionDecryptionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Encryption and Decryption Tool")
        master.geometry("400x300")
        master.configure(bg="#f0f0f0")

        self.label = tk.Label(master, text="Select file for Encryption or Decryption:", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack()

        self.selected_file_label = tk.Label(master, text="", font=("Arial", 10), bg="#f0f0f0")
        self.selected_file_label.pack()

        self.select_button = ttk.Button(master, text="Select File", command=self.select_file, style="Bold.TButton")
        self.select_button.pack(pady=10)

        self.encrypt_button = ttk.Button(master, text="Encrypt", command=self.encrypt, style="Green.TButton")
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = ttk.Button(master, text="Decrypt", command=self.decrypt, style="Blue.TButton")
        self.decrypt_button.pack(pady=5)

        self.filename = ""

    def select_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            filename_only = os.path.basename(self.filename)
            self.selected_file_label.config(text="Selected File: " + filename_only)
        else:
            self.selected_file_label.config(text="")

    def encrypt(self):
        if self.filename:
            try:
                original_information = open(self.filename, 'rb')

                encrypted_file_name = 'cipher_' + os.path.basename(self.filename)  # Get only the filename
                encrypted_file_object = open(encrypted_file_name, 'wb')

                content = original_information.read()
                content = bytearray(content)

                key = 192
                print('Encryption Process is in progress...!')
                for i, val in tqdm(enumerate(content)):
                    content[i] = val ^ key

                encrypted_file_object.write(bytes(content))  # Write encrypted content as bytes
                
                # Print some of the encrypted content to verify randomness
                print('Sample of encrypted content:', bytes(content[:20]))

                print('Encryption done successfully!')
                messagebox.showinfo("Success", "Encryption done successfully!")
            except Exception as e:
                print(f"Something went wrong: {str(e)}")
                messagebox.showerror("Error", f"Something went wrong: {str(e)}")
            finally:
                original_information.close()
                encrypted_file_object.close()
        else:
            messagebox.showerror("Error", "Please select a file to encrypt.")

    def decrypt(self):
        if self.filename:
            try:
                encrypted_file_object = open(self.filename, 'rb')

                original_filename, original_file_extension = os.path.splitext(os.path.basename(self.filename))
                decrypted_file = filedialog.asksaveasfilename(defaultextension=original_file_extension, filetypes=[("All files", "*.*")])
                if decrypted_file:
                    decrypted_file_object = open(decrypted_file, 'wb')

                    cipher_text = encrypted_file_object.read()

                    key = 192

                    cipher_text = bytearray(cipher_text)

                    print('Decryption Process is in progress...!')
                    for i, val in tqdm(enumerate(cipher_text)):
                        cipher_text[i] = val ^ key

                    decrypted_file_object.write(bytes(cipher_text))  # Write decrypted content as bytes
                    print('Decryption done successfully!')
                    messagebox.showinfo("Success", "Decryption done successfully!")
                else:
                    messagebox.showwarning("Warning", "Please provide a valid filename for decryption.")
            except Exception as e:
                print(f"Some problem with Ciphertext: {str(e)}")
                messagebox.showerror("Error", f"Some problem with Ciphertext: {str(e)}")
            finally:
                encrypted_file_object.close()
                decrypted_file_object.close()
        else:
            messagebox.showerror("Error", "Please select a file to decrypt.")

def main():
    root = tk.Tk()
    app = EncryptionDecryptionGUI(root)

    # Define custom styles for buttons
    style = ttk.Style(root)
    style.configure("Bold.TButton", font=("Arial", 12, "bold"))
    style.configure("Green.TButton", font=("Arial", 14), background="#4CAF50", foreground="white", borderwidth=5, relief="raised")
    style.map("Green.TButton", background=[("active", "#45a049")])
    style.configure("Blue.TButton", font=("Arial", 14), background="#008CBA", foreground="white", borderwidth=5, relief="raised")
    style.map("Blue.TButton", background=[("active", "#005f7f")])

    root.mainloop()

if __name__ == "__main__":
    main()
