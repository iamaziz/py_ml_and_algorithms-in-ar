def quicksort(a):
    
    if len(a) < 2:  # إذا كانت القائمة لاتحوي سوى رقم واحد
        return a   # قم بإرجاع الرقم الوحيد

    pivot = a[0]  # الرقم المحور (نختار الرقم الأول) عشوائياً
    right = []		# قائمة لتخزين الأرقام الأكبر من المحور
    left = []		# قائمة لتخزين الأرقام الأصغر من المحور

    # نقوم بزيارة جميع الأرقام في القائمة بإستثناء المحور
    for x in a[1:]:
        if x >= pivot:       # إذا كان الرقم الحالي اكبر من او يساوي المحور
            right.append(x)  # أضفه إلى قائم
        else:                # أو إذا أصغر
            left.append(x)   # أضفه إلى قائمة الأصغر

    # كرر إستدعاء الخوارزمية مع قائمتين الأكبر والإصغر مع وضع المحور في المنتصف
    return quicksort(left) + [pivot] + quicksort(right)