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
