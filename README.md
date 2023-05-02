## Test task (Python internship)

### Deployment instructions (Linux)

1. Create a directory and make it current:
```
    ox23@DESKTOP-Q6MI4SE:~$ mkdir maklai-internship
    ox23@DESKTOP-Q6MI4SE:~$ cd maklai-internship/ 
```

2. Clone from Git (be careful with last dot - the current directory)
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ git clone https://github.com/semyon72/maklai-internship .
    Cloning into 'maklai-internship'...
    ...
```

3. Initialize the Python virtual environment
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ python3 -m venv .venv 
```

4. Look at the structure
```
ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ tree -a -L 3
    .
    ├── apps
    │   └── test_task
    │       ├── admin.py
    │       ├── apps.py
    │       ├── __init__.py
    │       ├── migrations
    │       ├── models.py
    │       ├── serializers.py
    │       ├── tests.py
    │       ├── urls.py
    │       ├── utils
    │       └── views.py
    ├── .git
    │   ├── branches
    .......
    ├── maklai_internship_project
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    └── .venv
        ├── bin
        │   ├── activate
        │   ├── activate.csh
        │   ├── activate.fish
        │   ├── Activate.ps1
        │   ├── easy_install
        │   ├── easy_install-3.9
        │   ├── pip
        │   ├── pip3
        │   ├── pip3.9
        │   ├── python -> python3
        │   ├── python3 -> /usr/bin/python3
        │   └── python3.9 -> python3
        .......
```

5. Activate the virtual environment
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ source .venv/bin/activate 
```

6. Update pip (optional)
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ pip install -U pip
    Requirement already satisfied: pip in ./.venv/lib/python3.9/site-packages (20.3.4)
    ...
    Successfully installed pip-23.1.2
```

7. Install the packages from requirements.txt (the list shows that all packages were installed locally, from cache)
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ pip install -r requirements.txt
    Collecting asgiref==3.6.0
    Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
    Collecting click==8.1.3
    Using cached click-8.1.3-py3-none-any.whl (96 kB)
    Collecting Django==4.2
    Using cached Django-4.2-py3-none-any.whl (8.0 MB)
    Collecting djangorestframework==3.14.0
    Using cached djangorestframework-3.14.0-py3-none-any.whl (1.1 MB)
    Collecting joblib==1.2.0
    Using cached joblib-1.2.0-py3-none-any.whl (297 kB)
    Collecting nltk==3.8.1
    Using cached nltk-3.8.1-py3-none-any.whl (1.5 MB)
    Requirement already satisfied: pkg_resources==0.0.0 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 7)) (0.0.0)
    Collecting pytz==2023.3
    Using cached pytz-2023.3-py2.py3-none-any.whl (502 kB)
    Collecting regex==2023.3.23
    Using cached regex-2023.3.23-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (768 kB)
    Collecting sqlparse==0.4.4
    Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
    Collecting tqdm==4.65.0
    Using cached tqdm-4.65.0-py3-none-any.whl (77 kB)
    Installing collected packages: sqlparse, asgiref, tqdm, regex, pytz, joblib, Django, click, nltk, djangorestframework
    Successfully installed Django-4.2 asgiref-3.6.0 click-8.1.3 djangorestframework-3.14.0 joblib-1.2.0 nltk-3.8.1 pytz-2023.3 regex-2023.3.23 sqlparse-0.4.4 tqdm-4.65.0
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
```
8. Optional (will create db.sqlite3 file and not warn during server startup)
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ python manage.py migrate
```
    
9. Run the test server
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    April 30, 2023 - 13:44:00
    Django version 4.2, using settings 'maklai_internship_project.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

    Not Found: /
    [30/Apr/2023 13:44:07] "GET / HTTP/1.1" 404 2255
    [30/Apr/2023 13:44:23] "GET /paraphrase/ HTTP/1.1" 200 5322
```

10. Go to your browser (or another application that can send requests) and make a request
```    
    http://127.0.0.1:8000/paraphrase/?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars)) (, ,) (NP (NNS clubs)) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))
```

11. It can also be tested (simple tests are written)
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ python manage.py test apps.test_task.tests
    Found 10 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.053s

    OK
    Destroying test database for alias 'default'...
```


