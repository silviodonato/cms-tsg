### forceNewJEC

This customization function forces the usage of the latest Jet Energy Correction and PF Hadron Calibration (Feb 2022) provided by the Jet/MET group.

Example:
```
wget https://raw.githubusercontent.com/silviodonato/cms-tsg/forceNewJEC/forceNewJEC.py
hltGetConfiguration /dev/CMSSW_12_3_0/GRun [...] --customise forceNewJEC.forceNewJEC [...] > hlt.py
cmsRun hlt.py
```
