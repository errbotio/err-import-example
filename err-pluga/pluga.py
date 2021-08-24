# vim: sta:et:sw=4:ts=4:sts=4

"""nah"""
from errbot import BotPlugin, botcmd

from common import addition


class BotTest(BotPlugin):
    """Test"""

    @botcmd
    def a(self, *args):
        """test self messaging"""
        return "yeah I am A and I know how to add 2+2=%d" % addition(2, 2)
