# convert.py
#Purpose: Switch a string to a float type
#input: String
#Output: float
# "34.2"
# "34.2, Float"
from typing import Optional

def str_to_float(s) -> Optional[float]:
    try:
        s = float(s)
        return s
    except ValueError:
        return None
