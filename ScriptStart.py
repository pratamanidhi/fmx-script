import json
from config import Config as _config
from Suite import Suite as _suite
import time
from Utils import  Utils as _utils

if __name__ == "__main__":
    _utils.Initiate_Script()
    print("------- Sistem Login Started -------")
    login = _suite._Login()
    print("")
    print("------- Start Edit Cell Lines -------")
    _suite._getInventoryCellLine(login)
    print("")
    time.sleep(2)
    print("------- Start Edit Empty Plate -------")
    _suite._getInventoriesEmpPlate(login)
    print("")
    time.sleep(2)
    print("------- Start Edit Media -------")
    _suite._getInventoryMedia(login)
    print("")
    time.sleep(2)
    print("------- Start Edit Trypsin -------")
    _suite._getInventoryTrypsin(login)
    print("")
    time.sleep(2)
    print("------- Start Edit Empty Trough -------")
    _suite._getInventoryEmpT(login)
    print("")
    time.sleep(2)
    print("------- Start Edit Tip Caddy -------")
    _suite._getInventoryCaddy(login)
    print("")
    print("=== Start Accelerate System ===")
    _suite._changeMultiplier(login)
    print("")
    # while True:
    #     status = _suite._getCellStatus(login)
    #     if (status[0] == True) and (status[1] == True):
    #         print("onDone finish")
    #     break
    # print("Put Protocols here")

    print("=== wait for 10 minutes ===")
    time.sleep(600)
    print("------- Sistem Login Started -------")
    login = _suite._Login()
    print("")
    print("== Start Register Protocols ==")
    _suite._getCellLines(login)
    time.sleep(2)
    _utils.Finist_Script()
