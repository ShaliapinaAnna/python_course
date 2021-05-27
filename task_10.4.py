class Book:

    def __init__(self, author, chapter, page_number):
        self.chapter = chapter
        self.__author = author
        self.__page_number = page_number

    def change_author(self, author):
        if len(self.__author) > 0:
            self.__author = author
            print(f'author: {self.__author}')
        else:
            print('error 404...')

    def change_chapter(self, new_chapter):
        if len(self.__author) > 0:
            self.chapter = new_chapter
            print(f'chapter: {self.chapter}')
        else:
            print('error 404...')

    def change_page_number(self, new_page_number):
        if len(self.__author) > 0:
            self.__page_number = new_page_number
            print(f'page: {self.__page_number}')
        else:
            print('error 404...')


book = Book('Cinderella', 2, 15)
book.change_author('Charles Piero')
book.change_chapter(4)
book.change_page_number(36)
