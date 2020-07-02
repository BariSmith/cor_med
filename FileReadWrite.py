import os

# Функції для перевірки наявності файлу, читання з файлу, запису у файл

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filePath):
    if not fileExists(filePath):
        print('Файл, ' + filePath + 'відсутній - не можу прочитати.')
        return ''

    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data        


#  Функції для відкриття файлу, написання та читання рядків за один раз та закриття файлу

def openFileForWriting(filePath):
    fileHandle = open(filePath, 'w')
    return fileHandle

def writeALine(fileHandle, lineToWrite):

    lineToWrite = lineToWrite + '\n'
    fileHandle.write(lineToWrite)

def openFileForReading(filePath):
    if not fileExists(filePath):
        print('Файл, ' + filePath + 'відсутній - не можу прочитати.')
        return ''
    
    fileHandle = open(filePath, 'r')
    return fileHandle

def readALine(fileHandle):
    theLine = fileHandle.readline()

    #Це спеціальна перевірка спроб читання минулого кінця файлу(EOF).
    # Якщо це відбувається, повертаємо коли щось незвичне: False (which is not a string)
    # Якщо користувач бажає перевірити, код може легко виявити кінець файлу, :
    # if returnedValue is False:
    # досягнуто кінця файлу (EOF)
    
    if theLine == '':  # знайдено кінець файлу, return False
        return False
     
    #  Якщо рядок закінчується символом нового рядка '\ n', зніміть його з кінця
    if theLine.endswith('\n'):
        theLine = theLine.rstrip('\n')
        
    return theLine

def closeFile(fileHandle):
    fileHandle.close()
