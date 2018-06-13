from pprint import pprint
W = 'Weapons'
B = 'Blades'
S = 'Shields'
H = 'Helmets'
A = 'Armor'

testing_products = [
    (101, W, 'Arakh of Khal Drogo', 250),
    (315, W, 'Needle, Sword of Arya Stark', 1050),
    (918, S, 'Stark Infantry Shield', 760),
]

def individual_tupe(tupe):
  it_string = '* {weapon}: ${price}\n  Buy now using code: {category}-{code}'.format(weapon=tupe[-2],
  price=tupe[-1], category=tupe[1][0], 
  code=tupe[0])
  return it_string

def products_final(prod_arr):
  prod_format_arr = []
  for tupes in prod_arr:
    prod_format_arr.append(individual_tupe(tupes))
  return '\n'.join(prod_format_arr)
print(products_final(testing_products))

testing_recipients = """
Jon Snow <jon@starks.com>,
arya@starks.com   ,
Eddard "Ned" Stark <ned@starks.com>,
sansa@starks.com,
jon@starks.com,
   Arya No Face <arya@starks.com>
"""

def individual_email(address):
  em_string = ''
  if '<' and '>' in address:
    left_carrot = address.index('<') + 1
    right_carrot = address.index('>')
    em_string = address[left_carrot:right_carrot]
  else:
    em_string = address
  return em_string

def formatted_emails(email_string):
  email_arr = email_string.split(',')
  clean_email = []
  for email in email_arr:
    email = individual_email(email.strip())
    if email not in clean_email:
      clean_email.append(email)
  return clean_email

assert formatted_emails(testing_recipients) == [
        'jon@starks.com',
        'arya@starks.com',
        'ned@starks.com',
        'sansa@starks.com'
    ]
print('Format email assertion works!')
def send_email(recipients, products):
    return (formatted_emails(recipients), products_final(products))

pprint(send_email(testing_recipients, testing_products))
expected_output = (
    [
        'jon@starks.com',
        'arya@starks.com',
        'ned@starks.com',
        'sansa@starks.com'
    ],

    """* Arakh of Khal Drogo: $250
  Buy now using code: W-101
* Needle, Sword of Arya Stark: $1050
  Buy now using code: W-315
* Stark Infantry Shield: $760
  Buy now using code: S-918""")
print(expected_output[1])
print(send_email(testing_recipients, testing_products)[1])
assert expected_output[1] == send_email(testing_recipients, testing_products)[1]
print('ok')

assert send_email(testing_recipients, testing_products) == expected_output

print('All tests worked!')
