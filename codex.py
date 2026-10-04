from __future__ import annotations

import subprocess
import sys


def run(*args: str) -> None:
    print("[AERIS]", " ".join(args))
    subprocess.run(args, check=True)


def main() -> None:
    run(sys.executable, "-m", "compileall", "-q", ".")
    run(sys.executable, "-m", "pytest", "-q")


if __name__ == "__main__":
    main()
