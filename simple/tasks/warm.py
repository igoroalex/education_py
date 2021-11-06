def calc_bundled_temp(coats: int, temperature: str) -> str:
    return f"{round(float(temperature[:-2]) * 1.1 ** coats, 1)}*C"


assert calc_bundled_temp(2, "10*C") == "12.1*C"
# 10 * 1.1 = 11
# 11 * 1.1 = 12.1
assert calc_bundled_temp(1, "2*C") == "2.2*C"
assert calc_bundled_temp(4, "6*C") == "8.8*C"
assert calc_bundled_temp(20, "4*C") == "26.9*C"
