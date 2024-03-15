import numpy as np


def calc_r(l, c):
    return np.sqrt(l / (2 * c))

def c_per_pedal(num_pedals, c_full):
    return (c_full / (num_pedals * 2))
    
def max_i(num_pedals, i_per_pedal):
    return (num_pedals * i_per_pedal)

def c_smooth(i, f, vrpp):
    return i / (2 * f * vrpp)

# 6 outputs version
NUM_PEDALS = 6

# Assuming 160 mA max per pedal
I_MAX_P = 160e-3

# Combined current consumption
i_max = max_i(NUM_PEDALS, I_MAX_P)
print(f"Combined current consuption: {i_max} A")

# Mains powers frequency
F_HZ = 50

# Ripple after bridge
V_RPP = 0.5

# Capactiance combined after bridge
c_full = c_smooth(I_MAX_P * NUM_PEDALS, 50, 0.5)
print(f"Filter combined capacitance: {c_full * 1000} mF")

c_p = c_per_pedal(NUM_PEDALS, c_full)
print(f"Capacitance per LDO: {c_p * 1000} mF")

c_f = c_full - c_p * 6
print(f"Capacitance after bridge: {c_f * 1000} mF")
