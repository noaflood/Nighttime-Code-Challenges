#Code that calculates how many helium balloons it would 
#take to lift your desired object.
#
#helium balloon source: https://science.howstuffworks.com/science-vs-myth/everyday-myths/question185.htm
#average American source: https://news.gallup.com/poll/328241/americans-average-weight-holds-steady-2020.aspx
#Tesla source: https://weightofstuff.com/how-much-does-a-tesla-weigh/
#average house source (1): https://upgradedhome.com/how-much-does-a-house-weigh/ (2): https://www.hsh.com/homeowner/average-american-home.html
#Burj Khalifa source: https://www.burjkhalifa.ae/en/assets/FACT-SHEET.pdf 
#Mount Everest source: https://weightofstuff.com/how-much-does-mount-everest-weigh/ 

import math
import sys
import os

def calc_balloons(w):

    #calculate the number of balloons based on the weight of the object in poundds / 14 gram pull of a helium balloon, +1000 for lift
    balloons = round(int(w) / 0.0308) + 1000

    #format the string to have commas for readability
    balloons = format(balloons, ',d')
    os.system('clear')
    print("\nThat would take... about... {} balloons...\n".format(balloons))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

print('\nUp...\n\n\"Ellie, how much do you think the house weighs?\"')
input=input('Enter a weight in pounds, or enter a letter option below:\n(A) an average American\n(B) a Tesla model S\n(C) an average American house\n(D) the Burj Khalifa\n(E) Mount Everest\n')

if input=='A' or input=='a':
    weight = 181
    calc_balloons(weight)
elif input=='B' or input=='b':
    weight = 4793.5
    calc_balloons(weight)
elif input=='C' or input=='c':
    weight = 2435 * 200 * 2000
    calc_balloons(weight)
elif input=='D' or input=='d':
    weight = 500_000 * 2000
    calc_balloons(weight)
elif input=='E' or input=='e':
    weight = 357_000_000_000_000
    calc_balloons(weight)
elif is_number(input) and (input > 0) and (input < sys.float_info.max):
    weight = input
else:
    print("\"What?\"") 