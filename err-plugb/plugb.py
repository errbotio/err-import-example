# vim: sta:et:sw=4:ts=4:sts=4

"""nah"""
from errbot import BotPlugin, botcmd

class BotTest(BotPlugin):
    """ Test """
    @botcmd
    def b(self, *args):
        """ test self messaging """
        return 'yeah I am b'


