# Initialize score and lists for strengths and recommendations
score = 15
strengths = []
rec = []

def pswd_strength(message):
    """Add a strength message to the strengths list."""
    strengths.append(f"+ {message}")

def recommend(message):
    """Add a recommendation message to the recommendations list."""
    rec.append(message)

def report():
    """Print the password strengths and recommendations."""
    if strengths:
        print("Password Strengths:")
        for i in strengths:
            print(i)
    else:
        print("No strong points")
    
    if rec:
        print("\nRecommendations:")
        for i in rec:
            print(i)
