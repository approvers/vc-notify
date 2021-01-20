import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from conf import CREDENTIAL_FILE_NAME

CREDENTIAL = credentials.Certificate(CREDENTIAL_FILE_NAME)


def init():
    firebase_admin.initialize_app(CREDENTIAL, {
        'databaseURL': "https://vc-diff-default-rtdb.firebaseio.com",
        'databaseAuthVariableOverride': {
            'uid': 'my-service-worker'
        }
    })


def set_diff_ch(guild_id: int, ch_id: int):
    ref = db.reference(f"/guilds/{str(guild_id)}")
    ref.set({"diff_ch_id": ch_id})


def get_diff_ch(guild_id: int):
    ref = db.reference(f"/guilds/{guild_id}")
    data = ref.get("diff_ch_id")

    return int(data[0]["diff_ch_id"])
