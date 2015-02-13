import argparse

# To enable this option, add the following line to ~/.Xresources:
# xterm*disallowedWindowOps:
# Then run "xrdb -merge ~/.Xresources" and restart xterm.
XTERM_WINOPS_ENABLED = "xtermWinopsEnabled"

parser = argparse.ArgumentParser()
parser.add_argument("--disable-xterm-checksum-bug",
                    help="Don't use buggy parameter order for DECRQCRA",
                    action="store_true")
parser.add_argument("--include",
                    help="Regex for names of tests to run.",
                    default=".*")
parser.add_argument("--expected-terminal",
                    help="Terminal in use. Modifies tests for known differences.",
                    choices=("iTerm2", "xterm"),
                    default="iTerm2")
parser.add_argument("--no-print-logs",
                    help="Print logs after finishing?",
                    action="store_true")
parser.add_argument("--test-case-dir",
                     help="Create files with test cases in the specified directory",
                     default=None)
parser.add_argument("--stop-on-failure",
                    help="Stop running tests after a failure.",
                    action="store_true")
parser.add_argument("--force",
                    help="If set, assertions won't stop execution.",
                    action="store_true")
parser.add_argument("--options",
                    help="Space-separated options that are enabled.",
                    nargs="+",
                    choices=[ XTERM_WINOPS_ENABLED ])
parser.add_argument("--max-vt-level",
                    help="Do not run tests requiring a higher VT level than this.",
                    type=int,
                    default=5)

