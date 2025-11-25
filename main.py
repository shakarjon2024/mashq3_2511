# 1 - misol
def bahola(scores):
    result = []
    for s in scores:
        if s >= 90:
            result.append("A")
        elif s >= 70:
            result.append("B")
        elif s >= 50:
            result.append("C")
        else:
            result.append("D")
    return result


print(bahola((95, 67, 40, 82)))



# 2 - misol
def tasnif(ismlar):
    natija = []
    for ism in ismlar:
        if len(ism) < 3:
            natija.append("juda qisqa")
        elif len(ism) <= 5:
            natija.append("normal")
        else:
            natija.append("uzun")
    return natija

print(tasnif(["Ali", "Doniyor", "Ziyod", "Noz"]))



# 3 - misol
reverse_concat = lambda a, b: (a + b)[::-1]

# Misol:
print(reverse_concat("salom", "dunyo"))



# 4 - misol
check_age = lambda age: "ruxsat" if age >= 18 else "taqiqlanadi"


print(check_age(10))   
print(check_age(18))  
