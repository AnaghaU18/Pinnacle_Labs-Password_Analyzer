score = 15
strengths = []
rec = []

def pswd_strength(message):
    strengths.append(f"+ {message}")

def recommend(message):
    rec.append(message)

def report():
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