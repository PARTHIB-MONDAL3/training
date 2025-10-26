s = input("Enter a string: ")
#s=s.lower() to convert in lower
#vowels = "aeiouAEIOU"
vowels=set("aeiouAEIOU")# faster test on large input
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
