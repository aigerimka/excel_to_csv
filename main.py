import pandas as pd 
import openpyxl
import re
import os
import glob

# в os.listdir прописываешь путь к папке
# просто скачаешь с гугл диска, и скопируешь путь к папке, допустим, предприятия 1-267
# но если будешь парсить первую папку, парсер будет ломаться на файле, в названии которого долларовый значок
# в остальном он без проблем парсит

# что можно сделать:
# - пропарсить все остальные папки и посмотреть на каких файлах он ломается
# - улучшить код или сделать для себя более интуитивным
# в остальном по вопросам, просто пиши в личку с:

for file in os.listdir("/папка, где лежат эксель файлы"):

    print(file)

    # здесь ты в конце пути добавь бэкслеш или обычный слэш, что там добавляют в пути windows
    # тут будет путь к самому файлы
    all_df = pd.read_excel('/папка, где лежат эксель файлы' + file, engine='openpyxl', sheet_name=None)

    # парсим по одному объекту dict
    for i in all_df:
        df = all_df[i]

        df = df.dropna(how='all') # убираем пустые строки
        df = df.fillna(value='-') # убираем Nan и заменяем на обычный прочерк

        # Тут создается список наших хэдеров для нового df
        headers = ['Название компании']

        for i in df[df.columns[0]]:
            headers.append(i)

        # Так как название компании идет хэдером нынешнего df, то я уже сразу помещаю в наши значения заранее
        values = [df.columns[1]]

        # Цикл проходится по df и записывает их по порядку, чтобы потом было легче их скреплять с headers
        for j in range(0, len(df.index)): # строки
            value_str = []

            for i in range(1, len(df.columns)): # колонки

                if df.iloc[j, i] != '-':
                    value_str.append(df.iloc[j, i])

            if len(value_str) == 0:
                 # тут идет обычная обработка случаев, допустим, если возвращает пустой лист
                values.append('-')

            elif len(value_str) == 1:
                values.append(value_str[0])

            else:
                values.append(str(value_str))

        # наш новый датафрейм
        out_df = pd.DataFrame([values], columns=headers)

        print(out_df)
        print(df)
        
        # чтобы он в csv заново не записывал headers при добавлении новых записей, я оставлю в гите, файл out.csv с headers
        out_df.to_csv('out.csv', index=False, mode='a', header=False)