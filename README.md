# Тестовое задание Social Links

###Описание

Необходимо написать python скрипт, который на входе будет принимать параметр
*query (email)*, а на выходе выдает *json*
следующего формата:

```json
{
    "result": {...}
}
```
Данные скрипт получает с [Gravatar](https://ru.gravatar.com/)

###Начало работы

1. Склонировать репозиторий 

    `git clone https://github.com/maks-mishin/social_links.git`
    
2. Установить зависимости:

    `pip install requirements.txt`

3. Запустить скрипт и передать *email* как параметр:

    `python main.py eehzntm5@hotmail.com`

4. Результат работы:

```json
{
  "result": {
    "id": "57572911", 
    "requestHash": "8427e0d944fe405248fc4c4944b7288f", 
    "photos": [
      {
        "value": "https://secure.gravatar.com/avatar/8427e0d944fe405248fc4c4944b7288f",
        "type": "thumbnail"
      }
    ],
    "name": [],
    "displayName": "eehzntm5",
    "urls": [],
    "email_hash": "8427e0d944fe405248fc4c4944b7288f",
    "url": "http://gravatar.com/eehzntm5",
    "alias": "eehzntm5",
    "thumb": "https://secure.gravatar.com/avatar/8427e0d944fe405248fc4c4944b7288f"
  }
}

```