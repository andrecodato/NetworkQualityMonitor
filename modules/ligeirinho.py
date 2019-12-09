import time
import speedtest
import requests

from modules.debug.NQMDebug import NQMDebug


class Ligeirinho(NQMDebug):
    def make_speedtest(self):
        self.printa('Iniciando Ligeirinho...')
        time.sleep(3)
        self.printa('AI ARIBA, ARIBA!!!')
        try:
            self.printa('Realizando Speed Test...')
            # self.result = os.popen('speedtest-cli --single --json').read()

            # self.servers = []

            self.threads = 1

            self.s = speedtest.Speedtest()
            # self.s.get_servers(servers)
            self.s.get_servers()
            self.s.get_best_server()
            self.s.download(threads=self.threads)
            self.s.upload(threads=self.threads)
            self.s.results.share()

            self.results_dict = self.s.results.dict()
        except:
            self.printa('Deu erro na bagaça, reiniciando teste...')
            self.make_speedtest()

    def check_internet_connection(self):
        self.printa('Realizando checkup da conexão...')
        url = 'https://www.google.com'

        try:
            _ = requests.get(url, timeout=5)
            return True
        except requests.ConnectionError:
            self.printa(
                '[ERRO]Oh meu parceiro, não obtive acesso a rede mundial de comunicação!')
            return False

    def get_results(self):
        download = self.results_dict["download"]
        upload = self.results_dict["upload"]
        ping = self.results_dict["ping"]
        return download, upload, ping

    def get_full_results(self):
        return self.results_dict
