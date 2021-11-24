from user_leaderboard import UserLeaderBoard

def test_writetofile(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "scores.txt"
    UserLeaderBoard.save_score_to_file('Hello\n')  # or use str(file)
    assert p.read_text() == 'Hello\n'