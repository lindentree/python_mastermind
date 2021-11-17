from rng_api import RandomAPI


class TestRandomAPI:

    def get_mastermind_code_length(self):
        rc = RandomAPI(7)
        assert len(rc.get_mastermind_code()) == 4
