calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    str_tupe = (len(string), string.upper(), string.lower())
    count_calls()
    return str_tupe

def is_contains(string, list):
    count_calls()
    for i in range(len(list)):
        list[i] = list[i].lower()
    if list.count(string.lower()) >= 1:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



