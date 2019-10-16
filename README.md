# Platform for management of AAA's

This is an platform for manegement of any AAA's. (README under construction...)

Link for [UML Diagram](https://www.draw.io/?state=%7B%22ids%22:%5B%221dtpP6MSkNoDrZnQmgezmx-DImkRNRsJg%22%5D,%22action%22:%22open%22,%22userId%22:%22100061445533958635471%22%7D)

## From the rules

- Any and all code (variables, urls, views, etc) will be written in the English language.

- Commits may be made in Portuguese or English language.

- Project views will be written in the FBV (Function-Based-Views) standard.

- There will never be a submission to the master branch. Submissions will be made through pull requests so that code analysis can be done for the master project branch.

- Project developers can pull the request in two ways:

    1. Create a Project Fork for your own github and submit and create the pull request from the master branch of the developer to the master branch of the project.
    or  
    2. Create your branch in your terminal/computer and send it to the main project. Once this is done, a pull request from your branch must be created for the master branch.

## Requirements

- Python >= 3.6

## Of use

- Clone the github project (```git clone https://github.com/lucasousa/aaa-engenharia.git```) or make a fork

- Enter the folder that has just been created (```cd aaa/```)

- Create a virtualenv with your version of python, for example, if you use python 3.7, execute:  ```python3.7 -m venv env```

- Activate your virtualenv with  ```source env/bin/activate```

- Install the project dependencies. ```pip install -r requirements.txt```

- Create the database. ```python manage.py migrate```

- Create a superuser with ```python manage.py createsuperuser```

- Run the project. ```python manage.py runserver```
