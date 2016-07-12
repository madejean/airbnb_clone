import os
env_name = os.environ.get('AIRBNB_ENV')
environment = ['developement', 'production']
database = { enviroment[0]:'airbnb_dev', environment[1]:'airbnb_prod' }

if env_name == None:
    print "Please set AIRBNB_ENV environment variable to either produce or develop"
    quit()
elif env_name != "development" and env_name != "production":
    print "AIRBNB_ENV environment variable has an usupported value"
    quit()

if env_name == environment[0]:
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

else:
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = '3000'
    DATABASE = {
        'host': '158.69.77.113',
        'user': 'airbnb_user_prod',
        'database': database[environment[1]],
        'port': '3306',
        'charset': 'utf8',
        'password': os.environment.get('AIRBNB_DATABASE_PWD_PROD'),
}
        
