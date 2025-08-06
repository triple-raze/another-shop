import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from tools.database import execsql
import asyncio


print(asyncio.run(execsql("SELECT * FROM jwt")))