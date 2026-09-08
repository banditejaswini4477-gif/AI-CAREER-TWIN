print("===== AI CAREER TWIN =====")


# ================= USER PROFILE =================

name = input("Enter your name: ")
target = input("Enter your target job: ").lower()


# ================= JOB DATABASE =================

jobs = {

    "ai engineer": {
        "skills": ["Python", "DSA", "SQL", "Machine Learning", "Deep Learning"],
        "description": "AI Engineers build and deploy AI and Machine Learning systems."
    },

    "java developer": {
        "skills": ["Java", "DSA", "OOP", "SQL"],
        "description": "Java Developers build software applications using Java."
    },

    "software developer": {
        "skills": ["Java", "DSA", "OOP", "SQL"],
        "description": "Software Developers design, build and maintain software."
    },

    "data scientist": {
        "skills": ["Python", "SQL", "Machine Learning", "Deep Learning"],
        "description": "Data Scientists analyze data and build predictive models."
    }
}


# ================= REQUIRED SKILL LEVELS =================

required_levels = {
    "Python": 8,
    "Java": 8,
    "DSA": 7,
    "OOP": 8,
    "SQL": 7,
    "Machine Learning": 8,
    "Deep Learning": 7
}


# ================= CHECK TARGET JOB =================

if target not in jobs:

    print("\nJob not available.")

    print("Available jobs:")

    for job in jobs:
        print("-", job)

else:

    required_skills = jobs[target]["skills"]


    # ================= JOB REQUIREMENT ANALYSIS =================

    print("\n===== JOB REQUIREMENT ANALYSIS =====")

    print("Target Job:", target.title())

    print("Job Description:")
    print(jobs[target]["description"])

    print("\nRequired Skills:")

    for skill in required_skills:
        print("-", skill)


    # ================= USER SKILL INPUT =================

    print("\n===== ENTER YOUR SKILL LEVELS =====")

    skills = {}

    for skill in required_skills:

        level = int(
            input(
                "Enter your " + skill + " level (1-10): "
            )
        )

        skills[skill] = level


    # ================= DAY 9: SKILL GAP ANALYSIS =================

    print("\n===== SKILL GAP ANALYSIS =====")

    skill_gaps = {}

    for skill in required_skills:

        required = required_levels[skill]

        current = skills[skill]

        gap = required - current

        if gap < 0:
            gap = 0

        skill_gaps[skill] = gap

        print(
            skill,
            "| Required Level:", required,
            "| Your Level:", current,
            "| Gap:", gap
        )


    # ================= USER PROFILE =================

    print("\n===== USER PROFILE =====")

    print("Name:", name)
    print("Target Job:", target.title())

    print("\nYour Skills:")

    for skill, level in skills.items():

        print(skill + ":", level)


    # ================= SKILL ANALYSIS =================

    print("\n===== SKILL ANALYSIS =====")

    for skill, level in skills.items():

        if level >= 7:
            print(skill + ": Strong")

        elif level >= 4:
            print(skill + ": Average")

        else:
            print(skill + ": Weak")


    # ================= CAREER READINESS SCORE =================

    print("\n===== CAREER READINESS =====")

    total_ratio = 0

    for skill in required_skills:

        required=required_levels[skill]
        current=skills[skill]

        if current>=required:
            ratio=1
        else:
            ratio=current/required
        total_ratio+=ratio

    score=(total_ratio/len(required_skills))*100

    print("Career Readiness Score:",round(score,2),"%")

    if score >= 80:
        print("Status: Excellent")

    elif score >= 60:
        print("Status: Good")

    elif score >= 40:
        print("Status: Needs Improvement")

    else:
        print("Status: Beginner")


    # ================= WEAKEST SKILL DETECTION =================

    print("\n===== WEAKEST SKILL DETECTION =====")

    weakest_skill = min(
        skills,
        key=skills.get
    )

    print(
        "Weakest Skill:",
        weakest_skill
    )

    print(
        "Current Level:",
        skills[weakest_skill]
    )


    # ================= MULTIPLE SKILL GAP DETECTION =================

    print("\n===== MULTIPLE SKILL GAP DETECTION =====")

    weak_skills = []

    for skill, level in skills.items():

        if level < 4:
            weak_skills.append(skill)

    if len(weak_skills) == 0:

        print("No weak skills.")

    else:

        print("Skills that need improvement:")

        for skill in weak_skills:

            print("-", skill)


    # ================= SKILL MATCH ANALYSIS =================

    print("\n===== SKILL MATCH ANALYSIS =====")

    matched_skills = []
    missing_skills = []

    for skill, level in skills.items():

        if level == 0:
            missing_skills.append(skill)

        else:
            matched_skills.append(skill)


    print("Target Job:", target.title())


    print("\nMatched Skills:")

    if len(matched_skills) == 0:

        print("No matched skills.")

    else:

        for skill in matched_skills:
            print("-", skill)


    print("\nMissing Skills:")

    if len(missing_skills) == 0:

        print("No missing skills.")

    else:

        for skill in missing_skills:
            print("-", skill)


    # ================= PERSONALIZED ROADMAP =================

    print("\n===== PERSONALIZED ROADMAP =====")

    roadmaps = {

        "Python": [
            "Python Basics",
            "Functions",
            "Lists and Dictionaries",
            "OOP in Python",
            "Python Project"
        ],

        "DSA": [
            "Arrays",
            "Strings",
            "Hashing",
            "Two Pointers",
            "Trees"
        ],

        "SQL": [
            "SQL Basics",
            "Joins",
            "Subqueries",
            "Grouping and Aggregation",
            "Advanced SQL"
        ],

        "Machine Learning": [
            "Python for Machine Learning",
            "NumPy and Pandas",
            "Machine Learning Basics",
            "Model Evaluation",
            "Machine Learning Project"
        ],

        "Deep Learning": [
            "Neural Networks",
            "Deep Learning Basics",
            "CNN",
            "RNN",
            "Deep Learning Project"
        ],

        "Java": [
            "Java Basics",
            "Variables and Data Types",
            "Conditions and Loops",
            "Arrays",
            "Methods",
            "Collections",
            "Exception Handling",
            "Java Problems"
        ],

        "OOP": [
            "Classes and Objects",
            "Constructors",
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Abstraction",
            "Interfaces"
        ]
    }


    for skill in weak_skills:

        print("\nRoadmap for", skill)

        if skill in roadmaps:

            topics = roadmaps[skill]

            for i in range(len(topics)):

                print(
                    i + 1,
                    "-",
                    topics[i]
                )

        else:

            print("Roadmap not available.")


print("\n===== END OF CAREER TWIN =====")



# ================= DAY 11 ================= 
# CAREER COMPARISON & ALTERNATIVE CAREER RECOMMENDATION 
 
 
# ================= ALL SKILLS ================= 
 
all_skills = list(required_levels.keys()) 
 
 
# ================= ENTER ALL USER SKILLS ================= 
 
print("\n===== ENTER YOUR OVERALL SKILL LEVELS =====") 
 
user_skills = {} 
 
for skill in all_skills: 
 
    level = int( 
        input( 
            "Enter your " + skill + " level (1-10): " 
        ) 
    ) 
 
    user_skills[skill] = level 
 
 
# ================= CAREER FIT ANALYSIS ================= 
 
career_fit_scores = {} 
 
for career, details in jobs.items(): 
 
    career_skills = details["skills"] 
 
    total_ratio = 0 
 
    for skill in career_skills: 
 
        required = required_levels[skill] 
        current = user_skills[skill] 
 
        if current >= required: 
            ratio = 1 
        else: 
            ratio = current / required 
 
        total_ratio += ratio 
 
    fit_score = ( 
        total_ratio / len(career_skills) 
    ) * 100 
 
    career_fit_scores[career] = fit_score 
 
 
# ================= CAREER COMPARISON ================= 
 
print("\n===== CAREER COMPARISON =====") 
 
sorted_careers = sorted( 
    career_fit_scores.items(), 
    key=lambda x: x[1], 
    reverse=True 
) 
 
for career, score in sorted_careers: 
 
    print( 
        career.title(), 
        ":", 
        round(score, 2), 
        "%" 
    ) 
 
 
# ================= BEST CAREER RECOMMENDATION ================= 
 
print("\n===== CAREER RECOMMENDATION =====") 
 
best_career = sorted_careers[0][0] 
best_score = sorted_careers[0][1] 
 
print( 
    "Best Career Fit:", 
    best_career.title() 
) 
 
print( 
    "Career Fit Score:", 
    round(best_score, 2), 
    "%" 
) 
 
 
# ================= ALTERNATIVE CAREERS ================= 
 
print("\n===== ALTERNATIVE CAREERS =====") 
 
if len(sorted_careers) > 1: 
 
    for i in range(1, len(sorted_careers)): 
 
        career, score = sorted_careers[i] 
 
        print( 
            i, 
            "-", 
            career.title(), 
            "| Fit:", 
            round(score, 2), 
            "%" 
        ) 
 
else: 
 
    print("No alternative careers available.")
