# Password_Analyzer
A utility for evaluating password strength, detecting weaknesses, and recommending secure password practices.

## Features
- Length Check: A minimum length of 12 characters has been fixed.
- Complexity Check: Ensures that the password includes a combination of lowercase letters, uppercase letters, numbers and special characters.
- Entropy Calculation: Measures the randomness of the password. This helps determine its strength against brute-force attacks.
- Common Password Dictionary Check: Verifies if the user input password is among the most commonly used passwords as listed in text file ''.
- Pattern Detection: Recognises and suggests patterns to avoid, including sequential characters and keyboard patterns.
- Masked Input: Securely prompts users to enter the password without displaying the characters.
- Scoring System: 

## Installation

  ```sh

  ```

## Usage

```sh
python main.py
```

## Files
- main.py - Handles user input and calls the password analysis functions.
- strength_eval.py - Checks password length and complexity.
- pswd_eval.py - Calculates password entropy and checks against the common password dictionary.
- pattern_check.py - Recognises and suggests avoiding common password patterns.
- report.py - Manages scoring and generates reports based on the analysis
