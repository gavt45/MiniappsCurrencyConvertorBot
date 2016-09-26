# MiniappsCurrencyConvertorBot
Python http://miniapps.run bot to convert currences.

# Requirements:
Python libraries:

- django
- requests

Other:

- ngrok (download from https://ngrok.com/download)

# How to setup:
On linux:

1. Create django project: django-admin startproject MiniappsFinanceBot
2. Copy with replacement files from downloaded repo to MiniappsFinanceBot/MiniappsFinanceBot
3. Run ngrok: sudo ./ngrok http 8080
3. Now run server: sudo python MiniappsFinanceBot/manage.py runserver 8080
