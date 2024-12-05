import numpy as np

##### CONSTANTS ######
mh = 125 
k = 7e-4
vh = 246 
ms = np.array([20,40,50,55,60])
N_Zh = 2.2e6 #2.2 should be used
BR_s_bb = 0.9
BR_Z_ll = 2*3.3658/100 # From percent
Lambda_h_SM = 3.2/1000 #MeV to GeV https://pdg.lbl.gov/2022/tables/rpp2022-sum-gauge-higgs-bosons.pdf
integratedLumi = 10.8 #10.8e-18, atto
#####################
pre_scaling = np.array([1.1499e-5,9.327e-6,3.4005e-6,7.284e-6,5.7675e-6])


def Lambda_h_ss(s_mass):
    first_frac = (k**2*vh**2)/(32*np.pi*mh)
    second_frac = ((mh**2 + 2*s_mass**2)**2)/(mh**2 - s_mass**2)**2
    square_root = np.sqrt(1 - 4*((s_mass**2)/(mh**2)))
    return first_frac*second_frac*square_root


def BR_h_ss(s_mass):
    return Lambda_h_ss(s_mass) / (Lambda_h_SM + Lambda_h_ss(s_mass))

print("BR(h->ss): ",BR_h_ss(ms),"\n")

def N_evt(s_mass):
    return N_Zh * BR_Z_ll * BR_h_ss(s_mass) * BR_s_bb**2

print("Number of events: ",N_evt(ms),"\n")

def sigma(s_mass, int_Lumi):
    return N_evt(s_mass)/int_Lumi

print("sigma = N_evt / intLumi: ",sigma(ms,integratedLumi))

