from app.predictor import get_risk_level


def test_low_risk_level():
    assert get_risk_level(0.20) == "low"


def test_medium_risk_level_lower_boundary():
    assert get_risk_level(0.45) == "medium"


def test_medium_risk_level():
    assert get_risk_level(0.60) == "medium"


def test_high_risk_level_boundary():
    assert get_risk_level(0.75) == "high"


def test_high_risk_level():
    assert get_risk_level(0.95) == "high"