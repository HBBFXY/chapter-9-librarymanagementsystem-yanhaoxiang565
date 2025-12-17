class Book:
    """书籍类，包含书名、作者、ISBN属性，以及可借状态"""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # 标记书籍是否被借出

    def check_availability(self):
        """检查书籍是否可借"""
        return not self.is_borrowed

    def borrow_book(self):
        """借出书籍，修改可借状态"""
        if self.check_availability():
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        """归还书籍，恢复可借状态"""
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        """返回书籍的字符串描述"""
        status = "可借" if self.check_availability() else "已借出"
        return f"书名：{self.title}，作者：{self.author}，ISBN：{self.isbn}，状态：{status}"


class User:
    """用户类，包含姓名、借书卡号，以及借阅书籍列表"""
    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.borrowed_books = []  # 存储用户借阅的书籍对象

    def borrow(self, book):
        """用户借书操作"""
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name}成功借阅《{book.title}》")
        else:
            print(f"《{book.title}》已被借出，{self.name}借阅失败")

    def return_book(self, book):
        """用户还书操作"""
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print(f"{self.name}成功归还《{book.title}》")
        else:
            print(f"{self.name}未借阅《{book.title}》，归还失败")

    def __str__(self):
        """返回用户的字符串描述"""
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"姓名：{self.name}，借书卡号：{self.card_id}，已借书籍：{borrowed_titles if borrowed_titles else '无'}"


# 测试程序
if __name__ == "__main__":
    # 创建书籍实例
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787111641247")

    # 创建用户实例
    user1 = User("张三", "C001")
    user2 = User("李四", "C002")

    # 测试借书、还书功能
    print("===== 初始书籍状态 =====")
    print(book1)
    print(book2)

    print("\n===== 张三借阅书籍 =====")
    user1.borrow(book1)
    print(book1)
    print(user1)

    print("\n===== 李四尝试借阅同一本书 =====")
    user2.borrow(book1)
    print(user2)

    print("\n===== 张三归还书籍 =====")
    user1.return_book(book1)
    print(book1)
    print(user1)

    print("\n===== 李四再次借阅 =====")
    user2.borrow(book1)
    print(book2)
    print(user2)# 在这里编写代码
