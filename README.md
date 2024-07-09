# Password_Analyzer
A utility for evaluating password strength, detecting weaknesses, and recommending secure password practices.

## Features
- Length Check: A minimum length of 12 characters has been fixed.
- Complexity Check: Ensures that the password includes a combination of lowercase letters, uppercase letters, numbers and special characters.
- Entropy Calculation: Measures the randomness of the password. This helps determine its strength against brute-force attacks.
- Common Password Dictionary Check: Verifies if the user input password is among the most commonly used passwords as listed in text file ''.
- Pattern Detection: Recognises and suggests patterns to avoid, including sequential characters and keyboard patterns.
- Masked Input: Securely prompts users to enter the password without displaying the characters.
- Scoring System: Assigns a score, maximum 15, based on the checks. Points are deducted for every wekaness found.
- Report Generation: Generates a report listing the strengths of the password and recommendations to improve the password strength.

## Usage
1. Clone the repository:

```sh
git clone https://github.com/AnaghaU18/Pinnacle_Labs-Password_Analyzer.git
cd project
```

2. Ensure u have the required Python version (Python 3.6 or higher).

3. Run the utility:

```sh
python main.py
```

## Files
- main.py - Handles user input and calls the password analysis functions.
- strength_eval.py - Checks password length and complexity.
- pswd_eval.py - Calculates password entropy and checks against the common password dictionary.
- pattern_check.py - Recognises and suggests avoiding common password patterns.
- report.py - Manages scoring and generates reports based on the analysis.

## Example
Test case: Tr0ub4dor&3

```bash
Enter password: 

Entered password: ***********
Password Score: 14/15
Would you like to view the strengths and recommendations? [y/n]: y
Password Strengths:
+ Strong password complexity
+ Strong entropy
+ Uncommon password

Recommendations:
Increase password length

Thank you for using this password analyzer!
```
