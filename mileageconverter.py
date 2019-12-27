''' Converter miles to kilometers '''

print(f"Hello there,\nhow many miles is your next ultra trail?")
miles = input() # input returns a string from the user input
kilometers = float(miles) * 1.60934 # int would chop off decimals and reduce precison

print(f"\nCool, your ultra trail of {miles} miles is in kilometers {kilometers} km long")