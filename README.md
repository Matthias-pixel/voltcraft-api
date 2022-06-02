# voltcraft-api
Web API for Voltcraft SEM6000 Outlets

## Getting started
### 1. Clone repository
```
$ git clone https://github.com/Matthias-pixel/voltcraft-api.git voltcraft-api
$ cd voltcraft-api
```

### 2. Setup environment
1. Create a virtual environment
```
$ virtualenv -p python3 venv
```

2. Enter the virtual environment
```
$ source venv/bin/activate
```

3. Install packages
```
$ pip3 install -r requirements.txt
```

### 3. Start server
1. Go into the python-flask-api directory
```
$ cd server
```

2. Start server
```
$ python3 -m swagger_server
```