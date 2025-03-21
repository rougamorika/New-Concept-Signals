import ideal_diode
import warnings
r_d=0
x = input("Enter the value for x: ")
v_drop = input("Enter the value for v_drop: ")
r_d=input("Enter the value for r_d: ")
while(float(r_d)<=float(0.0)):
    warnings.warn("r_d should be greater than 0!!!")
    r_d=input("Enter the value for r_d: ")
a = ideal_diode.ideal_diode_current(float(x))
a_drop= ideal_diode.ideal_diode_current_with_drop(float(x),float(v_drop))
a_ramp= ideal_diode.ramp_diode_current(float(x),0.026,0.1)
a_exp= ideal_diode.exp_diode_current(float(x),0.026)

print("ideal:"+str(a)+" volts")
print("drop_ideal:"+str(a_drop)+" volts")
print("ramp:"+str(a_ramp)+" volts")
if(float(a_exp)<10000000000.0):
    print("exp:"+str(a_exp)+" volts")
else:
    print("exp:"+str(a_exp)+" volts")
    print("exp is too large,this value can be approximation rather than accurate value.")

