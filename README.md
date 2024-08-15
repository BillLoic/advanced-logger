# Advanced logger

it provides colorful printing and it is be able to customize

# Install

Run command:
`pip install advanced-logger`

# Try it

```python
import logger

logger.debug("Hello")
```

# Do something andvanced

1. Colorful printing

Write this line before any action

```python
import logger as log

logger = log.getLogger("test.test", colored=True)

logger.debug("Hello")
```

2. Write your own handler

If you want to pipe message to standard error output, you do:

```python
from logger.handler import FileObjectHandler
import logger as log
import sys

class StdErrHandler(FileObjectHandler):
    def __init__(self):
        super().__init__(sys.stderr)

logger = log.getLogger("test", handler=StdErrHandler())

logger.debug("test")
```

