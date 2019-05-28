<div dir="rtl" lang="ar">
<meta charset="utf-8">





# قراءة حزمة البيانات زهرة الآيريس


```python
from sklearn import datasets

iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target
```

## معاينة البيانات


```python
# نلقي نظرة على أول عينه من القياسات ونوعها
print(f' قياسات الزهرة \n{X_iris[10]}\nالنوع \n{y_iris[10]}')
```

     قياسات الزهرة
    [5.4 3.7 1.5 0.2]
    النوع
    0


# تدريب الشبكة على جزء من البيانات


```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.15, random_state=42)
```


```python
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
```


```python
clf.fit(X_train, y_train)

clf.score(X_test, y_test)
```




    1.0




```python
from sklearn import linear_model
log = linear_model.LogisticRegression(solver='lbfgs', C=1e5, multi_class='multinomial')
log.fit(X_train, y_train)  

log.score(X_test, y_test)
```




    1.0



# تحجيم البيانات


```python
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

sc.fit(X_train)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
```

# إختبار الشبكة على الجزء المتبقي من البيانات


```python
# %%HTML
# <style>.container { width:93%;} div.prompt {display: none;}</style> <!--or display: none -->
```


</div>
