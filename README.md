# CS_2_PasswordChecker_BYTE

A simple Python program that checks how strong a password is and gives tips to improve it.
Built for the Arithmatrix Virtual Internship Program (AVIP) 2026, Cybersecurity track, Task 2.

## How to Run
1. Install Python 3
2. Download `password_checker.py` and `test_cases.py`
3. Run the checker:

```
python password_checker.py
```

4. Run the tests:

```
python test_cases.py
```

## Rule Set
The program gives points for good password habits. The maximum score is 6.

| Rule | Points |
|------|--------|
| Length of 8 or more characters | +1 |
| Length of 12 or more characters | +1 |
| Has a lowercase letter | +1 |
| Has an uppercase letter | +1 |
| Has a number | +1 |
| Has a special character (! @ # $ etc.) | +1 |
| Is a known common password (e.g. "password", "123456") | Score reset to 0 |

## Strength Categories
| Score | Category |
|-------|----------|
| 0 to 3 | Weak |
| 4 to 5 | Moderate |
| 6 | Strong |

## Configurable Thresholds
These values are at the top of `password_checker.py` and can be changed:

| Setting | Default | Meaning |
|---------|---------|---------|
| `MIN_LENGTH` | 8 | Minimum length to earn a point |
| `STRONG_LENGTH` | 12 | Length that earns an extra point |
| `WEAK_MAX_SCORE` | 3 | Highest score still counted as Weak |
| `MODERATE_MAX_SCORE` | 5 | Highest score still counted as Moderate |

The list `COMMON_PASSWORDS` can also be edited.

## Sample Run
```
Enter a password to check: Hello123
Strength: Moderate
Score: 4 out of 6
How to improve:
 - Add special characters like ! @ # $
```

## Test Cases
The file `test_cases.py` checks these passwords:

| Password | Expected |
|----------|----------|
| abc | Weak |
| password | Weak |
| 12345678 | Weak |
| password123 | Weak |
| Hello123 | Moderate |
| Pass@123 | Moderate |
| Tr0ub4dor&3 | Moderate |
| Correct#Horse9Battery | Strong |
| MyC0ol&SafePass! | Strong |

## Screenshots
See the `screenshots/` folder for weak, moderate, and strong runs and the test results.

## Limitations
- The password is visible while typing. Real programs would hide it using Python's `getpass` module.
- The common-password list is very small. A real checker would use a much larger list.
- It checks rules only, so it can't detect patterns like "qwerty123".
