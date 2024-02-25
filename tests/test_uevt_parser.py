from pathlib import Path

from esoc_events.utils.uevt_parser import UevtParser


def test_uevt_parser() -> None:

    path = Path(__file__).parents[0] / "data" / "UEVT_JFCT_CCO2_00002.JUI"
    UevtParser(path)
