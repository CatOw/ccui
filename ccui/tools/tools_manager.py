"""
The tools manager of CCUI
"""

from cmd import Cmd
from rich import print as rprint

# CCUI Modules
from ccui.errors import (
    SwitchCCUIMode,
)

HELP_PATH = 'tools/utils/tools_prompt_help.txt'


class ToolsManagerPrompt(Cmd):
    def do_back(self, args: str):
        """
        back

        Description:
            Retrieve from Tools Manager back to CCUI.
        """
        if args.strip():
            return print("  Usage: back (no arguments)")
        raise SwitchCCUIMode('CCUI')


    do_quit = do_exit = do_return = do_back


def launch():
    pass


if __name__ == '__main__':
    launch()
