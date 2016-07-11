import os
env_name = os.environ.get('AIRBNB_ENV')

if env_name === 'dev':
    DEBUG = True
    HOST = 'localhost'
    PORT = '3333'
    DATABASE = {
        'host': '158.69.77.113',
        'user': 'DATABASE_USER',
        'database': 'airbnb_dev',
        'port': '3306',
        'charset': 'utf8',
        'password': 'PASSWORD',
    }

elif env_name == 'prod':
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = '3000'
    DATABASE = {
        'host': '158.69.77.113'.
        'user': 'DATABASE_USER',
        'database': 'airbnb_prod',
        'port': '3306',
        'charset': 'utf8',
        'password': 'PASSWORD',
}
        
