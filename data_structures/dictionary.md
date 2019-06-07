<div dir="rtl" lang="ar">

### القاموس "dictionary"

يستخدم للبيانات اللي تحتاج حفظ مفتاح مع قيمته (key-value pairs) من حيث نتسطيع استرجاع القيمه المطلوبة بإدخال اسم المفتاح المطلوب. من أهم مميزات القاموس هو ان اسامي المفاتيح **لابد ان تكون مخلتفة**، بمعنى أنه لايمكننا حفظ مفتاحين بنفس الأسم.

مثلاً لحفظ أسماءاصدقاءك مع رقم تلفون كل واحد منهم، القاموس يسهل لنا حفظ هذا النوع من التركيب البياني.  


شكل القاموس `{key : value}`


مثال:`{"phone_number" : "name"}`

</div>

```python
# قاموس لحفظ مجموعة من المفاتيح مع قيمة معينة لكل مفتاح
>>> friends_numbers = {"Thamer": 4444, "Zamil": 5555, "Norah": 7777}
>>> friends_numbers
{'Thamer': 4444, 'Zamil': 5555, 'Norah': 7777}

# إذا اردنا أسترجاع رقم معين
# نستدعي القاموس مع المفتاح المراد
>>> friends_numbers["Norah"]
7777

# إذا اردنا رؤية جميع المفاتيح في القاموس
>>> friends_numbers.keys()
dict_keys(['Thamer', 'Zamil', 'Norah'])

# وبالمثل  إذا أردنا رؤية جميع القيم المحفوظة بالقاموس
>>> friends_numbers.values()
dict_values([4444, 5555, 7777])

# لإضافة مفتاح وقيمة جديدة
>>> friends_numbers["Aziz"] = 4242
>>> friends_numbers
{'Thamer': 4444, 'Zamil': 5555, 'Norah': 7777, 'Aziz': 4242}

# لحذف مفتاح مع قيمته
>>> del friends_numbers["Zamil"]
>>> friends_numbers
{'Thamer': 4444, 'Norah': 7777, 'Aziz': 4242}


# مسميات أخرى للقاموس في لغات أخرى
# Object, Hash-Table, Map ... etc
```
