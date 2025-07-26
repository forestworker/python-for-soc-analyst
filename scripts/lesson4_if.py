name = input("What is your name? ")
failed_logins = int(input("Enter number of failed login attempts: "))

if failed_logins >= 5:
    print(f"ALERT! Possible brute-force attack on account {name}!")
elif failed_logins >= 3:
    print(f"Warning {name}, suspicious activity detected.")
else:
    print(f"All clear, {name}.")