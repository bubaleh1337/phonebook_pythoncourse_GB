from contextlib import suppress

phone_book: list[dict[str, str]] = []
path = 'phones.txt'

def open_pb():
	global phone_book, path
	with open(path, 'r', encoding='UTF-8') as file:
		data = file.readlines() # 'Kate:7444654:comment'
	for contact in data:
		contact = contact.strip().split(':') # .strip() - очищение начало и конец строки
		phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})

def save_pb():
	global phone_book, path
	data = []
	for contact in phone_book:
		data.append(':'.join([value for value in contact.values()]))
	with open(path, 'w', encoding='UTF-8') as file:
		file.write('\n'.join(data))

def get_pb() -> list[dict[str, str]]:
	global phone_book
	return phone_book

def add_contact(contact: dict[str, str]):
	global phone_book
	phone_book.append(contact)
	return contact.get('name')

def del_contact(index: int): 
	global phone_book
	return phone_book.pop(index-1).get('name') 

def search_pb(word: str) -> list[dict[str, str]]:
	result: list[dict[str, str]] = []
	for contact in phone_book:
		for field in contact.values():
			if word.lower().strip() in field.lower().strip():
				result.append(contact)
				break
	return result

def change_pb(contact: dict, index: int):
	global phone_book
	
	with suppress(Exception):
		if len(contact['name']) > 0:
			phone_book[index-1]['name'] = contact['name']
	with suppress(Exception):
		if len(contact['phone']) > 0:
			phone_book[index-1]['phone'] = contact['phone']
	with suppress(Exception):
		if len(contact['comment']) > 0:
			phone_book[index-1]['comment'] = contact['comment']
