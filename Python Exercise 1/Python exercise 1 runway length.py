speed = float(input("Enter the plane's take off speed in m/s:"))
acceleration = float(input("Enter the plane's acceleration in m/s2:"))

runway_length = ((speed**2)/(2*acceleration))

format_runway = "{:.4f}" .format(runway_length)
print("The minimum runway length needed for this airplane is", format_runway, 'meters')
