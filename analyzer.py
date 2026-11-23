"""Local, educational password feedback based on transparent rules."""

from getpass import GetPassWarning, getpass
import warnings

COMMON = {"password", "password123", "123456", "qwerty", "letmein", "admin", "iloveyou"}
SEQUENCES = ("0123456789", "abcdefghijklmnopqrstuvwxyz", "qwertyuiop", "asdfghjkl", "zxcvbnm")


def analyze(password: str) -> tuple[str, int, list[str]]:
    """Return a rating, character-group count and feedback without echoing input."""
    groups = sum(
        (
            any(char.islower() for char in password),
            any(char.isupper() for char in password),
            any(char.isdecimal() for char in password),
            any(not char.isalnum() and not char.isspace() for char in password),
        )
    )
    normalized = password.casefold()
    sequence = any(
        row[index:index + 4] in normalized or row[index:index + 4][::-1] in normalized
        for row in SEQUENCES
        for index in range(len(row) - 3)
    )
    repeated = any(
        normalized[index] == normalized[index + 1] == normalized[index + 2]
        for index in range(len(normalized) - 2)
    )
    common = normalized in COMMON
    feedback = []
    if len(password) < 15:
        feedback.append("Try a longer password or a passphrase with unrelated words.")
    if groups < 3:
        feedback.append("This uses few character groups. Favor length and unpredictability.")
    if common:
        feedback.append("This matches an entry in the built-in common-password list.")
    if sequence or repeated:
        feedback.append("Avoid consecutive keyboard/alphabet patterns or repeated characters.")

    if len(password) < 8 or common:
        rating = "Weak"
    elif len(password) < 15 or sequence or repeated:
        rating = "Needs improvement"
    else:
        rating = "Stronger by these checks"
    return rating, groups, feedback


def main() -> int:
    print("Use a made-up example for this exercise.")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", GetPassWarning)
            password = getpass("Example password: ")
    except (EOFError, KeyboardInterrupt, GetPassWarning):
        print("\nInput canceled or hidden input is unavailable. Use an interactive terminal.")
        return 1
    if not password.strip():
        print("Enter a non-blank example.")
        return 1
    rating, groups, feedback = analyze(password)
    print(f"{rating} | {len(password)} characters | {groups} of 4 character groups")
    for item in feedback:
        print(f"- {item}")
    print("Use a unique password per account. A heuristic rating cannot guarantee security.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
