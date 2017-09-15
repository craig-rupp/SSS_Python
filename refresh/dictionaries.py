my_set = {1, 2, 3}
print(my_set)
example = {'name' : 'Oscar', 'age': 27, 'grades' : [85, 74, 91]}
lottery_player = {
    'name' : 'Rolf',
    'numbers' : (13, 26, 18, 19)
}
universities = [
    {
        'name' : 'University of Texas at Austin',
        'location' : 'Austin, TX'
    },
    {
        'name' : 'Kingsman Academy',
        'location' : 'Stratford Upon England'
    }
]
for university in universities:
    print(university)

two_levels = {
    'defense' : {
        'CentreBack' : 'Koscielny',
        'WingBack' : 'Bellerin',
        'LWB' : 'Kolasinac'
    },
    'midfield' : {
        'HoldingMF': 'Xhaka',
        'BoxToBox' : 'Ramsey',
        'AttackingMf' : 'Ozil'
    },
    'attack' : {
        'RF' : 'Welbeck',
        'CF' : 'Lacazette',
        'LF' : 'Sanchez'
    }
}
print(two_levels['defense']['WingBack'])
print(sum(lottery_player['numbers'])/ len(lottery_player['numbers']))