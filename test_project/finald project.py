langDict = {}
# langDict = {"hello":{"Spanish":"hola","French":"bonjour"},
#             "good-bye":{"Spanish":"adios"}}

# infinite loop till user chooses to exit
while True:
    print(
        "Main Menu\n1 - translate a word\n2 - add word to dict\n3 - print current translation dictionary\n4 - "
        "exit\nPlease make a selection:")
    choice = input()
    # check if the input is a number or not
    if choice.isdigit():
        # if it is a number convert to int
        choice = int(choice)
        # translate a word
        if choice == 1:
            word = input("Provide an English word:")
            if word in langDict:
                print(langDict[word])
            else:
                print("Sorry no translation for that word")
        # add word to dict
        elif choice == 2:
            word = input("What Eng word are you providing a translation for:")
            if word in langDict:
                print("The word already exists:{0} - {1}".format(word, langDict[word]))
            language = input("What language is the translated word in:")
            translated = input("What is the translated word:")
            if word in langDict:
                langDict[word][language] = translated
            else:
                langDict[word] = {language: translated}
        # print current translation dictionary
        elif choice == 3:
            print(langDict)
        # exit
        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("**Invalid input")
    else:
        print("**Invalid input - integer only")
