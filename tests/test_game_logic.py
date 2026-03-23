from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_backwards_hints_fixed():
    # Target: Verify that a guess that is too high tells the user to go LOWER
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # This will fail if the AI is still lying to us!

    # Target: Verify that a guess that is too low tells the user to go HIGHER
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message # This will fail if the AI is still lying to us!

def test_get_range_for_difficulty():
    # Target: Verify that the correct range is returned for each difficulty level
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    
    # Target: Verify it defaults to Normal range if an unknown string is passed
    assert get_range_for_difficulty("Impossible") == (1, 100)