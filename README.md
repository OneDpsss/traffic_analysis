# Результаты работы модели классификации уровней специалистов

## Параметры запуска
```bash
python app path/to/hh.csv
Сгенерированные файлы
x_data.npy — признаки

y_data.npy — целевые значения

Отчет о качестве классификации
Класс	Precision	Recall	F1-score	Support
junior	0.87	0.91	0.89	6363
middle	0.86	0.85	0.86	6182
senior	0.95	0.71	0.81	844
accuracy			0.87	13389
macro avg	0.89	0.82	0.85	13389
weighted avg	0.87	0.87	0.87	13389
Важность признаков (топ-10)
Признак	Важность
numeric__experience_years	0.056
text_position__senior	0.013
text_position__lead	0.011
text_position__junior	0.009
text_position__teamlead	0.007
text_position__leader	0.006
text_position__тимлид	0.006
text_position__team	0.005
text_position__middle	0.003
text_position__architect	0.002


Текстовые признаки из названий позиций также вносят вклад

Лучше всего модель определяет junior (F1=0.89)

Хуже всего — senior (F1=0.81), возможно из-за малого количества примеров (844)
