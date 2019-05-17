"""
Base commands used for Atharia
"""
from evennia.commands.default.muxcommand import MuxCommand, MuxAccountCommand
from .mixins import ArxCommmandMixin


class ArxCommand(ArxCommmandMixin, MuxCommand):
    """Base command for Characters for Atharia"""
    pass


class ArxPlayerCommand(ArxCommmandMixin, MuxAccountCommand):
    """Base command for Players/Accounts for Atharia"""
    pass
