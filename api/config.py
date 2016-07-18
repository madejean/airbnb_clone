import os
env_name = os.environ.get('AIRBNB_ENV')
environment = ['developement', 'production', 'test']
database = { enviroment[0]:'airbnb_dev', environment[1]:'airbnb_prod', environment[2]:'airbnb_test' }

if env_name == None:
    print "Please set AIRBNB_ENV environment for production or developpment"
    quit()
elif env_name != "development" && env_name != "production" && env_name != 'test':
    print "wrong value for AIRBNB_ENV"
    quit()

if (env_name == environment[0]):
    DEBUG = True
    HOST = 'localhost'
    PORT = '3333'
    DATABASE = {
        'host': '158.69.77.113',
        'user': 'airbnb_user_dev',
        'database': database[environment[0]],
        'port': '3306',
        'charset': 'utf8',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV'),
    }

elif (env_name == environment[1]):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = '3000'
    DATABASE = {
        'host': '158.69.77.113',
        'user': 'airbnb_user_prod',
        'database': database[environment[1]],
        'port': '3306',
        'charset': 'utf8',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD'),
    }
        
else:
    DEBUG = False
    HOST = 'localhost'
    PORT = '5555'
    DATABASE = {
        'host' : '158.69.77.113',
        'user' : 'airbnb_user_test',
        'database' : database[environment[2]],
        'port' : '3306',
        'charset' : 'utf8',
        'password' : os.get.environ.get('AIRBNB_DATABASE_PW_TEST'),
    }
