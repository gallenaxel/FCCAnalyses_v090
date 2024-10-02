import ROOT

# global parameters
intLumi        = 7.2e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'e^{+}e^{-} #rightarrow Z H, Z #rightarrow l^{\pm}l^{\mp}, H #rightarrow ss #rightarrow 4b'
delphesVersion = '3.4.2'
energy         = 240
collider       = 'FCC-ee'
inputDir       = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/Paper_oct2_nTracks_Fix_all/final/'
formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']#,'stack']
#stackbkg       = ['nostack']
outdir         = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/Paper_oct2_nTracks_Fix_all/plots/'
splitLeg       = False

variables = [

    #gen variables
#    "n_tracks",
#    "n_RecoedPrimaryTracks",
    "n_seltracks_DVs",
    'n_trks_seltracks_DVs',
    'n_trks_2tracks_DVs',

    "DV_evt_seltracks_normchi2",
    "DV_evt_gt2tracks_normchi2",

    'invMass_seltracks_DVs',
    'invMass_gt2tracks_DVs',

    "Reco_seltracks_DVs_Lxyz_02000",
    "Reco_gt2tracks_DVs_Lxyz_02000",

    # "invMass_seltracks_DVs_zoom",

    # "Reco_seltracks_DVs_Lxyz_01800",
    # "Reco_seltracks_DVs_Lxyz_zoom",

    # "Reco_ee_invMass",
    # "Reco_mumu_invMass",

    # 'n_RecoElectrons',
    # 'n_RecoMuons',

    # "n_electrons_sel_iso",
    # "n_muons_sel_iso",

    #"Reco_seltracks_DVs_Lxy",
    #"Reco_seltracks_trackCut_DVs_Lxyz",
    #"Reco_seltracks_trackCut_DVs_Lxyz_zoom",
    #"n_seltracks_fullVertexSel_DVs",
    #"n_trks_seltracks_fullVertexSel_DVs",
    #"invMass_seltracks_fullVertexSel_DVs",
    #"DV_evt_seltracks_fullVertexSel_normchi2",
    #"Reco_seltracks_fullVertexSel_DVs_Lxyz",
    # "n_merged_DVs",
    # 'n_trks_merged_DVs',
    # 'invMass_merged_DVs',
    # "merged_DVs_chi2",
    # "merged_DVs_normchi2",
    # "Reco_DVs_merged_Lxy",
    # "Reco_DVs_merged_Lxyz",

             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['ExoticHiggs']  = [
    "selNone",
    "only_exactly_two_leptons",
    "pre-selection",
    "pre-selection+full_DV_sel",
    "pre-selection_nTracks",
]

extralabel = {}
extralabel['selNone'] = "No selection"
extralabel['only_exactly_two_leptons'] = "Two Leptons"
extralabel['pre-selection'] = "Pre-selection"
extralabel['pre-selection+full_DV_sel'] = "Pre-selection + Full DV selection"
extralabel["pre-selection_nTracks"] = "Pre-selection + ntrks > 2"

linestyle = {}

## Signal

linestyle['exoticHiggs_scalar_ms20GeV_sine-5_240912'] = 1
linestyle['exoticHiggs_scalar_ms20GeV_sine-6_240912'] = 1
linestyle['exoticHiggs_scalar_ms20GeV_sine-7_240912'] = 1
linestyle['exoticHiggs_scalar_ms60GeV_sine-5_240912'] = 2
linestyle['exoticHiggs_scalar_ms60GeV_sine-6_240912'] = 2
linestyle['exoticHiggs_scalar_ms60GeV_sine-7_240912'] = 2

colors = {}

## Signal

colors['exoticHiggs_scalar_ms20GeV_sine-5_240912'] = ROOT.kCyan+2
colors['exoticHiggs_scalar_ms20GeV_sine-6_240912'] = ROOT.kMagenta-6
colors['exoticHiggs_scalar_ms20GeV_sine-7_240912'] = ROOT.kCyan-6

colors['exoticHiggs_scalar_ms40GeV_sine-5_240912'] = ROOT.kCyan-5
colors['exoticHiggs_scalar_ms40GeV_sine-6_240912'] = ROOT.kMagenta-10
colors['exoticHiggs_scalar_ms40GeV_sine-7_240912'] = ROOT.kCyan-10

colors['exoticHiggs_scalar_ms60GeV_sine-5_240912'] = ROOT.kCyan+4
colors['exoticHiggs_scalar_ms60GeV_sine-6_240912'] = ROOT.kMagenta-8
colors['exoticHiggs_scalar_ms60GeV_sine-7_240912'] = ROOT.kCyan-8

## Backgrounds
colors['ZH'] = ROOT.kCyan-6
colors['p8_ee_WW_ecm240'] = ROOT.kRed-3
colors['p8_ee_ZZ_ecm240'] = ROOT.kGreen-5

# The one used for testing
colors['wzp6_ee_eeH_Hbb_ecm240'] = ROOT.kRed-10


plots = {}
plots['ExoticHiggs'] ={
    'signal':{
                     #'exoticHiggs_scalar_ms20GeV_sine-5_240912':['exoticHiggs_scalar_ms20GeV_sine-5_240912'],
                     'exoticHiggs_scalar_ms20GeV_sine-6_240912':['exoticHiggs_scalar_ms20GeV_sine-6_240912'],
                     #'exoticHiggs_scalar_ms20GeV_sine-7_240912':['exoticHiggs_scalar_ms20GeV_sine-7_240912'],

                     #'exoticHiggs_scalar_ms40GeV_sine-5_240912':['exoticHiggs_scalar_ms40GeV_sine-5_240912'],
                     #'exoticHiggs_scalar_ms40GeV_sine-6_240912':['exoticHiggs_scalar_ms40GeV_sine-6_240912'],
                     #'exoticHiggs_scalar_ms40GeV_sine-7_240912':['exoticHiggs_scalar_ms40GeV_sine-7_240912'],

                     'exoticHiggs_scalar_ms60GeV_sine-5_240912':['exoticHiggs_scalar_ms60GeV_sine-5_240912'],
                     'exoticHiggs_scalar_ms60GeV_sine-6_240912':['exoticHiggs_scalar_ms60GeV_sine-6_240912'],
                     #'exoticHiggs_scalar_ms60GeV_sine-7_240912':['exoticHiggs_scalar_ms60GeV_sine-7_240912'],
            },
            
'backgrounds':{
                    # 'Hbb':['Hbb'],
                    # 'HSM':['HSM'],
                    # 'HWW':['HWW'],
                    # 'HZZ':['HZZ'],
                    'p8_ee_WW_ecm240':['p8_ee_WW_ecm240'],
                    'p8_ee_ZZ_ecm240':['p8_ee_ZZ_ecm240'],
                    'ZH' : ['ZH'],
                    # 'wzp6_ee_ssH_Hbb_ecm240':['wzp6_ee_ssH_Hbb_ecm240'],
                    # 'wzp6_ee_ssH_Hcc_ecm240':['wzp6_ee_ssH_Hcc_ecm240'],
                    # 'wzp6_ee_ssH_Hgg_ecm240':['wzp6_ee_ssH_Hgg_ecm240'],
                    # 'wzp6_ee_ssH_Hmumu_ecm240':['wzp6_ee_ssH_Hmumu_ecm240'],
                    # 'wzp6_ee_ssH_Hss_ecm240':['wzp6_ee_ssH_Hss_ecm240'],
                    # 'wzp6_ee_ssH_Htautau_ecm240':['wzp6_ee_ssH_Htautau_ecm240'],

                    # 'wzp6_ee_bbH_Hbb_ecm240':['wzp6_ee_bbH_Hbb_ecm240'],
                    # 'wzp6_ee_bbH_Hcc_ecm240':['wzp6_ee_bbH_Hcc_ecm240'],
                    # 'wzp6_ee_bbH_Hgg_ecm240':['wzp6_ee_bbH_Hgg_ecm240'],
                    # 'wzp6_ee_bbH_Hmumu_ecm240':['wzp6_ee_bbH_Hmumu_ecm240'],
                    #'wzp6_ee_bbH_Hss_ecm240':['wzp6_ee_bbH_Hss_ecm240'],
                    # 'wzp6_ee_bbH_Htautau_ecm240':['wzp6_ee_bbH_Htautau_ecm240'],

                    # 'wzp6_ee_ccH_Hbb_ecm240':['wzp6_ee_ccH_Hbb_ecm240'],
                    # 'wzp6_ee_ccH_Hcc_ecm240':['wzp6_ee_ccH_Hcc_ecm240'],
                    # 'wzp6_ee_ccH_Hgg_ecm240':['wzp6_ee_ccH_Hgg_ecm240'],
                    #'wzp6_ee_ccH_Hmumu_ecm240':['wzp6_ee_ccH_Hmumu_ecm240'],
                    # 'wzp6_ee_ccH_Hss_ecm240':['wzp6_ee_ccH_Hss_ecm240'],
                    # 'wzp6_ee_ccH_Htautau_ecm240':['wzp6_ee_ccH_Htautau_ecm240'],

                    # 'wzp6_ee_eeH_Hbb_ecm240':['wzp6_ee_eeH_Hbb_ecm240'],
                    # 'wzp6_ee_eeH_Hcc_ecm240':['wzp6_ee_eeH_Hcc_ecm240'],
                    # 'wzp6_ee_eeH_Hgg_ecm240':['wzp6_ee_eeH_Hgg_ecm240'],
                    #'wzp6_ee_eeH_Hmumu_ecm240':['wzp6_ee_eeH_Hmumu_ecm240'],
                    #'wzp6_ee_eeH_Hss_ecm240':['wzp6_ee_eeH_Hss_ecm240'],
                    #'wzp6_ee_eeH_Htautau_ecm240':['wzp6_ee_eeH_Htautau_ecm240'],

                    # 'wzp6_ee_mumuH_Hbb_ecm240':['wzp6_ee_mumuH_Hbb_ecm240'],
                    # 'wzp6_ee_mumuH_Hcc_ecm240':['wzp6_ee_mumuH_Hcc_ecm240'],
                    # 'wzp6_ee_mumuH_Hgg_ecm240':['wzp6_ee_mumuH_Hgg_ecm240'],
                    #'wzp6_ee_mumuH_Hmumu_ecm240':['wzp6_ee_mumuH_Hmumu_ecm240'],
                    #'wzp6_ee_mumuH_Hss_ecm240':['wzp6_ee_mumuH_Hss_ecm240'],
                    #'wzp6_ee_mumuH_Htautau_ecm240':['wzp6_ee_mumuH_Htautau_ecm240'],

                    # 'wzp6_ee_tautauH_Hbb_ecm240':['wzp6_ee_tautauH_Hbb_ecm240'],
                    # 'wzp6_ee_tautauH_Hcc_ecm240':['wzp6_ee_tautauH_Hcc_ecm240'],
                    # 'wzp6_ee_tautauH_Hgg_ecm240':['wzp6_ee_tautauH_Hgg_ecm240'],
                    # 'wzp6_ee_tautauH_Hmumu_ecm240':['wzp6_ee_tautauH_Hmumu_ecm240'],
                    # 'wzp6_ee_tautauH_Hss_ecm240':['wzp6_ee_tautauH_Hss_ecm240'],
                    # 'wzp6_ee_tautauH_Htautau_ecm240':['wzp6_ee_tautauH_Htautau_ecm240'],

                    # 'wzp6_ee_nunuH_Hbb_ecm240':['wzp6_ee_nunuH_Hbb_ecm240'],
                    # 'wzp6_ee_nunuH_Hcc_ecm240':['wzp6_ee_nunuH_Hcc_ecm240'],
                    # 'wzp6_ee_nunuH_Hdd_ecm240':['wzp6_ee_nunuH_Hdd_ecm240'],
                    # 'wzp6_ee_nunuH_Hgg_ecm240':['wzp6_ee_nunuH_Hgg_ecm240'],
                    # 'wzp6_ee_nunuH_Hmumu_ecm240':['wzp6_ee_nunuH_Hmumu_ecm240'],
                    # 'wzp6_ee_nunuH_Hss_ecm240':['wzp6_ee_nunuH_Hss_ecm240'],
                    # 'wzp6_ee_nunuH_Htautau_ecm240':['wzp6_ee_nunuH_Htautau_ecm240'],
                    # 'wzp6_ee_nunuH_Huu_ecm240':['wzp6_ee_nunuH_Huu_ecm240'],

                    # 'wzp6_ee_eeH_HZZ_ecm240':['wzp6_ee_eeH_HZZ_ecm240'],
                    # 'wzp6_ee_mumuH_HZZ_ecm240':['wzp6_ee_mumuH_HZZ_ecm240'],
                    # 'wzp6_ee_qqH_HZZ_ecm240':['wzp6_ee_qqH_HZZ_ecm240'],
                    # 'wzp6_ee_tautauH_HZZ_ecm240':['wzp6_ee_tautauH_HZZ_ecm240'],

                    # 'wzp6_ee_eeH_HWW_ecm240':['wzp6_ee_eeH_HWW_ecm240'],
                    # 'wzp6_ee_mumuH_HWW_ecm240':['wzp6_ee_mumuH_HWW_ecm240'],
                    # 'wzp6_ee_qqH_HWW_ecm240':['wzp6_ee_qqH_HWW_ecm240'],
                    # 'wzp6_ee_tautauH_HWW_ecm240':['wzp6_ee_tautauH_HWW_ecm240'],

                    #'p8_ee_WW_ecm240':['p8_ee_WW_ecm240'],
                    #'p8_ee_ZZ_ecm240':['p8_ee_ZZ_ecm240'],

                }
            }


legend = {}
legend['exoticHiggs_scalar_ms20GeV_sine-5_240912'] = r'm20GeV-sin\theta=1e^{-5}'
legend['exoticHiggs_scalar_ms20GeV_sine-6_240912'] = r'm20GeV-sin\theta=1e^{-6}'
legend['exoticHiggs_scalar_ms20GeV_sine-7_240912'] = r'm20GeV-sin\theta=1e^{-7}'

legend['exoticHiggs_scalar_ms40GeV_sine-5_240912'] = r'm40GeV-sin\theta=1e^{-5}'
legend['exoticHiggs_scalar_ms40GeV_sine-6_240912'] = r'm40GeV-sin\theta=1e^{-6}'
legend['exoticHiggs_scalar_ms40GeV_sine-7_240912'] = r'm40GeV-sin\theta=1e^{-7}'

legend['exoticHiggs_scalar_ms60GeV_sine-5_240912'] = r'm60GeV-sin\theta=1e^{-5}'
legend['exoticHiggs_scalar_ms60GeV_sine-6_240912'] = r'm60GeV-sin\theta=1e^{-6}'
legend['exoticHiggs_scalar_ms60GeV_sine-7_240912'] = r'm60GeV-sin\theta=1e^{-7}'

legend['p8_ee_WW_ecm240'] = 'WW'
legend['p8_ee_ZZ_ecm240'] = 'ZZ'
legend['ZH'] = r'ZH, H \rightarrow SM'

# legend['wzp6_ee_ssH_Hbb_ecm240'] = 'Z(ss), H(bb)'
# legend['wzp6_ee_ssH_Hcc_ecm240'] = 'Z(ss), H(cc)'
# legend['wzp6_ee_ssH_Hgg_ecm240'] = 'Z(ss), H(gg)'
# legend['wzp6_ee_ssH_Hmumu_ecm240'] = 'Z(ss), H(mumu)'
# legend['wzp6_ee_ssH_Hss_ecm240'] = 'Z(ss), H(ss)'
# legend['wzp6_ee_ssH_Htautau_ecm240'] = 'Z(ss), H(tautau)'
# legend['wzp6_ee_bbH_Hbb_ecm240'] = 'Z(bb), H(bb)'
# legend['wzp6_ee_bbH_Hcc_ecm240'] = 'Z(bb), H(cc)'
# legend['wzp6_ee_bbH_Hgg_ecm240'] = 'Z(bb), H(gg)'
# legend['wzp6_ee_bbH_Hmumu_ecm240'] = 'Z(bb), H(mumu)'
# legend['wzp6_ee_bbH_Hss_ecm240'] = 'Z(bb), H(ss)'
# legend['wzp6_ee_bbH_Htautau_ecm240'] = 'Z(bb), H(tautau)'
# legend['wzp6_ee_ccH_Hbb_ecm240'] = 'Z(cc), H(bb)'
# legend['wzp6_ee_ccH_Hcc_ecm240'] = 'Z(cc), H(cc)'
# legend['wzp6_ee_ccH_Hgg_ecm240'] = 'Z(cc), H(gg)'
# legend['wzp6_ee_ccH_Hmumu_ecm240'] = 'Z(cc), H(mumu)'
# legend['wzp6_ee_ccH_Hss_ecm240'] = 'Z(cc), H(ss)'
# legend['wzp6_ee_ccH_Htautau_ecm240'] = 'Z(cc), H(tautau)'
legend['wzp6_ee_eeH_Hbb_ecm240'] = 'Z(ee), H(bb)'
# legend['wzp6_ee_eeH_Hcc_ecm240'] = 'Z(ee), H(cc)'
# legend['wzp6_ee_eeH_Hgg_ecm240'] = 'Z(ee), H(gg)'
# legend['wzp6_ee_eeH_Hmumu_ecm240'] = 'Z(ee), H(mumu)'
# legend['wzp6_ee_eeH_Hss_ecm240'] = 'Z(ee), H(ss)'
# legend['wzp6_ee_eeH_Htautau_ecm240'] = 'Z(ee), H(tautau)'
# legend['wzp6_ee_mumuH_Hbb_ecm240'] = 'Z(mumu), H(bb)'
# legend['wzp6_ee_mumuH_Hcc_ecm240'] = 'Z(mumu), H(cc)'
# legend['wzp6_ee_mumuH_Hgg_ecm240'] = 'Z(mumu), H(gg)'
# legend['wzp6_ee_mumuH_Hmumu_ecm240'] = 'Z(mumu), H(mumu)'
# legend['wzp6_ee_mumuH_Hss_ecm240'] = 'Z(mumu), H(ss)'
# legend['wzp6_ee_mumuH_Htautau_ecm240'] = 'Z(mumu), H(tautau)'
# legend['wzp6_ee_tautauH_Hbb_ecm240'] = 'Z(tautau), H(bb)'
# legend['wzp6_ee_tautauH_Hcc_ecm240'] = 'Z(tautau), H(cc)'
# legend['wzp6_ee_tautauH_Hgg_ecm240'] = 'Z(tautau), H(gg)'
# legend['wzp6_ee_tautauH_Hmumu_ecm240'] = 'Z(tautau), H(mumu)'
# legend['wzp6_ee_tautauH_Hss_ecm240'] = 'Z(tautau), H(ss)'
# legend['wzp6_ee_tautauH_Htautau_ecm240'] = 'Z(tautau), H(tautau)'
# legend['wzp6_ee_nunuH_Hbb_ecm240'] = 'Z(nunu), H(bb)'
# legend['wzp6_ee_nunuH_Hcc_ecm240'] = 'Z(nunu), H(cc)'
# legend['wzp6_ee_nunuH_Hdd_ecm240'] = 'Z(nunu), H(dd)'
# legend['wzp6_ee_nunuH_Hgg_ecm240'] = 'Z(nunu), H(gg)'
# legend['wzp6_ee_nunuH_Hmumu_ecm240'] = 'Z(nunu), H(mumu)'
# legend['wzp6_ee_nunuH_Hss_ecm240'] = 'Z(nunu), H(ss)'
# legend['wzp6_ee_nunuH_Htautau_ecm240'] = 'Z(nunu), H(tautau)'
# legend['wzp6_ee_nunuH_Huu_ecm240'] = 'Z(nunu), H(uu)'
# legend['wzp6_ee_eeH_HZZ_ecm240'] = 'Z(ee), H(ZZ)'
# legend['wzp6_ee_mumuH_HZZ_ecm240'] = 'Z(mumu), H(ZZ)'
# legend['wzp6_ee_qqH_HZZ_ecm240'] = 'Z(qq), H(ZZ)'
# legend['wzp6_ee_tautauH_HZZ_ecm240'] = 'Z(tautau), H(ZZ)'
# legend['wzp6_ee_eeH_HWW_ecm240'] = 'Z(ee), H(WW)'
# legend['wzp6_ee_mumuH_HWW_ecm240'] = 'Z(mumu), H(WW)'
# legend['wzp6_ee_qqH_HWW_ecm240'] = 'Z(qq), H(WW)'
# legend['wzp6_ee_tautauH_HWW_ecm240'] = 'Z(tautau), H(WW)'
