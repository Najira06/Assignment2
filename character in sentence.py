sentence = input("Enter a sentence: ")
for char in sentence:
    if char == "a" or char=="e" or char=="i" or char=="o" or char=="u":
        continue
    print(char)
