from pathlib import Path

from esoc_events.utils.evfm_parser import EvfmParser


def test_evfm_parser() -> None:

    path = (
        Path(__file__).parents[0]
        / "data"
        / "EVFM_20240114T000000_20240216T000000_20240122T123000_v01-00.JUIC-O"
    )
    EvfmParser(path)
