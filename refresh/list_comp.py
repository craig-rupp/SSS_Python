my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
print(an_equal_list)
a_multiple_list = [x * 3 for x in range(6)]
print(a_multiple_list)

print(9 % 2) # will be modulus 1
print([n for n in range(10) if n % 2 == 0])
people_you_know = ["Rolf", " Craig", "BEN ", "CRYSTaL"]
normalized_people = [person.strip().lower() for person in people_you_know]
print(people_you_know)
print(normalized_people)
capital_first_letter = []
for peep in normalized_people:
    capital_first_letter.append(peep[0].upper() + peep[1:])

print(capital_first_letter)
re_structured = []
