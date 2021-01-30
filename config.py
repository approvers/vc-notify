from os import environ

DISCORD_TOKEN = environ["VCDIFF_TOKEN"]
CREDENTIAL_B64 = environ["VCDIFF_CRED_B64"]

FIREBASE_SETTINGS = {
        'databaseURL': environ["VCDIFF_DB_URL"],
        'databaseAuthVariableOverride': {
            'uid': environ["VCDIFF_UID"]
        }
    }
