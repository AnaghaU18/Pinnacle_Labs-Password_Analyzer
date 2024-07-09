import re
import math
import report

def pswd_entropy(pswd):
    #global score
    charset_size = sum(bool(re.search(pattern, pswd)) for pattern in [
            "[a-z]", "[A-Z]", "[0-9]", "[!@#$%^&*(),.?\":{}|<>]"
        ])
    
    entropy = len(pswd) * math.log2(charset_size) if charset_size > 0 else 0
    
    if entropy <= 16:
        report.recommend(f"Low entropy should be increased.")
        report.score -= 2
    elif entropy <= 20:
        report.pswd_strength("Medium Entropy")
        report.recommend(f"Medium entropy is good, however it would be better to increase the entropy.")
        report.score -= 1
    else:
        report.pswd_strength(f"Strong entropy")

def pswd_dict_check(pswd):
    #global score
    common_passwords_file = "10-million-password-list-top-1000000.txt"
    try:
        with open(common_passwords_file, "r") as f:
            common_passwords = f.read().splitlines()
            if pswd in common_passwords:
                report.recommend("Avoid using common passwords")
                report.score -= 1
            else:
                report.pswd_strength("Uncommon password")
    except FileNotFoundError:
        print(f"Warning: {common_passwords_file} not found. Common password check skipped.")
    except Exception as e:
        print(f"Error reading {common_passwords_file}: {e}")