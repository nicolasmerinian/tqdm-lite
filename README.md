# tqdm-lite

Mini barre de progression Python inspirée de tqdm.
Le but était de pratiquer. On m'a parlé de tqdm, et j'ai voulu essayé de reproduire la fonctionnalité.

![Alt text](/./screenshot.png?raw=true "Screenshot")

## Installation
pip install git+https://github.com/nicolasmerinian/tqdm-lite.git

## Exemple d'utilisation

```python
from tqdm_lite import TqdmLite
import time

for _ in TqdmLite(range(10), prefix="Processing:"):
    time.sleep(0.2)
```

---

## ** Tester localement**

Dans le dossier racine :

```bash
pip install -e .
