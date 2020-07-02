import random
from FileReadWrite import *

FILE_PATH = 'MultipleChoiceQuestions.txt'
LETTERS_LIST = ['a', 'b', 'c', 'd']

# відкриття файлу та читання заголовка
fileHandle = openFileForReading(FILE_PATH)
titleText = readALine(fileHandle)

# знаходження загальної кількості питаннь в тестові
nQuestions = readALine(fileHandle)
nQuestions =int(nQuestions)

print('Привіт!  Це тест:')
print()
print(titleText)  # друкуємо заголовок
print()
print('Він складається з', nQuestions, 'питань.')
print()
print("Успіху!")
print()

score = 0
# Кожного разу через цикл обробляйте одне запитання
for questionNumber in range(0, nQuestions):
    questionText = readALine(fileHandle)  # читання рядка з питанням
    answers =[]
    for i in range(0, 4):
        thisAnswer = readALine(fileHandle)  # прочитати кожну відповідь
        answers.append(thisAnswer)
   
    correctAnswer = answers[0]  # збереження правильної відповіді
    #random.shuffle(answers)  # рндом 4х відповідей
    indexOfCorrectAnswer = answers.index(correctAnswer) # дивимось де правильна відповідь

    # задати питання та 4 рандомні відповіді
    print()
    print(str(questionNumber + 1) +'. ' + questionText)
    for index in range(0, 4):
        thisLetter = LETTERS_LIST[index]
        thisAnswer = answers[index]
        thisAnswerLine = '' + thisLetter  + ')  ' + thisAnswer
        print(thisAnswerLine)   
    
    print()

    # перевірка, що користувач вводить дійсну відповідь на лист
    while True:
        userAnswer = input('Ваша відповідь (a, b, c, or d): ')
        userAnswer = userAnswer.lower()  # перетвореня внесеної відповіді в lowercase
        if userAnswer in LETTERS_LIST:  # перевірка валідності відповіді
            break   
        else:
            print('Будь ласка, виберіть a, b, c, or d')
        
    # знаходження індекса пов'язаного з відповюдю користувача

    indexOfUsersAnswer = LETTERS_LIST.index(userAnswer)

    # отримуємо feedback
    if indexOfCorrectAnswer == indexOfUsersAnswer:
        score = score + 1
        print('Правильно')
    else:
        print("Вибачте але це не правильно")
        correctLetter = LETTERS_LIST[indexOfCorrectAnswer]
        print('Правильною відповіддю було: ', correctLetter + ')  ' + correctAnswer)
        
    print()
    print('Ваш результат:', score)

# показуємо відсоток правильних відповідей
pctCorrect = (score * 100.)/ nQuestions
print()
print('Закінчено!    Ви відповіли на:', str(pctCorrect) + '% питань правльно ')

closeFile(fileHandle)
