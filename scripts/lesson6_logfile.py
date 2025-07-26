with open("logs.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print("ALERT! Error found:", line.strip())