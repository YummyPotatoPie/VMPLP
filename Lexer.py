import LexerFunction as LF
import Registers as RG
import LowLevelFunctions as LLF

STRINGS = []
TEMP_TOKENS = []
TOKENS = []

Code = open('TEST_CODE.elp', 'r')

for line in Code: #Считывание кода
    if line == '\n':
        continue
    else:
        STRINGS.append(line)

for i in range(len(STRINGS)): #Создание токенов
    ERROR = False
    WORD = ''
    for j in range(len(STRINGS[i])):
        if STRINGS[i][0] == ' ':
            print('ERROR: Invalid code')
            ERROR = True
            break
        elif STRINGS[i][j] == ' ':
            TEMP_TOKENS.append(WORD)
            WORD = ''
            j += 1
        elif STRINGS[i][j] == ',' or STRINGS[i][j] == ';' or STRINGS[i][j] == '(' or STRINGS[i][j] == ')':
            TEMP_TOKENS.append(WORD)
            TEMP_TOKENS.append(STRINGS[i][j])
            WORD = ''
        else:
            WORD += STRINGS[i][j]
    if ERROR == True:
        break

for i in range(len(TEMP_TOKENS)):
    if TEMP_TOKENS[i] != '':
        TOKENS.append(TEMP_TOKENS[i])
    else:
        continue

STRINGS = []
TEMP_TOKENS = []

LF.Analyser(TOKENS)