# MiniappsCurrencyConvertorBot
Python 2.7 http://miniapps.run bot to convert currences.

# Requirements:
Python libraries:

- django
- requests

Other:

- ngrok (download from https://ngrok.com/download)
- and you need an account on https://openexchangerates.org/ to set 'CURRENCIESAPIID' in view.py equals to your API id

# How to setup:
On linux:

- Install libs: sudo apt-get install python-django
- And with pip: sudo python2.7 -m pip install django requests

1. Create django project: django-admin startproject MiniappsFinanceBot
2. Copy with replacement files from downloaded repo to MiniappsFinanceBot/MiniappsFinanceBot
3. Run ngrok: sudo ./ngrok http 8080
3. Now run server: sudo python MiniappsFinanceBot/manage.py runserver 8080
