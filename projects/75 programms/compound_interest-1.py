#compound_interest

def compound_interest(principle, rate, time):
 
    Amount = principle * (pow((1 + rate / 100), time))
    interest = Amount - principle
    print("Compound interest is", interest)
 
compound_interest(30000, 4.5, 30)
