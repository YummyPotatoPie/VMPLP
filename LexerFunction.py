import KEY_WORDS as KW
import Registers as RG
import LowLevelFunctions as LLF



def VAR_VALUE_TYPE(VALUE: str): #Функция определяет тип переменной 
    if (VALUE[0]  == "'" and VALUE[-1] == "'") or (VALUE[0]  == '"' and VALUE[-1] == '"'):
        return 'STR'
    elif VALUE == 'False' or VALUE == 'True':
        return 'BOOL'
    elif (VALUE[0] in KW.NUMBERS) and (VALUE[0] != '0'):
        for i in range(len(VALUE)):
            if (VALUE[i] not in KW.NUMBERS) and VALUE[i] != '.':
                return 'ERROR: Invalid value'
        if '.' in VALUE:
            return 'FLOAT'
        else:
            return 'INT'
    else:
        return 'ERROR: Invalid value'

def VAR_TYPE_REG(TYPE: str, NAME_VALUE: str): #Функция добавления типа переменной в регистр с переменной
    RG.VAR_REGISTERS[LLF.RegName(NAME_VALUE) - 1].append(TYPE)
    return None

def VAR_VALUE_REG(VALUE: str): #Функция добавления значений переменных в регистры (возвращеет номер регистра в который помещено значение переменной)
    for i in range(len(RG.DATA_REGISTERS)):
        if RG.DATA_REGISTERS[i] == '':
            RG.DATA_REGISTERS[i] += str(VALUE)
            return i + 1
    return 0

def VAR_REG(NAME_TOKEN: str): #Функция добавления имени переменной в регистр:
    for i in range(len(RG.VAR_REGISTERS)):
        if len(RG.VAR_REGISTERS[i]) == 0:
            RG.VAR_REGISTERS[i].append(NAME_TOKEN)
            return None
    return None

def VAR_OP(OP_TOKEN: str): #Функция проверки оператора присваивания
    if OP_TOKEN == KW.OPERATORS[0]:
        return True
    return False

def VAR_NAME_CHECK(NAME_TOKEN: str): #Функция проверки имени переменной
    for i in range(len(RG.VAR_REGISTERS)):
        if len(RG.VAR_REGISTERS[i]) != 0:
            if (RG.VAR_REGISTERS[i][0] == NAME_TOKEN) or (NAME_TOKEN in KW.KEY_WORDS) or (NAME_TOKEN in KW.OPERATORS):
                return False
    return True

def VAR_VALUE(VALUE: str, VAR_NAME: str): #Функция добавления номера регистра где находится значение переменной
    RG.VAR_REGISTERS[LLF.RegName(VAR_NAME) - 1].append(VAR_VALUE_REG(VALUE))
    return None

def VAR_ANALYSYS(TOKENS_PART: list): #Функция анализа строки присваивания
    TYPE = VAR_VALUE_TYPE(TOKENS_PART[-1])
    if TYPE != 'ERROR: Invalid value':
        if VAR_NAME_CHECK(TOKENS_PART[0]):
            if VAR_OP(TOKENS_PART[1]):
                VAR_REG(TOKENS_PART[0])
                VAR_VALUE(TOKENS_PART[-1], TOKENS_PART[0])
                VAR_TYPE_REG(TYPE, TOKENS_PART[0])
                return True
            else:
                return False
        else:
            return False
    else:
        return False




def OUT_OP(OP_TOKEN: str): #Функция проверки оператора вывода
    if OP_TOKEN == KW.OPERATORS[1]:
        return True
    return False

def OUT_VALUE_CHECK(NAME_TOKEN: str): #Функция проверки выводимого значения
    if (NAME_TOKEN[1][0]  == "'" and NAME_TOKEN[1][-1] == "'") or (NAME_TOKEN[1][0]  == '"' and NAME_TOKEN[1][-1] == '"'):
        return 0
    else: 
        for i in range(len(RG.VAR_REGISTERS)):
            if len(RG.VAR_REGISTERS[i]) != 0:
                if RG.VAR_REGISTERS[i][0] == NAME_TOKEN:
                    return 1
        if (NAME_TOKEN not in KW.KEY_WORDS) and (NAME_TOKEN not in KW.OPERATORS):
            return 2
    return -1

def OUT_STR(STR_TOKEN: str): #Функция вывода строк
    print(STR_TOKEN)
    return None

def OUT_VAR_NAME(NAME_TOKEN: str): #Функция вывода значений переменных
    print(RG.DATA_REGISTERS[RG.VAR_REGISTERS[LLF.RegName(NAME_TOKEN) - 1][1] - 1])
    return None

def OUT_NUM(NUM_TOKEN: str): #Функция вывода числовых значений
    print(NUM_TOKEN)
    return None

def OUT_ANALYSYS(TOKENS_PART: list): #Функция обработки вывода
    if OUT_VALUE_CHECK(TOKENS_PART[-1]):
        if OUT_OP(TOKENS_PART[0]):
            if OUT_VALUE_CHECK(TOKENS_PART[-1]) == 0:
                OUT_STR(TOKENS_PART[-1])
                return True
            elif OUT_VALUE_CHECK(TOKENS_PART[-1]) == 1:
                OUT_VAR_NAME(TOKENS_PART[-1])
                return True
            elif OUT_VALUE_CHECK(TOKENS_PART[-1]) == 2:
                OUT_NUM(TOKENS_PART[-1])
                return True
            else:
                return False
        else:
            return False
    else:
        return False




def PROD_REG(PROD_VALUE: float): #Функции добавления значений переменной во временный регистр:
    RG.TEMP_REGISTER1 += str(PROD_VALUE)
    return None

def SUM_REG(SUM_VALUE: float):
    RG.TEMP_REGISTER2 += str(SUM_VALUE)
    return None

def DIV_REG(DIV_VALUE: float):
    RG.TEMP_REGISTER3 += str(DIV_VALUE)
    return None





def Analyser(TOKENS: list): #Функция анализа токенов
    for i in range(len(TOKENS)):
        if (TOKENS[i] in KW.KEY_WORDS):

            if TOKENS[i] == KW.KEY_WORDS[0]: #Начало обработки строки присваивания
                j = i
                while TOKENS[j] != ';':
                    if TOKENS[j + 1] in KW.KEY_WORDS:
                        return 'ERROR: Invalid syntax'
                    j += 1
                if VAR_ANALYSYS(TOKENS[i + 1 : j]):
                    continue
                else:
                    return 'ERROR: Invalid syntax'

            elif TOKENS[i] == KW.KEY_WORDS[1]: #Начало обработки строки вывода
                j = i
                while TOKENS[j] != ';':
                    if TOKENS[j + 1] in KW.KEY_WORDS:
                        return 'ERROR: Invalid syntax'
                    j += 1
                if OUT_ANALYSYS(TOKENS[i + 1 : j]):
                    continue
                else:
                    return 'ERROR: Invalid syntax'

            elif TOKENS[i] == KW.KEY_WORDS[2]: #Начало обработки строки умножения
                j = i
                while TOKENS[j] != ';':
                    if TOKENS[j + 1] in KW.KEY_WORDS:
                        return 'ERROR: Invalid syntax'
                    j += 1
                if PROD_ANALYSYS(TOKENS[i + 1 : j]):
                    continue
                else:
                    return 'ERROR: Invalid syntax'
    return ''

