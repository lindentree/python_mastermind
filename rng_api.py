import requests

class RandomAPI:

    url = 'https://www.random.org/integers/'

    def get_mastermind_code(self, settings):
        """Returns code from api"""

        params = f'?num={settings["digits"]}&min=0&max={settings["upper_limit"]}&col=4&base=10&format=plain&rnd=new'

        try:
            response = requests.get(self.url+params)

        except requests.exceptions.RequestException as e:               
            print(e)

        return response.text.replace(" ", "").replace("\t", "").strip()


