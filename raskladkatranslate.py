zamena = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', '\\': 'ё',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.'
}
def raskladite(input_text):
    output_text = ''
    for char in input_text:
        if char.lower() in zamena:
            if char.isupper(): output_text += zamena[char.lower()].upper()
            else: output_text += zamena[char.lower()]
        else: output_text += char
    return output_text
print("Введите ваш текст:\n")
input_text = str(input())
output_text = raskladite(input_text)
print(output_text)
