

class KMeans:

    def distance(self, u, v):
        """
        حساب المسافة الإقليدية بين نقطتين
        المسافة = square_root( (u0 - v0)^2 + (u1 - v1)^2) )
        
        u: [int, int], النقطة الأولى
        v: [int, int], النقطة الثانية
        """
        sum_ = sum( (u[i] - v[i])**2 for i in range(len(u)) ) # ناتج الجمع اللي تحت الجذر
        return sum_**(1/2)                                    # نأخذ الجذر للمجموع


    def get_closer(self, target, *args):
        """
        حساب أي النقاط اقرب إلى النقطة الهدف
        
        target:  [float], النقطة الهدف
        *args: [[float]], مجموعة نقاط 
        """
        min_distance = float('inf')           # متغير للمسافة الأقصر، نبدأه بأكبر قيمة  
        for point in args:                    # زيارة نقاط المنتصف المدخلة 
            d = self.distance(point, target)  # حساب المسافة بين الهدف و نقطة المنتصف الحالية
            if d < min_distance:              # إذا كانت المسافة أقصر من المسافة الأقصر السابقة
                min_distance = d              # نحدث متغير المسافة الأقصر للمسافة الحالية
                closer = point                # نحتفط بـ نقطة المنتصف الحالية كالنقطة الأقرب
        return closer                         # بعد مقارنة جميع المسافات، إرجاع النقطة ذات المسافة الأقرب


    def get_center(self, cluster):
        """
        حساب نقطة المنتصف لكل النقاط في المجموعة
        
        cluster: [[float]], قائمة من النقاط
        """
        center = []                             # متغير لتخزين نقطة المنتصف
        n = len(cluster)                        # عدد النقاط في المجموعة
        for i in range(len(cluster[0])):        # عدد الأبعاد في كل نقطة
            c = sum(p[i] for p in cluster) / n  # المجموع لكل بُعد تقسيم عدد النقاط
            center.append(round(c, 1))          # اضف الناتج
        return center                           # إرجاع نقطة المنتصف التي تم حسابها


    def k_means(self, data, k=2, *centers, verbose=True):
        """
        خوارزمية التجميع "التصنيف" مع تنفيذ بأسلوب التكرار الذاتي
        
        data: [[float]],    مجموعة النقاط البيانية التي نرغب في تصنيفها في مجموعات
        k: int,             عدد المجموعات التي نرغب بتكوينها
        centers: [[float]], مُدخل إختياري - نقاط المنتصف (المركزية) الإبتدائية لكل مجموعة
        """
        # نحدد نقاط المنتصف المبدئية إذا كانت لم تدخل مع البيانات
        # عشوائياً نختار من النقاط الأولى في البيانات (بعدد المجموعات)  كنقاط منتصف أولية
        centers = list(centers) if centers else [data[i] for i in range(k)]
            
        clusters = [[] for _ in range(k)] # ننشئ قوائم فارغة لحفظ النقاط التابعة لكل قائمة بها
        
        # نقوم بزيارة جميع النقاط البيانية 
        # ولكل نقطة، سنحسب المسافة بينها وبين نقاط المنتصف  
        for point in data:
            # حساب أي نقاط المنتصف أقرب إلى النقطة البيانية الحالية
            nearest = self.get_closer(point, *centers)
            # نسترجع عنوان أو دليل (من بين قائمة نقاط المنتصف) نقطة المنتصف الأقرب للنقطة الحالية
            nearest_cluster_index = centers.index(nearest) 
            # نضيف النقطة الحالية إلى قائمة المجموعة التي تتبع لها من بين مجموعة القوائم
            clusters[nearest_cluster_index].append(point)
        # حساب نقاط المنتصف الجديدة
        new_centers = [self.get_center(cluster) for cluster in clusters]
        # الأمر التالي ليس جزء من الخوارزمية، لمجرد طباعة النتائج المرحلية
        if verbose: print(f"ITER:\tinit cents: {centers}\n\tnew cents: {new_centers}")
        
        # إذا نقاط المنتصف السابقة هي نفس الجديدة, تتوقف الخوارزمية وترجع الحل
        if centers == new_centers: return clusters, centers
        
        # وإلا فإنها ستقوم بتكرار العملية مع نقاط المنتصف الجديدة الجديدة
        return self.k_means(data, k, *new_centers, verbose=verbose)





if __name__ == "__main__":

    weights = [ 74,  77,  81,  76,  80,  91,  88,  93,  88,  92] # الوزن بالكيلوغرام
    heights = [179, 182, 181, 175, 174, 182, 178, 178, 174, 173] # الطول بالسنتيمتر

    samples = [list(point) for point in zip(weights, heights)]
    print("عينة البيانات:")
    print(samples)

    clusters, centroids = KMeans().k_means(samples)
    
    print("المجموعات:")
    for row in clusters: print(row)
    print("نقاط المنتصف:")
    print(centroids)
