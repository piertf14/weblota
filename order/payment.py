import culqipy
from django.conf import settings


class CulqiProcess(object):

    def __init__(self):
        culqipy.public_key = settings.CULQI_PUBLIC_KEY
        culqipy.secret_key = settings.CULQI_SECRET_KEY

    def generate_token(self, data):
        extra_data = {
            'card_number': data['card_number'],
            'currency_code': 'PEN',
            'cvv': data['cvv'],
            'exp_month': data['exp_month'],
            'exp_year': data['exp_year'],
            'fingerprint': "q352454534",
            'last_name': data['reserve'].user.last_name,
            'email': data['reserve'].user.email,
            'first_name': data['reserve'].user.first_name
        }
        token = culqipy.Token.create(extra_data)
        if not token.get('id', None):
            return None
        return token['id']

    def charge(self, data):
        try:
            token = self.generate_token(data)
            if token:
                extra_data = {
                    'address': data['address'],
                    'address_city': data['address_city'],
                    'amount': data['total'] * 1000,
                    'country_code': "PE",
                    'currency_code': "PEN",
                    'email': data['reserve'].user.email,
                    'first_name': data['reserve'].user.first_name,
                    'installments': 0,
                    'last_name': data['reserve'].user.last_name,
                    'metadata': "",
                    'phone_number': data['phone_number'],
                    'product_description': data['product_description'],
                    'token_id': self.token
                }
                charge_obj = culqipy.Charge.create(extra_data)
                return True, charge_obj["id"]
        except Exception as ex:
            return False, ex

        return False, None
