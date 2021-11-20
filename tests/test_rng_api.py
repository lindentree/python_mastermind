from rng_api import RandomAPI


class TestRandomAPI:

    def test_get_mastermind_code_length(self):
        rc = RandomAPI()
        assert len(rc.get_mastermind_code(7)) == 4
    
    def test_response_range(self):
        rc = RandomAPI()
        for x in rc.get_mastermind_code(7):
            if int(x) <= 7:
                assert True
            else:
                assert False
