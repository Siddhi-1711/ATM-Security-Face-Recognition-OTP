# ATM-Security-Face-Recognition-OTP

## Overview
The ATM Security System is a comprehensive application designed to manage ATM operations securely. It includes functionalities such as user registration, login, transaction processing (withdrawal, deposit, and balance inquiry), and OTP-based authentication for enhanced security.
## Features
•	User Registration: Allows users to register with their account details.
•	Login: Users can log in using their registered credentials.
•	Transaction Processing: Supports withdrawal, deposit, and balance inquiry operations.
•	OTP Authentication: Provides an extra layer of security through OTP verification during critical operations.
•	Face Recognition: An optional feature for secure login using facial recognition technology.
## Prerequisites
•	Python 3.x
•	Tkinter for GUI
•	OpenCV for facial recognition
•	Twilio API for OTP service (Sign up at Twilio and obtain your credentials)
•	Numpy, Pandas, and other necessary libraries
## Installation
1.	Clone the repository: git clone https://github.com/your_username/atm-security-system.git
2.	Navigate into the project directory: cd atm-security-system
3.	Install required packages
## Usage
Running the Application
To start the application, simply run: python main.py
This will launch the main window where you can access various functionalities like registering a new user, logging in, performing transactions, etc.
## User Registration
1.	Click on the "Register" button on the main window.
2.	Fill out the registration form with the required details.
3.	Submit the form to complete the registration process.
## Logging In
1.	Click on the "Login" button on the main window.
2.	Enter your registered credentials (Card Number and Pin).
3.	Click on the "Login" button to access your account.
## OTP Authentication
For enhanced security, the application utilizes OTP (One-Time Password) authentication during critical operations such as login and transactions. To enable OTP functionality, follow these steps:
### Twilio Integration
1.	Sign up for a Twilio account at Twilio.
2.	Verify your mobile number in the Twilio console.
3.	Obtain your Twilio credentials (Account SID, Auth Token, and Verify Service SID).
4.	Add these credentials to the appropriate place in the application code (otp1.py) for OTP generation and sending.
### Adding Mobile Number for OTP
1.	In the Twilio dashboard, navigate to the "Verify Caller IDs" section under Phone Numbers.
2.	Add the mobile number associated with the user's account for OTP verification.
3.	Ensure that the mobile number is correctly configured to receive OTP messages.
Once the Twilio integration is set up and the mobile number is added for OTP verification, the application will seamlessly generate and send OTPs to enhance the security of critical operations.
## Performing Transactions
Once logged in, you can perform various transactions like withdrawal, deposit, and checking your balance.
## Exiting the Application
To exit the application, click on the "Logout" button or close the main window.
## Contributing
Contributions to improve the ATM Security System are welcome. Please feel free to submit pull requests or report issues.

