from generator import (
    generate_password,
    check_strength,
    generate_pin,
    generate_passphrase,
    generate_multiple
)


password = generate_password()

print("╔══════════════════════════════════════════╗")
print("        🔐 PASSWORD GENERATOR")
print("╠══════════════════════════════════════════╣")

print("Standard Password :", password)
print("Strength          :", check_strength(password), "💪")
