from rng_api import RandomAPI


class TestRandomAPI:

    def test_get_mastermind_code_length(self):
        rc = RandomAPI()
        assert len(rc.get_mastermind_code(7)) == 4
