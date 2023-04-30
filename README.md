## Test task (Python internship)

### Deployment instructions (Linux)

1. Create a directory and make it current:

```
    ox23@DESKTOP-Q6MI4SE:~$ mkdir maklai-internship
    ox23@DESKTOP-Q6MI4SE:~$ cd maklai-internship/ 
```

2. Initialize local Git repository
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ git init
    hint: Using 'master' as the name for the initial branch. This default branch name
    hint: is subject to change. To configure the initial branch name to use in all
    hint: of your new repositories, which will suppress this warning, call:
    hint: 
    hint:   git config --global init.defaultBranch <name>
    hint: 
    hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
    hint: 'development'. The just-created branch can be renamed via this command:
    hint: 
    hint:   git branch -m <name>
    Initialized empty Git repository in /home/ox23/maklai-internship/.git/
```

3. Clone from Git
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ git clone https://github.com/semyon72/maklai-internship
    Cloning into 'maklai-internship'...
    remote: Enumerating objects: 24, done.
    remote: Counting objects: 100% (24/24), done.
    remote: Compressing objects: 100% (18/18), done.
    remote: Total 24 (delta 2), reused 24 (delta 2), pack-reused 0
    Receiving objects: 100% (24/24), 8.03 KiB | 8.03 MiB/s, done.
    Resolving deltas: 100% (2/2), done.
```

4. Initialize the Python virtual environment

```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ python3 -m venv .venv 
```

5. Look at the structure
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ tree -a -L 3
        .
        ├── .git
        │   ├── branches
        .....
        ├── maklai-internship
        │   ├── apps
        │   │   └── test_task
        │   ├── .git
        │   │   ├── branches
        ...........
        │   ├── maklai_internship_project
        │   │   ├── asgi.py
        │   │   ├── __init__.py
        │   │   ├── settings.py
        │   │   ├── urls.py
        │   │   └── wsgi.py
        │   ├── manage.py
        │   ├── README.md
        │   └── requirements.txt
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
            .....
```

6. For convenience, change the current directory and create a symlink to the actual, newly created virtual environment
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship$ cd maklai-internship/
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ ln -s ../.venv/ .venv
```

7. Activate the virtual environment
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ source .venv/bin/activate 
```

8. Update pip (optional)
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ pip install -U pip
    Requirement already satisfied: pip in /home/ox23/maklai-internship/.venv/lib/python3.9/site-packages (20.3.4)
    Collecting pip
    Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
    Installing collected packages: pip
    Attempting uninstall: pip
        Found existing installation: pip 20.3.4
        Uninstalling pip-20.3.4:
        Successfully uninstalled pip-20.3.4
    Successfully installed pip-23.1.2
```

9. Install the packages from requirements.txt (the list shows that all packages were installed locally, from cache)
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ pip install -r requirements.txt
    Collecting asgiref==3.6.0 (from -r requirements.txt (line 1))
    Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
    Collecting click==8.1.3 (from -r requirements.txt (line 2))
    Using cached click-8.1.3-py3-none-any.whl (96 kB)
    Collecting Django==4.2 (from -r requirements.txt (line 3))
    Using cached Django-4.2-py3-none-any.whl (8.0 MB)
    Collecting djangorestframework==3.14.0 (from -r requirements.txt (line 4))
    Using cached djangorestframework-3.14.0-py3-none-any.whl (1.1 MB)
    Collecting joblib==1.2.0 (from -r requirements.txt (line 5))
    Using cached joblib-1.2.0-py3-none-any.whl (297 kB)
    Collecting nltk==3.8.1 (from -r requirements.txt (line 6))
    Using cached nltk-3.8.1-py3-none-any.whl (1.5 MB)
    Requirement already satisfied: pkg_resources==0.0.0 in /home/ox23/maklai-internship/.venv/lib/python3.9/site-packages (from -r requirements.txt (line 7)) (0.0.0)
    Collecting pytz==2023.3 (from -r requirements.txt (line 8))
    Using cached pytz-2023.3-py2.py3-none-any.whl (502 kB)
    Collecting regex==2023.3.23 (from -r requirements.txt (line 9))
    Using cached regex-2023.3.23-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (768 kB)
    Collecting sqlparse==0.4.4 (from -r requirements.txt (line 10))
    Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
    Collecting tqdm==4.65.0 (from -r requirements.txt (line 11))
    Using cached tqdm-4.65.0-py3-none-any.whl (77 kB)
    Installing collected packages: pytz, tqdm, sqlparse, regex, joblib, click, asgiref, nltk, Django, djangorestframework
    Successfully installed Django-4.2 asgiref-3.6.0 click-8.1.3 djangorestframework-3.14.0 joblib-1.2.0 nltk-3.8.1 pytz-2023.3 regex-2023.3.23 sqlparse-0.4.4 tqdm-4.65.0
```
10. Optional (will create db.sqlite3 file and not warn during server startup)
```
    ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ python manage.py migrate
```
    
11. Run the test server
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ python manage.py runserver
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

12. Go to your browser (or another application that can send requests) and make a request
```    
    http://127.0.0.1:8000/paraphrase/?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars)) (, ,) (NP (NNS clubs)) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))
```

13. It can also be tested (simple tests are written)
```
    (.venv) ox23@DESKTOP-Q6MI4SE:~/maklai-internship/maklai-internship$ python manage.py test apps.test_task.tests
    Found 10 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.053s

    OK
    Destroying test database for alias 'default'...
```


