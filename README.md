# People Management App
An Application built to manage peoples' details and data.

## Backend
The Backend of the Application is built using the Python Framework Django.

## Frontend
The Frontend of the Application is built using React and Babel for compiling/transforming JavaScript

## Usage
I created some helper scripts to make it easier to setup and run:

1. `make_env.sh`
    - Creates the Python environment and installs requirements
2. `migrate.sh`
    - Creates DB and/or applies necessary migrations
3. `run_server.sh`
    - Runs server

Once the server is running it can be accesed via a browser by going to 
[localhost port 8000](http://127.0.0.1:8000]) or if configured in `/etc/hosts` http://www.people-app.com

- The API can be queried using `http://127.0.0.1:8000/people/`
- The optional parameter `?order_by=email` can be added to sort the results (sorts by name by default)

---
## Installation procedure (for reference)

---
This section is a record of the commandline steps carried out to setup the environment and dependencies

##### Environment setup and Installing Backend components:
- Installed Python 3 (using brew on OSX)
- Created virtualenv in project directory: 
    - `virtualenv env -p python3`
- Created `requirements.txt` file and installed:
    - `pip install -r requirements`
- Added `127.0.0.1  www.people-app.com` to my `/etc/hosts` file to test Django ALLOWED_HOSTS in browser

##### Installing UI components:
- Installed Node (using brew on OSX)
- Installed dependencies:
    - `npm i -D webpack webpack-cli`
    - `npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties`
    - `npm i react react-dom prop-types`
    - `npm i weak-key --save-dev`

