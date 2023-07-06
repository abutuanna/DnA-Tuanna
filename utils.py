import sqlalchemy.types
from sqlalchemy.engine import create_engine, URL
from urllib.parse import quote, quote_plus

# create SQL Server engine
def sql_engine():
    server = ".\SQLEXPRESS"
    database = "ABBANK"
    params = quote_plus("DRIVER={SQL Server Native Client 11.0};"
                        "SERVER="+server+";"
                        "DATABASE="+database+";"
                        "Trusted_Connection=yes")
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": params})
    return create_engine(connection_url)

# create Oracle Engine
def oracle_engine(username, password):
    host = 'dwh-db.techcombank.com.vn'
    server_name = 'dwprd'
    engine_path = 'oracle+cx_oracle://' + username + ':%s' + \
                   '@' + host + '/?service_name='+server_name
    path = engine_path @quote(password)
    return create_engine(path)

#create table
def create_table(data, schema, table_name, engine, if_exists):
    # dtype = {
    #     c : sqlalchemy.types.VARCHAR(100)
    # }
    data.to_sql(
        table_name,
        engine,
        schema=schema,
        index=False,
        if_exists=if_exists
    )