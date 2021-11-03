curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_deepjet.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_calo.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_global_calo.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_globalGlobal_calo.py
curl -O https://raw.githubusercontent.com/mmasciov/cmssw/defaultRun3Tracking_forJIRA/HLTrigger/Configuration/python/customizeHLTforRun3Tracking.py
curl -O https://raw.githubusercontent.com/annamasce/TauTriggerTools/triggerRnD_counter/HLTProducers/python/applyL2TauTag.py
curl -O https://raw.githubusercontent.com/khaosmos93/MuonHLTForRun3/master/customizeMuonHLTForRun3.py


#Fix for CMSSW_12_1_0_pre3 (#33885)

for file in *py; do
    sed -i 's/from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation/from CommonTools.RecoAlgos.primaryVertexAssociation_cfi import primaryVertexAssociation/g' $file 
#    sed -i 's/process.schedule.remove/process.HLTSchedule.remove/g' $file
done





# git cms-addpkg RecoMuon/TrackerSeedGenerator
# git clone -b dev https://github.com/wonpoint4/RecoMuon-TrackerSeedGenerator.git RecoMuon/TrackerSeedGenerator/data



