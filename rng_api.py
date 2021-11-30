import requests
import random

class RandomAPI:

    """Accesses the external Random API"""

    url = 'https://www.random.org/integers/'

    def get_mastermind_code(self, settings: dict) -> str:

        """Returns formatted numeric string code from external api"""

        params = f'?num={settings["digits"]}&min=0&max={settings["upper_limit"]}&col={settings["digits"]}&base=10&format=plain&rnd=new'

        try:
            response = requests.get(self.url+params)

        except requests.exceptions.RequestException as e:
            print(e)
            print("There was a problem with the external API, using fallback rng!")

            return self.create_fallback_code(settings)

        return response.text.replace(" ", "").replace("\t", "").strip()

    def create_fallback_code(self, settings: dict) -> str:

        """Generates a pseudorandom numeric string if Random API fails or is not available"""

        digits = [str(x) for x in range(settings["upper_limit"] + 1)]
        passcode = ""

        for i in range(settings["digits"]):
            digit = random.sample(digits, 1)[0]
            passcode += digit

        return passcode
