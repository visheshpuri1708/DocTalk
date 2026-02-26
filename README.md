<b>DocTalk</b> is a virtual Doctor appointment booking website that has been developed to override the problems of booking an appointment with a doctor especially prevalent in the pandemic situation. This website is supported to eliminate the hardships faced by this existing manual booking system. No formal knowledge is needed for the user to use this system. 

DocTalk is a MERN stack website built using ReactJS, JavaScript, CSS and 'antd' library is used for the icons. The database is being managed using MongoDB. The alerts are sent using react-hot-toast module.


<b>Steps to book an appointment</b>:

* The website is hosted using Heroku and can be visited here: https://doctalk.herokuapp.com/

* A user has to register for an account using name, email and password. After filling all the details, the user will be sent to login screen where the user has to enter the email and password to sign in.
<p align="center">
  <img src="/client/src/register.png" width="39%" />
  <img src="/client/src/login.png" width="39%" /> 
  
</p>

* After successful login, the user will be able to see the list of all doctors registered on the platform. The user can see all their appointments in the Appointments section. 
<p align="center">
  <img src="/doctor_list.png" width="80%" height="75%"/>
</p>

* If a user wants to apply for a doctor account, they can head to the Apply-Doctor tab in the options pane and fill in the personal and professional details. After submitting details, the request is sent to the admin for approval or rejection. Notifications are sent to both user and admin regarding the approvals or rejections.
<p align="center">
  <img src="/apply_doctor.png" width="80%" height="75%" />
  <img src="/admin_notification.png" width="80%" height="75%" />
</p>

* If a user wants to book an appointment with a doctor, they just have to click on a doctors tab and the system will ask for a date and time to check the availability of the doctor. If the doctor is available, the Book Now button will be activated and the user will be able to book the appointment.


* The doctor will get a notification regarding the appointment and the doctor has to approve the appointment or reject it. The notifications are sent for approvals or rejections. The doctor can view all his current and past appointments. A doctor is able to update their profile in the Profile section.

* Logout button is provided to logout from the user account.

DoctorTalk Analytics Dashboard (Data Science Extension)

To enhance DocTalk with a Data Science & Analytics layer, we built a Python-based dashboard using:

Streamlit

Pandas

Plotly

PyMongo

This dashboard provides:

📌 Total Appointments
📌 Active Bookings
📌 Cancellation Rate
📌 Average Wait Time
📌 Monthly Booking Trends
📌 Appointments by Region
📌 Specialty Distribution
📌 Status Breakdown

Running the Analytics Dashboard
1️. Install Python Dependencies

Make sure Python 3.9+ is installed.

pip install streamlit pymongo pandas plotly matplotlib
2️. Ensure MongoDB is Running

If running locally:

mongod

Default connection used in dashboard:

mongodb://localhost:27017

Database name:

doctalk

Collection name:

appointments
