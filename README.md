# Japanese-Mosaic

This program is made to solve japanese mosaic

## Описание

Японская мозаика - это графическая головоломка, в результате решения которой выявляется пиксельная картинка.
Чтобы разгадать картинку нужно, используя чистую логику, определить, какие клеточки должны быть закрашены, а какие останутся пустыми.

## Правила

Каждая головоломка представляет собой сетку, отдельные клеточки которой содержат цифры. Каждая цифра указывает, сколько клеточек должно быть закрашено вокруг клеточки с цифрой, включая ее саму. В результате решения головоломки выявляется скрытая картинка.

## Программа

- JapaneseMosaic - класс, решающий задание (основа - mosaic_test)
- JMFilePrepare - класс, считывающий задание из файла (основа - read_task)
- main - скрипт для работы

## Тестовые данные

'10-15 1.txt' - простой отладочный (есть решение)
'10-15 3.txt' - тестовый (нужно решение)
