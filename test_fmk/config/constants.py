from os import environ
from dotenv import load_dotenv

env = environ.get('MY_ENV', 'local')

if env == 'local':
    load_dotenv()

base_url = 'https://www.aliexpress.com/'

usr_email = environ.get('USER_EMAIL')
if usr_email == '':
    raise Exception(f'======== .env file with USER_EMAIL did not loaded ========')

usr_pass = environ.get('USER_PASS')
if usr_pass == '':
    raise Exception(f'======== .env file with USER_PASS did not loaded ========')
