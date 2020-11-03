plainText = input("Type your text here : ")
key = int(input("Type the key : "))

char = ""

if key < 0 or key > 25:
    print("Give a valid key.")
else:
    for i in plainText:
        Ascii = ord(i)
        index = Ascii + key
        if Ascii > 64 and Ascii < 91:
            if index > 64 and index < 91:
                char = char + chr(index)
            elif index > 90 and index < 116:
                rem = index % 91
                indx = rem + 65
                char = char + chr(indx)
        elif Ascii > 96 and Ascii < 123:
            if index > 96 and index < 123:
                char = char + chr(index)            
            elif index > 122 and index < 148:
                rem = index % 123
                indx = rem + 97
                char = char + chr(indx)
        elif Ascii > 47 and Ascii < 58:
            if index > 47 and index < 58:
                char = char + chr(index)
            elif index > 57 and index < 83:
                rem = index % 58
                indx = (rem % 10) + 48
                char = char + chr(indx)
        
        else:
            char = char + i

    print(char)   
            

    
        
    
