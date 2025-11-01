# tqdm-lite

Mini Python progress bar inspired by tqdm. 

The goal was to practice. Someone told me about tqdm, so I wanted to try to reproduce its functionality.

![Alt text](/./gif-tqdm-github.gif?raw=true "GIF showing the rendering")

## Installation
pip install git+https://github.com/nicolasmerinian/tqdm-lite.git

## Example of use

```python
from tqdm_lite import TqdmLite
import time

for _ in TqdmLite(range(10), prefix="Processing:"):
    time.sleep(0.2)
```

---

## **To test locally**

In the root directory :

```bash
pip install -e .
