# e_commerce
E-Commerce project with FastAPI and Mongo


## Design Document:
https://docs.google.com/document/d/1FslfqIKXR4RCkBDvfiZGfJS9oO78y6Y0sEBKcx0ZSjk/edit 



## Setup for local development:
1. Spin up free MO mongodb server in Mongodb atlas. 
2. Note down username and password. Add local file named `.mongodb_ssh.sh` and add user credentials as:
    ```
    export DB_USER="<username>"
    export DB_PASS="<password>"
    ```
3. RUN setup.sh script (Only once to setup python environment and installing requirements.)
4. RUN run_dev.sh script to start application
5. Go to `http://127.0.0.1:8000/testdb` to test DB connection. 
6. TODO: Load fake data. 