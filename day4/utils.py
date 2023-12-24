import os
from sqlalchemy import create_engine

mysql_user = os.environ.get('MYSQLUSER')
mysql_pass = os.environ.get('MYSQLPASS')
mysql_host = "192.168.1.50"
mysql_db = "Meraki"

def sql_writer(pd_data, tb_name, exists='replace'):
    sql_con = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:3306/{mysql_db}")
    pd_data.to_sql(name=tb_name, con=sql_con, if_exists=exists, index=False)