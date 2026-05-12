
import re

def clock_to_seconds(clock):
    """Convert NBA clock string like PT12M00.00S to seconds."""
    if clock is None:
        return None

    match = re.match(r"PT(\d+)M([\d.]+)S", str(clock))
    if not match:
        return None

    minutes = int(match.group(1))
    seconds = float(match.group(2))

    return int(minutes * 60 + seconds)


def elapsed_seconds(period, clock):
    if period is None or clock is None:
        return None

    period = int(period)
    remaining_seconds = clock_to_seconds(clock)

    if remaining_seconds is None:
        return None

    if period <= 4:
        return (period - 1) * 720 + (720 - remaining_seconds)
    else:
        return 4 * 720 + (period - 5) * 300 + (300 - remaining_seconds)