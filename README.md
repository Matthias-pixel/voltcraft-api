# voltcraft-api
Web API for Voltcraft SEM6000 Outlets

## Getting started
### 1. Clone repository
```
$ git clone --recurse-submodules https://github.com/Matthias-pixel/voltcraft-api.git voltcraft-api
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

## Usage
### 1. Configure server
    Configure aliases in config.yaml

### 3. Start server
1. Go into the server directory
```
$ cd server
```

2. Start server
```
$ python3 -m voltcraft_api
```

### Use API
1. Turn an outlet on
    GET /v1/on/{alias}
    replace {alias} with the outlet's alias
2. Turn an outlet off
    GET /v1/off{alias}
3. Get measurement data
    GET /v1/info/{alias}
4. List all outlets from config.yaml
    GET /v1/list