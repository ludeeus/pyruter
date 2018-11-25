# pyruter [![Build Status](https://travis-ci.org/ludeeus/pyruter.svg?branch=master)](https://travis-ci.org/ludeeus/pyruter) [![PyPI version](https://badge.fury.io/py/pyruter.svg)](https://badge.fury.io/py/pyruter)

_Python package to interact with the local API of Google Home devices._

## Install

```bash
pip install pyruter
```

This package also include a CLI tool, run `pyruter --help` to see what it can do.

### Example usage

```python
"""Example usage of pyruter."""
import asyncio
import aiohttp
from pyruter.api import Departures

async def test_pyruter():
    """Example usage of pyruter."""
    stopid = 2190400
    destination = 'Drammen'
    custom_session = aiohttp.ClientSession()
    data = Departures(LOOP, stopid, destination, custom_session)
    await data.get_departures()

    print("Departures:", data.departures)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test_pyruter())
```

**NB!: The `destination` has to be the final destination, and not where you are hopping off.