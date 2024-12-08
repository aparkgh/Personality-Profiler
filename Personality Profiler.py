def personality_profiler():
    print("Welcome to the Personality Profiler!")
    print("Answer the following questions to determine your personality type.")
    
    questions = [
        ("You enjoy social gatherings and meeting new people.", "E", "I"),
        ("You rely more on facts than intuition.", "S", "N"),
        ("You prioritize logic over emotions when making decisions.", "T", "F"),
        ("You like to have a structured plan rather than being spontaneous.", "J", "P"),
    ]
    
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    for question, option1, option2 in questions:
        print(f"\n{question}")
        answer = input(f"Enter '{option1}' or '{option2}': ").strip().upper()
        if answer == option1:
            scores[option1] += 1
        elif answer == option2:
            scores[option2] += 1
        else:
            print("Invalid input. Skipping question.")
    
    personality = (
        "E" if scores["E"] > scores["I"] else "I" +
        "S" if scores["S"] > scores["N"] else "N" +
        "T" if scores["T"] > scores["F"] else "F" +
        "J" if scores["J"] > scores["P"] else "P"
    )
    
    print(f"\nYour personality type is: {personality}")
    
personality_profiler()
