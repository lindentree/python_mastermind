from game_session import GameSession

class TestGame:

    def test_correct_guess(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('7789') == 'OOOO'

    def test_guess_feedback(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('0087') == 'OX'

    def test_guess_feedback_none(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('0000') == ''
    
    def test_guess_feedback_all_wrong_place(self):
        g = GameSession('7789')
        assert g.provide__guess_feedback('9877') == 'XXXX'

    def test_guess_feedback_dupes(self):
        g = GameSession('3035')
        assert g.provide__guess_feedback('3055') == 'OOO'


