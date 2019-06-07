<div dir="rtl" lang="ar">

### القائمة "List"


مثلاً، إذا أردنا معالجة قائمة من الأرقام، لابد ان نحتفظ بها في هيكل بيانات معين. في لغة بايثون هناك مايسمى بـ "List" أو "قائمة" تتيح لنا حفظ الأرقام مؤقتاً خلال معالجتها في البرنامج (في لغات أخرى قد تختلف التسمية مابين مصفوفة، متوجه ..
الخ).


شكل القائمة `[ ]`

مثال: لحفظ الأرقام بين 1 و 5 في قائمة

</div>

```python
# قائمة لحفظ الأرقام مؤقتا خلال معالجتها
>>> numbers =  [1, 2, 3, 4, 5]
>>> numbers
[1, 2, 3, 4, 5]
```

<div dir="rtl" lang="ar">

 بعض العمليات المتاحة على هيكل البيانات "قائمة":

</div>

```python
# إضافة عضو او رقم جديد للقائمة
# في هذا المثال سيتم اضافة الرقم 77 الى القائمة
>>> numbers.append(77)
>>> numbers
[1, 2, 3, 4, 5, 77]

# إزالة واسترجاع آخر عضو أضيف ألى القائمة
# في هذا المثال
>>> top_number = numbers.pop()
>>> top_number
77

# عكس إتجاه البيانات المحفوظة في القائمة من اليسار ألى اليمين
>>> numbers.reverse()
>>> numbers
[5, 4, 3, 2, 1]
```