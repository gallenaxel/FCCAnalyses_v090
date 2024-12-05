import ROOT

# global parameters
intLumi        = 10.8e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'Zh, Z #rightarrow l^{\pm}l^{\mp}, h #rightarrow ss #rightarrow 4b'
delphesVersion = '3.4.2'
energy         = 240
collider       = 'FCC-ee'
inputDir       = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/final/"
#formats        = ['png','pdf']
formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/dec5_MC/plots/"
splitLeg       = True

variables = [

    #gen variables
    # 'n_GenElectrons',
    # 'n_GenMuons',
    # 'n_GenZ',
    # 'n_GenHiggs',
    # 'n_Genb',
    # 'n_GenHS',
    # 'AllGenHS_mass',
    # 'AllGenHS_e',
    'decayLengthsHS',
    #'LxyHS',
    'lifetimeHS',
    #'lifetimeHSLAB',
    
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['ExoticHiggs']  = [
    "selNone",
]

extralabel = {}
extralabel['selNone'] = "Before selection"

colors = {}
colors['exoticHiggs_scalar_ms20GeV_sine-5_240912'] = ROOT.kRed+2
colors['exoticHiggs_scalar_ms20GeV_sine-6_240912'] = ROOT.kRed+2
colors['exoticHiggs_scalar_ms60GeV_sine-6_240912'] = ROOT.kOrange+7
colors['exoticHiggs_scalar_ms60GeV_sine-7_240912'] = ROOT.kOrange+7

linestyle = {}
linestyle['exoticHiggs_scalar_ms20GeV_sine-5_240912'] = 1
linestyle['exoticHiggs_scalar_ms20GeV_sine-6_240912'] = 1
linestyle['exoticHiggs_scalar_ms60GeV_sine-6_240912'] = 2
linestyle['exoticHiggs_scalar_ms60GeV_sine-7_240912'] = 2

plots = {}
plots['ExoticHiggs'] = {'signal':{
                    'exoticHiggs_scalar_ms20GeV_sine-5_240912':['exoticHiggs_scalar_ms20GeV_sine-5_240912'],
                    'exoticHiggs_scalar_ms20GeV_sine-6_240912':['exoticHiggs_scalar_ms20GeV_sine-6_240912'],
                    'exoticHiggs_scalar_ms60GeV_sine-6_240912':['exoticHiggs_scalar_ms60GeV_sine-6_240912'],
                    'exoticHiggs_scalar_ms60GeV_sine-7_240912':['exoticHiggs_scalar_ms60GeV_sine-7_240912'],
},
 'backgrounds':{
    'exoticHiggs_scalar_ms60GeV_sine-7_240912':['exoticHiggs_scalar_ms60GeV_sine-7_240912']             
                 }
                 }


legend = {}
legend['exoticHiggs_scalar_ms20GeV_sine-5_240912'] = r'20 GeV, 1 \times10^{-5}'
legend['exoticHiggs_scalar_ms20GeV_sine-6_240912'] = r'20 GeV, 1 \times10^{-6}'
legend['exoticHiggs_scalar_ms60GeV_sine-6_240912'] = r'60 GeV, 1 \times10^{-6}'
legend['exoticHiggs_scalar_ms60GeV_sine-7_240912'] = r'60 GeV, 1 \times10^{-7}'
