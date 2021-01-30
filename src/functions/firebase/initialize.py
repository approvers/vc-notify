import firebase_admin

from src.functions.firebase.credential import get_credential

from config import FIREBASE_SETTINGS


def initialize() -> None:
    CREDENTIAL = get_credential()

    firebase_admin.initialize_app(CREDENTIAL, FIREBASE_SETTINGS)
