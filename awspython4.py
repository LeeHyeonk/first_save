import sys
import os
import requests
import base64
import json
import logging
import time
import pymysql
import pandas as pd
import csv


conn = pymysql.connect(
    database='leedata',
    host='database-2.cimvg7h4h4i1.us-east-2.rds.amazonaws.com',
    port=3306,
    user='leeuser',
    password='leeuser1',
    use_unicode = True,
    charset = 'utf8'
    )


def main():
    #call RDS
    
    try :
        cursor = conn.cursor()

    except :
        logging.error("RDS에 연결되지 않았습니다.")
        sys.exit(1)

    
    cursor.execute("CREATE TABLE customers(name VARCHAR(20), age VARCHAR(20));")

if __name__ == "__main__":
    main()


