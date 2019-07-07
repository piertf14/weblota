import uuid
import culqipy
from django.conf import settings


class CulqiProcess(object):
    token = None
    charge = None

    def __init__(self):
        culqipy.public_key = settings.CULQI_PUBLIC_KEY
        culqipy.secret_key = settings.CULQI_SECRET_KEY

    def generate_token(self):
        token = culqipy.Token.create(
            card_number="4111111111111111",
            currency_code="PEN",
            cvv="123",
            exp_month=9,
            exp_year=2020,
            fingerprint="q352454534",
            last_name="Muro",
            email="wmuro@me.com",
            first_name="William"
        )
        self.token = token['id']

    def charge(self):
        charge_obj = culqipy.Charge.create(
            address="Avenida Lima 1232",
            address_city="LIMA",
            amount=1000,
            country_code="PE",
            currency_code="PEN",
            email="wmuro@me.com",
            first_name="William",
            installments=0,
            last_name="Muro",
            metadata="",
            phone_number=3333339,
            product_description="Venta de prueba",
            token_id=self.token)

        self.charge = charge_obj["id"]