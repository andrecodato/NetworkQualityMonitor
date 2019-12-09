import datetime

from modules.ligeirinho import Ligeirinho
from modules.xicoxavier import XicoXavier


class Main():
    li = Ligeirinho()
    xixa = XicoXavier()


# li.make_speedtest()
# print(li.get_full_results())

    xixa.create_simple_res_file("teste_simple")
    xixa.create_full_res_file("teste_full")


if __name__ == "__main__":
    Main()
