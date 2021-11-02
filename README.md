# cms-tsg

You can apply the customization functions by adding this piece of code to your `hlt.py`
```
from customizeHLTforRun3 import *
process = TRK_newTracking(process)
#process = TAU_newL2sequence(process)
#process = BTV_addDeepJet(process)
#process = BTV_newCaloBTag(process)
#process = MUO_newTracking(process)
```

The list of customization functions are available at 
