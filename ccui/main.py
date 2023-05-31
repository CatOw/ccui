"""
The main interaction console of CCUI
"""

from cmd import Cmd
from rich import print as rprint

# CCUI Modules
import ccui.util
from ccui.errors import (
    ExitCCUIRestart,
    ExitCCUIShutdown,
    ExitCCUIReload,
    SwitchCCUIMode,
)

HELP_PATH = 'utils/ccui_prompt_help.txt'


class CCUIPrompt(Cmd):
    def do_help(self, args: str) -> None:
        """
        help

        Description:
            Provide all commands.
        """
        if args.strip():
            return print("  Usage: help (no arguments)")
        ccui.util.output_file_content(HELP_PATH)


    def do_man(self, command: str) -> None:
        """
        Description:
            Provide a manual for given command.

        Parameter List:
            command -- Displays manual for specific given command.
        """
        if not command.strip():
            return print('  Usage: man [command]')
        try:
            print(getattr(self, "do_" + command).__doc__)
        except AttributeError:
            rprint(f"[#E74856]ERROR: No such command '{command}'[/#E74856]")


    def do_restart(self, args: str) -> None:
        """
        restart

        Description:
            A complete restart of CCUI to update code changes.
        """
        if args.strip():
            return print("  Usage: restart (no arguments)")
        raise ExitCCUIRestart

    
    def do_shutdown(self, args: str) -> None:
        """
        shutdown

        Description:
            Shutdown CCUI.
        """
        if args.strip():
            return print("  Usage: shutdown (no arguments)")
        raise ExitCCUIShutdown


    def do_reload(self, args: str):
        """
        reload

        Description:
            Reload CCUI.
        """
        if args.strip():
            return print("  Usage: reload (no arguments)")
        raise ExitCCUIReload


    def do_clear(self, args: str) -> None:
        """
        clear

        Description:
            Clear the terminal.
        """
        if args.strip():
            return print("  Usage: clear (no arguments)")
        ccui.util.clear()


    def do_tools(self, args: str) -> None:
        """
        tools

        Description:
            Show available tools.
        """
        if args.strip():
            return print("  Usage: tools (no arguments)")
        ccui.util.output_file_content('utils/ccui_tools.txt')


    def do_tool(self, args: str) -> None:
        """
        tool (no arguments)

        Description:
            Activate the tools manager.
        """
        if args.strip():
            return print('  Usage: tool (no arguments)')
        raise SwitchCCUIMode('ToolsMgr')


    def do_pac(self, args: str) -> None:
        """
        An upcoming feature which will allow to install
        community made contributions.
        """
        rprint("[#B4009E]An upcoming command!")


    def do_quote(self, args: str) -> None:
        """
        quote

        Description:
            Nice quotes :)
        """
        if args.strip():
            return print("But I don't have any arguments >:(")
        ccui.util.output_random_quote()


    # -Alternative names for commands-
    # do_ is an identifier for commands
    do_commands = do_help
    do_reboot = do_restart
    do_exit = do_quit = do_stop = do_shutdown
    do_refresh = do_reload
    do_cls = do_clear
    do_addon = do_plug = do_tweak = do_pac


def launch(fresh_launch: bool = True) -> None:
    """
    Handles the CCUI initial prompt, Prevents KeyboardInterrupt.

    Keyword arguments:
    fresh_launch -- set default prompt (default True)
    """
    # The loop will ever be broken only if:
    # 1. Fatal error.
    # 2. Restart.
    # 3. Shutdown.
    # 4. Reload.

    # Default prompt, CCUI
    prompt = CCUIPrompt()
    mode = "[CCUI] >> "

    while True:
        try:
            prompt.prompt = mode

            if fresh_launch:
                # This runs ONLY if launched by __main__.py
                ccui.util.clear()
                prompt.cmdloop(ccui.util.output_file_content("utils/ccui_logo.txt", "*", "CCUI"))
            else:
                prompt.cmdloop()

        # Handle Prompt Exceptions
        except KeyboardInterrupt:
            print("^C")
        except SwitchCCUIMode as switch_mode:
            # Initializes the mode's class
            mode = f"[{switch_mode.mode}] >> "
            
        finally:
            fresh_launch = False


if __name__ == '__main__':
    launch()
