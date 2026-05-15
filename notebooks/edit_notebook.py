import json

with open('/Users/yangguang/GitHub/project_FTS/notebooks/task3_Yangguang.ipynb', 'r') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "TASK1_PARAMS = {" in source:
            new_source = """# ============================================================
# Per-series SARIMA parameters derived from Task 1 (Lukas)
# ============================================================
# (p, q): AR and MA orders from ACF/PACF of log-returns
# m: dominant seasonal period from Welch periodogram on log-returns
# We use seasonal order (P=1, D=0, Q=1, m) to capture the cycle.
# ============================================================

import os
ROOT_DIR = "/Users/yangguang/GitHub/project_FTS"

TASK1_PARAMS = {
    # series : ((p, d, q), (P, D, Q, m))
    'gurkor':       ((0, 1, 0), (1, 0, 1, 12)),
    'guitars':      ((1, 1, 2), (1, 0, 1, 2)),
    'slingshots':   ((0, 1, 0), (1, 0, 1, 2)), 
    'basses':       ((0, 1, 0), (1, 0, 1, 4)),
    'tomtoms':      ((1, 1, 2), (1, 0, 1, 2)),
    'tromboner':    ((0, 1, 0), (1, 0, 1, 24)),
    'tents':        ((2, 1, 0), (1, 0, 1, 2)),
    'violins':      ((1, 1, 1), (1, 0, 1, 2)),
}
"""
            cell['source'] = [line + '\n' for line in new_source.split('\n')[:-1]]
            break

with open('/Users/yangguang/GitHub/project_FTS/notebooks/task3_Yangguang.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
