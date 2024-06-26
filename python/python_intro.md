<div dir="rtl" lang="ar">



قائمة المحتويات:

<!-- TOC -->

- [انواع البيانات](#%d8%a7%d9%86%d9%88%d8%a7%d8%b9-%d8%a7%d9%84%d8%a8%d9%8a%d8%a7%d9%86%d8%a7%d8%aa)
- [المتغيرات](#%d8%a7%d9%84%d9%85%d8%aa%d8%ba%d9%8a%d8%b1%d8%a7%d8%aa)
- [الدوال](#%d8%a7%d9%84%d8%af%d9%88%d8%a7%d9%84)
- [الأوامر الشرطية](#%d8%a7%d9%84%d8%a3%d9%88%d8%a7%d9%85%d8%b1-%d8%a7%d9%84%d8%b4%d8%b1%d8%b7%d9%8a%d8%a9)
- [القوائم](#%d8%a7%d9%84%d9%82%d9%88%d8%a7%d8%a6%d9%85)
- [التكرار](#%d8%a7%d9%84%d8%aa%d9%83%d8%b1%d8%a7%d8%b1)
- [الأصناف](#%d8%a7%d9%84%d8%a3%d8%b5%d9%86%d8%a7%d9%81)

<!-- /TOC -->

<hr>


### انواع البيانات

عند كتابة أي برنامج، نحتاج للتعامل مع البيانات. على مستوى معالج الكمبيوتر البيانات في جوهرها ليست سوى سلاسل طويلة جداً ممثلة في رقمين فقط 0 و 1 (تسمى النظام الثنائي) بحيث كل جزء يمثل بيانات معينة كصورة أو اسم أو رقم وما إلى ذلك.
ولكن لصعوبة التعامل مع النظام الثنائي، أنواع اخرى للبيانات  تستخدم لتسهيل كتابة البرامج.

في بايثون هناك ثلاثة أنواع اساسية للبيانات:

- أرقام
- نصية
- منطقية
</div>


```python
# أرقام
# أي رقم من مجموعة الأرقام الحقيقية
>>> 3
3
>>> 12413.144
12413.144

>>> # يمكن للأرقام ان تكون صحيحة
>>> type(123)
<class 'int'>
>>> # أو عشرية
>>> type(77.13)
<class 'float'>
```

```python
# نصية
# أي حرف او مجموعة من الحروف
>>> "ع"
ع
>>> "السلام عليكم"
السلام عليكم

>>> type('السلام عليكم')
<class 'str'>
```

```python
# منطقية
# وتعني صح أو خطأ
>>> True
True
>>> False
False

>>> type(False)
<class 'bool'>
```

<hr>


<div dir="rtl" lang="ar">

### المتغيرات


لتسهيل أسترجاع البيانات وتبادلها خلال كتابة برنامج ما، نحتاح إلى حفظ البيانات في مكان ما مع **أسم** مُعين بحيث يسهل الرجوع لها متى مادعت الحاجة إلى استخدامها من خلال **إستدعاء ذلك الأسم** فقط.

مثل هذه **الإسماء** (والتي تكون إختيارية) تسمى **متغيرات**.  

في بايثون، تعريف المتغيرات يأخذ الشكل: `الأسم = البيانات`

مثلاً لتعريف مُتغيّر يحمل الأسم `salam` و يشير إلى نوع بيانات نصية تحمل الرسالة `"السلام عليكم، مرحباً بكم"`:

</div>

```python
>>> salam = "السلام عليكم، مرحباً بكم"
# لاحظ الفائدة من استخدام المتغير
# في كل مرة نحتاج أن نستخدم الرسالة
# لاينبغي أن نقوم بكتابتها مرة أخرى
# بل مجرد نستدعي اسم المتغير الذي يشير إلى القيمة المطلوبة
>>> salam
'السلام عليكم، مرحباً بكم'
>>> salam
'السلام عليكم، مرحباً بكم'


# يمكن استخدام المتغيرات مع أي نوع من أنواع البيانات
>>> pi = 3.141592
>>> pi
3.141592
```

> المتغيرات هي مجرد أسماء تشير إلى مكان معين في ذاكرة الكمبيوتر، مثل العنوان

<hr>


<div dir="rtl" lang="ar">


### الدوال

الدالة "function" هي مجرد كتلة أو حزمة من الأوامر المرتبطة لتقوم بغرض معين، مثلاً دالة لجمع عددين. مثل المتغيرات، الدوال يكون لها أسماء معينة أيضاً.

يمكن للدوال ان تقبل _مدخلات_ أو تكون _بدون مدخلات_. كما يكمن للدوال ان _تُرجع_ نتيجة أو _لاترجع_ نتيجة.

في بايثون، تعريف الدالة يكون عن طريق استخدام الكلمة المحجوزة `def` (إختصار لكلمة define وتعني عرّف) متبوع بأسم الدالة اللتي نريد إنشاءها، و يأخذ الشكل التالي:

</div>

```python
# مثال 1
# لتعريف دالة تقوم بجمع العددين 2 و 1 وإرجاع الناتج
# و تحمل الإسم add_two_one
# و لا تقبل أي مدخلات
>>> def add_two_one():
>>>     return 1 + 2

# يتم إستدعاء الدالة عن طريق أسمها
>>> add_two_one()
3



# مثال 2
# لتعريف دالة تقبل رقم كمدخلات ثم تقوم بجمعه مع الرقم 2 وترجع نتيجة الجمع
>>> def add_two(my_number):
>>>     return my_number + 2

# بعدها يكمن استدعاء الدالة مع أي رقم نريد ان نحصل على حاصل جمعه مع الرقم 2
>>> add_two(10)
12
>>> add_two(15)
17
```

<div dir="rtl" lang="ar">

**الدوال المعرفة مسبقاً**

 بدلاً من إنشاء دوال لكل شي نريد برمجته، غالبية لغات البرمجة تحتوي على مجموعة كبيرة جداً من الدوال المُعرّفة مسبقاً، واللتي يمكن إستخدامها مباشرة لتسهل عمل المبرمج. كل ماعلينا هو أن نعرف اسم الدالة المطلوبة ومدخلاتها.

في لغة بايثون، أشهر الدوال المعرفة مسبقاً هي دالة الطباعة `print` واللتي تقوم بطباعة المدخلات على الشاشة. وهذه أمثلة اخرى:

</div>

```python
# أمثلة لدوال معرفة مسبقاً في لغة بايثون

# مثال 1
# دالة "الرفع" لحساب الرقم مرفوع لأس معين
# مثلا لحساب نتيجة 4 أُس 2
>>> pow(4, 2)
16

# مثال 2
# دالة "العد أو الطول" لتعداد عدد العناصر الموجودة في بيانات معينة
# مثلاً نستطيع عد كم عدد الحروف في جملة "السلام عليكم" كالتالي
>>> len("السلام عليكم")
12

```

> لمعلومات اكثر إذهب إلى صفحة: [قائمة الدوال المعرفة في بايثون](https://docs.python.org/3/library/functions.html)

<hr>

### الأوامر الشرطية

    # TODO: اضف شرح مع امثلة هنا

### القوائم

    # TODO: اضف شرح مع امثلة هنا

### التكرار

    # TODO: اضف شرح مع امثلة هنا

### الأصناف

    # TODO: اضف شرح مع امثلة هنا
    # i.e. class


</div>
