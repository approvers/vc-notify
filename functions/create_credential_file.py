import os
import json
import base64

from conf import CREDENTIAL_B64, CREDENTIAL_FILE_NAME


def create_credential_file():
    with open(CREDENTIAL_FILE_NAME, "wb") as f:
        f.write(base64.b64decode(CREDENTIAL_B64))
