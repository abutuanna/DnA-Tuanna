import cx_Oracle
import pyodbc
import sqlalchemy

# Oracle connection
def Oracle_conn(username, password):
    dsn = cx_Oracle.makedsn(
        host='dwh-db.techcombank.com.vn',
        port=1521,
        service_name='dwprd'
    )
    try:
        return cx_Oracle.connect(username, password, dsn)
    except Exception as ex:
        print(ex)

# SQL Server Connection
def SQL_conn():
    server_name = '.\SQLEXPRESS'
    port = '1433'
    conn_str = 'DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server_name+';PORT='+port+';Trusted_connection=yes;'
    try:
        return pyodbc.connect(conn_str)
    except Exception as ex:
        print(ex)