import tkinter as tk
from PIL import Image, ImageTk
import csv
import json
#from app import saving_data

def transaction(user_id, user_data):

    def saving_data(user_data):
    # Read the existing data from the file
        with open('login-verification-master\data.txt', 'r', encoding='utf-8') as file:
            existing_data = json.load(file)

    # Update the specific user's initial_deposit
        user_id = user_data.get('Id')
        if user_id in existing_data:
            existing_data[user_id]['initial_deposit'] = user_data.get('initial_deposit')

        # Write the updated data back to the file
            with open('C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/data.txt', 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
    def update_csv(user_id, current_balance):
        # Open "details.csv" in read mode and create a temporary list to hold the updated data
        updated_data = []
        with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Id"] == user_id:
                    row["initial_deposit"] = str(current_balance)
                updated_data.append(row)

        # Write the updated data back to the CSV file
        with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="w", newline="") as file:
            fieldnames = ["Id", "Name", "phone_number", "initial_deposit"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_data)


    def open_withdraw_window():
        withdraw_window = tk.Toplevel()
        withdraw_window.title("Withdraw")
        withdraw_window.geometry("400x200")

        # Create labels and entry fields for deposit amount
        withdraw_label = tk.Label(withdraw_window, text="Enter Withdraw Amount:")
        withdraw_label.pack()
        withdraw_entry = tk.Entry(withdraw_window, font=("Helvetica", 16), width=20)
        withdraw_entry.pack()

        def update_withdraw(user_id, withdraw_amount):
    # Open "details.csv" and create a temporary list to hold the updated data
            updated_data = []
            with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Id"] == user_id:
                        current_balance = float(row["initial_deposit"])
                        current_balance -= withdraw_amount
                        row["initial_deposit"] = str(current_balance)
                    updated_data.append(row)

    # Write the updated data back to the CSV file
            with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="w", newline="") as file:
                fieldnames = ["Id", "Name", "phone_number", "initial_deposit"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_data)
                
        withdraw = tk.Label(withdraw_window, text="Notification", bg="grey", fg="white", width=50, height=1, font=('times', 15, 'bold'))
        withdraw.pack(pady=10)

        def perform_withdraw():
              # Replace with the actual user ID
            withdraw_amount = float(withdraw_entry.get())

            update_withdraw(user_id, withdraw_amount)
            withdraw.config(text=f"Deposited {withdraw_amount} successfully.")
            withdraw_window.destroy()

        

        withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=perform_withdraw)
        withdraw_button.pack(pady=10)
        
        

    def open_deposit_window():
        deposit_window = tk.Toplevel()
        deposit_window.title("Deposit")
        deposit_window.geometry("400x200")

        # Create labels and entry fields for deposit amount
        deposit_label = tk.Label(deposit_window, text="Enter Deposit Amount:")
        deposit_label.pack()
        deposit_entry = tk.Entry(deposit_window, font=("Helvetica", 16), width=20)
        deposit_entry.pack()

        def update_deposit(user_id, deposit_amount):
    # Open "details.csv" and create a temporary list to hold the updated data
            updated_data = []
            with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Id"] == user_id:
                        current_balance = float(row["initial_deposit"])
                        current_balance += deposit_amount
                        row["initial_deposit"] = str(current_balance)
                    updated_data.append(row)

    # Write the updated data back to the CSV file
            with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="w", newline="") as file:
                fieldnames = ["Id", "Name", "phone_number", "initial_deposit"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_data)

        deposit = tk.Label(deposit_window, text="Notification", bg="grey", fg="white", width=50, height=1, font=('times', 15, 'bold'))
        deposit.pack(pady=10)

        def perform_deposit():
              # Replace with the actual user ID
            deposit_amount = float(deposit_entry.get())

            update_deposit(user_id, deposit_amount)
            deposit.config(text=f"Deposited {deposit_amount} successfully.")
            deposit_window.destroy()

        

        deposit_button = tk.Button(deposit_window, text="Deposit", command=perform_deposit)
        deposit_button.pack(pady=10)
        

        


    def check_balance_window():
    # Create a tkinter window
        window = tk.Tk()
        window.title("Check Balance Window")
        window.geometry("400x200")
        def check_balance(user_id):
    # Open "details.csv" and find the user's balance
            with open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/Details/Details.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                user_found = False  # Flag to check if the user is found
                for row in reader:
                    if row["Id"] == user_id:
                        current_balance = float(row["initial_deposit"])
                        message_label.config(text=f"Current balance: {current_balance}")
                        user_found = True
                        break  # Exit the loop when the user is found

                if not user_found:
                    message_label.config(text="User not found")

        message_label = tk.Label(window, text="Notification", bg="grey", fg="white", width=50, height=1, font=('times', 15, 'bold'))
        message_label.pack(pady=10)

        

        balance_check_button = tk.Button(window, text="Check Balance", command=lambda: check_balance(user_id))  
        balance_check_button.pack()
    def logout():
        window.destroy()

    # Create a new window for transactions
    window = tk.Toplevel()
    window.title("Transaction Window")
    window.geometry("1200x520+300+100")

    left_frame = tk.Frame(window)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

    # Load and display the image
    image = Image.open("C:/Users/SIDDHI/Desktop/ATM-Security-FaceRecognition-OTP/Security - Copy (2)/login-verification-master/images/Atm.jpg")
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(left_frame, image=image)
    image_label.pack()

    right_frame = tk.Frame(window)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Create and configure the label for the text
    welcome_label = tk.Label(right_frame, text="Welcome to ATM System", font=("Helvetica", 24), fg="dark blue")
    welcome_label.pack(padx=10, pady=(20, 10))

    font_size = 16
    withdraw_button = tk.Button(right_frame, text="Withdraw", width=15, height=2, font=("Helvetica", font_size), pady=10, bg="gray")
    withdraw_button.pack(pady=(0, 10))

    deposit_button = tk.Button(right_frame, text="Deposit", width=15, height=2, font=("Helvetica", font_size), pady=10, bg="gray")
    deposit_button.pack(pady=(0, 10))

    balance_button = tk.Button(right_frame, text="Check Balance", width=15, height=2, font=("Helvetica", font_size), pady=10, bg="gray")
    balance_button.pack(pady=(0, 10))

    logout_button = tk.Button(right_frame, text="Logout", width=15, height=2, font=("Helvetica", font_size), pady=10, bg="green")
    logout_button.pack(pady=(0, 10))

    withdraw_button.config(command=open_withdraw_window)
    deposit_button.config(command=open_deposit_window)
    balance_button.config(command=check_balance_window)
    logout_button.config(command=logout)

    # Add buttons for withdraw, deposit, check balance, and logout
    window.mainloop()
