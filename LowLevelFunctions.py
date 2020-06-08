import Registers as RG

def RegName(VAR_NAME: str): #Функция определяет в каком регистре находится переменная под именем VAR_NAME
    if VAR_NAME == '':
        return 0
    for i in range(len(RG.VAR_REGISTERS)):
        if RG.VAR_REGISTERS[i][0] == VAR_NAME:
            return i + 1
    return 0
