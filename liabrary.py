import subprocess
def load_library():
    subprocess.run('pip install pandas')
    subprocess.run('pip install cx_oracle')
    subprocess.run('pip install pyodbc')
    subprocess.run('pip install sqlalchemy')