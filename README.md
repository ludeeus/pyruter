# Archived: Moved to GitLab https://gitlab.com/ludeeus/pyruter

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
destination = 'Sandvika' #optional
ruter = Ruter()

#Get deperture information:
result = ruter.getDepartureInfo(stopid, destination)

#Print the result:
print(result)
```
