# Invoice Payment System
* Developed By Django Web Framework (version: 2.2 Lts) and Stripe Payment Gateway.

## Instructions (Windows 10x64):
* Some commands may differ depending on OS. Just google it.

* Install latest version of Python3 (64 bit).

* Clone the repository.

* Install and active virtual environment directory:
  >> cd Repository/venv/Scripts/
  >> activate
  >>(venv):~$ This (venv) sign will be shown up if virtual environment activated successfully
  
* Install all the requirements using previously opened CMD where the virtual environment was activated:
  >>(venv):~$ pip install -r requirements.txt
  
* Run Local Server:
  >>(venv):~$ python manage.py runserver
  
* Create SuperUser:
  >>(venv):~$ python manage.py createsuperuser
  
* PATHs:
  1. Django Admin Dashboard: http://127.0.0.1:8000/admin/ (default) (Username = admin, Password = admin123)
  2. Homepage: http://127.0.0.1:8000/
