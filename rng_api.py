import requests

class RandomAPI:

    def __init__(self):
	    self.url = 'https://www.random.org/integers/'

    def get_mastermind_code(self, limit):
        """Returns code from api"""

        params = f'?num=4&min=0&max={limit}&col=4&base=10&format=plain&rnd=new'

        try:
            response = requests.get(self.url+params)

        except requests.exceptions.RequestException as e:               
            print(e)

        return response.text.replace(" ", "").replace("\t", "").strip()


