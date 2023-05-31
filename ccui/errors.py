"""
CCUI's Error Codes
"""

# --Launch related errors--
# Responsible for restarting CCUI
class ExitCCUIRestart(Exception):
    pass


# Responsible for shutting down CCUI
class ExitCCUIShutdown(Exception):
    pass


# Responsible for reloading CCUI
class ExitCCUIReload(Exception):
    pass


# Responsible for switching CCUI mode
class SwitchCCUIMode(Exception):
    def __init__(self, mode):
        self.mode = mode

# ----