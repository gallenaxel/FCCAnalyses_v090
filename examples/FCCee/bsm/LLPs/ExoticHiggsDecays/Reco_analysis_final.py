
#Input directory where the files produced at the stage1 level are
#inputDir = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/ZH_ZZ_WW_SIGNAL_FINAL/"
inputDir = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_iso_newLumi_bkg_sig_oct30/stage1/"

#Output directory where the files produced at the final-selection level are #ISR_ForNote_all
#outputDir  = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/Paper_oct2_nTracks_Fix_all/final_binningFix/"
outputDir  = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_iso_newLumi_bkg_sig_dec3_newCrossSec/final/"


# #Integrated luminosity for scaling number of events (required only if setting doScale to true)
intLumi = 10.8e6 #pb^-1

# #Scale event yields by intLumi and cross section (optional)
doScale = True

# # #Save event yields in a table (optional)
saveTabular = True

#Mandatory: List of processes
processList = {

        #'test':{}
        # #privately-produced signals 
        'exoticHiggs_scalar_ms20GeV_sine-5_240912':{},
        'exoticHiggs_scalar_ms20GeV_sine-6_240912':{},
        'exoticHiggs_scalar_ms20GeV_sine-7_240912':{},
        'exoticHiggs_scalar_ms40GeV_sine-5_240912':{},
        'exoticHiggs_scalar_ms40GeV_sine-6_240912':{},
        'exoticHiggs_scalar_ms40GeV_sine-7_240912':{},
        'exoticHiggs_scalar_ms60GeV_sine-5_240912':{},
        'exoticHiggs_scalar_ms60GeV_sine-6_240912':{},
        'exoticHiggs_scalar_ms60GeV_sine-7_240912':{},
        
        "exoticHiggs_scalar_ms20GeV_sin3e-6_241002":{},
        "exoticHiggs_scalar_ms50GeV_sine-6_241002":{},

        "exoticHiggs_scalar_ms50GeV_sin3e-6_241014":{},
        "exoticHiggs_scalar_ms50GeV_sin3e-7_241014":{},
        "exoticHiggs_scalar_ms55GeV_sine-6_241014":{},
        "exoticHiggs_scalar_ms55GeV_sin3e-7_241014":{},

        # #centrally produced backgrounds
        # # ss Backgrounds
        # 'wzp6_ee_ssH_Hbb_ecm240':{},
        # 'wzp6_ee_ssH_Hcc_ecm240':{},
        # 'wzp6_ee_ssH_Hgg_ecm240':{},
        # 'wzp6_ee_ssH_Hmumu_ecm240':{},
        # 'wzp6_ee_ssH_Hss_ecm240':{},
        # 'wzp6_ee_ssH_Htautau_ecm240':{},

        # ## bb Backgrounds
        # 'wzp6_ee_bbH_Hbb_ecm240':{},
        # 'wzp6_ee_bbH_Hcc_ecm240':{},
        # 'wzp6_ee_bbH_Hgg_ecm240':{},
        # 'wzp6_ee_bbH_Hmumu_ecm240':{},
        # 'wzp6_ee_bbH_Hss_ecm240':{},
        # 'wzp6_ee_bbH_Htautau_ecm240':{},
    

        # ## cc Backgrounds
        # 'wzp6_ee_ccH_Hbb_ecm240':{},
        # 'wzp6_ee_ccH_Hcc_ecm240':{},
        # 'wzp6_ee_ccH_Hmumu_ecm240':{},
        # 'wzp6_ee_ccH_Hss_ecm240':{},
        # 'wzp6_ee_ccH_Htautau_ecm240':{},


        # ## ee Backgrounds
        # 'wzp6_ee_eeH_Hbb_ecm240':{},
        # 'wzp6_ee_eeH_Hcc_ecm240':{},
        # 'wzp6_ee_eeH_Hgg_ecm240':{},
        # 'wzp6_ee_eeH_Hmumu_ecm240':{},
        # 'wzp6_ee_eeH_Hss_ecm240':{},
        # 'wzp6_ee_eeH_Htautau_ecm240':{},


        # ## mumu Backgrounds
        # 'wzp6_ee_mumuH_Hbb_ecm240':{},
        # 'wzp6_ee_mumuH_Hcc_ecm240':{},
        # 'wzp6_ee_mumuH_Hgg_ecm240':{},
        # 'wzp6_ee_mumuH_Hmumu_ecm240':{},
        # 'wzp6_ee_mumuH_Hss_ecm240':{},
        # 'wzp6_ee_mumuH_Htautau_ecm240':{},

        # ## tautau Backgrounds
        # 'wzp6_ee_tautauH_Hbb_ecm240':{},
        # 'wzp6_ee_tautauH_Hcc_ecm240':{},
        # 'wzp6_ee_tautauH_Hgg_ecm240':{},
        # 'wzp6_ee_tautauH_Hmumu_ecm240':{},
        # 'wzp6_ee_tautauH_Hss_ecm240':{},
        # 'wzp6_ee_tautauH_Htautau_ecm240':{},

        # ## nunu Backgrounds
        # 'wzp6_ee_nunuH_Hbb_ecm240':{},
        # 'wzp6_ee_nunuH_Hcc_ecm240':{},
        # 'wzp6_ee_nunuH_Hdd_ecm240':{},
        # 'wzp6_ee_nunuH_Hgg_ecm240':{},
        # 'wzp6_ee_nunuH_Hmumu_ecm240':{},
        # 'wzp6_ee_nunuH_Hss_ecm240':{},
        # 'wzp6_ee_nunuH_Htautau_ecm240':{},
        # 'wzp6_ee_nunuH_Huu_ecm240':{},

        # ## ZZ Backgrounds
        # 'wzp6_ee_eeH_HZZ_ecm240':{},
        # 'wzp6_ee_mumuH_HZZ_ecm240':{},
        # 'wzp6_ee_qqH_HZZ_ecm240':{},
        # 'wzp6_ee_tautauH_HZZ_ecm240':{},

        # ## WW Backgrounds
        # 'wzp6_ee_eeH_HWW_ecm240':{},
        # 'wzp6_ee_mumuH_HWW_ecm240':{},
        # 'wzp6_ee_qqH_HWW_ecm240':{},
        # 'wzp6_ee_tautauH_HWW_ecm240':{},

        # ## Other
        # 'p8_ee_WW_ecm240':{},
        # 'p8_ee_ZZ_ecm240':{},

}

# ###Dictionary for prettier names of processes (optional)
processLabels = {
    # #signals
    'exoticHiggs_scalar_ms20GeV_sine-5_240912': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms20GeV_sine-6_240912': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms20GeV_sine-7_240912': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-7}$",
    "exoticHiggs_scalar_ms20GeV_sin3e-6_241002": "$m_S$ = 20 GeV, sin $\theta = 3 * 10^{-6}$",

    'exoticHiggs_scalar_ms40GeV_sine-5_240912': "$m_S$ = 40 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms40GeV_sine-6_240912': "$m_S$ = 40 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms40GeV_sine-7_240912': "$m_S$ = 40 GeV, sin $\theta = 1 * 10^{-7}$",  

    "exoticHiggs_scalar_ms50GeV_sine-6_241002": "$m_S$ = 50 GeV, sin $\theta = 1 * 10^{-6}$",

    'exoticHiggs_scalar_ms60GeV_sine-5_240912': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms60GeV_sine-6_240912': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms60GeV_sine-7_240912': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-7}$",
    
    'exoticHiggs_scalar_ms50GeV_sin3e-6_241014': "$m_S$ = 50 GeV, sin $\theta = 3 * 10^{-6}$",
    'exoticHiggs_scalar_ms50GeV_sin3e-7_241014': "$m_S$ = 50 GeV, sin $\theta = 3 * 10^{-7}$",
    'exoticHiggs_scalar_ms55GeV_sine-6_241014':  "$m_S$ = 55 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms55GeV_sin3e-7_241014': "$m_S$ = 55 GeV, sin $\theta = 3 * 10^{-7}$",
    


    # #backgrounds
    ## ss Backgrounds
    'wzp6_ee_ssH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ssbar) + H(bbar)",
    'wzp6_ee_ssH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ssbar) + H(ccbar)",
    'wzp6_ee_ssH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ssbar) + H(gg)",
    'wzp6_ee_ssH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ssbar) + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_ssH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ssbar) + H(ssbar)",
    'wzp6_ee_ssH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ssbar) + H($\tau^{-}\tau^{+}$)",

    ## bb Backgrounds
    'wzp6_ee_bbH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z(bbar) + H(bbar)",
    'wzp6_ee_bbH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z(bbar) + H(ccbar)",
    'wzp6_ee_bbH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z(bbar) + H(gg)",
    'wzp6_ee_bbH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z(bbar) + + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_bbH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z(bbar) + H(ssbar)",
    'wzp6_ee_bbH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z(bbar) + + H($\tau^{-}\tau^{+}$)",


    ## cc Backgrounds
    'wzp6_ee_ccH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ccbar) + H(bbar)",
    'wzp6_ee_ccH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ccbar) + H(ccbar)",
    'wzp6_ee_ccH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ccbar) + H(gg)",
    'wzp6_ee_ccH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ccbar) + + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_ccH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ccbar) + H(ssbar)",
    'wzp6_ee_ccH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z(ccbar) + + H($\tau^{-}\tau^{+}$)",


    ## ee Backgrounds
    'wzp6_ee_eeH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + H(bbar)",
    'wzp6_ee_eeH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + H(ccbar)",
    'wzp6_ee_eeH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + H(gg)",
    'wzp6_ee_eeH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_eeH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + H(ssbar)",
    'wzp6_ee_eeH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + + H($\tau^{-}\tau^{+}$)",


    ## mumu Backgrounds
    'wzp6_ee_mumuH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + H(bbar)",
    'wzp6_ee_mumuH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + H(ccbar)",
    'wzp6_ee_mumuH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + H(gg)",
    'wzp6_ee_mumuH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_mumuH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + H(ssbar)",
    'wzp6_ee_mumuH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + + H($\tau^{-}\tau^{+}$)",

    ## tautau Backgrounds
    'wzp6_ee_tautauH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + H(bbar)",
    'wzp6_ee_tautauH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + H(ccbar)",
    'wzp6_ee_tautauH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + H(gg)",
    'wzp6_ee_tautauH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_tautauH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + H(ssbar)",
    'wzp6_ee_tautauH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + + H($\tau^{-}\tau^{+}$)",

    ## nunu Backgrounds
    'wzp6_ee_nunuH_Hbb_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H(bbar)",
    'wzp6_ee_nunuH_Hcc_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H(ccbar)",
    'wzp6_ee_nunuH_Hdd_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H(ddbar)",
    'wzp6_ee_nunuH_Hgg_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H(gg)",
    'wzp6_ee_nunuH_Hmumu_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H($\mu^{-}\mu^{+}$)",
    'wzp6_ee_nunuH_Hss_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H(ssbar)",
    'wzp6_ee_nunuH_Htautau_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H($\tau^{-}\tau^{+}$)",
    'wzp6_ee_nunuH_Huu_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\nu^{+}\nu^{-}$) + H(uubar)",

    # ZZ Backgrounds
    'wzp6_ee_eeH_HZZ_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + H(ZZ)",
    'wzp6_ee_mumuH_HZZ_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + H(ZZ)",
    'wzp6_ee_qqH_HZZ_ecm240':"e^{-}e^{+} $\rightarrow$ Z(qqbar) + H(ZZ)",
    'wzp6_ee_tautauH_HZZ_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + H(ZZ)",

    ## WW Backgrounds
    'wzp6_ee_eeH_HWW_ecm240':"e^{-}e^{+} $\rightarrow$ Z(e^{+}e^{-}) + H(WW)",
    'wzp6_ee_mumuH_HWW_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\mu^{+}\mu^{-}$) + H(WW)",
    'wzp6_ee_qqH_HWW_ecm240':"e^{-}e^{+} $\rightarrow$ Z(qqbar) + H(WW)",
    'wzp6_ee_tautauH_HWW_ecm240':"e^{-}e^{+} $\rightarrow$ Z($\tau^{+}\tau^{-}$) + H(WW)",

    ## Other
    'p8_ee_WW_ecm240':"e^{-}e^{+} $\rightarrow$ W^{+}W^{-}",
    'p8_ee_ZZ_ecm240':"e^{-}e^{+} $\rightarrow$ ZZ",

}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

procDictAdd={
   
    'exoticHiggs_scalar_ms20GeV_sine-5_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 9.024e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-6_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 9.024e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-7_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 9.024e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},

    'exoticHiggs_scalar_ms40GeV_sine-5_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 11.327e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms40GeV_sine-6_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 11.327e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms40GeV_sine-7_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 11.327e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},

    'exoticHiggs_scalar_ms60GeV_sine-5_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.256e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-6_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.256e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-7_240912': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.256e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    
    "exoticHiggs_scalar_ms20GeV_sin3e-6_241002": {"numberOfEvents":10000, "sumOfWeight": 10000, "crossSection":  9.024e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "exoticHiggs_scalar_ms50GeV_sine-6_241002": {"numberOfEvents":10000, "sumOfWeight": 10000,  "crossSection":  12.122e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},

    "exoticHiggs_scalar_ms50GeV_sin3e-6_241014": {"numberOfEvents":10000, "sumOfWeight": 10000, "crossSection":  12.122e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "exoticHiggs_scalar_ms50GeV_sin3e-7_241014": {"numberOfEvents":10000, "sumOfWeight": 10000, "crossSection":  12.122e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},

    "exoticHiggs_scalar_ms55GeV_sine-6_241014": {"numberOfEvents":10000, "sumOfWeight": 10000,  "crossSection":  11.500e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "exoticHiggs_scalar_ms55GeV_sin3e-7_241014": {"numberOfEvents":10000, "sumOfWeight": 10000, "crossSection":  11.500e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},



    'wzp6_ee_nunuH_Hbb_ecm240' : {'numberOfEvents': 1200000, 'sumOfWeights': 1200000, 'crossSection': 0.0269, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Hcc_ecm240' : {'numberOfEvents': 1100000, 'sumOfWeights': 1100000, 'crossSection': 0.001335, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Htautau_ecm240' : {'numberOfEvents': 1200000, 'sumOfWeights': 1200000, 'crossSection': 0.002897, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Hss_ecm240' : {'numberOfEvents': 1008052, 'sumOfWeights': 1008052, 'crossSection': 1.109e-05, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'p8_ee_WW_ecm240' : {'numberOfEvents': 373375386, 'sumOfWeights': 373375386, 'crossSection': 16.4385, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'p8_ee_ZZ_ecm240' : {'numberOfEvents': 56162093, 'sumOfWeights': 56162093, 'crossSection': 1.35899, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Hmumu_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.005e-05, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_bbH_Htautau_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.00188, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_HWW_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001453, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_Hgg_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0005528, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_HZZ_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001891, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_Hmumu_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.558e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ccH_Hgg_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001911, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_Hbb_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.003932, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_Hss_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.624e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_Hcc_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001956, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Hgg_ecm240' : {'numberOfEvents': 1055845, 'sumOfWeights': 1055845, 'crossSection': 0.003782, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ssH_Htautau_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001879, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_bbH_Hss_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 7.193e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_Hcc_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001952, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ccH_Hss_ecm240' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 5.607e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ccH_Hcc_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0006747, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_Hmumu_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.469e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_qqH_HWW_ecm240' : {'numberOfEvents': 1100000, 'sumOfWeights': 1100000, 'crossSection': 0.01148, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_HZZ_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0001786, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_Hbb_ecm240' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 0.00394, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ssH_Hbb_ecm240' : {'numberOfEvents': 200000, 'sumOfWeights': 200000, 'crossSection': 0.01745, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ccH_Hmumu_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 5.079e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_Htautau_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0004491, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_Hss_ecm240' : {'numberOfEvents': 352836, 'sumOfWeights': 352836, 'crossSection': 1.718e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_Htautau_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0004243, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_Htautau_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0004235, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_HWW_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001541, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_Hgg_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0005863, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_bbH_Hgg_ecm240' : {'numberOfEvents': 200000, 'sumOfWeights': 200000, 'crossSection': 0.002454, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ssH_Hgg_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.002453, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_bbH_Hbb_ecm240' : {'numberOfEvents': 100000, 'sumOfWeights': 100000, 'crossSection': 0.01745, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ccH_Htautau_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001464, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_bbH_Hcc_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0008664, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_Hss_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.62e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ssH_Hss_ecm240' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 7.19e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ssH_Hcc_ecm240' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 0.0008661, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_bbH_Hmumu_ecm240' : {'numberOfEvents': 300000, 'sumOfWeights': 300000, 'crossSection': 6.521e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_HWW_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.001456, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_Hgg_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.0005538, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_qqH_HZZ_ecm240' : {'numberOfEvents': 1200000, 'sumOfWeights': 1200000, 'crossSection': 0.001409, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_Hbb_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.004171, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_tautauH_HZZ_ecm240' : {'numberOfEvents': 330996, 'sumOfWeights': 330996, 'crossSection': 0.0001783, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ssH_Hmumu_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 6.519e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_ccH_Hbb_ecm240' : {'numberOfEvents': 200000, 'sumOfWeights': 200000, 'crossSection': 0.01359, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_mumuH_Hmumu_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 1.472e-06, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_eeH_Hcc_ecm240' : {'numberOfEvents': 400000, 'sumOfWeights': 400000, 'crossSection': 0.000207, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Hdd_ecm240' : {'numberOfEvents': 4979640, 'sumOfWeights': 4979640, 'crossSection': 9.702e-09, 'kfactor': 1.0, 'matchingEfficiency': 1.0},
    'wzp6_ee_nunuH_Huu_ecm240' : {'numberOfEvents': 4900000, 'sumOfWeights': 4900000, 'crossSection': 4.158e-09, 'kfactor': 1.0, 'matchingEfficiency': 1.0},

}


#Number of CPUs to use
nCPUS = 4

#produces ROOT TTrees, default is False
doTree = False

     

##Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    # For plotting
    "selNone": "n_tracks > -1",

    # For event selection
    "only_exactly_two_leptons": "((n_RecoElectrons >= 2) && (n_electrons_sel_iso == 2) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) || ((n_RecoMuons >= 2) && (n_muons_sel_iso == 2) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1)))",
    "pre-selection" : "(((n_RecoElectrons >= 2) && (n_electrons_sel_iso == 2) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) && (isoReco_ee_invMass > 70 && isoReco_ee_invMass < 110)) || (((n_RecoMuons >= 2) && (n_muons_sel_iso == 2) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) && (isoReco_mumu_invMass > 70 && isoReco_mumu_invMass < 110))",
    "pre-selection+full_DV_sel" : "((((n_RecoElectrons >= 2) && (n_electrons_sel_iso == 2) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) && (isoReco_ee_invMass > 70 && isoReco_ee_invMass < 110)) || (((n_RecoMuons >= 2) && (n_muons_sel_iso == 2) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) && (isoReco_mumu_invMass > 70 && isoReco_mumu_invMass < 110))) && (Sum(n_trks_seltracks_DVs>2&&Reco_seltracks_DVs_Lxyz>4&&Reco_seltracks_DVs_Lxyz<2000&&invMass_seltracks_DVs>2&&DV_evt_seltracks_normchi2<5))>1",


}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    # For plotting
    "selNone": "Before selection",

    # For event selection
    "only_exactly_two_leptons": "Exactly 2 oppositely charged leptons",
    "pre-selection" : "pre-selection",
    "pre-selection+full_DV_sel" : "pre-selection + Full DV-selection",
}

defineList={
   "n_trks_gt2tracks_DVs":"n_trks_seltracks_DVs[n_trks_seltracks_DVs>2]",
    "DV_evt_gt2tracks_normchi2":"DV_evt_seltracks_normchi2[n_trks_seltracks_DVs>2]",
    "invMass_gt2tracks_DVs":"invMass_seltracks_DVs[n_trks_seltracks_DVs>2]",
    "Reco_gt2tracks_DVs_Lxyz":"Reco_seltracks_DVs_Lxyz[n_trks_seltracks_DVs>2]",
    "Reco_gt2tracksgt2GeVmass_DVs_Lxyz":"Reco_seltracks_DVs_Lxyz[n_trks_seltracks_DVs>2&&invMass_seltracks_DVs>2]",
    "n_DV_fullsel":"(Sum(n_trks_seltracks_DVs>2&&Reco_seltracks_DVs_Lxyz>4&&Reco_seltracks_DVs_Lxyz<2000&&invMass_seltracks_DVs>2&&DV_evt_seltracks_normchi2<5))"
}

###Dictionary for the ouput variable/histograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.

histoList = {
    "n_tracks":                             {"name":"n_tracks",                            "title":"Number of reconstructed tracks",                               "bin":100, "xmin":-0.5,"xmax":99.5},
    "n_RecoedPrimaryTracks":                {"name":"n_RecoedPrimaryTracks",               "title": "Number of reconstructed primary tracks",                      "bin":10, "xmin":-0.5,"xmax":9.5},
    "DV_evt_seltracks_chi2":               {"name":"DV_evt_seltracks_chi2",               "title":"The #chi^{2} distribution of the DVs",                         "bin":100, "xmin":-0.5, "xmax":11.5},
    
    'n_seltracks_DVs': {"name":"n_seltracks_DVs",            "title":"Number of DVs",                                                "bin":12, "xmin":-0.5, "xmax":11.5, "ymin":0.001},
    'n_trks_seltracks_DVs': {"name":'n_trks_seltracks_DVs',                "title":"DV track multiplicity",                                "bin":13, "xmin":1.5, "xmax":15},
    'n_trks_2tracks_DVs': {"name":'n_trks_gt2tracks_DVs',                "title":"DV track multiplicity", "bin":13, "xmin":1.5, "xmax":15},
   
    "DV_evt_seltracks_normchi2":           {"name":"DV_evt_seltracks_normchi2",           "title":"DV normalized #chi^{2} distribution",              "bin":45, "xmin":0, "xmax":9},
    "DV_evt_gt2tracks_normchi2":           {"name":"DV_evt_gt2tracks_normchi2",           "title":"DV normalized #chi^{2} distribution",              "bin":45, "xmin":0, "xmax":9},

    'invMass_seltracks_DVs':                {"name":'invMass_seltracks_DVs',               "title":"Invariant mass at the DVs [GeV]",                              "bin":30, "xmin":0, "xmax":15},
    'invMass_gt2tracks_DVs':                {"name":'invMass_gt2tracks_DVs',               "title":"Invariant mass at the DVs [GeV]",                              "bin":30, "xmin":0, "xmax":15},

    'invMass_seltracks_DVs_zoom':                {"name":'invMass_seltracks_DVs',               "title":"Invariant mass at the DVs [GeV]",                              "bin":40, "xmin":0, "xmax":5},

    "Reco_seltracks_DVs_Lxyz_02000":     {"name":"Reco_seltracks_DVs_Lxyz",    "title":"DV radius [mm]",                             "bin":50, "xmin":0, "xmax":2000, "ymin":0.001},
    "Reco_gt2tracks_DVs_Lxyz_02000":     {"name":"Reco_gt2tracks_DVs_Lxyz",    "title":"DV radius [mm]",                             "bin":50, "xmin":0, "xmax":2000, "ymin":0.001},
    "Reco_gt2tracksgt2GeVmass_DVs_Lxyz": {"name":"Reco_gt2tracksgt2GeVmass_DVs_Lxyz",    "title":"DV radius [mm]",                             "bin":25, "xmin":0, "xmax":2000, "ymin":0.001},
    "Reco_gt2tracksgt2GeVmass_DVs_Lxyz_zoom": {"name":"Reco_gt2tracksgt2GeVmass_DVs_Lxyz",    "title":"DV radius [mm]",                             "bin":25, "xmin":0, "xmax":200, "ymin":0.001},


    "Reco_seltracks_DVs_Lxyz_zoom":     {"name":"Reco_seltracks_DVs_Lxyz","title":"DV radius [mm]",                             "bin":30, "xmin":0, "xmax":100, "ymin":0.001},

    "n_DV_fullsel" : {"name":"n_DV_fullsel", "title":"Number of DVs",                                                "bin":15, "xmin":-0.5, "xmax":14.5, "ymin":0.001},

    'n_RecoElectrons':                      {"name":'n_RecoElectrons',                     "title": "Number of reco. electrons",                           "bin":10,"xmin":-0.5,"xmax":9.5},
    'n_RecoMuons':                          {"name":'n_RecoMuons',                         "title": "Number of reco. muons",                               "bin":10,"xmin":-0.5,"xmax":9.5},
    
    'n_electrons_sel_iso':                  {"name":'n_electrons_sel_iso',                 "title": "Number of reco. iso. electrons",                                "bin":10,"xmin":-0.5,"xmax":9.5},    
    'n_muons_sel_iso':                      {"name":'n_muons_sel_iso',                     "title": "Number of reco. iso. muons",                                    "bin":10,"xmin":-0.5,"xmax":9.5},

    "isoReco_ee_invMass":                      {"name":"isoReco_ee_invMass",                     "title": "Invariant mass of reco. iso. e^{-} e^{+} [GeV]",                 "bin":50,"xmin":50,"xmax":150},
    "isoReco_mumu_invMass":                    {"name":"isoReco_mumu_invMass",                   "title": "Invariant mass of reco. iso. #mu^{-} #mu^{+} [GeV]",             "bin":50,"xmin":50,"xmax":150},    

}