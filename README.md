# pyruter - A module to get information about the next departure from a stop.

#### Notes
This has been tested with python 3.6  
This module uses these external libararies:
- requests

#### Install
```bash
pip install pyruter
```

#### Usage:
```python
from pyruter import Ruter

stopid = 2190400
ruter = Ruter()

#Get deperture information:
result = ruter.getDepartureInfo(stopid)

#Print the result:
print(result)
```