# Overview
<a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Apache 2.0 License"></a>

This base layer provides a function to add logrotate support to any reactive charm.

# Usage

Declarative via `layer.yaml`


```yaml
options:
  logrotate:
    /var/log/foobar.log:
      - copytruncate
      - rotate 5
      - size 100k

```

In your charm code

```python
from charms.layer import logrotate

@when(logrotate.installed, ...)
def setup_logrotate():
    logrotate_opts = {
        /var/log/foobar.log: [
            'copytruncate', 
            'rotate 5', 
            'size 100k', 
        ]
    }
    logrotate.configure(logrotate_opts)
```
