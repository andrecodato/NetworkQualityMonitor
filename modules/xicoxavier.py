import csv

from modules.debug.NQMDebug import NQMDebug


class XicoXavier(NQMDebug):
    def create_simple_res_file(self, file_name):
        with open(("results/" + file_name + '.csv'), "w") as simple_res:
            writer = csv.writer(simple_res, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(['Ping', 'Download', 'Upload', 'Server'])

    def create_full_res_file(self, file_name):
        with open(("results/" + file_name + '.csv'), "w") as full_res:
            writer = csv.writer(full_res, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(['Server Name', 'Server Country', 'Server Sponsor',
                             'Server ID', 'Client IP', 'Client ISP', 'Ping',
                             'Download', 'Upload', 'Share Link'])

    def append_simple_res(self, file_name, results_to_append):
        with open("results/" + file_name + ".csv", "a") as simple_res:
            writer = csv.writer(simple_res, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(results_to_append)

    def append_full_res(self, file_name, results_to_append):
        with open("results/" + file_name + ".csv", "a") as full_res:
            writer = csv.writer(full_res, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(results_to_append)
