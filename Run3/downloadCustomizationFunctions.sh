curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK.py
sleep 0.1
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_global_calo.py
sleep 0.1
curl -O https://raw.githubusercontent.com/mmasciov/cmssw/defaultRun3Tracking_forJIRA/HLTrigger/Configuration/python/customizeHLTforRun3Tracking.py
sleep 0.1
curl -O https://raw.githubusercontent.com/annamasce/TauTriggerTools/triggerRnD_counter/HLTProducers/python/applyL2TauTag.py
sleep 0.1
curl -O https://raw.githubusercontent.com/khaosmos93/MuonHLTForRun3/master/customizeMuonHLTForRun3.py
sleep 0.1

#Fix for CMSSW_12_1_0_pre3 (#33885)

sed -i 's/from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation/from CommonTools.RecoAlgos.primaryVertexAssociation_cfi import primaryVertexAssociation/g' customise_TRK.py 
sed -i 's/from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation/from CommonTools.RecoAlgos.primaryVertexAssociation_cfi import primaryVertexAssociation/g' customise_TRK_replacement_global_calo.py

sed -i 's/process.schedule.remove/process.HLTSchedule.remove/g' applyL2TauTag.py


