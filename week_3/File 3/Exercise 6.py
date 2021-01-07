countries = ["Chile", "Slovenia", "Denmark", "Sam", "Syria", "Greece", "China", "USA", "Sam"]

word = "Sam"
sam_count = 0
for country in countries:
    if country == word:
        break
    else:
        sam_count += 1

print("Sam is occuring this many times:", sam_count)
