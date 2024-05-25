import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from twilio.rest import Client
from transact import transaction
import csv

# Twilio credentials
account_sid = "Your Account SID"
auth_token = "Your Author Token"
verify_sid = "Your Verfied SID"

otp_entry = None
otp_trials = 0
otp_window = None  # Define the otp_window at a broader scope
user_id = None  # Define user_id at a broader scope
user_data = None  # Define user_data at a broader scope
verified_number = None  # Define verified_number at a broader scope

def otp_verification(user_id, user_data):
    global otp_trials, otp_window, otp_entry, verified_number
    otp_trials = 0
    # Send OTP before creating the verification window
    send_otp(user_id, user_data)
    otp_window = tk.Toplevel()
    otp_window.title("OTP Verification")
    otp_window.geometry("1200x520+300+100") # Adjust the window size as needed

    # Load and display the image (replace 'Atm.jpg' with your image file)
    atm_image = Image.open("C:/Users/SIDDHI/Desktop/Security - Copy (3)/Security - Copy (2)/login-verification-master/images/Atm.jpg") # Update the path to your image
    atm_image = atm_image.resize((480, 480), Image.LANCZOS) # Adjust the size as needed
    atm_photo = ImageTk.PhotoImage(atm_image)
    image_label = tk.Label(otp_window, image=atm_photo)
    image_label.image = atm_image
    image_label.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

    # Right side (OTP functionality)
    otp_label = tk.Label(otp_window, text="Enter OTP:", font=("Helvetica", 16))
    otp_label.grid(row=0, column=1, pady=10, sticky="e")

    otp_entry = tk.Entry(otp_window, font=("Helvetica", 16), width=20)
    otp_entry.grid(row=0, column=2, pady=10)

    verify_button = tk.Button(otp_window, text="Verify OTP", width=15, height=2, font=("Helvetica", 16), bg="green", command=verify_otp)
    verify_button.grid(row=1, column=2, pady=10)

    otp_window.mainloop()

def send_otp(user_id, user_data):
    global verified_number
    with open('C:/Users/SIDDHI/Desktop/Security - Copy (3)/Security - Copy (2)/login-verification-master/Details/Details.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Id"] == user_id:
                verified_number = row["phone_number"]
                break
        else:
            messagebox.showerror("User Not Found", "User ID not found in database.")
            return

    client = Client(account_sid, auth_token)
    verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=verified_number, channel="sms")
    messagebox.showinfo("OTP Sent", "OTP has been sent to your number.")

def verify_otp():
    global otp_trials, verified_number
    otp_code = otp_entry.get()
    client = Client(account_sid, auth_token)
    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp_code)
    if verification_check.status == "approved":
        messagebox.showinfo("OTP Verified", "OTP verification successful!")
        otp_window.destroy()
        transaction(user_id, user_data)
    else:
        otp_trials += 1
        if otp_trials < 3:
            messagebox.showerror("OTP Verification Failed", f"Incorrect OTP. Please try again. Remaining trials: {3 - otp_trials}")
        else:
            messagebox.showerror("Maximum OTP Trials Exceeded", "You have exceeded the maximum number of OTP trials.")

