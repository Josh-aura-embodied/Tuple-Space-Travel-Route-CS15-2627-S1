
mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

# Display the first destination
print("First destination:", mission_route[0])

# Display the last destination
print("Last destination:", mission_route[-1])

# Display the total number of destinations
print("Total destinations:", len(mission_route))

# Display every destination in order
print("Mission Route:")
for destination in mission_route:
    print(destination)

# Check whether Europa is included
if "Europa" in mission_route:
    print("Europa is part of the mission route!")
else:
    print("Europa is not part of the mission route.")
