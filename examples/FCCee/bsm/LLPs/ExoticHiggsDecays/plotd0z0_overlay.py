import ROOT
from math import sqrt
import AtlasStyle

#sampleList =["wzp6_ee_eeH_HZZ_ecm240.root","exoticHiggs_scalar_ms60GeV_sine-7","exoticHiggs_scalar_ms60GeV_sine-6","exoticHiggs_scalar_ms60GeV_sine-5",
#            "exoticHiggs_scalar_ms20GeV_sine-7","exoticHiggs_scalar_ms20GeV_sine-6","exoticHiggs_scalar_ms20GeV_sine-5"]

sampleList = ["wzp6_ee_eeH_HZZ_ecm240","exoticHiggs_scalar_ms20GeV_sine-6","exoticHiggs_scalar_ms60GeV_sine-7"]

folder_prefix = "R04"

histos={}

for sample in sampleList:
    histos[sample]={}

    f=ROOT.TFile(folder_prefix+"/%s.root"%sample)
    t=f.Get("events")

    ROOT.gROOT.SetBatch(True)
    t.Draw("jets_e>>jetE%s(100,0,140)"%sample)
    histos[sample]["jets_e"]=ROOT.gROOT.FindObject("jetE%s"%sample)
    histos[sample]["jets_e"].SetDirectory(0)
    histos[sample]["jets_e"].SetTitle("jets_e;Jet Energy [GeV];Normalized number of Jets")

    t.Draw("jets_pt>>jetPt%s(100,0,140)"%sample)
    histos[sample]["jets_pt"]=ROOT.gROOT.FindObject("jetPt%s"%sample)
    histos[sample]["jets_pt"].SetDirectory(0)
    histos[sample]["jets_pt"].SetTitle("jets_pt;Jet p_{T} [GeV];Normalized number of Jets")

    t.Draw("jets_eta>>jetEta%s(100,-5,5)"%sample)
    histos[sample]["jets_eta"]=ROOT.gROOT.FindObject("jetEta%s"%sample)
    histos[sample]["jets_eta"].SetDirectory(0)
    histos[sample]["jets_eta"].SetTitle("jets_eta;Jet \eta ;Normalized number of Jets")

    t.Draw("jets_nJets>>nJets%s(21,-1,20)"%sample)
    histos[sample]["jets_nJets"]=ROOT.gROOT.FindObject("nJets%s"%sample)
    histos[sample]["jets_nJets"].SetDirectory(0)
    histos[sample]["jets_nJets"].SetTitle("jets_nJets; Number of Jets ; Counts")

    t.Draw("Sum$(jets_pt>20)>>nJets2%s(21,-1,20)"%sample)
    histos[sample]["Sum$(jets_pt>20)"]=ROOT.gROOT.FindObject("nJets2%s"%sample)
    histos[sample]["Sum$(jets_pt>20)"].SetDirectory(0)
    histos[sample]["Sum$(jets_pt>20)"].SetTitle("Sum$(jets_pt>20); Number of Jets ; Counts")

    t.Draw("track_p>>hp%s(100,0,100)"%sample,"has_track")
    histos[sample]["track_p"]=ROOT.gROOT.FindObject("hp%s"%sample)
    histos[sample]["track_p"].SetDirectory(0)
    histos[sample]["track_p"].SetTitle("track_p;p [GeV];Normalized number of tracks")

    t.Draw("abs(track_d0)>>hd0%s(100,0,2500)"%sample,"has_track&&track_p>10")
    histos[sample]["track_d0"]=ROOT.gROOT.FindObject("hd0%s"%sample)
    histos[sample]["track_d0"].SetDirectory(0)
    histos[sample]["track_d0"].SetTitle("track_d_0;|d_{0}| [mm];Normalized number of tracks")

    t.Draw("abs(track_z0)>>hz0%s(100,0,2500)"%sample,"has_track&&track_p>10")
    histos[sample]["track_z0"]=ROOT.gROOT.FindObject("hz0%s"%sample)
    histos[sample]["track_z0"].SetDirectory(0)
    histos[sample]["track_z0"].SetTitle("track_z0;|z_{0}| [mm];Normalized number of tracks")

    t.Draw("track_d0cov>>hd0cov%s(100,0,2500)"%sample,"has_track&&track_p>10")
    histos[sample]["track_d0cov"]=ROOT.gROOT.FindObject("hd0cov%s"%sample)
    histos[sample]["track_d0cov"].SetDirectory(0)
    histos[sample]["track_d0cov"].SetTitle("track_d0cov;#sigma_{d_{0}}^{2} [mm^{2}];Normalized number of tracks")

    t.Draw("track_z0cov>>hz0cov%s(100,0,2500)"%sample,"has_track&&track_p>10")
    histos[sample]["track_z0cov"]=ROOT.gROOT.FindObject("hz0cov%s"%sample)
    histos[sample]["track_z0cov"].SetDirectory(0)
    histos[sample]["track_z0cov"].SetTitle("track_z0cov;#sigma_{z_{0}}^{2} [mm^{2}];Normalized number of tracks")

    t.Draw("track_d0sig>>hd0sig%s(100,0,100)"%sample,"has_track")
    histos[sample]["track_d0sig"]=ROOT.gROOT.FindObject("hd0sig%s"%sample)
    histos[sample]["track_d0sig"].SetDirectory(0)
    histos[sample]["track_d0sig"].SetTitle("track_d0sig;|d_{0}|/#sigma_{d_{0}};Normalized number of tracks")

    t.Draw("track_z0sig>>hz0sig%s(100,0,100)"%sample,"has_track&&track_p>10")
    histos[sample]["track_z0sig"]=ROOT.gROOT.FindObject("hz0sig%s"%sample)
    histos[sample]["track_z0sig"].SetDirectory(0)
    histos[sample]["track_z0sig"].SetTitle("track_z0sig;|z_{0}|/#sigma_{z_{0}};Normalized number of tracks")

    t.Draw("abs(truth_prod_z)>>hprodz%s(100,0,2500)"%sample,"truth_charge!=0&&truth_p>10")
    histos[sample]["prod_z"]=ROOT.gROOT.FindObject("hprodz%s"%sample)
    histos[sample]["prod_z"].SetDirectory(0)
    histos[sample]["prod_z"].SetTitle("prod_z;MC particle production |z| [mm];Normalized number of particles")


    t.Draw("sqrt(truth_prod_x*truth_prod_x+truth_prod_y*truth_prod_y)>>hprodr%s(100,0,2500)"%sample,"truth_charge!=0&&truth_p>10")
    histos[sample]["prod_r"]=ROOT.gROOT.FindObject("hprodr%s"%sample)
    histos[sample]["prod_r"].SetDirectory(0)
    histos[sample]["prod_r"].SetTitle("prod_z;MC particle production R_{xy} [mm];Normalized number of particles")

c=ROOT.TCanvas("c","c",800,600)
c.SetLogy()

legend = ROOT.TLegend(0.4,0.7,0.81,0.9)
legend.SetFillStyle(0)
legend.SetLineStyle(0)
legend.SetBorderSize(0)
legend.SetTextSize(0.035)
legend.SetTextFont(42)

for plot in ["jets_e","jets_pt","jets_eta","jets_nJets","Sum$(jets_pt>20)"]:#["track_p","track_d0","track_z0","track_d0sig","track_z0sig","track_d0cov","track_z0cov","prod_z","prod_r"]:
    drawopt="hist"
    colorind=1
    legend.Clear()
    for sample in sampleList:
        histos[sample][plot].SetLineColor(colorind)
        histos[sample][plot].Scale(1/histos[sample][plot].Integral())
        histos[sample][plot].GetYaxis().SetRangeUser(1e-6,10)
        histos[sample][plot].Draw(drawopt)
        drawopt="hist same"
        colorind+=1
        legend.AddEntry(histos[sample][plot],sample,"l")
    legend.Draw()
    c.SaveAs(folder_prefix+"/pt1/%s.pdf"%plot)



# c.SetLogy(0)
# c.SetLogz(1)
# t.Draw("track_p:abs(track_d0)>>h(100,0,2500,100,0,100)","has_track","colz")
# c.SaveAs("plots/%s/track_d0vsp.png"%sample)

# t.Draw("track_p:abs(track_d0)>>h(100,0,2500,100,0,10)","has_track","colz")
# c.SaveAs("plots/%s/track_d0vsp_zoom.png"%sample)

# c.SetLogx(1)
# c.SetLogy(1)
# c.SetLogz(1)
# t.Draw("track_p:abs(track_d0)>>h(1000,0.1,10000,1000,0.1,100)","has_track","colz")
# h=ROOT.gROOT.FindObject("h")
# h.GetYaxis().SetRangeUser(0.5,100)
# h.GetXaxis().SetRangeUser(0.5,2500)
# h.Draw("colz")
# c.SaveAs("plots/%s/track_d0vsp_log.png"%sample)
