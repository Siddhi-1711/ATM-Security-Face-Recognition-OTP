import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from transact import transaction
from twilio.rest import Client

otp_entry = None
otp_trials = 0 
otp_window = None  # Define the otp_window at a broader scope
user_id = None  # Define user_id at a broader scope
user_data = None  # Define user_data at a broader scope

def otp_verification():
     account_sid = "ACba260bff32ece0002bfa3fe216044ea1"
     auth_token = "cf15587fa9a3ba24d6003afcf4af24d6"
     verify_sid = "VA315439473f87f58dd5c1fa2b50e1a9d4"
     verified_number = "+917030355113"
     
     client = Client(account_sid, auth_token)
# Function to send OTP
     
     def send_otp():
          verification = client.verify.v2.services(verify_sid) \
            .verifications \
            .create(to=verified_number, channel="sms")
          messagebox.showinfo("OTP Sent", "OTP has been sent to your number.")
          

     
     

# Function to verify OTP
     def verify_otp():
          global otp_trials
          otp_code = otp_entry.get()
          verification_check = client.verify.v2.services(verify_sid) \
          .verification_checks \
               .create(to=verified_number, code=otp_code)
          if verification_check.status == "approved":
               messagebox.showinfo("OTP Verified", "OTP verification successful!")
               otp_window.destroy()
        # Call the transaction function with user_id and user_data
               transaction(user_id, user_data)
          else:
               global otp_trials
               otp_trials += 1  # Increment the number of OTP trials
               if otp_trials < 3:
                    messagebox.showerror("OTP Verification Failed", "Incorrect OTP. Please try again. Remaining trials: " + str(3 - otp_trials))
               else:
                    messagebox.showerror("Maximum OTP Trials Exceeded", "You have exceeded the maximum number of OTP trials.")
                      # Close the OTP verification window

# Function to initiate OTP verification
     def start_otp_verification():
          global otp_entry
          global otp_entry
          global otp_window
          global user_id
          global user_data
    # Create a new Tkinter window for OTP verification
          otp_window = tk.Toplevel()
          otp_window.title("OTP Verification")
          otp_window.geometry("1200x520+300+100")

    # Load and display the image (replace 'Atm.jpg' with your image file)
          atm_image = Image.open("C:\\Users\\SIDDHI\\Desktop\\Security-Copy(2)\\login-verification-master\\images\\Atm.jpg")
          atm_image = atm_image.resize((480, 480), Image.LANCZOS)  # Adjust the size as needed
          atm_photo = ImageTk.PhotoImage(atm_image)
          image_label = tk.Label(otp_window, image=atm_photo)
          image_label.image = atm_image
          image_label.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

    # Right side (OTP functionality)
          otp_label = tk.Label(otp_window, text="Enter OTP:",font=("Helvetica", 16))
          otp_label.grid(row=0, column=1, pady=10, sticky="e")

          otp_entry = tk.Entry(otp_window, font=("Helvetica", 16), width=20)
          otp_entry.grid(row=0, column=2, pady=10)

          resend_button = tk.Button(otp_window, text="Send OTP", width=15, height=2, font=("Helvetica", 16), bg="green", command=send_otp)
          resend_button.grid(row=1, column=3, pady=10)

          verify_button = tk.Button(otp_window, text="Verify OTP", width=15, height=2, font=("Helvetica", 16), bg="green", command=verify_otp)
          verify_button.grid(row=1, column=2, pady=10)
          
          
          otp_window.mainloop()

# Call this function to start OTP verification
     start_otp_verification()
