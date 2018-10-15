import Basic3 
toEncode = input('Enter the string to encode- ')
toIncrease = int(input('Enter a number (To decrease put negative sign) - '))
alpha = input ('Enter the alphabet- ').replace(",",'').replace(" ",'')
lengthOfAlpha = len(alpha)
if toIncrease > (lengthOfAlpha-1):
    incrementOf = toIncrease % lengthOfAlpha;
else:
    incrementOf = toIncrease;
for x in toEncode:
    if x==' ':
        print(' ', end='')
    else:
        print(Basic3.sencode(alpha, x, incrementOf), end='')

        #abcdefghijklmnopqrstuvwxyz