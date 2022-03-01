import FWCore.ParameterSet.Config as cms

psets = [
  cms.PSet(
    record = cms.string('PFCalibrationRcd'),
    tag = cms.string('PFCalibration_v1_hlt'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('HLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK4CaloHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4CaloHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK4PFClusterHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFClusterHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK4PFHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK4PFchsHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFchsHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK4PFPuppiHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFPuppiHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK8CaloHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8CaloHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK8PFClusterHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFClusterHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK8PFHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK8PFchsHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFchsHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_AK8PFPuppiHLT_hlt_v1'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFPuppiHLT'),
  )
]

def forceNewJEC(process):
    if not hasattr(process, "GlobalTag"):
        Exception("The process has not GlobalTag. Please contact silvio.donato@cern.ch")
    gt = getattr(process, "GlobalTag")
    if not hasattr(gt, "toGet"):
        gt.toGet = cms.VPSet()
    for pset in psets:
        gt.toGet.append(pset)
    return process

