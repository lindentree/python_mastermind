from game import Game

class TestGame:

    def test_correct_guess(self):
        g = Game('7789')
        assert g.provide__guess_feedback('7789') == 'CCCC'

    def test_guess_feedback(self):
        g = Game('7789')
        assert g.provide__guess_feedback('0087') == 'CW'

    def test_guess_feedback_none(self):
        g = Game('7789')
        assert g.provide__guess_feedback('0000') == ''
    
    def test_guess_feedback_all_wrong_place(self):
        g = Game('7789')
        assert g.provide__guess_feedback('9877') == 'WWWW'


    def test_guess_caching(self):
        g = Game('7789')
        g.guesses['6668'] = True
        assert '6668' in g.guesses