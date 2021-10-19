# SS Challenge

#### A Python based API for Zip Codes.

## Overview

This REST API contains some basic routes for adding, removing, and viewing stored zip codes. This is meant to demonstrate ability for an interview challenge.

## Run

To run the API you will need to have both [**Python3.8**](https://www.python.org/downloads/) and the [**Flask**](https://flask.palletsprojects.com/en/2.0.x/installation/) module installed. As this is a very basic flask API you can follow the run instructions below here or see the [docs](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing) for help with your specific system.

#### Locally (Linux/MacOS)

After cloning the repo and installing all prerequisites simply run:

```
$ export FLASK_APP=ss_challenge
$ flask run
```

This will start the API locally on port 5000.

> **NOTE:** If you do not install the flask CLI you may need to use ```python -m flask run``` instead.

## Routes

The following routes ara exposed from the API:

    POST /insert/:zip_code - Inserts specified Zip Code to memory
    DELETE /delete/:zip_code - Deletes specified Zip Code from memory
    GET /has/:zip_code - Checks specified Zip Code in memory
    GET /display - Returns stored Zip Codes from memory
    
> **NOTE:** A Postman collection for the API has been provided as a convenvience in the __collection.json__ file. It also contains examples for the routes (shows basic error handling).
