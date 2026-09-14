"""Put the repository root on `sys.path` so `scripts.*` imports resolve.

Every test file contributed to this repository carried its own copy of this —
three different spellings of it, one per author, two of which put `scripts/`
itself on the path and one of which put the root on. Which spelling a suite
needs depends on whether it imports `scripts.x` or bare `x`, so a file written
against one convention fails under the other, and nothing said which was
intended. Doing it once here fixes the convention: import `scripts.x`.

`scripts/` has no `__init__.py` and does not need one — it resolves as a
namespace package. Each of the modules below guards its entry point behind
`if __name__ == "__main__"`, so importing one runs no work.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
