# pyruter

[![Build Status](https://travis-ci.org/ludeeus/pyruter.svg?branch=master)](https://travis-ci.org/ludeeus/pyruter)

_A module to get information about the next departure from a stop._

## Install

```bash
pip install pyruter
```

## Sample usage

```python
import pyruter

stopid = 2190400
destination = 'Drammen' #optional

#Get deperture information:
result = pyruter.get_departure_info(stopid, destination)

#Print the result:
print(result)
```
