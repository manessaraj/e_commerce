#!/bin/bash
source .mongodb_ssh.sh
## Run Database ### 
export MONGO_URI="mongodb+srv://$DB_USER:$DB_PASS@cluster0.i0vj3wz.mongodb.net/?retryWrites=true&w=majority"
export DB_NAME='e_commerce'
export DEBUG_MODE="false"
# Runserver
uvicorn src.main:app --reload