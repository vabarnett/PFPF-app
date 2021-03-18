# PFPF-app
Perfect Fit Patterns created using Flask

A web app to allow users to create made-to-measure sewing patterns tailored to their own measurements

# Instructions
Install and activate python venv first.

```
$ cd PFPF-APP
On macOS and Linux:
python3 -m venv env
source env/bin/activate

On Windows:
py -m venv env
.\env\Scripts\activate
```

To run the app, cd into the PFPF-APP directory and run the app

```
$ cd PFPF-APP
$ flask run
```

The app.db file stores all the data for this app using SQLite. This is git ignored, and on a new project this can be initialized with the following commands

```
$ flask db init
$ flask db current
```

The persistence to the db can be tested with the python repl

```
$ python
>>> from app.models import User
test sqlite:////Users/priyasamuel/programming/PFPF-app/app.db
>>> u = User(username='susan', email='susan@example.com')
>>> u
<User susan
>>> from app import db
>>> db.session.add(u)
>>> db.session.commit()
>>> exit()
```
Inspecting the app.db file with an sqlite3 client shows the schema and the entry we added above.

```
$ sqlite3 app.db 
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite> .tables
alembic_version  user           
sqlite> select * from user;
1|susan|susan@example.com|
```
