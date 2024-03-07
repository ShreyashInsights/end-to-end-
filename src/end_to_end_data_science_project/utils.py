import os
import sys
from src.end_to_end_data_science_project.exception import CustomException
from src.end_to_end_data_science_project.logger import logging
import pandas as pd 



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df