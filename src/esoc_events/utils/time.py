from datetime import datetime


def parse_fdyn_time(doy_utc: str):
    """
    Args:
        doy_utc (str): "2023-104T12:47:12.000Z"

    Returns:
        datetime: the corresponding date
    """
    fdyn_format = "%Y-%jT%H:%M:%S.%fZ"
    return datetime.strptime(doy_utc, fdyn_format)


def format_time(date: datetime):
    """
    Args:
        date (datetime)

    Returns:
        str: the ISOC representation "2023-104T12:47:12Z"
    """

    return date.isoformat(timespec="seconds") + "Z"


def fdyn_to_iso(doy_utc: str):
    """
    Args:
        doy_utc (str): "2023-104T12:47:12.000Z"

    Returns:
        str: the ISOC representation "2023-104T12:47:12Z"
    """
    return format_time(parse_fdyn_time(doy_utc))
