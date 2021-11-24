import requests

class RandomAPI:

    url = 'https://www.random.org/integers/'

    def get_mastermind_code(self, settings: dict) -> str:
        """Returns code from external api"""

        params = f'?num={settings["digits"]}&min=0&max={settings["upper_limit"]}&col=4&base=10&format=plain&rnd=new'

        try:
            response = requests.get(self.url+params)

        except requests.exceptions.RequestException as e:               
            print(e)

        return response.text.replace(" ", "").replace("\t", "").strip()


