def generate_suffix_combinations(phone_number):
    """
    Given a phone number string, extract its last five digits
    and append every three-digit sequence from 000 to 999.
    Returns a list of 1,000 strings.
    """
    # Ensure we have at least 5 digits
    if len(phone_number) < 5 or not phone_number[-5:].isdigit():
        raise ValueError("Phone number must be at least 5 digits long.")

    base = phone_number[-5:]
    combos = [f"{base}{i:03d}" for i in range(1000)]
    return combos

def main():
    phone = "07500000000".strip()
    try:
        passwords = generate_suffix_combinations(phone)
    except ValueError as e:
        print(f"Error: {e}")
        return

    output_file = "generated_passwords.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

    print(f"✔ Generated {len(passwords)} combinations and saved to '{output_file}'")

if __name__ == "__main__":
    main()
