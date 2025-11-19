# te_demo.py  —— 不手动启动 JVM（推荐）
import numpy as np
import math

# 给老代码补别名（NumPy 2里一些老别名/属性不存在）
if not hasattr(np, "float"):   np.float   = float
if not hasattr(np, "int"):     np.int     = int
if not hasattr(np, "bool"):    np.bool    = bool
if not hasattr(np, "complex"): np.complex = complex
if not hasattr(np, "object"):  np.object  = object
if not hasattr(np, "math"):    np.math    = math  

from idtxl.data import Data
from idtxl.multivariate_te import MultivariateTE

# 造点数据：x_{t-1} -> y_t
rng = np.random.default_rng(0)
T = 500
x = rng.normal(size=T)
y = np.zeros(T)
for t in range(1, T):
    y[t] = 0.8 * x[t-1] + 0.2 * rng.normal()

arr = np.vstack([x, y])             # [variables, time]
data = Data(arr, dim_order='ps')

settings = {
    'cmi_estimator': 'JidtKraskovCMI',
    'max_lag_sources': 3, 'min_lag_sources': 1,
    'verbosity': 1,
}

te = MultivariateTE()
res = te.analyse_network(settings=settings, data=data)
print("OK")
