file = open("teams.txt", "r")

lines = "This is a new line" + "\n"
file.readline()
lines += file.readline()
lines += file.readline()
lines += file.readline()
lines += file.readline()

file = open("teams.txt", "w")
file.write(lines)


file.close()
