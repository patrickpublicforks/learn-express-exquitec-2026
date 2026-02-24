import re
from datetime import timedelta

def parse_time_string(time_str):
    """
    Convert a string like '30m', '2h', '45s', '1d' into a datetime.timedelta object.
    Supports multiple formats like '1h30m', '2d5h', etc.
    """
    if not isinstance(time_str, str) or not time_str.strip():
        raise ValueError("Input must be a non-empty string.")

    # Regex to match number + unit (d, h, m, s)
    pattern = re.compile(r'(\d+)([dhms])', re.IGNORECASE)
    matches = pattern.findall(time_str)

    if not matches:
        raise ValueError(f"Invalid time format: {time_str}")

    kwargs = {}
    for value, unit in matches:
        value = int(value)
        unit = unit.lower()
        if unit == 'd':
            kwargs['days'] = kwargs.get('days', 0) + value
        elif unit == 'h':
            kwargs['hours'] = kwargs.get('hours', 0) + value
        elif unit == 'm':
            kwargs['minutes'] = kwargs.get('minutes', 0) + value
        elif unit == 's':
            kwargs['seconds'] = kwargs.get('seconds', 0) + value

    return timedelta(**kwargs)