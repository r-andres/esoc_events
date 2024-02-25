from pathlib import Path

from esoc_events.utils.fecs_parser import FecsParser


def test_fecs_parser() -> None:

    path = Path(__file__).parents[0] / "data" / "FECS_JFCT_C024_______00001.JUI"
    parser = FecsParser(path)
    assert len(parser.passes) == 4

    first_pass = FecsParser.extract_pass(parser.passes[0])
    assert first_pass.get("station") == "MLG"
