TraceMe: Finding Missing Persons
TraceMe is an innovative platform designed to assist in locating missing persons by leveraging face recognition technology, real-time data, and community involvement. This tool aims to support families, communities, and law enforcement in their search efforts by providing an efficient and user-friendly system.

Features
User Registration/Login: Secure authentication for authorities and public users.
Image Upload & Processing: Users can upload images of missing individuals.
Face Recognition: AI-powered matching of uploaded images with a database of reported missing persons.
Notification System: Alerts authorities when a match is found.
Database Management: Stores and organizes data related to missing individuals.
Technologies Used
Python: Core programming language.
Flask: Web framework for building the API.
Dlib: Image processing and face recognition library.
OpenCV: Computer vision tasks.
SQLite: Database for storing user and image data.
PostgreSQL (optional for production): Alternative database management.
Installation and Setup
Prerequisites
Ensure you have the following installed on your system:

Python 3.8+
CMake (required for building dlib)
pip (Python package manager)
Steps to Run the Project
Clone the Repository

bash-
Copy code
git clone https://github.com/humaira0316/traceme.git
cd traceme
Install Required Packages

bash-
Copy code
pip install -r requirements.txt
Set Up the Database

bash-
Copy code
python database.py
Run the Flask Server

bash-
Copy code
python app.py
Required Dependencies
Ensure these libraries are installed (listed in requirements.txt):

Flask
OpenCV-Python
face-recognition
dlib
numpy
sqlite3 (built-in with Python)
Troubleshooting Installation Issues
CMake Installation: Ensure CMake is installed and available in your PATH. Check using:
bash
Copy code
cmake --version
Windows Users: Make sure you have Visual Studio Build Tools installed for building dlib.
Usage
Register Missing Persons: Access /register_missing endpoint to upload data and photos.
Search for Matches: Use /search_missing endpoint to check uploaded photos against the database.
Receive Alerts: Get notified if a match is found.
Project Structure
bash
Copy code
/TraceMe
  |-- app.py            # Main Flask app
  |-- database.py       # Database setup script
  |-- face_utils.py     # Utility functions for face encoding and comparison
  |-- /uploads/         # Directory to store uploaded images
  |-- requirements.txt  # Project dependencies
Future Enhancements
Integration with a notification service (SMS/Email alerts).
Enhanced UI for public use.
Multi-language support.
Use of more robust databases like PostgreSQL for larger-scale applications.
License
This project is licensed under the MIT License. See LICENSE for more details.

Contributors
Aryan Gupta, Amar Deep Rao, Kavyshree Jaiswal, Humaira Hashmi (Team Members)
Acknowledgements
Special thanks to the open-source community for the dlib and face-recognition libraries.
