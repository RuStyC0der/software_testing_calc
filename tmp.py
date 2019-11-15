import re
import os
if __name__ == '__main__':
    with open("calc.ui", "r") as ui:
        a = ui.read()
        z = re.findall("comboBox_\d+", a)
        z = set(z)
        # print(z)
        for i in z:
            print("self.ui.", i, ".", "addItem(\"cm\", 1)", sep="")
            print("self.ui.", i, ".", "addItem(\"m\", 100)", sep="")
            print("self.ui.", i, ".", "addItem(\"km\", 100000)", sep="")
    # for i in range(10000):
    #     print(i)
