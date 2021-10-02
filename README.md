# Instructions to set-up
Clone this directory
Make sure flask is installed, `pip install flask`
In the folder run `py -3 -m venv venv` to set up the enviro

# First try
In this directory run `export FLASK_APP=server/app`
In this directory run `export FLASK_ENV=development`
In this directory run `flask run`

#If that doesn't work
Go in /server directory and run `export FLASK_APP=app` and `export FLASK_ENV=development` then `flask run`
Then go in ../client and run `npm install` if it's first time then `npm start`
Tl;dr server and client must be started separetly, first start flask server then node.js client.
