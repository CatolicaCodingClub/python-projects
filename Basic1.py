msg = 'abcdefghijklmopqrstuvwxyzab'
inp = input('A letter ')
letterat = msg.index(inp.lower(),0, len(msg))
if len(inp) > 1:
    print ('enter only one letter')
else:
    if (ord(inp) > 64) & (ord(inp) < 91):
        print ((msg[letterat+2]).upper())
    else:
        print (msg[letterat+2])
   
    
    
