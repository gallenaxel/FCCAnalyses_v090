import ROOT

samples = ["/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms20GeV_sine-5_240912",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms20GeV_sine-6_240912",
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms20GeV_sine-7_240912",
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms20GeV_sin3e-6_241002",

            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms40GeV_sine-5_240912",
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms40GeV_sine-6_240912",
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms40GeV_sine-7_240912",

            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms50GeV_sine-6_241002",            
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms50GeV_sin3e-6_241014",            
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms50GeV_sin3e-7_241014",            

            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms60GeV_sine-5_240912",
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms60GeV_sine-6_240912",
            "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/stage1/exoticHiggs_scalar_ms60GeV_sine-7_240912",

           ]

for sample in samples:
    file_path = f"{sample}.root"
    f = ROOT.TFile(file_path)
    t = f.Get("events")
    
    # if "sine-5" in sample:
    #     print(sample)
    #     print('Total: ',t.GetEntries('LxyHS'))
    #     print('Less than 2: ',t.GetEntries('LxyHS<2'))
    #     print("Fraction: ", 100 * round(t.GetEntries('LxyHS<2')/t.GetEntries('LxyHS'),3),"%")
    # elif "sine-7" in sample:
    #     print(sample)
    #     print('Total: ',t.GetEntries('LxyHS'))
    #     print('Greater than 2000: ',t.GetEntries('LxyHS>2000'))
    #     print("Fraction: ", 100 * round(t.GetEntries('LxyHS>2000')/t.GetEntries('LxyHS'),3),"%")     
    #elif "sin3e-7" in sample:
    print(sample[101:])
    print('Total: ',t.GetEntries('LxyHS'))
    print('in [2,2000]: ',t.GetEntries('LxyHS>2&&LxyHS<2000'))
    print("Fraction: ", 100 * round(t.GetEntries('LxyHS>2&&LxyHS<2000')/t.GetEntries('LxyHS'),3),"%")
    print('----------------------')
