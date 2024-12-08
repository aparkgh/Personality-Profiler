def personality_checker():
    print("Welcome to the Personality Checker!")
    print("Answer the following questions with 'Y' for Yes or 'N' for No to determine your personality type.")

    questions = [
        ("You enjoy social gatherings and meeting new people.", "E", "I"),
        ("You rely more on facts than intuition.", "S", "N"),
        ("You prioritize logic over emotions when making decisions.", "T", "F"),
        ("You like to have a structured plan rather than being spontaneous.", "J", "P"),
    ]
    
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    for question, positive_trait, negative_trait in questions:
        print(f"\n{question}")
        answer = input("Enter 'Y' (Yes) or 'N' (No): ").strip().upper()
        if answer == "Y":
            scores[positive_trait] += 1
        elif answer == "N":
            scores[negative_trait] += 1
        else:
            print("Invalid input. Please enter 'Y' or 'N'. Skipping question.")
    
    # calculate personality type
    personality = (
        ("E" if scores["E"] > scores["I"] else "I") +
        ("S" if scores["S"] > scores["N"] else "N") +
        ("T" if scores["T"] > scores["F"] else "F") +
        ("J" if scores["J"] > scores["P"] else "P")
    )
    
    print(f"\nYour personality type is: {personality}")
    
personality_checker()
