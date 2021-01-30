import base64

from config import CREDENTIAL_B64
from firebase_admin import credentials


def get_credential() -> credentials.Certificate:
    decoded_base64 = base64.b64decode(CREDENTIAL_B64).decode()
    credential = credentials.Certificate(decoded_base64)

    return credential
