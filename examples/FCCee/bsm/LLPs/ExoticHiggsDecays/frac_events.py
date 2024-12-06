import ROOT

samples = ["/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms20GeV_sine-7_240912/chunk_0",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms20GeV_sine-5_240912/chunk_0",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms40GeV_sine-5_240912/chunk_0",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms60GeV_sine-5_240912/chunk_0",
           ]

for sample in samples:
    file_path = f"{sample}.root"
    f = ROOT.TFile(file_path)
    t = f.Get("events")

    events_outside = []
    events_inside = []
    total_events = []
    for e in t:
        for value in e.Reco_seltracks_DVs_Lxyz:
            total_events.append(value)
            if "sine-7" in sample:
                if value > 2000:
                    events_outside.append(value)

    if "sine-7" in sample:
        print(sample[-29:])
        print("----------------------")
        print("Events w. r>2m: ",len(events_outside))
        print("Total events: ", len(total_events))
        print("Fraction: ", 100 * round(len(events_outside)/len(total_events),3),"%")
        print("======================")

    else:   
        print(sample[-29:])
        print("----------------------")
        print("Events w. r<2mm: ",len(events_inside))
        print("Total events: ", len(total_events))
        print("Fraction: ", 100 * round(len(events_inside)/len(total_events),3),"%")
        print("======================")