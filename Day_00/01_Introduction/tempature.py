faren = raw_input("Enter the temperature in Fahrenheit): ")
faren = float(faren)             # The calculation on the right gets saved to the variable on the left
cel = 5./9. * (faren - 32.)
print "The temperature in Celcius is " + str(cel) + " degrees."