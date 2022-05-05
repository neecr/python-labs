word = "London is capital of Great Britain"
upper = 0
lower = 0

for i in word:
    if i.isupper():
        upper += 1
    else:
        lower += 1

print(upper, "большие буквы")
print(lower, "маленькие буквы")

