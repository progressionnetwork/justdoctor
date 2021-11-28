# justdoctor

# Хакатон по искусственному интеллекту
## Команда «JUSTATOM»

![alt text](https://github.com/atomicai/justdoctor/blob/master/features_graph.png)

Как запустить flask web:
1. перед запуском:

export FLASK_APP=justatom.atom
flask run

## Что сделали на хакатоне:
Проанализировали фичи из текстового датасета;
Распарсили текстовый датасет и извлекли фичи;
Препроцессор умеет работать с разряженными датасетами;
Привели фичи в катег. и бинарную формы;
Сгенерировали нормализованный датасет;
Обучили на нем модель решающих деревьев ;
Модель предсказывает летальный исход;
Модель умеет объяснять своё решение (визуальный граф);
Реализован веб интерфейс для предсказаний онлайн;
Модель сохраняется в pickle и может работать распределенно;


## Преимущества нашего решения:
Процессинг датасета к понятному для модели вида;
Использование моделей мл для обучения на CPU;
Интерпретируемость модели;
Возможность быстрого дообучения на новых данных;
Скорость работы;
Применимость и адаптируемость к новым данным;
Предсказываем вероятность летального исхода в том числе и по эвристическим правилам;

## Адаптивность и масштабируемость проекта:
В будущем планируется доработка веб интерфейса для поддержки разных форматов входных данных в тот, который читается нашей моделью, сделав решение адаптивным. 
Реализация полноценного веб интерфейса для удобного ввода мед данных о пациенте для масштабирования проекта.
Добавление в модель предсказаний по разным критериям: выбор правильного лечения, помощь в постановке диагноза и интерпретации результатов путем взаимодействия с графами знаний и визуальным отображением взаимосвязей из анамнеза пациентов.
Получение дополнительных данных из внешних источников для коррекции результатов предсказания и диагностирвоания.
Вывод статистически важной информации для помощи в принятии решений.



- Для препроцессинга данных использовалась нормализация текста, процессорные функции и классификаторы
- Для парсинга данных использовался regexp, извлечение между плавающими разделителями
- Для получения значений с плавающей точкой использовалась реализованная функция выделения таких значений 
- Для работы с датасетом использовалась библиотека pandas
- Для поиска доминантных фичей использовался ExtraTreesClassifier из набора sklearn
- Модель машинного обучения использовалась DecisionTreeClassifier
- Для построения графов использовался matplotlib и tree из набора sklearn

Выделенные фичи:

'id',         'temperatura',         'ves',         'rost',
         'pedikulez_status',         'chesotka_status',
         'flyurogramma',         'gepatit_status',         'spid_status',         'hron_bolezn_pecheni_status',
         'operativnie_vmeshatelstva',         'perelivanie_krovi_status',         'kontakti_s_inficirovannimi',         'prebivanie_zagranicey',         'lihoradka_status',
         'saharniy_diabet_status',         'ostr_serdsosudistaya_nedost_status',
         'gepatit_c_status',         'letal_status',
         'sepsis_status',         'mas_krovopoterya_status',         'polip_kishki',         'gospitalizirovan',         'poryadok_gosp',         'sposob_postupleniya',
         'cel_postupleniya',
         'strahov_anamnez',         'allergologicheskiy_anamnez',         'vred_privichki',         'obraz_jizni',         'obshee_sost',         'temperatura_utro',
         'temperatura_vecher',
         'soznanie',         'v_kontakte',         'emotionalnaya_labilnost',         'orientacia_v_prostr',
         'teloslojenie',
         'invalidnost',         'sost_pitaniya',
         'index_massi_tela',
         'ploshad_poverhn_tela',         'kojnie_pokrovi',         'skleri_status',
         'vidimie_slizistie',         'kostno_mishechnaya_sistema',         'zev',         'peref_limfouzli',         'oteki',
         'shitovidnaya_jeleza',         'selezenka',         'serd_sodud_sistema',         'forma_gr_kletki',         'chislo_dihaniy',
         'pishevar_sistema',         'rektalno',
         'organi_mocheispuscaniya',

