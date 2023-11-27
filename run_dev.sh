#!/bin/bash

## Run Database ### 
export MONGO_URI='mongodb://localhost:27017'
export DB_NAME='e_commerce'

# Runserver
uvicorn src.main:app --reload