import report

def pswd_length(pswd):
    #global score
    if len(pswd) >= 12:
        report.pswd_strength(f"Password Length ({len(pswd)}) >= 12")
    else:
        report.recommend("Increase password length")
        if len(pswd) >= 9:
            report.score -= 1
        elif len(pswd) >= 6:
            report.score -= 2
        elif len(pswd) >= 3:
            report.score -= 3
        elif len(pswd) >= 0:
            report.score -= 4

def pswd_complexity(pswd):
    #global score
    char_types = {
            "lowercase": any(c.islower() for c in pswd),
            "uppercase": any(c.isupper() for c in pswd),
            "numeric": any(c.isdigit() for c in pswd),
            "special": any(not c.isalnum() for c in pswd)
            }

    missing_types = [name for name, found in char_types.items() if not found]

    if missing_types:
        if len(missing_types) <= 4:
            report.score -= len(missing_types)
        report.recommend(f"Include: {', '.join(missing_types)} characters")

    else:
        report.pswd_strength("Strong password complexity")