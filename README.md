WELCOME
=======

How to set me up under a fresh env

Requirements
---------
1. pip
2. virtualenvwrapper
3. postgresql running with a db called djangotutorial and a postgres/postgres user who can access it (or edit settings.py to match your configuration)

Setup
---------

    $ mkvirtualenv text_your_city
    $ cdvirtualenv
    $ git clone git@github.com:yuletide/text_your_city.git
    $ pip install -r text_your_city/requirements.txt
    $ cd text_your_city
    $ python manage.py syncdb
    create the superuser account when prompted
    $ python manage.py runserver

Everything should then work. Access the site at:

 * [http://localhost:8000/admin/](http://localhost:8000/admin/) create a poll here
 * [http://localhost:8000/polls/](http://localhost:8000/polls/) view poll listing here (most views are not yet built)

... under construction