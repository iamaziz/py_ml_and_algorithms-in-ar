class Node:
    def __init__(self, val, next_=None):
        self.value = val
        self.next_ = next_


class LinkedList:
    def __init__(self, head):
        """تبدأ القائمة المتصلة بإضافة العنصر الأول - الرأس """
        self.head = Node(head)

    def add(self, new):
        """لإضافة عنصر جديد إلى القائمة"""
        node = Node(new)
        node.next_ = self.head
        self.head = node

    def __repr__(self, s=[]):
        """لطباعة القائمة"""
        current = self.head
        while current:
            s.append(str(current.value))
            current = current.next_
        return "LinkedList( " + " -> ".join(s[::-1]) + " )"

    def __contains__(self, val):
        """للبحث عن عنصر في القائمة"""
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next_
        return False

    def __len__(self):
        """عد العناصر الموجودة في القائمة"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_
        return count



if __name__ == "__main__":

    # لتعريف قائمة جديدة، نقوم بإنشاء نسخة من كائن القائمة المتصلة في الأعلى
    # ننشئ القائمة مع قيمة ابتدائية وهي العنصر الأول في القائمة
    l = LinkedList(4)

    # لإضافة عناصر إلى القائمة
    for x in [10, 3, 15]:
        l.add(x)

    # هل الرقم 33 موجود في القائمة
    print(33 in l)

    # طباعة القائمة الحالية
    print(l)

    # كم عدد يوجد في القائمة الحالية
    print(len(l))
