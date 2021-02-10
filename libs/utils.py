import os, pymysql, requests, json, logging, urllib, hashlib, random, smtplib, sys

def getMysql():
    config = {
        "host": "localhost",
        "username": "root",
        "password": "3w_Bfp5gqA+5",
        "database": "odds",
        "port": 3306,
    } if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV']== 'production' else {
        "host": "localhost",
        "username": "root",
        "password": "Juemin_90",
        "database": "odds",
        "port": 3306,
    }
    db = pymysql.connect(host=config['host'], user=config['username'], password=config['password'], database=config['database'], port=kjconfig['port'])
    return db
