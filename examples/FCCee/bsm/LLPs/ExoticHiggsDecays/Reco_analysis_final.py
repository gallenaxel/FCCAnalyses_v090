
#Input directory where the files produced at the stage1 level are
inputDir = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/ZH_ZZ_WW_FINAL/"

#Output directory where the files produced at the final-selection level are
outputDir  = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/poster_backgrounds/poster_final_binning/"


# #Integrated luminosity for scaling number of events (required only if setting doScale to true)
intLumi = 7.2e6 #pb^-1

# #Scale event yields by intLumi and cross section (optional)
doScale = True

# # #Save event yields in a table (optional)
saveTabular = True

#Mandatory: List of processes
processList = {

        #'test':{}
        #privately-produced signals 
        # 'exoticHiggs_scalar_ms20GeV_sine-5':{},
        # 'exoticHiggs_scalar_ms20GeV_sine-6':{},
        # 'exoticHiggs_scalar_ms20GeV_sine-7':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-5':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-6':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-7':{},

        # #centrally produced backgrounds
        # ## ss Backgrounds
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
        # 'wzp6_ee_ccH_Hgg_ecm240':{},
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

        # # ## Other
        # 'p8_ee_WW_ecm240':{},
        # 'p8_ee_ZZ_ecm240':{},

}

###Dictionary for prettier names of processes (optional)
processLabels = {
    # #signals
    'exoticHiggs_scalar_ms20GeV_sine-5': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms20GeV_sine-6': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms20GeV_sine-7': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-7}$",
    'exoticHiggs_scalar_ms60GeV_sine-5': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms60GeV_sine-6': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms60GeV_sine-7': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-7}$",

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
   
    'exoticHiggs_scalar_ms20GeV_sine-5': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.858e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.858e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-7': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.858e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-5': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.618e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.618e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-7': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.618e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},

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
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    # For plotting
    "selNone": "n_tracks > -1",

    # For event selection
    "preSel": "((n_RecoElectrons >= 2) && (n_electrons_sel_iso == 2) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) || ((n_RecoMuons >= 2) && (n_muons_sel_iso == 2) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1)))",

    "selZ": "(Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)",                   
    "selZ+nDVs_seltracks": "((Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)) && n_seltracks_fullVertexSel_DVs >= 1",
    "selZ+nDVs_seltracks+LxyzCut": "((Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)) && n_seltracks_fullVertexSel_DVs >= 1 && Reco_seltracks_trackCut_DVs_Lxyz.at(0) > 50",
    #"selZ+nDVs_merge": "((Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)) && n_merged_fullVertexSel_DVs >= 1",
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    # For plotting
    "selNone": "Before selection",

    # For event selection
    "preSel": "Exactly 2 oppositely charged leptons",
    "selZ": "70 < $m_{ll}$ < 110 GeV",
    "selZ+nDVs_seltracks": "n DVs $\geq$ 2",
    "selZ+nDVs_seltracks+LxyzCut" : "r$_{PV-DV} > 50$"
    #"selZ+nDVs_merge": "n DVs $\geq$ 2 (merged)",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.

histoList = {
    "n_tracks":                             {"name":"n_tracks",                            "title":"Number of reconstructed tracks",                               "bin":100, "xmin":-0.5,"xmax":99.5},
    "n_RecoedPrimaryTracks":                {"name":"n_RecoedPrimaryTracks",               "title": "Number of reconstructed primary tracks",                      "bin":10, "xmin":-0.5,"xmax":9.5},
    'n_seltracks_trackCut_DVs':             {"name":"n_seltracks_trackCut_DVs",            "title":"Number of DVs",                                                "bin":12, "xmin":-0.5, "xmax":11.5, "ymin":0.001},
    'n_trks_seltracks_DVs':                 {"name":'n_trks_seltracks_DVs',                "title":"Number of tracks from the DVs",                                "bin":30, "xmin":1.5, "xmax":29.5},
    'invMass_seltracks_DVs':                {"name":'invMass_seltracks_DVs',               "title":"Invariant mass at the DVs [GeV]",                              "bin":40, "xmin":-0.5, "xmax":39.5},
    #"DV_evt_seltracks_chi2":               {"name":"DV_evt_seltracks_chi2",               "title":"The #chi^{2} distribution of the DVs",                         "bin":100, "xmin":-0.5, "xmax":11.5},
    "Reco_seltracks_DVs_Lxy":               {"name":"Reco_seltracks_DVs_Lxy",              "title":"Transverse distance between PV and DVs [mm]",                  "bin":50, "xmin":0, "xmax":2000},
    "Reco_seltracks_trackCut_DVs_Lxyz":     {"name":"Reco_seltracks_trackCut_DVs_Lxyz",    "title":"Distance between PV and DVs [mm]",                             "bin":30, "xmin":0, "xmax":2000, "ymin":0.001, "ytitle":"DVs"},
    #"DV_evt_seltracks_normchi2":           {"name":"DV_evt_seltracks_normchi2",           "title":"The normalised #chi^{2} distribution of the DVs",              "bin":40, "xmin":0, "xmax":10},
    "n_merged_DVs":                         {"name":"n_merged_DVs",                        "title":"Number of DVs",                                                "bin":10, "xmin":-0.5, "xmax":9.5},
    'n_trks_merged_DVs':                    {"name":'n_trks_merged_DVs',                   "title":"Number of tracks from the DVs from sel tracks + merge",        "bin":30, "xmin":1.5, "xmax":29.5},

    'invMass_merged_DVs':                   {"name":'invMass_merged_DVs',                  "title":"Invariant mass at the DVs [GeV]",                              "bin":40, "xmin":-0.5, "xmax":39.5},
    #"merged_DVs_chi2":                     {"name":"merged_DVs_chi2",                     "title":"The #chi^{2} distribution of the merged DVs",                  "bin":100, "xmin":-0.5, "xmax":11.5},
    #"merged_DVs_normchi2":                 {"name":"merged_DVs_normchi2",                 "title":"The normalised #chi^{2} distribution of the merged DVs",       "bin":40, "xmin":0, "xmax":10},
    "Reco_DVs_merged_Lxy":                  {"name":"Reco_DVs_merged_Lxy",                 "title":"Transverse distance between PV and DVs [mm]",                  "bin":50, "xmin":0, "xmax":2000},
    "Reco_DVs_merged_Lxyz":                 {"name":"Reco_DVs_merged_Lxyz",                "title":"Distance between PV and DVs [mm]",                             "bin":50, "xmin":0, "xmax":2000},

    'n_RecoElectrons':                      {"name":'n_RecoElectrons',                     "title": "Number of reconstructed electrons",                           "bin":10,"xmin":-0.5,"xmax":9.5},
    'n_electrons_sel_iso':                  {"name":'n_electrons_sel_iso',                 "title": "Number of isolated electrons",                                "bin":10,"xmin":-0.5,"xmax":9.5},
    "Reco_ee_invMass":                      {"name":"Reco_ee_invMass",                     "title": "Invariant mass of reconstructed e- e+ [GeV]",                 "bin":30,"xmin":50,"xmax":150, "ymin":0.001},
    'n_RecoMuons':                          {"name":'n_RecoMuons',                         "title": "Number of reconstructed muons",                               "bin":10,"xmin":-0.5,"xmax":9.5},
    'n_muons_sel_iso':                      {"name":'n_muons_sel_iso',                     "title": "Number of isolated muons",                                    "bin":10,"xmin":-0.5,"xmax":9.5},
    "Reco_mumu_invMass":                    {"name":"Reco_mumu_invMass",                   "title": "Invariant mass of reconstructed #mu- #mu+ [GeV]",             "bin":100,"xmin":50,"xmax":150, "ymin":0.001},    

}