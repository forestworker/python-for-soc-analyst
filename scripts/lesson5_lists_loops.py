names = ["Dawid", "Ola", "Gosia"]
attempts = [1, 3, 5]

for name, num_attempts in zip(names, attempts):
    if num_attempts >= 5:
        print(f"ALERT! {name} had {num_attempts} failed login attempts!")
    elif num_attempts >= 3:
        print(f"Warning: {name} had {num_attempts} failed logins.")
    else:
        print(f"OK: {name} had only {num_attempts} attempts.")