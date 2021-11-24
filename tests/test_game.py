from game_session import GameSession

class TestGameSession:

    def test_correct_guess(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('7789') == 'CCCC'

    def test_guess_feedback(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('0087') == 'CW'

    def test_guess_feedback_none(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('0000') == ''
    
    def test_guess_feedback_all_wrong_place(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('9877') == 'WWWW'


