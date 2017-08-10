import os

BasketballPlayerDatabase = 'BasketballPlayerDatabase.p'

Root_URL = 'https://' + os.getenv('HEROKU_APP_NAME') + '.herokuapp.com'
#Root_URL = '/'
#Root_URL = 'https://joesbasketball3.herokuapp.com/'
#Root_URL = 'https://joesbasketballtest.herokuapp.com/'
#Root_URL = 'https://pure-refuge-18946.herokuapp.com'

#also have to change env in main file
