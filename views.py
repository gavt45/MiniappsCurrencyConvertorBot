# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
import requests

CURRENCIESAPIID='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #openexchangerates.org api id
currencies=[ # Code uses only 1 2 and 3 
    "BRL",
    "USD",
    "EUR",
    "RUB",
]
def play(request, frome, to):
        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=' + CURRENCIESAPIID+'&base=USD')
        respJson = response.json()
        rates = respJson['rates']
        try:
            if int(frome)==1:
                VALUEE=request.GET["my_input"]
                FINALVALUE = float(VALUEE) * float(rates[currencies[int(to)]])
                resp = \
                    """<?xml version="1.0" encoding="UTF-8"?>
                        <page version="2.0" style="category">
                        <div protocol="telegram">
                        Price for USD to """ + str(currencies[int(to)]) + """ is """ + str(FINALVALUE) + """
                        </div>
                        </page>"""
            elif int(frome)==2:
                VALUEE = request.GET["my_input"]
                FINALVALUE = float(VALUEE)*(float(rates[currencies[int(frome)]])/float(rates[currencies[int(to)]]))
                resp = \
                    """<?xml version="1.0" encoding="UTF-8"?>
                        <page version="2.0" style="category">
                        <div protocol="telegram">
                        Price for EUR to """ + str(currencies[int(to)]) + """ is """ + str(FINALVALUE) + """
                        </div>
                        </page>"""
            elif int(frome)==3:
                VALUEE = request.GET["my_input"]
                FINALVALUE = float(VALUEE)*(float(rates[currencies[int(frome)]]) / float(rates[currencies[int(to)]]))
                resp = \
                    """<?xml version="1.0" encoding="UTF-8"?>
                        <page version="2.0" style="category">
                        <div protocol="telegram">
                        Price for RUB to """ + str(currencies[int(to)]) + """ is """ + str(FINALVALUE) + """
                        </div>
                        </page>"""
            print 'resp in try: ' + resp
            return HttpResponse(resp)

        except:
            resp = \
                """<?xml version="1.0" encoding="UTF-8"?>
                    <page version="2.0" style="category">
                    <div>
                        <input
                            navigationId="submit"
                            name="my_input"
                            title="Input value"/>
                    </div>
                    <navigation id="submit">
                        <link pageId="/polls/"""+frome+"""/"""+to+"""" accesskey="True">Done</link>
                    </navigation>
                    </page>"""
            print 'resp in except: '+resp
            return HttpResponse(resp)
