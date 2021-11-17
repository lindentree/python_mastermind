from rng_api import RandomAPI


class TestRandomAPI:

    rc = RandomAPI(7)

    def test_get_mastermind_code_length(self):
        rc = RandomAPI(7)
        assert len(rc.get_mastermind_code()) == 4
