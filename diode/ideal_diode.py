# this code is used to implement the ideal diode models
import numpy as np

def ideal_diode_current(V: float):
    if(V>0):
        return V
    else:
        return 0

def ideal_diode_current_with_drop(V: float,v_drop: float):
    if(V-v_drop>0):
        return V-v_drop
    else:
        return 0
    
def exp_diode_current(V: float, V_t: float):
    return V_t*(np.exp(V/V_t)-1)

def ramp_diode_current(V: float,V_t: float, R_d: float):
    if V<0:
        return 0
    if V>0:
        return (V-V_t)/R_d



# for ideal diode model,Voltage is not a function of V_t
# it shall be viewed as an on-switch if V>0,an off-switch if V<0 
# for exponential diode model, it shall follow exp model,but the shockley equation is not used for breakdown
# for ramp diode model, it shall follow ramp equation 
# with the following parameters:
# V: voltage
# V_t: thermal voltage
# R_d: dynamic resistance
# v_drop: voltage drop
