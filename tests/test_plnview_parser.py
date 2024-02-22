from pathlib import Path

from esoc_events.utils.plnview_parser import PlnViewParser


def test_plnview_parser() -> None:

    path = Path(__file__).parents[0] / 'data' / 'PLNVIEW_20240222T000000_20250101T000000_20240222T135018_v01-00.PASS-O'
    parser = PlnViewParser(path)
    assert len(parser.sessions) == 5605
    assert len(parser.satellite('JUIC').sessions) == 163
    assert len(parser.after('2024-08').sessions) == 73
    assert len(parser.before('2024-10').sessions) == 58

    assert len(parser.reset().ground_station('MLG').sessions) == 1026
