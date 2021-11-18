import requests


class RandomAPI:
    url = 'https://www.random.org/integers/'


    def __init__(self, limit):
	    self.limit = limit

    def get_mastermind_code(self):
        """Returns code from api"""

        params = f'?num=4&min=0&max={self.limit}&col=4&base=10&format=plain&rnd=new'

        try:
            response = requests.get(self.url+params)

        except requests.exceptions.RequestException as e:               
            print(e)

        return response.text.replace(" ", "").replace("\t", "").strip()

x = RandomAPI(7).get_mastermind_code()

print(x)
print(len(x))
