#Simple traffic light simulator
# Input from user
traffic_light = input("Enter the traffic light color (red, yellow, green): ")

# Output based on the traffic light color
if traffic_light == "red":
    print("STOP!")
elif traffic_light == "yellow":
    print("Prepare to stop")
elif traffic_light == "green":
    print("You can Go")
else:
    print("Wrong input")
    