#!/usr/bin/env python3

import subprocess
import sys
import difflib
import os
import signal
from libs.libraries import BASIC_LIBS, STDLIB_ONLY

# ──────────────────────────────────────────────
#  COLOR CODES
# ──────────────────────────────────────────────
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"


# ──────────────────────────────────────────────
#  SIGNAL HANDLER — clean Ctrl+C, no traceback
# ──────────────────────────────────────────────
def _handle_sigint(sig, frame):
    print(f"\n\n  {YELLOW}Interrupted. Goodbye.{RESET}\n")
    sys.exit(0)

signal.signal(signal.SIGINT, _handle_sigint)


# ──────────────────────────────────────────────
#  HELPERS
# ──────────────────────────────────────────────
def banner():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           🐍  PYTHON LIBRARY INSTALLER  v1.1                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")


def separator():
    print(f"{DIM}{'─' * 62}{RESET}")


def run_pip(package: str) -> tuple:
    """Run pip install. Returns (success: bool, stderr: str)."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package, "--quiet"],
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stderr.strip()


def install_one(package: str, index: int = None, total: int = None) -> bool:
    prefix = ""
    if index is not None and total is not None:
        pct = int((index / total) * 100)
        bar_len = 20
        filled = int(bar_len * index / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        prefix = f"[{bar}] {pct:3d}%  "

    # stdlib packages ship with Python — skip pip
    if package.lower() in STDLIB_ONLY:
        print(
            f"  {DIM}{prefix}{RESET}{CYAN}Built-in{RESET}    "
            f"{BOLD}{package}{RESET} ...  {GREEN}✔ ships with Python{RESET}"
        )
        return True

    print(
        f"  {DIM}{prefix}{RESET}{CYAN}Installing{RESET}  {BOLD}{package}{RESET} ...",
        end="", flush=True
    )
    ok, err = run_pip(package)
    if ok:
        print(f"  {GREEN}✔ OK{RESET}")
    else:
        hint = ""
        if "No matching distribution" in err:
            hint = f" {DIM}(not found on PyPI){RESET}"
        elif "externally-managed" in err:
            hint = f" {DIM}(use venv or --break-system-packages){RESET}"
        print(f"  {RED}✘ FAILED{hint}{RESET}")
    return ok


def install_basic():
    separator()
    print(f"{BOLD}  📦 Installing {len(BASIC_LIBS)} libraries...{RESET}")
    separator()

    ok_count = 0
    fail_list = []

    for i, lib in enumerate(BASIC_LIBS, 1):
        ok = install_one(lib, i, len(BASIC_LIBS))
        if ok:
            ok_count += 1
        else:
            fail_list.append(lib)

    separator()
    print(f"\n  {GREEN}✔ Installed:{RESET} {ok_count}/{len(BASIC_LIBS)}")
    if fail_list:
        print(f"  {RED}✘ Failed ({len(fail_list)}):{RESET}")
        for f in fail_list:
            print(f"       {DIM}• {f}{RESET}")
    print()


def fuzzy_suggest(name: str):
    """Return top-3 closest library names from known list."""
    matches = difflib.get_close_matches(
        name.lower(),
        [lib.lower() for lib in BASIC_LIBS],
        n=3,
        cutoff=0.4,
    )
    lower_map = {lib.lower(): lib for lib in BASIC_LIBS}
    return [lower_map[m] for m in matches if m in lower_map]


def is_exact(name: str) -> bool:
    return name.lower() in {lib.lower() for lib in BASIC_LIBS}


def _print_all_libs():
    separator()
    print(f"{BOLD}  📋 All known libraries ({len(BASIC_LIBS)}):{RESET}")
    separator()
    cols = 4
    for i in range(0, len(BASIC_LIBS), cols):
        row = BASIC_LIBS[i:i + cols]
        line = "".join(f"  {lib:<30}" for lib in row)
        print(f"  {DIM}{line}{RESET}")
    separator()


def _get_input(prompt: str) -> str:
    """Safe input() — never raises, returns '' on EOF/interrupt."""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print()
        return ""


# ──────────────────────────────────────────────
#  INTERACTIVE MODE
# ──────────────────────────────────────────────
def interactive_mode():
    separator()
    print(f"{BOLD}  🔍 Interactive Installer — type library names{RESET}")
    print(f"  {DIM}'list' → show all  |  'done' / 'q' → exit mode{RESET}")
    separator()

    while True:
        raw = _get_input(f"\n  {CYAN}>{RESET} Library name: ")

        if not raw:
            continue

        cmd = raw.lower()

        if cmd in ("quit", "q", "exit", "done"):
            print(f"  {YELLOW}Leaving interactive mode.{RESET}")
            break

        if cmd == "list":
            _print_all_libs()
            continue

        # Exact match → install immediately
        if is_exact(raw):
            print(f"  {GREEN}✔ Recognized.{RESET} Installing {BOLD}{raw}{RESET}...")
            install_one(raw)
            continue

        suggestions = fuzzy_suggest(raw)

        if suggestions:
            print(f"\n  {YELLOW}⚠  '{raw}' not in known list. Did you mean:{RESET}")
            for idx, s in enumerate(suggestions, 1):
                print(f"       {BOLD}[{idx}]{RESET} {s}")
            print(f"       {BOLD}[n]{RESET} No — install '{raw}' as-is anyway")
            print(f"       {BOLD}[s]{RESET} Skip")

            while True:
                ans = _get_input(f"  {CYAN}>{RESET} Your choice: ").lower()

                if ans == "n":
                    print(f"  Installing {BOLD}{raw}{RESET} as-is...")
                    install_one(raw)
                    break
                elif ans in ("s", ""):
                    print(f"  {DIM}Skipped.{RESET}")
                    break
                elif ans in ("1", "2", "3"):
                    idx = int(ans) - 1
                    if idx < len(suggestions):
                        chosen = suggestions[idx]
                        print(f"  Installing {BOLD}{chosen}{RESET}...")
                        install_one(chosen)
                    break
                else:
                    print(f"  {RED}Invalid. Enter 1/2/3, n, or s.{RESET}")
        else:
            ans = _get_input(
                f"  {YELLOW}Unknown: '{raw}'. Install it anyway? [y/n]:{RESET} "
            ).lower()
            if ans == "y":
                install_one(raw)
            else:
                print(f"  {DIM}Skipped.{RESET}")


# ──────────────────────────────────────────────
#  MAIN MENU  (loop — no recursion, no crashes)
# ──────────────────────────────────────────────
def main_menu():
    while True:
        banner()
        print(f"  {BOLD}Choose an option:{RESET}\n")
        print(f"  {CYAN}[1]{RESET}  Install all basic libraries  {DIM}(~200 packages){RESET}")
        print(f"  {CYAN}[2]{RESET}  Interactive installer        {DIM}(search & pick){RESET}")
        print(f"  {CYAN}[3]{RESET}  Show all available libraries")
        print(f"  {CYAN}[q]{RESET}  Quit")
        separator()

        choice = _get_input(f"\n  {CYAN}>{RESET} Your choice: ").lower()

        if choice == "1":
            install_basic()
            print(f"  {GREEN}All done! Check the results above.{RESET}\n")
            _get_input(f"  {DIM}Press Enter to return to menu...{RESET}")

        elif choice == "2":
            interactive_mode()
            print(f"\n  {GREEN}Session finished.{RESET}\n")
            _get_input(f"  {DIM}Press Enter to return to menu...{RESET}")

        elif choice == "3":
            _print_all_libs()
            _get_input(f"\n  {DIM}Press Enter to return to menu...{RESET}")

        elif choice in ("q", "quit", "exit", ""):
            print(f"\n  {YELLOW}Goodbye.{RESET}\n")
            sys.exit(0)

        else:
            print(f"  {RED}  Invalid choice. Enter 1, 2, 3, or q.{RESET}\n")


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    if os.name == "nt":
        os.system("color")   # Enable ANSI colors on Windows CMD
    main_menu()