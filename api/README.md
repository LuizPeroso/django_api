Blank API
=============

**//TODO: CHANGE ME :) Api short description.**

--------------------
# **/Api Configuration**
--------------------
## **/Environment Variables**

### Debug config, deploy set to False
1. DEBUG: _Default_: True

### Sentry configuration
1. **RAVEN_DSN_WORKER**: _Default_: ""

### ELK configuration
1. **LOGSTASH_HOST**: _Default_: "127.0.0.1"
2. **LOGSTASH_PORT**: _Default_: 28777

### Database configuration
3. **DB_NAME**: Sets database name. _Default_:'mysql'
1. **DB_USER**: Sets database connection user. _Default_: 'root'
2. **DB_PASSWORD**: Sets database connection password. _Default_: 'root'
5. **DB_HOST**: Sets database connection host. _Default_: '172.17.0.1'
4. **DB_PORT**: Sets database connection port. _Default_: '3306'

### CORS configuration
1. **CORS_ORIGIN_ALLOW_ALL**: Sets if the Api allowed all cors. _Default_: True

### AUTHENTICATION API configuration
1. **AUTHENTICATION_HOST**: Sets a host to authentication use. _Default_: 'http://172.17.0.1:8001'
2. **AUTHENTICATION_API**: Sets a endpoint to authentication use. _Default_: AUTHENTICATION_HOST + '/api/v1/check'

----------------------
# **/Api Setup**
----------------------
## **Setup**
### Installing the Api:
```sh
$ pip install -r requirements.txt
```

### Tests
**Running automated tests:**
```sh
$ pip install -r requirements_test.txt
```

```sh
$ python manage.py test --settings main.settings_test
```

**Validate Jenkins:**
```sh
$ python manage.py jenkins --settings main.settings_test --enable-coverage
```

-----------------
# **/Api Endpoints**
-----------------

**//TODO: CHANGE ME :) Describe all API endpoints using the template.**
## **/api/v1/example**
**//TODO: CHANGE ME :) Endpoint short description.**
**This endpoint needs authentication.**

### [GET]
### **Filters:** ALL FIELDS AND SUB-FIELDS.

### Input:

#### Output:
