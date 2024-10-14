import ROOT

#Mandatory: List of processes
processList = {
        #'custom_process' : {},      


        ## SIGNALS
        # "exoticHiggs_scalar_ms20GeV_sine-5_240912" : {'chunks':20},
        # "exoticHiggs_scalar_ms20GeV_sine-6_240912" : {'chunks':20},        
        # "exoticHiggs_scalar_ms20GeV_sine-7_240912" : {'chunks':20},
        # "exoticHiggs_scalar_ms40GeV_sine-5_240912" : {'chunks':20},
        # "exoticHiggs_scalar_ms40GeV_sine-6_240912" : {'chunks':20},    
        # "exoticHiggs_scalar_ms40GeV_sine-7_240912" : {'chunks':20},    
        # "exoticHiggs_scalar_ms60GeV_sine-5_240912" : {'chunks':20},
        # "exoticHiggs_scalar_ms60GeV_sine-6_240912" : {'chunks':20},    
        # "exoticHiggs_scalar_ms60GeV_sine-7_240912" : {'chunks':20},
    
        # "exoticHiggs_scalar_ms20GeV_sin3e-6_241002" : {'chunks':20},
        # "exoticHiggs_scalar_ms50GeV_sine-6_241002" : {'chunks':20},

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
        'wzp6_ee_eeH_Hbb_ecm240':{'chunks':50},
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
        # 'wzp6_ee_eeH_HZZ_ecm240':{'chunks':20},
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
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/output_MadgraphPythiaDelphes/"
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/output_MadgraphPythiaDelphes_240912/"

#Optional: output directory, default is local dir
#outputDir = "/eos/user/a/axgallen/FCC_storage/v090_batch/stage1/"
outputDirEos = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/oct14_iso_bkg/stage1/"

# import ROOT
# from podio import root_io
# input_file_path = "ZeeHbb_partial.root"
# podio_reader = root_io.Reader(input_file_path)
# for event in podio_reader.get("events"):
#   for mc_particle in event.get("Particle"):
#     if mc_particle.getCharge() != 0:
#       mc_particle_vertex = mc_particle.getVertex()
#       d = (mc_particle_vertex.x*mc_particle_vertex.x + mc_particle_vertex.y*mc_particle_vertex.y + mc_particle_vertex.z*mc_particle_vertex.z)**0.5
#       if d > 2000:
#         print(f"x: {mc_particle_vertex.x}, y: {mc_particle_vertex.y}, z: {mc_particle_vertex.z}")
#         print(f"Distance = {d:.2f}")
#         print(f"Particle: {mc_particle}")
# exit()

#Optional: ncpus, default is 4
nCPUS       = 8

#Optional running on HTCondor, default is False
runBatch    = True

userBatchConfig = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/user_config.sh"

#Optional batch queue name when running on HTCondor, default is workday (8h). testmatch is 3 days and tomorrow is 1 day. nextweek is 1 week
batchQueue = "nextweek"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#USER DEFINED CODE
# For costum displaced vertex selection, apply selection on the DVs with invariant mass higher than 1 GeV and distance from PV to DV less than 2000 mm, but longer than 4 mm
# and count the number of DVs that fulfill this selection
ROOT.gInterpreter.Declare("""
#include <cmath>
#include <vector>
#include <math.h>

#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticleData.h"
#include "edm4hep/MCParticleData.h"
#include "edm4hep/ParticleIDData.h"
#include "ReconstructedParticle2MC.h"
#include "VertexingUtils.h"

                          
using Vec_b = ROOT::VecOps::RVec<bool>;
using Vec_d = ROOT::VecOps::RVec<double>;
using Vec_f = ROOT::VecOps::RVec<float>;
using Vec_i = ROOT::VecOps::RVec<int>;
using Vec_ui = ROOT::VecOps::RVec<unsigned int>;

using rp = edm4hep::ReconstructedParticleData;
using Vec_rp = ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>;
using Vec_mc = ROOT::VecOps::RVec<edm4hep::MCParticleData>;
using Vec_tlv = ROOT::VecOps::RVec<TLorentzVector>;

                          
            
struct sel_iso {
    sel_iso(float arg_max_iso);
    float m_max_iso = .25;
    Vec_rp operator() (Vec_rp in, Vec_f iso);
  };

sel_iso::sel_iso(float arg_max_iso) : m_max_iso(arg_max_iso) {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_iso::operator() (Vec_rp in, Vec_f iso) {
    Vec_rp result;
    result.reserve(in.size());
    for (size_t i = 0; i < in.size(); ++i) {
        auto & p = in[i];
        if (iso[i] < m_max_iso) {
            result.emplace_back(p);
        }
    }
    return result;
}

 
// compute the cone isolation for reco particles
struct coneIsolation {

    coneIsolation(float arg_dr_min, float arg_dr_max);
    double deltaR(double eta1, double phi1, double eta2, double phi2) { return TMath::Sqrt(TMath::Power(eta1-eta2, 2) + (TMath::Power(phi1-phi2, 2))); };

    float dr_min = 0;
    float dr_max = 0.4;
    Vec_f operator() (Vec_rp in, Vec_rp rps) ;
};

coneIsolation::coneIsolation(float arg_dr_min, float arg_dr_max) : dr_min(arg_dr_min), dr_max( arg_dr_max ) { };
Vec_f coneIsolation::coneIsolation::operator() (Vec_rp in, Vec_rp rps) {
  
    Vec_f result;
    result.reserve(in.size());

    std::vector<ROOT::Math::PxPyPzEVector> lv_reco;
    std::vector<ROOT::Math::PxPyPzEVector> lv_charged;
    std::vector<ROOT::Math::PxPyPzEVector> lv_neutral;

    for(size_t i = 0; i < rps.size(); ++i) {

        ROOT::Math::PxPyPzEVector tlv;
        tlv.SetPxPyPzE(rps.at(i).momentum.x, rps.at(i).momentum.y, rps.at(i).momentum.z, rps.at(i).energy);
        
        if(rps.at(i).charge == 0) lv_neutral.push_back(tlv);
        else lv_charged.push_back(tlv);
    }
    
    for(size_t i = 0; i < in.size(); ++i) {

        ROOT::Math::PxPyPzEVector tlv;
        tlv.SetPxPyPzE(in.at(i).momentum.x, in.at(i).momentum.y, in.at(i).momentum.z, in.at(i).energy);
        lv_reco.push_back(tlv);
    }

    
    // compute the isolation (see https://github.com/delphes/delphes/blob/master/modules/Isolation.cc#L154) 
    for (auto & lv_reco_ : lv_reco) {
    
        double sumNeutral = 0.0;
        double sumCharged = 0.0;
    
        // charged
        for (auto & lv_charged_ : lv_charged) {
    
            double dr = coneIsolation::deltaR(lv_reco_.Eta(), lv_reco_.Phi(), lv_charged_.Eta(), lv_charged_.Phi());
            if(dr > dr_min && dr < dr_max) sumCharged += lv_charged_.P();
        }
        
        // neutral
        for (auto & lv_neutral_ : lv_neutral) {
    
            double dr = coneIsolation::deltaR(lv_reco_.Eta(), lv_reco_.Phi(), lv_neutral_.Eta(), lv_neutral_.Phi());
            if(dr > dr_min && dr < dr_max) sumNeutral += lv_neutral_.P();
        }
        
        double sum = sumCharged + sumNeutral;
        double ratio= sum / lv_reco_.P();
        result.emplace_back(ratio);
    }
    return result;
}


                          

""")
#END USER DEFINED CODE

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

            # Vertex fitting

            # First, reconstruct a vertex from all tracks 
            # Input parameters are 1 = primary vertex, _EFlowTrack_trackStates contains all tracks, bool beamspotconstraint = true, bsc sigma x/y/z
            .Define("VertexObject_allTracks",  "VertexFitterSimple::VertexFitter_Tk ( 1, EFlowTrack_1, true, 4.5, 20e-3, 300)")

            # Select the tracks that are reconstructed  as primaries
            .Define("RecoedPrimaryTracks",  "VertexFitterSimple::get_PrimaryTracks( EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0.)")
            .Define("n_RecoedPrimaryTracks",  "ReconstructedParticle2Track::getTK_n( RecoedPrimaryTracks )")

            # the final primary vertex :
            .Define("PrimaryVertexObject",   "VertexFitterSimple::VertexFitter_Tk ( 1, RecoedPrimaryTracks, true, 4.5, 20e-3, 300) ")
            .Define("PrimaryVertex",   "VertexingUtils::get_VertexData( PrimaryVertexObject )")

            # the secondary tracks
            .Define("SecondaryTracks", "VertexFitterSimple::get_NonPrimaryTracks( EFlowTrack_1, RecoedPrimaryTracks)")

            # Displaced vertex reconstruction
            
            # select tracks with pT > 1 GeV
            .Define('sel_tracks_pt', 'VertexingUtils::sel_pt_tracks(1)(EFlowTrack_1)')
            
            # select tracks with |d0 |> 2 mm
            .Define('sel_tracks', 'VertexingUtils::sel_d0_tracks(2)(sel_tracks_pt)')
            
            # find the DVs with sel pt and d0
            .Define("DV_evt_seltracks", "VertexFinderLCFIPlus::get_SV_event(sel_tracks, EFlowTrack_1, PrimaryVertexObject, true, 9., 40., 5.)")

            # number of DVs
            .Define('n_seltracks_DVs', 'VertexingUtils::get_n_SV(DV_evt_seltracks)')

            # number of tracks from the DVs
            .Define('n_trks_seltracks_DVs', 'VertexingUtils::get_VertexNtrk(DV_evt_seltracks)')

            # invariant mass at the DVs (assuming the tracks to be pions)
            .Define('invMass_seltracks_DVs', 'VertexingUtils::get_invM(DV_evt_seltracks)')

            # get the chi2 distributions of the DVs from selected tracks
            .Define("DV_evt_seltracks_chi2",    "VertexingUtils::get_chi2_SV(DV_evt_seltracks)")
            .Define("DV_evt_seltracks_normchi2","VertexingUtils::get_norm_chi2_SV(DV_evt_seltracks)") # DV chi2 (normalised)

            # get the decay radius of all the DVs from selected tracks
            .Define("Reco_seltracks_DVs_Lxy","VertexingUtils::get_dxy_SV(DV_evt_seltracks, PrimaryVertexObject)")
            .Define("Reco_seltracks_DVs_Lxyz","VertexingUtils::get_d3d_SV(DV_evt_seltracks, PrimaryVertexObject)")

            
            # Reconstructed electrons and muons

            # Electrons
            .Alias('Electron0', 'Electron#0.index')
            .Define('RecoElectrons',  'ReconstructedParticle::get(Electron0, ReconstructedParticles)') 
            .Define('n_RecoElectrons',  'ReconstructedParticle::get_n(RecoElectrons)') #count how many electrons are in the event in total

            # some kinematics of the reconstructed electrons and positrons
            .Define("RecoElectron_e", "ReconstructedParticle::get_e(RecoElectrons)")
            .Define("RecoElectron_p", "ReconstructedParticle::get_p(RecoElectrons)")
            .Define("RecoElectron_pt", "ReconstructedParticle::get_pt(RecoElectrons)")
            .Define("RecoElectron_px", "ReconstructedParticle::get_px(RecoElectrons)")
            .Define("RecoElectron_py", "ReconstructedParticle::get_py(RecoElectrons)")
            .Define("RecoElectron_pz", "ReconstructedParticle::get_pz(RecoElectrons)")
            .Define("RecoElectron_charge",  "ReconstructedParticle::get_charge(RecoElectrons)")

            # compute the electron isolation and store electrons with an isolation cut of 0.12 in a separate column muons_sel_iso
            .Define("electrons_iso", "coneIsolation(0.01, 0.5)(RecoElectrons, ReconstructedParticles)")
            .Define("electrons_sel_iso", "sel_iso(0.12)(RecoElectrons, electrons_iso)")
            .Define("n_electrons_sel_iso", "electrons_sel_iso.size()")

            # some kinematics of the isolated reconstructed electrons and positrons
            .Define("isoRecoElectron_e", "ReconstructedParticle::get_e(electrons_sel_iso)")
            .Define("isoRecoElectron_p", "ReconstructedParticle::get_p(electrons_sel_iso)")
            .Define("isoRecoElectron_pt", "ReconstructedParticle::get_pt(electrons_sel_iso)")
            .Define("isoRecoElectron_px", "ReconstructedParticle::get_px(electrons_sel_iso)")
            .Define("isoRecoElectron_py", "ReconstructedParticle::get_py(electrons_sel_iso)")
            .Define("isoRecoElectron_pz", "ReconstructedParticle::get_pz(electrons_sel_iso)")
            .Define("isoRecoElectron_charge",  "ReconstructedParticle::get_charge(electrons_sel_iso)")

            # finding the invariant mass of the reconstructed electron and positron pair
            .Define("isoReco_ee_energy", "if ((n_RecoElectrons>1) && (n_electrons_sel_iso == 2) && (isoRecoElectron_charge.at(0) != isoRecoElectron_charge.at(1))) return (isoRecoElectron_e.at(0) + isoRecoElectron_e.at(1)); else return float(-1.);")
            .Define("isoReco_ee_px", "if ((n_RecoElectrons>1) && (n_electrons_sel_iso == 2) && (isoRecoElectron_charge.at(0) != isoRecoElectron_charge.at(1))) return (isoRecoElectron_px.at(0) + isoRecoElectron_px.at(1)); else return float(-1.);")
            .Define("isoReco_ee_py", "if ((n_RecoElectrons>1) && (n_electrons_sel_iso == 2) && (isoRecoElectron_charge.at(0) != isoRecoElectron_charge.at(1))) return (isoRecoElectron_py.at(0) + isoRecoElectron_py.at(1)); else return float(-1.);")
            .Define("isoReco_ee_pz", "if ((n_RecoElectrons>1) && (n_electrons_sel_iso == 2) && (isoRecoElectron_charge.at(0) != isoRecoElectron_charge.at(1))) return (isoRecoElectron_pz.at(0) + isoRecoElectron_pz.at(1)); else return float(-1.);")
            .Define("isoReco_ee_invMass", "if ((n_RecoElectrons>1) && (n_electrons_sel_iso == 2) && (isoRecoElectron_charge.at(0) != isoRecoElectron_charge.at(1))) return sqrt(isoReco_ee_energy*isoReco_ee_energy - isoReco_ee_px*isoReco_ee_px - isoReco_ee_py*isoReco_ee_py - isoReco_ee_pz*isoReco_ee_pz ); else return float(-1.);")


            # Muons
            .Alias('Muon0', 'Muon#0.index')
            .Define('RecoMuons',  'ReconstructedParticle::get(Muon0, ReconstructedParticles)')
            .Define('n_RecoMuons',  'ReconstructedParticle::get_n(RecoMuons)') #count how many muons are in the event in total

            # some kinematics of the reconstructed muons
            .Define("RecoMuon_e",      "ReconstructedParticle::get_e(RecoMuons)")
            .Define("RecoMuon_p",      "ReconstructedParticle::get_p(RecoMuons)")
            .Define("RecoMuon_pt",      "ReconstructedParticle::get_pt(RecoMuons)")
            .Define("RecoMuon_px",      "ReconstructedParticle::get_px(RecoMuons)")
            .Define("RecoMuon_py",      "ReconstructedParticle::get_py(RecoMuons)")
            .Define("RecoMuon_pz",      "ReconstructedParticle::get_pz(RecoMuons)")
            .Define("RecoMuon_charge",  "ReconstructedParticle::get_charge(RecoMuons)")

            # compute the muon isolation and store muons with an isolation cut of 0.25 in a separate column muons_sel_iso
            .Define("muons_iso", "coneIsolation(0.01, 0.5)(RecoMuons, ReconstructedParticles)")
            .Define("muons_sel_iso", "sel_iso(0.25)(RecoMuons, muons_iso)")
            .Define("n_muons_sel_iso", "muons_sel_iso.size()")

            # some kinematics of the isolated reconstructed muons
            .Define("isoRecoMuon_e",      "ReconstructedParticle::get_e(muons_sel_iso)")
            .Define("isoRecoMuon_p",      "ReconstructedParticle::get_p(muons_sel_iso)")
            .Define("isoRecoMuon_pt",      "ReconstructedParticle::get_pt(muons_sel_iso)")
            .Define("isoRecoMuon_px",      "ReconstructedParticle::get_px(muons_sel_iso)")
            .Define("isoRecoMuon_py",      "ReconstructedParticle::get_py(muons_sel_iso)")
            .Define("isoRecoMuon_pz",      "ReconstructedParticle::get_pz(muons_sel_iso)")
            .Define("isoRecoMuon_charge",  "ReconstructedParticle::get_charge(muons_sel_iso)")

            # finding the invariant mass of the reconstructed muon pair
            .Define("isoReco_mumu_energy", "if ((n_RecoMuons>1) && (n_muons_sel_iso == 2) && (isoRecoMuon_charge.at(0) != isoRecoMuon_charge.at(1))) return (isoRecoMuon_e.at(0) + isoRecoMuon_e.at(1)); else return float(-1.);")
            .Define("isoReco_mumu_px", "if ((n_RecoMuons>1) && (n_muons_sel_iso == 2) && (isoRecoMuon_charge.at(0) != isoRecoMuon_charge.at(1))) return (isoRecoMuon_px.at(0) + isoRecoMuon_px.at(1)); else return float(-1.);")
            .Define("isoReco_mumu_py", "if ((n_RecoMuons>1) && (n_muons_sel_iso == 2) && (isoRecoMuon_charge.at(0) != isoRecoMuon_charge.at(1))) return (isoRecoMuon_py.at(0) + isoRecoMuon_py.at(1)); else return float(-1.);")
            .Define("isoReco_mumu_pz", "if ((n_RecoMuons>1) && (n_muons_sel_iso == 2) && (isoRecoMuon_charge.at(0) != isoRecoMuon_charge.at(1))) return (isoRecoMuon_pz.at(0) + isoRecoMuon_pz.at(1)); else return float(-1.);")
            .Define("isoReco_mumu_invMass", "if ((n_RecoMuons>1) && (n_muons_sel_iso == 2) && (isoRecoMuon_charge.at(0) != isoRecoMuon_charge.at(1))) return sqrt(isoReco_mumu_energy*isoReco_mumu_energy - isoReco_mumu_px*isoReco_mumu_px - isoReco_mumu_py*isoReco_mumu_py - isoReco_mumu_pz*isoReco_mumu_pz ); else return float(-1.);")


        )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            ################### TRACKS #####################
            "n_tracks",
            "n_RecoedPrimaryTracks",
            'sel_tracks',
            ################### DV LEVEL #####################
            'n_seltracks_DVs',
            'n_trks_seltracks_DVs',
            'invMass_seltracks_DVs',
            "DV_evt_seltracks_chi2",
            "DV_evt_seltracks_normchi2",
            "Reco_seltracks_DVs_Lxy",
            "Reco_seltracks_DVs_Lxyz",
            ################### ELECTRONS #####################
            'n_RecoElectrons',
            "RecoElectron_e",
            "RecoElectron_p",
            "RecoElectron_pt",
            "RecoElectron_px",
            "RecoElectron_py",
            "RecoElectron_pz",
            "RecoElectron_charge",
            #------------------ ISO -------------------------#
            "n_electrons_sel_iso",
            "isoRecoElectron_e",
            "isoRecoElectron_p",
            "isoRecoElectron_pt",
            "isoRecoElectron_px",
            "isoRecoElectron_py",
            "isoRecoElectron_pz",
            "isoRecoElectron_charge",
            "isoReco_ee_invMass",
            ################### MUONS #####################
            'n_RecoMuons',
            "RecoMuon_e",
            "RecoMuon_p",
            "RecoMuon_pt",
            "RecoMuon_px",
            "RecoMuon_py",
            "RecoMuon_pz",
            "RecoMuon_charge",
            #------------------ ISO -------------------------#
            "n_muons_sel_iso",
            "isoRecoMuon_e",
            "isoRecoMuon_p",
            "isoRecoMuon_pt",
            "isoRecoMuon_px",
            "isoRecoMuon_py",
            "isoRecoMuon_pz",
            "isoRecoMuon_charge",
            "isoReco_mumu_invMass",
            ########################################

        ]
        return branchList
