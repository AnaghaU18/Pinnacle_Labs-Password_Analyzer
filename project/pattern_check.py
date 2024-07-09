import re
import report

def pswd_pattern(pswd):
    #global score
    patterns = {
            "Character repition": r'(.)\1{2,}',               # Character repetition
            "Sequential numbers": r'012|123|234|345|456|567|678|789|890',  # Sequential numbers
            "Sequential characters": r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz',  # Sequential characters
            "Common keyboard patterns": r'qwerty|asdf|zxcv|qaz|wsx|edc|rfv|tgb|yhn|ujm|ik,|ol\.|pl;'  # Common keyboard patterns
    }
    
    found_vulnerable_pattern = False

    for pattern in patterns.keys():
        if re.search(patterns[pattern], pswd, re.IGNORECASE):
            report.recommend(f"Avoid {pattern} pattern")
            report.score -= 1
            found_vulnerable_pattern = True
    
    if found_vulnerable_pattern:
        report.pswd_strength("No common/vulnerable patterns")