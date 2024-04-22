from typing import Any

from esoc_events.utils.uevt_parser import UevtParser
from esoc_events.utils.uevt_writer import Uevt


def test_uevt_writer(tmp_path: Any) -> None:
    uevt_file = tmp_path / "uevt.xml"
    uevt = Uevt(
        "2023-01-01T00:00:00.000Z",
        "2024-01-01T00:00:00.000Z",
        "2024-02-01T00:00:00.000Z",
    )
    uevt.add_event("A84H", "1", "2024-01-01T00:00:00.000Z", "300")
    uevt.add_event("A74H", "1", "2024-01-01T02:00:00.000Z", "300")
    uevt.add_event("A83H", "1", "2024-01-01T03:00:00.000Z", "300")
    uevt.dump(uevt_file)

    parser = UevtParser(uevt_file)
    assert len(parser.events) == 3

    assert len(parser.reset().after("2024-01-01T01:59:59.000Z").events) == 2
    assert len(parser.reset().before("2024-01-01T02:00:00.000Z").events) == 1
    assert len(parser.reset().id("A74H").events) == 1
    assert len(parser.reset().ids(["A74H"]).events) == 1

    assert len(parser.reset().count(1).events) == 3
    assert len(parser.reset().counts([1]).events) == 3

    assert parser.query_item("A84H", "1") is not None
    assert parser.query_item("A84H", "2") is None
