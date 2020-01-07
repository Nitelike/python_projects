alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = input('Введите тест для шифрования (только латинские буквы): ')
key = int(input('Введите ключ: '))

uppered_text = text.upper()

changed_letters = ''

for i in uppered_text:
    old_pos = alphabet.find(i)
    new_pos = (old_pos + key) % 26
    changed_letters += alphabet[new_pos]

print(changed_letters)
