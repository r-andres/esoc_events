from esoc_events.utils.time import fdyn_to_iso


def test_fdyn_to_iso() -> None:
    doy_utc = "2023-104T12:47:12.000Z"
    assert fdyn_to_iso(doy_utc) == "2023-04-14T12:47:12Z"
