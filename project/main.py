import getpass
import strength_eval
import report
import pattern_check
import pswd_eval

def main():
    # Using getpass to securely get user input without echoing
    pswd = getpass.getpass("Enter password: ")
    
    # Masking the password input
    print(f"\nEntered password: {'*' * len(pswd)}")

    # Password Strength Evaluation
    strength_eval.pswd_length(pswd)
    strength_eval.pswd_complexity(pswd)

    # Password Entropy and Dictionary Check
    pswd_eval.pswd_entropy(pswd)
    pswd_eval.pswd_dict_check(pswd)

    # Pattern Check
    pattern_check.pswd_pattern(pswd)

    # Score and Report
    print(f"Password Score: {report.score}/15")
    if report.score < 15:
        opt = input("Would you like to view the strengths and recommendations? [y/n]: ").lower()
        if opt == 'y':
            report.report()
    print("\nThank you for using this password analyzer!")

if __name__ == "__main__":
    main()
