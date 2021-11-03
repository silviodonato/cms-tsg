## New Tracking (patatrack tracks + single iteration)
from Run3.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking as TRK_newTracking

## New L2 Tau reconstruction
from Run3.applyL2TauTag import update as TAU_newL2sequence

## New tracking (patatrack tracks + single iteration) in muon reco
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackWithIsoAndTriplets as MUO_newTracking

## New ML-based inside-out seeding for muon reconstruction
from Run3.customizeMuonHLTForRun3 import customizeIOSeedingPatatrack as MUO_newIO

## New ML-based outside-in muon for muon reconstruction
from RecoMuon.TrackerSeedGenerator.customizeOIseeding import customizeOIseeding as MUO_newOI

## Replace regional pixel tracks with global pixel tracks in TkMu triggers
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackTkMu as MUO_updateTkMu

## Replace regional pixel tracks with global pixel tracks in OpenMu triggers
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackOpenMu as MUO_updateOpenMu

## Replace regional pixel tracks with global pixel tracks in NoVtx triggers
from Run3.customizeMuonHLTForRun3 import customizeMuonHLTForPatatrackNoVtx as MUO_updateNoVtx

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

## Add MC_PFBTagDeepJet (process, doPF=True, doPuppi=False, roiReplace=False)
## Add MC_PFBTagDeepJetROIForBTag (process, doPF=True, doPuppi=False, roiReplace=True)
from Run3.customise_TRK import addDeepJet

