from datetime import datetime, timedelta


def add_seconds(secs: float) -> datetime:
    """Calculates the exact time after a specified number of seconds have passed.
    Args:
        secs: number of seconds to add.
    Returns:
        The updated datetime object."""

    current_time = datetime.now()
    return current_time + timedelta(seconds=secs)
