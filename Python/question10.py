temp_in_celsius = float(input("Enter temperature in Celsius: "))

#Convert to Fahrenheit (°F = °C × 9/5 + 32)
temp = (temp_in_celsius * 9/5) + 32
print("Temperature in Fahrenheit is:", temp)

#Output 
if temp_in_celsius <0:
    print("Very cold! Wear thick jacket")
elif 0 <= temp_in_celsius <15:
    print("Cold! Wear a jacket")
elif 16 <= temp_in_celsius <25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")
