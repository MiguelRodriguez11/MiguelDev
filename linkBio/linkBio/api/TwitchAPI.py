import os
import time
import dotenv
import requests

class TwitchAPI:

    dotenv.load_dotenv()

    CLIENT_ID= os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET=os.environ.get("TWITCH_CLIENT_SECRET")

    def __init__(self) -> None:
        self.token = None
        self.token_exp = 0

    def generate_token(self):

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "client_credentials",
                "client_id": self.CLIENT_ID,
                "client_secret": self.CLIENT_SECRET
            }
        )

        if response.status_code == 200:
            date = response.json()
            self.token = date["access_token"]
            self.token_exp = time.time() + date["expires_in"]
        else:
            self.token = None
            self.token_exp = 0

    def token_valid(self) -> bool:
        return time.time() < self.token_exp

    def live(self) -> bool:

        if not self.token_valid():
            self.generate_token()

        response = requests.get(
            f"https://api.spotify.com/v1/users/12136310349",
            headers={
                "Authorization": f"Bearer {self.token}"
            }
        )

        if response.status_code == 200 and response.json()["data"]:
            data = response.json()["data"]
            print(data)
            return True

        return False
