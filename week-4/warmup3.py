#Warmup 3 Set Operations
language_list1 = ["BASIC", "Pascal", "Assembly", "Fortran", "C", "C++", "Perl", "Java", "XML", "HTML", "CSS", "JavaScript", "Visual Basic", "VB.NET", "C#"]
language_list2 = ["HTML", "XML", "CSS", "JavaScript", "TypeScript", "JSON", "PHP", "SQL", "Python"]

#Convert list to set

language_list1_set1 = set(language_list1)
language_list1_set2 = set(language_list2)

#print language sets
print(language_list1_set1 | language_list1_set2) # Union: All languages from both lists, no duplicates
print(language_list1_set1 & language_list1_set2) # Intersection: Languages in both lists
print(language_list1_set1 - language_list1_set2) # Difference: Languages only in the first list