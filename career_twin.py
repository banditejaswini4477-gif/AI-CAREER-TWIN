print("=====AI CAREER TWIN=====")
name=input("Enter your name:")
target=input("Enter yor target job:")
java=int(input("Java level(1-10):"))
dsa=int(input("DSA level(1-10):"))
python=int(input("Python level(1-10):"))
sql=int(input("SQL level(1-10):"))
ml=int(input("ML level(1-10):"))
oop=int(input("OOP level(1-10):"))
dl=int(input("Deep Learning Level(1-10):"))

print("\n===== YOUR CAREER PROFILE =====")
print("Name:",name)
print("Target:",target)
print("Java:",java)
print("DSA:",dsa)
print("Python:",python)
print("SQL:",sql)
print("ML:",ml)
print("OOP:",oop)
print("Deep Learning:",dl)


print("\n===== SKILL ANALYSIS =====")

if java>=7:
    print("java: Strong")
elif java>=4:
    print("java: Average")
else:
    print("java: Weak")

if dsa>=7:
    print("DSA: Strong")
elif dsa>=4:
    print("DSA: Average")
else:
    print("DSA: Weak")

if python>=7:
    print("python: Strong")
elif python>=4:
    print("python: Average")
else:
    print("python: Weak")

if sql>=7:
    print("SQL: Strong")
elif sql>=4:
    print("SQL: Average")
else:
    print("SQL: Weak")

if ml>=7:
    print("Machine Learning: Strong")
elif ml>=4:
    print("Machine Learning: Average")
else:
    print("Machine Learning: Weak")

if oop>=7:
    print("object oriented programing:Strong")
elif oop>=4:
    print("object oriented programing:Average")
else:
    print("object oriented programing:Weak")

if dl>=7:
    print("Deep Learning: Strong")
elif dl>=4:
    print("Deep Learning: Average")
else:
    print("Deep Learning: Weak")


print("\n ===== CAREER READINESS =====")

score=(java+dsa+python+sql+ml+oop+dl)/70*100
print("Career Readiness Score:",round(score,2),"%")
if score>=80:
    print("Status: Excellent")
elif score>=60:
    print("Status: Good")
elif score>=40:
    print("Status: Needs Improvement")
else:
    print("Status: Beginner")


print("\n===== SKILL GAP =====")

weakest_skill="java"
lowest_score=java

if dsa<lowest_score:
    weakest_skill="DSA"
    lowest_score=dsa

if python<lowest_score:
    weakest_skill="Python"
    lowest_score=python

if sql<lowest_score:
    weakest_skill="SQL"
    lowest_score=sql

if ml<lowest_score:
    weakest_skill="Machine Learning"
    lowest_score=ml

if oop<lowest_score:
    weakest_skill="object oriented programing"
    lowest_score=oop

if dl<lowest_score:
    weakest_skill="Deep Learning"
    lowest_score=dl

print("weakest_skill:",weakest_skill)
print("Current Level:",lowest_score)


print("\n ===== ALL SKILLGAPS =====")

weak_skills=[]

if java<4:
    weak_skills.append("Java")

if dsa<4:
    weak_skills.append("DSA")

if python<4:
    weak_skills.append("Python")

if sql<4:
    weak_skills.append("SQL")

if ml<4:
    weak_skills.append("Machine Learning")

if oop<4:
    weak_skills.append("object oriented programing")

if dl<4:
    weak_skills.append("Deep Learning")

if len(weak_skills)==0:
    print("No Weak Skills")
else:
    print("Weak Skills:")

    for skill in weak_skills:
        print("-",skill)


print("\n ===== JOB REQUIREMENT ANALYSIS =====")

job=target.lower()

if "ai" in job or "ml" in job:
    required_skills=["Python","DSA","SQL","Machine Learning","Deep Learning"]

elif "software" in job or "developer" in job:
    required_skills=["Java","DSA","SQL","OOP"]

else:
    required_skills=["DSA","SQL","Python"]

print("Target Job:",target)
print("Required Skills:")

for skill in required_skills:
    print("-",skill)


print("\n ===== SKILL MATCH ANALYSIS =====")

missing_skills=[]

for skill in required_skills:
    if skill=="Java" and java==0:
        missing_skills.append(skill)
    elif skill=="DSA" and dsa==0:
        missing_skills.append(skill)
    elif skill=="SQL" and sql==0:
        missing_skills.append(skill)
    elif skill=="OOP" and oop==0:
        missing_skills.append(skill)
    elif skill=="Python" and python==0:
        missing_skills.append(skill)
    elif skill=="Machine Learning" and ml==0:
        missing_skills.append(skill)
    elif skill=="Deep Learning" and dl==0:
            missing_skills.append(skill)

print("Target job:",target)
print("Missing skills:")
if len(missing_skills)==0:
    print("No missing skills!")
else:
    for skill in missing_skills:
        print("-",skill)

