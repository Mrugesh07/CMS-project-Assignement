
## Installation

1. Clone the repository:

   

Create and activate a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configuration

Create a .env file in the project root and configure the following environment variables:
env
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite://db.sqlite3  # Use your preferred database URL
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser for admin access:

bash
Copy code
python manage.py createsuperuser
Running the Project
bash
Copy code
python manage.py runserver


