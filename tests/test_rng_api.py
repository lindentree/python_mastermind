from rng_api import RandomAPI


class TestRandomAPI:

    def test_get_mastermind_code_length(self):
        rc = RandomAPI()
        setting = {
       "digits": 4,
       "upper_limit": 5,
       "guesses": 12
   }
        assert len(rc.get_mastermind_code(setting)) == 4
    
   
