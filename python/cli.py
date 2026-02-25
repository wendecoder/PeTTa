import sys
import subprocess
import os

def main():
    # -------------------------
    # 1. Ensure a metta file is provided
    # -------------------------
    if len(sys.argv) < 2:
        print("Usage: petta <metta-file> [args...]")
        sys.exit(1)

    args = sys.argv[1:]

    # -------------------------
    # 2. Locate main.pl
    # -------------------------
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_pl = os.path.join(base_dir, "src", "main.pl")

    if not os.path.exists(main_pl):
        print(f"Error: main.pl not found at {main_pl}")
        sys.exit(1)

    # -------------------------
    # 3. Build SWI-Prolog command
    # -------------------------
    cmd = [
        "swipl",
        "--stack_limit=8g",
        "-q",
        "-s", main_pl,
        "-g", "main",
        "--"
    ] + args

    # -------------------------
    # 5. Run the command
    # -------------------------
    try:
        subprocess.run(cmd, check=True, env=os.environ)
    except subprocess.CalledProcessError as e:
        print(f"Error running petta: {e}")
        sys.exit(e.returncode)
