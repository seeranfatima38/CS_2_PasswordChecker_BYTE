# TASK - 2 Password Strength Checker

# SETINGS
MIN_LENGTH = 10         # minimum length to earn a point
STRONG_LENGTH = 12     # length that earns an extra point
WEAK_MAX_SCORE = 2    # score up to this = Weak
MODERATE_MAX_SCORE = 5 # score up to this = Moderate, above = Strong

# a few passwords that are always weak, no matter what
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "letmein", "yodaddu"]


def check_password(password):
    score = 0
    tips = []

    # Rule 1: length
    if len(password) >= MIN_LENGTH:
        score = score + 1
    else:
        tips.append("Use at least " + str(MIN_LENGTH) + " characters")

    if len(password) >= STRONG_LENGTH:
        score = score + 1

    # Rules 2-5: character types
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_lower:
        score = score + 1
    else:
        tips.append("Add lowercase letters")

    if has_upper:
        score = score + 1
    else:
        tips.append("Add uppercase letters")

    if has_digit:
        score = score + 1
    else:
        tips.append("Add numbers")

    if has_special:
        score = score + 1
    else:
        tips.append("Add special characters like ! @ # $")

    # Rule 6: common passwords are always weak
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips.append("This is a very common password")

    # turn the score into a category
    if score <= WEAK_MAX_SCORE:
        category = "Weak"
    elif score <= MODERATE_MAX_SCORE:
        category = "Moderate"
    else:
        category = "Strong"

    return category, score, tips


# ---- main program ----
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    category, score, tips = check_password(password)

    print("Strength:", category)
    print("Score:", score, "out of 6")

    if len(tips) > 0:
        print("How to improve:")
        for tip in tips:
            print(" -", tip)