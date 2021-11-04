## New Tracking (patatrack tracks + single iteration)
from Run3.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking as TRK_newTracking

## New L2 Tau reconstruction
from Run3.applyL2TauTag import update as TAU_newL2sequence

## New tracking (patatrack tracks + single iteration) in muon reco
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackWithIsoAndTriplets
def MUO_newTracking(process): 
    customizeMuonHLTForPatatrackWithIsoAndTriplets(process, loadPatatrack=False)
    return process

## New ML-based inside-out seeding for muon reconstruction
from Run3.customizeMuonHLTForRun3 import customizeIOSeedingPatatrack as MUO_newIO

## New ML-based outside-in muon for muon reconstruction
from RecoMuon.TrackerSeedGenerator.customizeOIseeding import customizeOIseeding as MUO_newOI

## Replace regional pixel tracks with global pixel tracks in TkMu triggers
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackTkMu
def MUO_updateTkMu(process): 
    customizeMuonHLTForPatatrackWithIsoAndTriplets(process, loadPatatrack=False)
    return process

## Replace regional pixel tracks with global pixel tracks in OpenMu triggers
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackOpenMu
def MUO_updateOpenMu(process): 
    customizeMuonHLTForPatatrackWithIsoAndTriplets(process, loadPatatrack=False)
    return process

## Replace regional pixel tracks with global pixel tracks in NoVtx triggers
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackNoVtx
def MUO_updateNoVtx(process): 
    customizeMuonHLTForPatatrackWithIsoAndTriplets(process, loadPatatrack=False)
    return process

## Calo b-tagging: none
## PF b-tagging: new regional PF b-tagging [new sequence]
from Run3.customise_TRK_replacement import customiseRun3BTagRegionalTracks_Replacement as BTV_noCalo_roiPF

## Calo b-tagging: new regional calo b-tagging [new sequence]
## PF b-tagging: new regional PF b-tagging [new sequence]
from Run3.customise_TRK_replacement_calo import customiseRun3BTagRegionalTracks_Replacement_calo as BTV_roiCalo_roiPF

## Calo b-tagging: new regional calo b-tagging [new sequence]
## PF b-tagging: new global PF b-tagging
from Run3.customise_TRK_replacement_global_calo import customiseRun3BTagRegionalTracks_Replacement_global_calo as BTV_roiCalo_globalPF

## Calo b-tagging: new "global" calo b-tagging
## PF b-tagging: new global PF b-tagging
from Run3.customise_TRK_replacement_globalGlobal_calo import customiseRun3BTagRegionalTracks_Replacement_global_globalCalo as BTV_globalCalo_globalPF

from Run3.customise_TRK import addDeepJet
from Run3.customise_TRK_deepjet import customiseRun3BTagRegionalTracks_DeepJet

#customiseRun3BTagRegionalTracks_DeepJet

## Add MC_PFBTagDeepJet
def BTV_addMCDeepJetPath(process):
    process = addDeepJet(process, doPF=True, doPuppi=False, roiReplace=False) 
    return process

## Add MC_PFBTagDeepJet
def BTV_addMCDeepJetROIForBTagPath(process):
    process = addDeepJet(process, doPF=True, doPuppi=False, roiReplace=True) 
    return process

##Add a DeepJet version to all the paths with PF b-tagging
def BTV_moveToDeepJet(process): 
    process = addDeepJet(process, doPF=True, doPuppi=False, roiReplace=False)
    process = customiseRun3BTagRegionalTracks_DeepJet(process)
    return process

##Add a DeepJet version based on ROI PF to all the paths with PF b-tagging
def BTV_moveToDeepJetROI(process): 
    process = addDeepJet(process, doPF=True, doPuppi=False, roiReplace=True)
    process = customiseRun3BTagRegionalTracks_DeepJet(process)
    return process

