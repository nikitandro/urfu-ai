# UrFU-ai


## Модели

Обучены на датасете [nazeboan/stackoverflow-questions-classification-challenge](https://www.kaggle.com/datasets/nazeboan/stackoverflow-questions-classification-challenge)

Обучение велось на третьей версии датасета

Базовая модель - `bert-base-uncased`

Для обоих моделей определён оптимальный гиперпараметр `learning_rate=5e-5`, другие проверенные варианты: `3e-5`, `7e-5`

Другие гиперпараметры не проверялись



### Модель попроще:

https://drive.google.com/file/d/1nRnoZvIdtreIxgA1fLLDrD4hD4u9ej4T/view?usp=sharing

Умеет определять только язык программирования, лучше уверенность

Лучшая версия обучилась между второй и третьей эпохой

```
Training loss:   0.266200
Validation loss: 0.489455
```

### Модель посложнее:

https://drive.google.com/file/d/1sriXS2r8t4u2R5dNf2dh-TBtfoVgy_eL/view?usp=sharing

Умеет определять язык и топик одним лейблом, хуже уверенность

Лучшая версия обучилась между четвёртой и пятой эпохой

Для определения главенствующего тега в каждом вопросе использовалось ранжирование по популярности в датасете

```
Training loss:   2.610100
Validation loss: 3.378597
```

#### Пример ответов

```
Запрос> Не могу запустить код на фласке, пишет что порт занят, хотя ничего не запущено
Query: Can't run the code on the flask, says the port is busy, but nothing's running.
Response: ('python-flask', 0.943072497844696)

Запрос> что делать, если в спринге джава не запускается секьюрити
Query: What do you do if the java doesn't start security in the spring?
Response: ('java-spring', 0.7576866745948792)
```
