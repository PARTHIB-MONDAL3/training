vowels = set("aeiouAEIOU")
vowel_names = []

for _ in range(5):
    name = input("Enter a name: ").strip()#strip removes the whitespaces
    if name and name[0] in vowels:
#This first ensures the string isn’t empty (name is truthy only if it has at least one character), then checks whether the first character name is a vowel by testing membership in the vowels collection; 
# if both conditions hold, the name qualifies as starting with a vowel
        vowel_names.append(name)
#vowel_names.sort() #sort alphabetically order
print("Names starting with a vowel:", vowel_names)
