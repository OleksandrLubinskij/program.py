# -*- coding: utf-8 -*-
import re


def remove_timestamps(text):
    pattern = r'\b\d{1,2}:\d{2}(?::\d{2})?\b'
    cleaned_text = re.sub(pattern, '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text


text = """"""  # Твій текст повністю

# cleaned_text = remove_timestamps(test_text)
# print(cleaned_text)

with open("file_to_edit.txt", "r", encoding="utf-8") as file:
    for line in file:
        text += remove_timestamps(line)

with open("edited_file.txt", "w", encoding="utf-8") as file:
    file.write(text)
