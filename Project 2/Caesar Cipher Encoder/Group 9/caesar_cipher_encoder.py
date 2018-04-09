# caesar cipher encoder

alphaL = [chr(i) for i in range(ord("a"), ord("z") + 1)]
alphaU = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
wrd = input("Please insert your word: ")
wrdl = len(wrd)
nwrd = []
shift = 2

for i in range(0, wrdl):
    if wrd[i].isupper():
        ilet = alphaU.index(wrd[i])

        if ilet <= (25 - shift):
            x = ilet + shift
        else:
            x = (ilet - 25) + (shift - 1)
        nwrd += [alphaU[x]]
    else:
        ilet = alphaL.index(wrd[i])

        if ilet <= (25 - shift):
            x = ilet + shift
        else:
            x = (ilet - 25) + (shift - 1)
        nwrd += [alphaL[x]]

ewrd = "".join(nwrd)
print(ewrd)