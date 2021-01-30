from src.presentation.client import Client
from src.functions.firebase.initialize import initialize

initialize_firebase = initialize


def start():
    bot_client = Client()
    bot_client.launch()

    initialize_firebase()
