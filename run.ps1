cd venv
cd Scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\Activate.ps1
cd ..
cd ..
python manage.py runserver