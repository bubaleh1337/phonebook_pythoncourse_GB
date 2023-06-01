main_menu = '''\nГлавное меню:
		1. Открыть файл • 
		2. Записать файл •
		3. Показать контакт •
		4. Добавить контакт •
		5. Найти контакт •
		6. Изменить контакт •
		7. Удалить контакт •
		8. Выход •\n '''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта'
save_successful = 'Телефонная книга успешно сохранена'

load_error = 'Телефонная книга пуста или не открыта'

input_new_contact = 'Введите данные нового контакта: '
new_contact = {'name': 'Введите имя: ',
               'phone': 'Введите номер телефона: ',
               'comment': 'Введите комментарий: '}

def new_contact_successful(name: str):
		return f'Контакт {name} успешно добавлен'

cancel_input = 'Отмена ввода'

index_del_contact = 'Введите индекс контакта, который хотите удалить: '
def del_contact(name: str):
		return f'Контакт {name} успешно удалён!'

input_change = 'Какой контакт хотите изменить: '
input_index = 'Введите индекс контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтобы не менять: '

def change_successful(name: str | dict) -> str:
    return f'Контакт {name} успешно изменен!'

input_search = 'Какой контакт хотите найти? '
def empty_search(word) -> str:
    return f'Контакты содержащие слово "{word}" не найдены'