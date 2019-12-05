import os
import json

from debug.NQMDebug import NQMDebug


class Ligeirinho(NQMDebug):
    def __init__(self):
        self.printa('Iniciando Ligeirinho...')
        try:
            self.printa('Realizando Speed Test...')
            self.result = os.popen('speedtest-cli --json').read()
        except:
            self.printa('Deu erro na bagaça, reiniciando teste...')
            self.__init__()


ligeiro = Ligeirinho()
