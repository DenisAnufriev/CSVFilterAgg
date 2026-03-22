from src.aggregation import aggregate


def test_aggregate_avg():
    rows = [{"price": "100"}, {"price": "300"}]
    assert aggregate(rows, "price", "avg") == 200


def test_aggregate_min():
    rows = [{"price": "100"}, {"price": "300"}]
    assert aggregate(rows, "price", "min") == 100


def test_aggregate_max():
    rows = [{"price": "100"}, {"price": "300"}]
    assert aggregate(rows, "price", "max") == 300
