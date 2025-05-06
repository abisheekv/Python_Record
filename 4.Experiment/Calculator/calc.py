import math
from stad_calc import basic as bc
from stad_calc import scientific as sc 
from stad_calc import conversion as cn
while True:
    
    n=(input(""" Enter the choice input or type "exit" to exit ~
        1. Basic Calculator Functions
        2. Scientific Calculator Functions
        3. Number Base Conversion\n"""))
    if n.lower() == "exit":
        break
    match(int(n)):
        case 1:
            n=(input(""" Enter the choice input or type "exit" to exit ~
            1. Addition
            2. Substract
            3. Multiplication
            4. Division
            5. Power
            6. Root
            7. Modulus \n"""))
        
        case 2:
            while True:
                n=(input(""" Enter the choice input or type "exit" to exit ~
                8. Exponent
                9. log(base 10)
                10. Natural Log
                11. Sine
                12. Cosine
                13. Tangent
                14. Cosec
                15. Sec
                16. Cot
                17. arcSine
                18. arcCosine
                19. arcTangent
                20. arcCosec
                21. arcSec
                22. arcCot
                23. Hyperbolic Sine
                24. Hyperbolic Cosine
                25. Hyperbolic Tangent
                26. Factorial: \n"""))
                if int(n) < 8 or int(n) > 26:
                    print("Please enter a valid input")
                else:
                    break
        
        case 3:
            while True:
                n=(input(""" Enter the choice input or type "exit" to exit ~
                27. Binary AND
                28. Binary OR
                29. Binary XOR
                30. Binary NOT
                31. Binary Left Shift
                32. Binary Right Shift
                33. Decimal to Binary
                34. Decimal to Octal
                35. Decimal to Hexadecimal
                36. Binary to Decimal
                37. Octal to Decimal
                38. Hexadecimal to Decimal\n"""))
                if int(n) < 27 or int(n) > 38:
                    print("Please enter a valid input")
                else:
                    break
    if(n.lower()=="exit"):
        break
    n=int(n)
    if 1 <= n <= 7:
        a,b=map(int,input("Enter the numbers for operation: ").split())
    if 11 <= n <= 26:
        a=int(input("Enter the number for operation: "))
        while True:
            b=input("Is the input in degree or radians? [d/r]: ").lower()
            if b == 'd':
                a=math.radians(a)
                break
            elif b == 'r':
                break
            else:
                print("Please enter either d or r for degree or radian") 
    if 27 <= n <= 38:
        if n in [27,28,29]:
            a,b=map(int,input("Enter the numbers for operation: ").split())
        else:
            a=int(input("Enter the number for operation: "))
    
    match n:
        case 1:
            print(bc.add(a,b))
        case 2:
            print(bc.sub(a,b))
        case 3:
            print(bc.mul(a,b))
        case 4:
            print(bc.div(a,b))
        case 5:
            print(bc.power(a,b))
        case 6:
            print(bc.root(a,b))
        case 7:
            print(bc.mod(a,b))
        case 8:
            print(sc.exp(a))
        case 9:
            print(sc.log10(a))
        case 10:
            print(sc.ln(a))
        case 11:
            print(round(sc.sin(a),3))
        case 12:
            print(round(sc.cos(a),3))
        case 13:
            print(round(sc.tan(a),3))
        case 14:
            print(round(sc.cosec(a),3))
        case 15:
            print(round(sc.sec(a),3))
        case 16:
            print(round(sc.cot(a),3))
        case 17:
            print(round(sc.arcsin(a),3))
        case 18:
            print(round(sc.arccos(a),3))
        case 19:
            print(round(sc.arctan(a),3))
        case 20:
            print(round(sc.arccosec(a),3))
        case 21:
            print(round(sc.arcsec(a),3))
        case 22:
            print(round(sc.arccot(a),3))
        case 23:
            print(round(sc.hypsin(a),3))
        case 24:
            print(round(sc.hypcos(a),3))
        case 25:
            print(round(sc.hyptan(a),3))
        case 26:
            print(sc.factorial(a))
        case 27:
            print(cn.band(a,b))
        case 28:
            print(cn.bor(a,b))
        case 29:
            print(cn.bxor(a,b))
        case 30:
            print(cn.bnot(a))
        case 31:
            print(cn.lshift(a))
        case 32:
            print(cn.rshift(a))
        case 33:
            print(cn.binary(a))
        case 34:
            print(cn.octal(a))
        case 35:
            print(cn.hexadecimal(a))
        case 36:
            print(cn.btodecimal(a))
        case 37:
            print(cn.otodecimal(a))
        case 38:
            print(cn.htodecimal(a))
        case _:
            print("Please enter a valid choice.")
                                                            


