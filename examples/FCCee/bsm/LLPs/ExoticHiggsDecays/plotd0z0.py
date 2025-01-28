import ROOT
from math import sqrt

samples=["R04/wzp6_ee_eeH_HZZ_ecm240","R04/exoticHiggs_scalar_ms20GeV_sine-6","R04/exoticHiggs_scalar_ms60GeV_sine-5"]
# sample="exoticHiggs_scalar_ms20GeV_sine-5"
print(ROOT.gROOT.GetVersion())
for sample in samples:
    f=ROOT.TFile("%s.root"%sample)
    t=f.Get("events")
    #t.Show(0)

    # jet_count = []
    # for e in t:
    #     jets_pt_list = list(e.jets_pt)
    #     filtered_jets = [pt for pt in jets_pt_list if pt >= 1]
    #     jet_count.append(len(filtered_jets))


    hist_ = ROOT.TH1F("Track_d0_njetCut", " Title", 100,0,2500)
    for index,e in enumerate(t):
        if e.jets_nJets < 7:
            for index2,track in enumerate(e.has_track):
                if track==True:
                    hist_.Fill(e.track_d0[index2])

    c = ROOT.TCanvas("c", "c", 800, 600)
    hist_.GetXaxis().SetTitle("|d_{0}| [mm]")
    hist_.GetYaxis().SetTitle("Norm # of tracks")
    drawopt ="hist"
    hist_.Scale(1/hist_.Integral())
    hist_.Draw()
    c.SetLogy()    
    c.SaveAs("tracks_njetCut_%s.pdf"%sample[-6:])

        #for index in range(0,len(e.has_track)):
            #print(index)
            # if e.jets_nJets < 7:
            # print(f"Event nr:{index} has {e.jets_nJets} jets")
    # hist = ROOT.TH1F("jet_count_hist", "Number of Jets After Removal", 20, 0, 20)

    # for count in jet_count:
    #     hist.Fill(count)

    # c = ROOT.TCanvas("c", "c", 800, 600)
    # hist.GetXaxis().SetTitle("Number of Jets")
    # hist.GetYaxis().SetTitle("Counts")
    # hist.Draw()
    # c.SetLogy()
    # c.SaveAs("custom_njets_cut_1GeV_%s.pdf"%sample[-6:])
    
    #print(e.RP_MC_index)
    #print(e.RP_Track)
    #print(e.track_d0)
# #     # print(e.truth_prod_x)
#     print(e.has_track)
    # print("------------------------------")
    # for rp_ind in range(0,len(e.has_track)):
    #     d0=e.track_d0[rp_ind]
    #     z0=e.track_z0[rp_ind]
    #     if abs(d0)>500:
    #         mc_ind=e.RP_MC_index[rp_ind]
    #         charge=e.truth_charge[mc_ind]
    #         if charge==0: print("NOT CHARGED")
    #         mom=e.truth_p[mc_ind]
    #         prod_x=e.truth_prod_x[mc_ind]
    #         prod_y=e.truth_prod_y[mc_ind]
    #         prod_z=e.truth_prod_z[mc_ind]
    #         prod_r=sqrt(prod_x*prod_x+prod_y*prod_y)
    #         genstatus=e.truth_genStatus[mc_ind]
    #         simstatus=e.truth_simStatus[mc_ind]
    #         pdg=e.truth_pdg[mc_ind]
    #         print(f"Track: d0 = {abs(d0):.2f}, z0 = {abs(z0):.2f} |  Truth production: rxy = {prod_r:.2f}, z = {abs(prod_z):.2f} | Truth momentum: p = {mom:.2f} | Truth data: genstatus = {genstatus}, simstatus = {simstatus}, pdg = {pdg}")

# for e in t:
#     print("------------------------------")
#     for mc_ind in range(0,len(e.truth_prod_x)):
#         charge=e.truth_charge[mc_ind]
#         if charge==0: continue
#         mom=e.truth_p[mc_ind]
#         prod_x=e.truth_prod_x[mc_ind]
#         prod_y=e.truth_prod_y[mc_ind]
#         prod_z=e.truth_prod_z[mc_ind]
#         prod_r=sqrt(prod_x*prod_x+prod_y*prod_y)
#         genstatus=e.truth_genStatus[mc_ind]
#         simstatus=e.truth_simStatus[mc_ind]
#         pdg=e.truth_pdg[mc_ind]
#         # if prod_r>500:
#         print(f"Truth production: rxy = {prod_r:.2f}, z = {abs(prod_z):.2f} | Truth p = {mom:.2f} | Truth data: genstatus = {genstatus}, simstatus = {simstatus}, pdg = {pdg}")




# c=ROOT.TCanvas("c","c",800,600)
# c.SetLogy()

# t.Draw("track_p>>h(100,0,100)","has_track")
# c.SaveAs("plots/%s/track_p.png"%sample)
# t.Draw("abs(track_d0)>>h(100,0,2500)","has_track")
# c.SaveAs("plots/%s/track_d0.png"%sample)
# t.Draw("abs(track_z0)>>h(100,0,2500)","has_track")
# c.SaveAs("plots/%s/track_z0.png"%sample)
# # t.Draw("track_d0cov>>h(100,0,2500)","abs(track_d0)>2")
# t.Draw("track_d0cov>>h(100,0,2500)","has_track")
# c.SaveAs("plots/%s/track_d0cov.png"%sample)
# t.Draw("track_z0cov>>h(100,0,2500)","has_track")
# c.SaveAs("plots/%s/track_z0cov.png"%sample)
# # t.Draw("track_d0sig>>h(100,0,2500)","abs(track_d0)>2")
# t.Draw("track_d0sig>>h(100,0,2500)","has_track")
# c.SaveAs("plots/%s/track_d0sig.png"%sample)
# t.Draw("track_z0sig>>h(100,0,2500)","has_track")
# c.SaveAs("plots/%s/track_z0sig.png"%sample)

# t.Draw("abs(truth_prod_x)>>h(100,0,2500)","truth_charge!=0")
# c.SaveAs("plots/%s/truth_prod_x.png"%sample)
# t.Draw("abs(truth_prod_y)>>h(100,0,2500)","truth_charge!=0")
# c.SaveAs("plots/%s/truth_prod_y.png"%sample)
# t.Draw("abs(truth_prod_z)>>h(100,0,2500)","truth_charge!=0")
# c.SaveAs("plots/%s/truth_prod_z.png"%sample)

# t.Draw("sqrt(truth_prod_x*truth_prod_x+truth_prod_y*truth_prod_y)>>h(100,0,2500)","truth_charge!=0")
# c.SaveAs("plots/%s/truth_prod_r.png"%sample)
# t.Draw("sqrt(truth_prod_x*truth_prod_x+truth_prod_y*truth_prod_y)>>h(100,0,2500)","truth_charge!=0")
# c.SaveAs("plots/%s/truth_prod_r.png"%sample)

# c.SetLogy(0)
# c.SetLogz(1)
# t.Draw("track_p:abs(track_d0)>>h(100,0,2500,100,0,100)","has_track","colz")
# c.SaveAs("plots/%s/track_d0vsp.pdf"%sample)

# c.SetLogy(0)
# c.SetLogz(1)
# t.Draw("truth_p:sqrt(truth_prod_x*truth_prod_x+truth_prod_y*truth_prod_y)>>h(100,0,2500,100,0,100)","truth_charge!=0","colz")
# c.SaveAs("plots/%s/truth_rvsp.pdf"%sample)




