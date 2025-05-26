def getScore(score : int) -> str:
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    x = input( "Enter your score: ")
    try:
        score = getScore(int(x))
        print("Your score is: " + score)
    except ValueError as e:
        print("Error: " + str(e))