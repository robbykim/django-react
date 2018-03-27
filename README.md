# django-react
An incredibly minimal boilerplate project setup for Django and React. Built with create-react-app and Django and glue code to link the two.

## Setup

### React
```shell
cd frontend
yarn install
```

### Django
```shell
cd ..    # Should be in the root folder
virtualenv env/dev
source env/dev/bin/activate
pip install -r requirements.txt
```

## Running the development server

To access the React development server
```shell
cd frontend
yarn start
```

Go to http://localhost:3000/

To access the Django served static React page
```shell
cd frontend
yarn run build
cd ..
python manage.py runserver
```

Go to http://localhost:8000/

