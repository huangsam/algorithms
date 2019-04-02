import pytest

from online.dailycoding.get_itinerary import get_itinerary


@pytest.mark.array
@pytest.mark.backtrack
class TestGetItinerary:
    @pytest.mark.parametrize(
        "start, flights, expected",
        [
            (
                "YUL",
                [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")],
                [("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL"), ("HNL", "AKL")],
            ),
            ("SFO", [("SFO", "HNL"), ("HNL", "SFO")], [("SFO", "HNL"), ("HNL", "SFO")]),
            ("HNL", [("SFO", "HNL"), ("HNL", "SFO")], [("HNL", "SFO"), ("SFO", "HNL")]),
            (
                "HNL",
                [("SFO", "HNL"), ("HNL", "SFO"), ("HNL", "ORD")],
                [("HNL", "SFO"), ("SFO", "HNL"), ("HNL", "ORD")],
            ),
        ],
    )
    def test_get_itinerary_good(self, start, flights, expected):
        result = get_itinerary(start, flights)
        if result is None:
            assert result == expected
        else:
            print(result, expected)
            for i, j in zip(result, expected):
                assert i == j

    @pytest.mark.parametrize(
        "start, flights",
        [
            ("YUL", []),
            ("YUL", [("SFO", "HNL")]),
            ("YUL", [("SFO", "HNL"), ("YUL", "ORD")]),
            ("SFO", [("SFO", "HNL"), ("SFO", "ORD")]),
        ],
    )
    def test_get_itinerary_bad(self, start, flights):
        result = get_itinerary(start, flights)
        assert result is None