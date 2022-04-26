# Subjective-Examination-System-Using-Natural-Language-Processing

- download the code to local repository
- go to the folder
- open the folder in cmd
```cmd
pip install -r requirements.txt
python
>>import nltk
>>nltk.download()
```
- python manage.py runserver
- copy the url generated and paste it in browser
- ip-address/index in browser

## To remove all the data and run new

- go to migration folder in user and examination folder 
- delete all files except __init__
- delete sqllite file
- open cmd in the folder
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
