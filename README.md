# Подсчет пешеходов на переходе

**Pedestrian Counter v 1.0.0**

Проект представляет собой веб-приложение для подсчета пешеходов на изображении.
Система использует YOLO для поиска людей и OpenCV для обработки изображения.

> **English**
> This project is a web application for counting pedestrians in an image.
> The system uses YOLO to detect people and OpenCV to process the image.

---

## Технологии

* Python
* Flask
* YOLO
* OpenCV
* SQLite
* HTML
* CSS

> **English**
> Technologies used: Python, Flask, YOLO, OpenCV, SQLite, HTML and CSS.

---

## Возможности

* загрузка изображения;
* поиск объектов класса `person`;
* отрисовка рамок вокруг найденных пешеходов;
* подсчет количества людей;
* сохранение истории обработки в SQLite;
* отображение результата на веб-странице.

> **English**
> Features: image upload, `person` detection, bounding box drawing, pedestrian counting, SQLite history saving and result display on a web page.

---

## Структура проекта

```text
pedestrian_counter/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   └── history.db
│
├── static/
│   ├── style.css
│   ├── favicon.ico
│   ├── uploads/
│   └── results/
│
├── templates/
│   └── index.html
│
└── utils/
    ├── __init__.py
    ├── detector.py
    └── db.py
```

> **English**
> The project contains the Flask application, HTML template, CSS styles, image folders, database file and utility modules.

---

## Описание файлов

`app.py` — основной файл Flask-приложения.
`utils/detector.py` — обработка изображения и вызов YOLO.
`utils/db.py` — работа с базой данных SQLite.
`templates/index.html` — веб-интерфейс.
`static/style.css` — оформление страницы.
`static/uploads/` — исходные изображения.
`static/results/` — обработанные изображения.

> **English**
> `app.py` starts the Flask app.
> `detector.py` runs YOLO detection.
> `db.py` works with SQLite.
> `index.html` is the web interface.
> `style.css` contains page styles.

---

## Запуск проекта

1. Откройте папку проекта в Visual Studio Code.

2. Создайте виртуальное окружение:

```bash
python -m venv .venv
```

3. Активируйте окружение:

```bash
.venv\Scripts\activate
```

4. Установите зависимости:

```bash
pip install -r requirements.txt
```

5. Запустите приложение:

```bash
python app.py
```

6. Откройте в браузере:

```text
http://127.0.0.1:5000
```

> **English**
> Open the project folder, create a virtual environment, activate it, install dependencies, run `python app.py`, and open `http://127.0.0.1:5000` in a browser.

---

## Использование

1. Откройте сайт.
2. Выберите изображение с пешеходным переходом.
3. Нажмите кнопку запуска обработки.
4. Посмотрите количество найденных пешеходов.
5. Проверьте обработанное изображение с рамками.

> **English**
> Open the app, upload a crossing image, start processing and check the detected pedestrian count with bounding boxes.

---

## Возможные ошибки

### Не запускается Python

Попробуйте:

```bash
py app.py
```

### Не устанавливаются библиотеки

Обновите pip:

```bash
python -m pip install --upgrade pip
```

Затем снова выполните:

```bash
pip install -r requirements.txt
```

## Ограничения

Приложение обрабатывает только изображения.
Система считает все найденные объекты класса `person`, поэтому люди вне перехода также могут попасть в подсчет.

> **English**
> The app processes images only. It counts all detected `person` objects, so people outside the crossing may also be counted.

---

## Автор

**AzaTu**

© AzaTu
