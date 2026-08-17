print("=====AI CAREER TWIN=====")
name=input("Enter your name:")
target=input("Enter yor target job:")
java=int(input("Java level(1-10):"))
dsa=int(input("DSA level(1-10):"))
python=int(input("Python level(1-10):"))
sql=int(input("SQL level(1-10):"))
ml=int(input("ML level(1-10):"))

print("\n===== YOUR CAREER PROFILE =====")
print("Name:",name)
print("Target:",target)
print("Java:",java)
print("DSA:",dsa)
print("Python:",python)
print("SQL:",sql)
print("ML:",ml)



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


print("\n ===== CAREER READINESS =====")

score=(java+dsa+python+sql+ml)/50*100
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
    weakest_skill="Machine Learing"
    lowest_score=ml

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
    
if len(weak_skills)==0:
    print("No Weak Skills")
    
else:
    print("Weak Skills:")

    for skill in weak_skills:
        print("-",skill)
