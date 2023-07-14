import letters


def processing(sentence):
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    row5 = ""
    row6 = ""
    row7 = ""
    row8 = ""
    row9 = ""
    row10 = ""
    for letter in sentence:
        if letter == " ":
            row1 += findrow(letter, 0)
            row2 += findrow(letter, 1)
            row3 += findrow(letter, 2)
            row4 += findrow(letter, 3)
            row5 += findrow(letter, 4)
            row6 += findrow(letter, 5)
            row7 += findrow(letter, 6)
            row8 += findrow(letter, 7)
            row9 += findrow(letter, 8)
            row10 += findrow(letter, 9)   
            print(row1 +"\n"+ row2 +"\n"+ row3 +"\n"+ row4 +"\n"+ row5 +"\n"+ row6 +"\n"+ row7 +"\n"+ row8 +"\n"+ row9 +"\n"+ row10) 
            print("\n")
            row1 = ""
            row2 = ""
            row3 = ""
            row4 = ""
            row5 = ""
            row6 = ""
            row7 = ""
            row8 = ""
            row9 = ""
            row10 = ""
        else: 
            row1 += findrow(letter, 0)
            row2 += findrow(letter, 1)
            row3 += findrow(letter, 2)
            row4 += findrow(letter, 3)
            row5 += findrow(letter, 4)
            row6 += findrow(letter, 5)
            row7 += findrow(letter, 6)
            row8 += findrow(letter, 7)
            row9 += findrow(letter, 8)
            row10 += findrow(letter, 9)

    print(row1 +"\n"+ row2 +"\n"+ row3 +"\n"+ row4 +"\n"+ row5 +"\n"+ row6 +"\n"+ row7 +"\n"+ row8 +"\n"+ row9 +"\n"+ row10)
    print("\n")
        
        

def findrow(letter, row):
    if letter == 'A' or letter == 'a':
        return letters.A[row]
    elif letter == 'B' or letter == 'b':
        return letters.B[row]
    elif letter == 'C' or letter == 'c':
        return letters.C[row]
    elif letter == 'D' or letter == 'd':
        return letters.D[row]
    elif letter == 'E' or letter == 'e':
        return letters.E[row]
    elif letter == 'F' or letter == 'f':
        return letters.F[row]
    elif letter == 'G' or letter == 'g':
        return letters.G[row]
    elif letter == 'H' or letter == 'h':
        return letters.H[row]
    elif letter == 'I' or letter == 'i':
        return letters.I[row]
    elif letter == 'J' or letter == 'j':
        return letters.J[row]
    elif letter == 'K' or letter == 'k':
        return letters.K[row]
    elif letter == 'L' or letter == 'l':
        return letters.L[row]
    elif letter == 'M' or letter == 'm':
        return letters.M[row]
    elif letter == 'N' or letter == 'n':
        return letters.N[row]
    elif letter == 'O' or letter == 'o':
        return letters.O[row]
    elif letter == 'P' or letter == 'p':
        return letters.P[row]
    elif letter == 'Q' or letter == 'q':
        return letters.Q[row]
    elif letter == 'R' or letter == 'r':
        return letters.R[row]
    elif letter == 'S' or letter == 's':
        return letters.S[row]
    elif letter == 'T' or letter == 't':
        return letters.T[row]
    elif letter == 'U' or letter == 'u':
        return letters.U[row]
    elif letter == 'V' or letter == 'v':
        return letters.V[row]
    elif letter == 'W' or letter == 'w':
        return letters.W[row]
    elif letter == 'X' or letter == 'x':
        return letters.X[row]
    elif letter == 'Y' or letter == 'y':
        return letters.Y[row]
    elif letter == 'Z' or letter == 'z':
        return letters.Z[row]
    elif letter == '!':
        return letters.exclamationPoint[row]
    elif letter == '?':
        return letters.questionMark[row]
    elif letter == '.':
        return letters.dot[row]
    elif letter == ':':
        return letters.colon[row]
    elif letter == '*':
        return letters.times[row]
    elif letter == '=':
        return letters.equals[row]
    elif letter == '+':
        return letters.plus[row]
    elif letter == '-':
        return letters.minus[row]
    elif letter == '/':
        return letters.slash[row]
    elif letter == '1':
        return letters.num1[row]
    elif letter == '2':
        return letters.num2[row]
    elif letter == '3':
        return letters.num3[row]
    elif letter == '4':
        return letters.num4[row]
    elif letter == '5':
        return letters.num5[row]
    elif letter == '6':
        return letters.num6[row]
    elif letter == '7':
        return letters.num7[row]
    elif letter == '8':
        return letters.num8[row]
    elif letter == '9':
        return letters.num9[row]
    elif letter == '0':
        return letters.num0[row]
    
    elif letter == " ":
        return letters.space[row]
    

sentence = input("Give a sentence: ")
print("\n")
processing(sentence)