# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse

CURRENCIESAPIID='d5daacd93abb414eb1df502507a382f6'

currencies=[
    "BRL",
    "USD",
    "EUR",
    "RUB",
]

"""
def push_test(request):
     Проверка пушей
    for i in range(0, 1):
        req = urllib.request.Request("http://ec2.globalussd.mobi/push?protocol=telegram&service=eyeline.peter&subscriber=014084507047&push=" + str(i))
        resp = urllib.request.urlopen(req)
        time.sleep(10)

    return HttpResponse(resp.read())
"""
import requests
def play(request, frome, to):
        """ Начало игры """

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
                FINALVALUE = float(VALUEE)*(float(rates[currencies[3]])/float(rates[currencies[2]]))
                resp = \
                    """<?xml version="1.0" encoding="UTF-8"?>
                        <page version="2.0" style="category">
                        <div protocol="telegram">
                        Price for EUR to """ + str(currencies[int(to)]) + """ is """ + str(FINALVALUE) + """
                        </div>
                        </page>"""
            elif int(frome)==3:
                VALUEE = request.GET["my_input"]
                FINALVALUE = float(VALUEE)/float(rates[currencies[1]]) * float(rates[currencies[int(to)]])
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
        respother =\
        """<?xml version="1.0" encoding="UTF-8"?>
                <page version="2.0" style="category">
              <div protocol="telegram">
                Получается что<br/>
                """+str(int(num))+""" доллар в """+str(currencies[int(num)])+""" будет """+str(FINALVALUE)+"""
              </div>
        </page>"""