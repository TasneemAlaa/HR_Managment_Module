# HR_Managment_Module
## Record Attendence 
This application supposed to track the attendence of the employees which allows them to check-in and check-out 

## Getting Started
Fork the project repository and Clone your forked repository to your machine.

Developers using this project should already have Python3, and pip installed on their local machines.

**Installing Dependencies**
1. Python 3.6.9 - Follow instructions to install the latest version of python for your platform in the python docs.

2. PIP Dependencies - Once you have your virtual environment setup and running, install dependencies by navigating to the project directory and running:

    -`pip install requirments.txt`
- **Key Dependencies**.

 **1. Flask** is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 **2. SQLAlchemy** is the Python SQL toolkit and ORM used in this project to handle the Postgesql database.
  
 
## Database

Sqlite3 were used the databse file can be found in *D:\courses\HR_Managment_Module\instance\empattenden.db

**Models**
1. Users: It contains the data required by user to login or signup.
2. Attendence: To record the time of the employee's arrival and leaving. 
Those can be find in *models.py


## Running The App
To run the code
`python main.py`
