import ROOT

#Mandatory: List of processes
processList = {
        #'custom_process' : {},      


        # SIGNALS
        # "exoticHiggs_scalar_ms20GeV_sine-5" : {},
        # "exoticHiggs_scalar_ms20GeV_sine-6" : {},        
        # "exoticHiggs_scalar_ms20GeV_sine-7" : {},
        # "exoticHiggs_scalar_ms60GeV_sine-5" : {},
        # "exoticHiggs_scalar_ms60GeV_sine-6" : {},    
        # "exoticHiggs_scalar_ms60GeV_sine-7" : {},
    

        ## BACKGROUNDS
        # ss Backgrounds
        # 'wzp6_ee_ssH_Hbb_ecm240':{'chunks':20},
        # 'wzp6_ee_ssH_Hcc_ecm240':{'chunks':20},
        # 'wzp6_ee_ssH_Hgg_ecm240':{'chunks':20},
        # 'wzp6_ee_ssH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_ssH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_ssH_Htautau_ecm240':{'chunks':20},

        # # bb Backgrounds
        # 'wzp6_ee_bbH_Hbb_ecm240':{'chunks':20},
        # 'wzp6_ee_bbH_Hcc_ecm240':{'chunks':20},
        # 'wzp6_ee_bbH_Hgg_ecm240':{'chunks':20},
        # 'wzp6_ee_bbH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_bbH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_bbH_Htautau_ecm240':{'chunks':20},
    

        # cc Backgrounds
        # 'wzp6_ee_ccH_Hbb_ecm240':{'chunks':20},
        # 'wzp6_ee_ccH_Hcc_ecm240':{'chunks':20},
        #'wzp6_ee_ccH_Hgg_ecm240':{'chunks':250},
        # 'wzp6_ee_ccH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_ccH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_ccH_Htautau_ecm240':{'chunks':20},


        # # ee Backgrounds
        'wzp6_ee_eeH_Hbb_ecm240':{},#{'chunks':20},
        # 'wzp6_ee_eeH_Hcc_ecm240':{'chunks':20},
        # 'wzp6_ee_eeH_Hgg_ecm240':{'chunks':20},
        # 'wzp6_ee_eeH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_eeH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_eeH_Htautau_ecm240':{'chunks':20},


        # # mumu Backgrounds
        # 'wzp6_ee_mumuH_Hbb_ecm240':{'chunks':20},
        # 'wzp6_ee_mumuH_Hcc_ecm240':{'chunks':20},
        # 'wzp6_ee_mumuH_Hgg_ecm240':{'chunks':20},
        # 'wzp6_ee_mumuH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_mumuH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_mumuH_Htautau_ecm240':{'chunks':20},

        # # tautau Backgrounds
        # 'wzp6_ee_tautauH_Hbb_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_Hcc_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_Hgg_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_Htautau_ecm240':{'chunks':20},

        # # nunu Backgrounds
        # 'wzp6_ee_nunuH_Hbb_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Hcc_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Hdd_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Hgg_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Hmumu_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Hss_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Htautau_ecm240':{'chunks':20},
        # 'wzp6_ee_nunuH_Huu_ecm240':{'chunks':20},

        # # ZZ Backgrounds
        'wzp6_ee_eeH_HZZ_ecm240':{},
        # 'wzp6_ee_mumuH_HZZ_ecm240':{'chunks':20},
        # 'wzp6_ee_qqH_HZZ_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_HZZ_ecm240':{'chunks':20},

        # # WW Backgrounds
        # 'wzp6_ee_eeH_HWW_ecm240':{'chunks':20},
        # 'wzp6_ee_mumuH_HWW_ecm240':{'chunks':20},
        # 'wzp6_ee_qqH_HWW_ecm240':{'chunks':20},
        # 'wzp6_ee_tautauH_HWW_ecm240':{'chunks':20},

        # # Other
        #'p8_ee_WW_ecm240':{'chunks':100},
        #'p8_ee_ZZ_ecm240':{'chunks':100},
}

#/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/custom_process/
#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
prodTag     = "FCCee/winter2023/IDEA/"


#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events
# inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/output_MadgraphPythiaDelphes/"


#Optional: output directory, default is local dir
# outputDir = "/eos/user/a/axgallen/FCC_storage/v090_batch/stage1/"
# outputDirEos = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/new_repo_test/"



#Optional: ncpus, default is 4
nCPUS       = 8

#Optional running on HTCondor, default is False
runBatch    = False

userBatchConfig = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/user_config.sh"

#Optional batch queue name when running on HTCondor, default is workday (8h). testmatch is 3 days and tomorrow is 1 day. nextweek is 1 week
batchQueue = "nextweek"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#USER DEFINED CODE
# ROOT.gInterpreter.Declare("""
# #include <cmath>
# #include <vector>
# #include <math.h>

# #include "TLorentzVector.h"
# #include "ROOT/RVec.hxx"
# #include "edm4hep/ReconstructedParticleData.h"
# #include "edm4hep/MCParticleData.h"
# #include "edm4hep/ParticleIDData.h"
# #include "ReconstructedParticle2MC.h"
# #include "VertexingUtils.h"

                          
# using Vec_b = ROOT::VecOps::RVec<bool>;
# using Vec_d = ROOT::VecOps::RVec<double>;
# using Vec_f = ROOT::VecOps::RVec<float>;
# using Vec_i = ROOT::VecOps::RVec<int>;
# using Vec_ui = ROOT::VecOps::RVec<unsigned int>;

# using rp = edm4hep::ReconstructedParticleData;
# using Vec_rp = ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>;
# using Vec_mc = ROOT::VecOps::RVec<edm4hep::MCParticleData>;
# using Vec_tlv = ROOT::VecOps::RVec<TLorentzVector>;
# """)
# #END USER DEFINED CODE

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
    
        df2 = (
            df

            .Alias("Particle1", "Particle#1.index")
            .Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
            .Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")

            # number of tracks
            .Define("n_tracks","ReconstructedParticle2Track::getTK_n(EFlowTrack_1)")

            # Number of Jets
            .Define("n_jets", "ReconstructedParticle::get_n(Jet)")

            # all track impact parameters
            .Define("track_p","ReconstructedParticle2Track::getRP2TRK_mom (ReconstructedParticles,EFlowTrack_1)")
            .Define("track_d0","ReconstructedParticle2Track::getRP2TRK_D0 (ReconstructedParticles,EFlowTrack_1)")
            .Define("track_z0","ReconstructedParticle2Track::getRP2TRK_Z0 (ReconstructedParticles,EFlowTrack_1)")
            .Define("track_d0cov","ReconstructedParticle2Track::getRP2TRK_D0_cov (ReconstructedParticles,EFlowTrack_1)")
            .Define("track_z0cov","ReconstructedParticle2Track::getRP2TRK_Z0_cov (ReconstructedParticles,EFlowTrack_1)")
            .Define("track_d0sig","ReconstructedParticle2Track::getRP2TRK_D0_sig (ReconstructedParticles,EFlowTrack_1)")
            .Define("track_z0sig","ReconstructedParticle2Track::getRP2TRK_Z0_sig (ReconstructedParticles,EFlowTrack_1)")

            # Truth decay
            .Define('truth_p', 'MCParticle::get_p(Particle)')
            .Define('truth_prod_x', 'MCParticle::get_vertex_x(Particle)')
            .Define('truth_prod_y', 'MCParticle::get_vertex_y(Particle)')
            .Define('truth_prod_z', 'MCParticle::get_vertex_z(Particle)')
            .Define('truth_end_x', 'MCParticle::get_endPoint_x(Particle)')
            .Define('truth_end_y', 'MCParticle::get_endPoint_y(Particle)')
            .Define('truth_end_z', 'MCParticle::get_endPoint_z(Particle)')
            .Define('truth_charge', 'MCParticle::get_charge(Particle)')
            .Define('truth_pdg', 'MCParticle::get_pdg(Particle)')
            .Define('truth_genStatus', 'MCParticle::get_genStatus(Particle)')
            .Define('truth_simStatus', 'MCParticle::get_simStatus(Particle)')
            .Define('RP_MC_index',"ReconstructedParticle2MC::getRP2MC_index(MCRecoAssociations0, MCRecoAssociations1, ReconstructedParticles)")
            .Define('RP_Track',"ReconstructedParticle2Track::get_recoindTRK(ReconstructedParticles,EFlowTrack_1)")
            .Define('has_track',"ReconstructedParticle2Track::hasTRK(ReconstructedParticles)")

            # Jets
            .Define("jet_pT",     "ReconstructedParticle::get_pt(Jet)") #transverse momentum pT
            .Define("jet_eta",     "ReconstructedParticle::get_eta(Jet)") #pseudorapidity eta
            .Define("jet_phi",     "ReconstructedParticle::get_phi(Jet)") 

            # MET
            .Define("MET", "ReconstructedParticle::get_pt(MissingET)") #absolute value of MET
        )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            "n_tracks",
            "n_jets",
            "track_p",
            "track_d0",
            "track_z0",
            "track_d0cov",
            "track_z0cov",
            "track_d0sig",
            "track_z0sig",
            "truth_p",
            "truth_prod_x",
            "truth_prod_y",
            "truth_prod_z",
            "truth_end_x",
            "truth_end_y",
            "truth_end_z",
            "RP_MC_index",
            "RP_Track",
            "has_track",
            "truth_charge",
            "truth_genStatus",
            "truth_simStatus",
            "truth_pdg",
            "jet_pT",
            "jet_eta",
            "jet_phi",
            "MET",
        ]
        return branchList
