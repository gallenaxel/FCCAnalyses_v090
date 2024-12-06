import ROOT

samples = ["/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms20GeV_sine-7_240912/chunk_0",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms20GeV_sine-5_240912/chunk_0",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms40GeV_sine-5_240912/chunk_0",
           "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/FINAL_comb/stage1/exoticHiggs_scalar_ms60GeV_sine-5_240912/chunk_0",
           ]

nbins = 1000
xmin = 0
xmax = 2000

for sample in samples:
    file_path = f"{sample}.root"
    f = ROOT.TFile(file_path)
    t = f.Get("events")

    hist = ROOT.TH1F("Reco_seltracks_DVs_Lxyz", "Histogram of Reco_seltracks_DVs_Lxyz", nbins, xmin, xmax)

    for e in t:
        for value in e.Reco_seltracks_DVs_Lxyz:
            hist.Fill(value)

    # Get the first bin details
    first_bin_content = hist.GetBinContent(1)
    first_bin_low_edge = hist.GetBinLowEdge(1)
    first_bin_high_edge = hist.GetBinLowEdge(2)


    print(f"Sample: {sample}")
    print(f"First bin range: [{first_bin_low_edge}, {first_bin_high_edge}) and this bin contains {first_bin_content} events")
    print(f"Total entries in [0,2000]: {hist.GetEntries()}")
    print("======================")
