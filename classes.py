import requests
import json
from config import keys

class ConvException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(iz: str, to: str, amount: str):
        if iz == to:
            raise ConvException(f"Вы пытаетесь конвертировать одну и ту же валюту ({iz}).")
        iz, to = iz.lower(), to.lower()
        try:
            _iz = keys[iz]
        except KeyError:
            raise ConvException(f"Пока не умеем конвертировать валюту {iz}")
        try:
            _to = keys[to]
        except KeyError:
            raise ConvException(f"Пока не умеем конвертировать валюту {to}")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvException(f"Количество укажите числом, если нужно дробное число, укажите через точку")
        r = requests.get(f'https://api.apilayer.com/currency_data/convert?to={_to}&from={_iz}&amount={amount}&apikey=4xP8r3R1pvV6PXsjMnr1KXzE2sgdu7K9')
        itog = round(json.loads(r.content)['result'], 2)
        return itog
