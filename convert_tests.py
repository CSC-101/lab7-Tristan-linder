from typing import Optional
def str_to_float(s) -> Optional[float]:
    try:
        s = float(s)
        return s
    except ValueError:
        return None
s = "34"
print(str_to_float(s))
print(type(float(s)))
s2 = "WAH"
print(str_to_float(s2))
print(type(float(s)))
