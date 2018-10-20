# pyruter

[![Build Status](https://travis-ci.org/ludeeus/pyruter.svg?branch=master)](https://travis-ci.org/ludeeus/pyruter)

_A module to get information about the next departure from a stop._

## Install

```bash
pip install pyruter
```

## Sample usage

```python
from pyruter import Ruter

stopid = 2190400
destination = 'Drammen' #optional
ruter = Ruter()

#Get deperture information:
result = ruter.get_departure_info(stopid, destination)

#Print the result:
print(result)
```
