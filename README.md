# Backend setup
## Create python3 virtualenv
```
python3 -m venv env
source env/bin/activate # you need to run this before running any python commands
```

## Install dependencies
```
pip install -r requirements.txt
```

## Start backend server
```
PYTHONPAH=$(pwd) python3 backend/application.py
```
Changes to backend code are auto reloaded.

# Frontend setup
## Build packages
```
npm install
```

## Start webpack dev server
In a different command line window
```
npm run start
```
Changes to frontend code are auto reloaded.

# View the App
Homepage: http://localhost:5000
The explanation of the table seen on the homepage is in the video. 
All fields are sortable by clicking on the header and can be filtered by entering values in the blanks below the headers. Data can be filtered using multiple fields as well. 
