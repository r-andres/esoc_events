from pathlib import Path

from esoc_events.utils.evtc_parser import EvtcParser


def test_evtc_parser() -> None:

    path = Path(__file__).parents[0] / "data" / "EVTC__000055.jui"
    EvtcParser(path)
