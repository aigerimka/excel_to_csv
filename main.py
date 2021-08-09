import pandas as pd 
import openpyxl
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

for file in os.listdir("/Volumes/Seagate Backup Plus Drive/Сара/Предприятия объединение-20210808T130628Z-001/Предприятия объединение"):

    print(file)

    # здесь ты в конце пути добавь бэкслеш или обычный слэш, что там добавляют в пути windows
    # тут будет путь к самому файлы
    all_df = pd.read_excel('/Volumes/Seagate Backup Plus Drive/Сара/Предприятия объединение-20210808T130628Z-001/Предприятия объединение/' + file, engine='openpyxl', sheet_name=None)

    # парсим по одному объекту dict
    for i in all_df:
        df = all_df[i]

        df = df.dropna(how='all') # убираем пустые строки
        df = df.fillna(value='-') # убираем Nan и заменяем на обычный прочерк

        # Тут создается список наших headers для нового df
        # Название компании идет заголовком колонки, поэтому он не будет отображаться
        # Добавляю заранее в списочек
        headers = ['Название компании']
        
        try:
            for i in df[df.columns[0]]:
                headers.append(i)
            
            values = [df.columns[1]]
        except IndexError:
            continue

        # Аналогично и с заголовком второй колонки, там у нас уже идет значение к "Название компании"
        # Также заранее помещаем в списочек
        

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
        
        # чтобы он в csv заново не записывал headers при добавлении новых записей, я оставлю в гите, готовый файл out.csv с headers
        out_df.to_csv('out.csv', index=False, mode='a', header=False)