incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def data_transformer(names):
    string = list(map(lambda x: f'{x["name"]} {x["last_name"]}', names))
    return string

print(data_transformer(incoming_ajax_data))
