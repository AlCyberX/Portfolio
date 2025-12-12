'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
payperhour = float(input("Pay Per Hour: "))
desiredincome = float(input("Desired weekly income: "))

if payperhour > 0:
    hoursneeded = desiredincome / payperhour
    print("You need to work", format(hoursneeded, ".2f"), "hours to earn $", desiredincome)