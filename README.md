# Instructions to set-up
Clone this directory
Make sure flask is installed, `pip install flask`  
Make sure npm is installed. (Node.js on windows, apt-get install npm on Unix)  
In the folder run `py -3 -m venv venv` to set up the environment EVERY TIME YOU PULL FROM MAIN, or any branch you haven't worked one, because the environment is going to come with the previous person's route to the Python interpreter.  
Have XAMPP or any other database server running on localhost and make sure you have created a database name "lunar_dada".

# Required libraries
`pip install flask`
`pip install flask-cors`
`pip install flask-mysql`
`pip install flask-bycrip`
`pip install flask-login`
`pip install flask-wrappers` I think this one might come with the basic flask installation


# First try
In this directory run `export FLASK_APP=server/app`  
In this directory run `export FLASK_ENV=development`  
In this directory run `flask run`  

(If that doesn't work >> Go in /server directory and run `export FLASK_APP=app` >> Then `export FLASK_ENV=development`  
Then `flask run` >> Then go in ../client and run `npm install` if it's first time)  

Then go into /client folder  
Then `npm install`
Then `npm start`  
Tl;dr server and client must be started separetly, first start flask server then node.js client.  
