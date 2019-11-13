# webdevclass

To install this web app you will need to have:

Access to a Mysql Database.
Python with PIP installed
Node with NPM installed

1. Set up the database.  

--Use the chatdb.sql file to create the appropriate database.  

2. Get the appropriate python libraries  

-- Run pip install -r requirements.txt in the root folder  

3. Set up the javascript libraries  

-- CD into the static folder  

-- run  npm install  which will install jquery  

4. In the root folder open up the app.py file and set the username and password and host address of the database.  

5. In the root folder run the followinig two commands  

-- export FLASK_ENV=development  // in a windows environment exchange "set" for "export"  

-- flask run  

This will start a development web server on port 5000.  

you should at this point be able to access the web page at http://127.0.0.1:5000/

