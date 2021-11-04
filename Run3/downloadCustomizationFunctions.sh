curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_deepjet.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_calo.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_global_calo.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/python/customise_TRK_replacement_globalGlobal_calo.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA/test/runHLTPaths_cfg.py
curl -O https://raw.githubusercontent.com/mmasciov/cmssw/defaultRun3Tracking_forJIRA/HLTrigger/Configuration/python/customizeHLTforRun3Tracking.py
curl -O https://raw.githubusercontent.com/annamasce/TauTriggerTools/triggerRnD_counter/HLTProducers/python/applyL2TauTag.py
curl -O https://raw.githubusercontent.com/khaosmos93/MuonHLTForRun3/master/customizeMuonHLTForRun3.py
curl -O https://raw.githubusercontent.com/khaosmos93/MuonHLTForRun3/master/mvaScale.py

#Fix for CMSSW_12_1_0_pre3 (#33885)

for file in customise_TRK*py; do
    sed -i 's/from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation/from CommonTools.RecoAlgos.primaryVertexAssociation_cfi import primaryVertexAssociation/g' $file 
#    sed -i 's/process.schedule.remove/process.HLTSchedule.remove/g' $file
done

    sed -i 's/import HLTrigger.Configuration.MuonHLTForRun3.mvaScale/from . import mvaScale/g' customizeMuonHLTForRun3.py



cat runHLTPaths_cfg.py | grep "def fixMenu" -A100  | grep "def prescale_path(path,ps_service)" -B100  | grep -v prescale_path > tmp.py
mv tmp.py runHLTPaths_cfg.py
