# UTFT
Writing Unit tests and Functional Testing in Python

#### Setup

- Make sure you have `virtualenv`. You can plain `virtualenv` or `virtualenvwrapper`.

```shell
$ mkvirtualenv UTFT
New python executable in UTFT/bin/python
Also creating executable in UTFT/bin/python
Installing setuptools, pip, wheel...done.
(UTFT)$ 
(UTFT)$ pip install -r requirements.txt 
...
Successfully installed mock-1.0.1 py-1.4.27 pyGravatar-0.0.6 pytest-2.7.1 requests-2.7.0
(UTFT)$
(UTFT)$ cat phonebook.sql| sqlite3 phonebook.db
```

#### About Me

This is a command line interface for phonebook. From command line you will be
able to add new entry to phonebook, edit existing entry, view and delete. Yes, you can
also search for existing entries. That's about the application.

#### What you'll learn ?

As the name suggests, we'll learn how to write unit tests, functional tests in Python.
We will be using standard library unit test module, py.test, mock etc ...

We will learn how to assert basic types, objects, fixtures, mocking etc ...

Also writing tests will help you organize your code better.


#### How to read the source

The main entry for the program in `cli.py`, start jumping to the code from there on.

- `cli.py` - Handles initial invocation of the program and resolves the action, calls the function.
- `views.py` - Entry point for all actions.
- `validations.py` - All valdiation for user input and custom app validation.
- `ui.py` - All user handling input/displaying errors.
- `db.py` - SQLITE3 connection + all db operations.
- `prompt.py` - Cool way to get prompt depending on environment.
- `service.py` - Gravatar external service calls.
- `file_store.py` - Store image to the local file system.

All unit tests start with `test_ut_` and integration tests startwith `test_it_`.
All tests can be found in `test` branch.

#### Demo

```shell
(UTFT)$ cat phonebook.sql| sqlite3 phonebook.db
(UTFT)$
(UTFT)$ python cli.py
python cli.py ['add|display_one|display_all']
(UTFT)$ python cli.py add
Phone:89
First Name:Kracekumar
Last Name:Ramaraju
Email:me@kracekumar.com
Record added
(UTFT)$ 
(UTFT)$ python cli.py display_all
################################################################################
Id: 1
First Name: Kracekumar
Last Name: Ramaraju
Email: me@kracekumar.com
Thumbnail Path: /Users/avi/code/UTFT/20150621095734151846.jpeg
Phone: 89
################################################################################
(UTFT)$ 
(UTFT)$ python cli.py display_one
Id:1
################################################################################
Id: 1
First Name: Kracekumar
Last Name: Ramaraju
Email: me@kracekumar.com
Thumbnail Path: /Users/avi/code/UTFT/20150621095734151846.jpeg
Phone: 89
################################################################################
(UTFT)$ 
(UTFT)$ python cli.py display_one
Id:2
Record not found
(UTFT)$ 
(UTFT)$ python cli.py add
Phone:
First Name:
Last Name:
Email:
################################################################################
phone:['Value is missing']
first_name:['Value is missing']
################################################################################
Phone:4590
First Name:
################################################################################
first_name:['Value is missing']
################################################################################
First Name:Haris
Record added
(UTFT)$ 
(UTFT)$ python cli.py display_all
################################################################################
Id: 1
First Name: Kracekumar
Last Name: Ramaraju
Email: me@kracekumar.com
Thumbnail Path: /Users/avi/code/UTFT/20150621095734151846.jpeg
Phone: 89
################################################################################
Id: 2
First Name: Haris
Last Name: 
Email: 
Thumbnail Path: None
Phone: 4590
################################################################################
(UTFT)$
```

#### Concepts covered

- How to use unittest module
- How to use py.test and why py.test
- Writing simple functions as testcases
- Using different py.test command line features
- Capturing stdout with py.test
- Setting fixtures with py.test
- Writing Test classes which py.test can pick
- Using pytest.fixture
- Running specific test module/class/function etc ...
- Writing setup and teardown in pytest style
- How to mock expensive resources like network call, System Call.
- Patching modules/functions/classes.
- How to use Stubs/Fakes.
