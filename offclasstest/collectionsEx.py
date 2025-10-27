states=['west bengal','chennai','jammu and kashmir']
states.append('odhisa')
print(states)

print('********************************************************************************')

states.sort()
print(states)

print('******************************************************************************')

data=(23244,99979)
print(data)
data1=('parthib',7886868,'qweryusvgbs')
#data.append(77863)
print(data)
print(data1)


set1={1,44,66}
set2={33,554,87}
set3=set1.union(set2)
print(set3)

student = {"name": "Gopi", "age": 25}
student["city"] = "Mumbai"
student["phone"]=7747474747
print(student)


from collections import defaultdict

inventory = defaultdict(int)# the int is the datatype
inventory['apple1'] = 0
inventory['apple'] += 5
inventory['banana'] += 3
inventory['orange'] += 2
inventory['apple1'] += 10
inventory["ccc"] += 7

collectiong=defaultdict(list)

collectiong=[('A',1),('B',34),('A',56)]
print(collectiong)


add_100=lambda y:y+10
print(add_100(0.5))

 
# List of employees with their names and salaries
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Charlie", "salary": 40000}
]

# Sorting by salary, and then by name alphabetically
sorted_employees = sorted(employees, key=lambda x: (x["salary"], x["name"]))

print(sorted_employees)
sorted_employees = sorted(
    employees, 
    key=lambda x: (-x['salary'], x['name'])
)

print(sorted_employees)

