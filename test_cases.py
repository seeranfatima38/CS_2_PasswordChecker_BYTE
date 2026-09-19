# ---- settings you can change (configurable thresholds) ----
MIN_LENGTH = 8         # minimum length to earn a point
STRONG_LENGTH = 12     # length that earns an extra point
WEAK_MAX_SCORE = 3     # score up to this = Weak
MODERATE_MAX_SCORE = 5 # score up to this = Moderate, above = Strong
 
# a few passwords that are always weak, no matter what
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "letmein"]
 
 
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
 
 
# ---- test cases ----
tests = [
    # (password, expected category)
    ("abc", "Weak"),
    ("password", "Weak"),
    ("12345678", "Weak"),
    ("password123", "Weak"),
    ("Hello123", "Moderate"),
    ("Pass@123", "Moderate"),
    ("Tr0ub4dor&3", "Moderate"),
    ("Correct#Horse9Battery", "Strong"),
    ("MyC0ol&SafePass!", "Strong"),
]
 
passed = 0
 
for password, expected in tests:
    category, score, tips = check_password(password)
 
    if category == expected:
        result = "PASS"
        passed = passed + 1
    else:
        result = "FAIL"
 
    print(result, "|", password, "| expected:", expected, "| got:", category)
 
print()
print(passed, "of", len(tests), "tests passed")
 