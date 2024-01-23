from sqlalchemy import create_engine

mysql_user = "你的MySQL用户名"
mysql_pass = "你的MySQL密码"
mysql_host = "你的MySQL数据库IP地址"
mysql_db = "你的MySQL数据库名称"

def sql_writer(pd_data, tb_name, exists='replace'):
    sql_con = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:3306/{mysql_db}")
    pd_data.to_sql(name=tb_name, con=sql_con, if_exists=exists, index=False)