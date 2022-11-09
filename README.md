# Урок 27. Знакомство с Django. Домашнее задание 
***

Реализовано:
```
Request
GET /

Response
200 
{"status": "Ok"}
```

```
Request
GET /cat/

Response
200
[
	{
		"id": 1,
		"name": "Автотовары"
	},
	...
]

Request
GET /ad/

Response
200
[
	{
		"id": 1,
		"name": "Толстовка",
		"author": "Мария",
		"price": 500,
	},
	...
] 

```
```
Request
GET /cat/1/

Response
200
{
	"id": 1,
	"name": "Автотовары"
}

404


Request
GET /ad/1/

Response
200
{
	"id": 1,
	"name": "Толстовка",
	"author": "Мария",
	"price": 500,
	"description": "Продаю новую кофту на рост 110 см, по всем вопросам пишите", 
	"address": "Москва, ул. Борисовские Пруды, 16к2",
	"is_published": true
}

404
```
```
Request
POST /cat/
{
	"name": "Кухня"
}

Response
200
{
	"id": 2,
	"name": "Кухня"
}


Request
POST /ad/
{
	"name": "Гель для душа",
	"author": "Настя",
	"price": 0,
	"description": "Отдам даром, не подошел", 
	"address": "Москва, метро Коломенская",
	"is_published": false
}

Response
200
{
	"id": 2,
	"name": "Гель для душа",
	"author": "Настя",
	"price": 0,
	"description": "Отдам даром, не подошел", 
	"address": "Москва, метро Коломенская",
	"is_published": false
}
```