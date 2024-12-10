import numpy as np

Lumi = 10.8e+06 #in pb-1

events_20gev = np.array([97.459,66.302,18.923])
events_50gev = np.array([130.918,81.830,21.021])
events_60gev = np.array([89.165,55.270,10.772])

events_ZZ = np.array([14677092,1323648])
events_WW = np.array([177535800,1119163])

data_cleaned = {
    "ssH_Hbb": [188460.000, 25.442, 0, 0, 0, 0],
    "ssH_Hcc": [9353.880, 0.031, 0, 0, 0, 0],
    "ssH_Hgg": [26492.400, 0.265, 0, 0, 0, 0],
    "ssH_Hmumu": [70.405, 56.354, 1.046, 0, 0, 0],
    "ssH_Hss": [77.652, 0.001, 0, 0, 0, 0],
    "ssH_Htautau": [20293.200, 784.079, 90.153, 0, 0, 0],
    "bbH_Hbb": [188460.000, 64.076, 0, 0, 0, 0],
    "bbH_Hcc": [9357.120, 2.082, 0, 0, 0, 0],
    "bbH_Hgg": [26503.200, 4.373, 0, 0, 0, 0],
    "bbH_Hmumu": [70.427, 55.689, 1.015, 0, 0, 0],
    "bbH_Hss": [77.684, 0.019, 0, 0, 0, 0],
    "bbH_Htautau": [20304.000, 823.226, 85.987, 0, 0, 0],
    "ccH_Hbb": [146772.000, 20.548, 0, 0, 0, 0],
    "ccH_Hcc": [7286.760, 0.036, 0, 0, 0, 0],
    "ccH_Hmumu": [54.853, 43.974, 0.813, 0, 0, 0],
    "ccH_Hss": [60.556, 0.001, 0, 0, 0, 0],
    "ccH_Htautau": [15811.200, 609.364, 69.767, 0, 0, 0],
    "eeH_Hbb": [45046.800, 29663.768, 28354.258, 5.068, 0, 0],
    "eeH_Hcc": [2235.600, 1507.147, 1443.505, 0.017, 0, 0],
    "eeH_Hgg": [6332.040, 3990.499, 3822.937, 0.032, 0, 0],
    "eeH_Hmumu": [16.826, 14.789, 12.076, 0, 0, 0],
    "eeH_Hss": [18.554, 12.569, 12.030, 0, 0, 0],
    "eeH_Htautau": [4850.280, 2769.922, 2476.771, 0, 0, 0],
    "mumuH_Hbb": [42552.000, 32123.640, 31340.966, 6.383, 0, 0],
    "mumuH_Hcc": [2112.480, 1625.031, 1586.525, 0.042, 0, 0],
    "mumuH_Hgg": [5981.040, 4498.834, 4392.775, 0.120, 0, 0],
    "mumuH_Hmumu": [15.898, 1.131, 0.300, 0, 0, 0],
    "mumuH_Hss": [17.539, 13.569, 13.252, 0, 0, 0],
    "mumuH_Htautau": [4582.440, 2792.379, 2615.897, 0, 0, 0],
    "tautauH_Hbb": [42465.600, 1479.395, 14.863, 0, 0, 0],
    "tautauH_Hcc": [2108.160, 75.188, 0.864, 0, 0, 0],
    "tautauH_Hgg": [5970.240, 184.062, 2.090, 0, 0, 0],
    "tautauH_Hmumu": [15.865, 10.016, 0.217, 0, 0, 0],
    "tautauH_Hss": [17.496, 0.625, 0.007, 0, 0, 0],
    "tautauH_Htautau": [4573.800, 584.497, 28.232, 0, 0, 0],
    "nunuH_Hbb": [290520.000, 41.883, 0, 0, 0, 0],
    "nunuH_Hcc": [14418.000, 0.013, 0, 0, 0, 0],
    "nunuH_Hgg": [40845.600, 1.045, 0, 0, 0, 0],
    "nunuH_Hmumu": [108.540, 99.462, 1.875, 0, 0, 0],
    "nunuH_Hss": [119.772, 0.000, 0, 0, 0, 0],
    "nunuH_Htautau": [31287.600, 1615.587, 167.467, 0, 0, 0],
    "nunuH_Huu": [0.045, 0.000, 0, 0, 0, 0],
}


ZH_dict = {

    'nunuH_Hbb' : {'numberOfEvents': 1200000, 'sumOfWeights': 1200000, 'crossSection': 0.0269, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Hcc' : {'numberOfEvents': 1100000, 'sumOfWeights': 1100000, 'crossSection': 0.001335, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Htautau' : {'numberOfEvents': 1200000, 'sumOfWeights': 1200000, 'crossSection': 0.002897, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Hss' : {'numberOfEvents': 1008052, 'sumOfWeights': 1008052, 'crossSection': 1.109e-05, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Hmumu' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.005e-05, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'bbH_Htautau' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.00188, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_HWW' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001453, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_Hgg' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0005528, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_HZZ' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001891, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_Hmumu' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.558e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ccH_Hgg' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001911, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_Hbb' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.003932, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_Hss' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.624e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_Hcc' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001956, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Hgg' : {'numberOfEvents': 1055845, 'sumOfWeights': 1055845, 'crossSection': 0.003782, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ssH_Htautau' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001879, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'bbH_Hss' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 7.193e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_Hcc' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001952, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ccH_Hss' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 5.607e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ccH_Hcc' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0006747, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_Hmumu' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.469e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'qqH_HWW' : {'numberOfEvents': 1100000, 'sumOfWeights': 1100000, 'crossSection': 0.01148, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_HZZ' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001786, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_Hbb' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 0.00394, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ssH_Hbb' : {'numberOfEvents': 200000, 'sumOfWeights': 200000, 'crossSection': 0.01745, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ccH_Hmumu' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 5.079e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_Htautau' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0004491, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_Hss' : {'numberOfEvents': 352836, 'sumOfWeights': 352836, 'crossSection': 1.718e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_Htautau' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0004243, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_Htautau' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0004235, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_HWW' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001541, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_Hgg' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0005863, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'bbH_Hgg' : {'numberOfEvents': 200000, 'sumOfWeights': 200000, 'crossSection': 0.002454, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ssH_Hgg' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.002453, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'bbH_Hbb' : {'numberOfEvents': 100000, 'sumOfWeights': 100000, 'crossSection': 0.01745, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ccH_Htautau' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001464, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'bbH_Hcc' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0008664, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_Hss' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.62e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ssH_Hss' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 7.19e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ssH_Hcc' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 0.0008661, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'bbH_Hmumu' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 6.521e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_HWW' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001456, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_Hgg' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0005538, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'qqH_HZZ' : {'numberOfEvents': 1200000, 'sumOfWeights': 1200000, 'crossSection': 0.001409, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_Hbb' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.004171, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'tautauH_HZZ' : {'numberOfEvents': 330996, 'sumOfWeights': 330996, 'crossSection': 0.0001783, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ssH_Hmumu' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 6.519e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ccH_Hbb' : {'numberOfEvents': 200000, 'sumOfWeights': 200000, 'crossSection': 0.01359, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'mumuH_Hmumu' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.472e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'eeH_Hcc' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.000207, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Hdd' : {'numberOfEvents': 4979640, 'sumOfWeights': 4979640, 'crossSection': 9.702e-09, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'nunuH_Huu' : {'numberOfEvents': 4900000, 'sumOfWeights': 4900000, 'crossSection': 4.158e-09, 'kfactor': 1.0, 'matchingEfficiency': 1.0},

}


dict = {

    'ms20GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 9.024e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'ms60GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.256e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "ms50GeV_sine-6": {"numberOfEvents":10000, "sumOfWeight": 10000,  "crossSection":  12.122e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'WW' : {'numberOfEvents': 373375386, 'sumOfWeights': 373375386, 'crossSection': 16.4385, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'ZZ' : {'numberOfEvents': 56162093, 'sumOfWeights': 56162093, 'crossSection': 1.35899, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
}

              
def calc_uncert(dictionary,events_value):
    scaling_factor = Lumi * dictionary['crossSection'] * (1/dictionary['numberOfEvents'])
    return np.sqrt(events_value) * scaling_factor


total_uncert = []

for process in ZH_dict.keys(): 
    if process in data_cleaned:
        uncertainty = calc_uncert(ZH_dict[process], np.array(data_cleaned[process]))
        total_uncert.append(uncertainty)


total_uncert = np.array(total_uncert)

comb_uncert = np.sqrt(np.sum(total_uncert**2,axis=0,dtype=float))
print(f'Zh uncert:  [{round(comb_uncert[0],9)}   {round(comb_uncert[2],9)}]')
print('WW uncert: ',calc_uncert(dict['WW'],events_WW))
print('ZZ uncert: ',calc_uncert(dict['ZZ'],events_ZZ))
print('-----------------------------------------')
print('20 GeV uncert: ',calc_uncert(dict['ms20GeV_sine-6'],events_20gev))
print('50 GeV uncert: ',calc_uncert(dict['ms50GeV_sine-6'],events_50gev))
print('60 GeV uncert: ',calc_uncert(dict['ms60GeV_sine-6'],events_60gev))