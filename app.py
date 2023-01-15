class Book:
   def __init__(self, book_path) -> None:
       self.__pages = []
       self.__book_path = book_path
       self.__content = ""
       self.__curr_page = 0
       self.__last_page = 0
 
   def __open_book(self):
       with open(self.__book_path, "r") as f:
           if f.readable():
               self.__content = f.read()
               f.close()
 
   def __build_book(self):
       self.__open_book()
       self.__pages = self.__content.split("--")
       self.__last_page = len(self.__pages)-1
 
   def __next_page(self):
       if self.__curr_page + 1 <= self.__last_page:
           self.__curr_page += 1
 
   def __skip_page(self, pages):
       if -1 < pages <= self.__last_page:
           self.__curr_page = pages
 
   def __prev_page(self):
       if -1 < self.__curr_page-1 < self.__last_page:
           self.__curr_page = self.__curr_page-1
 
   def read(self):
       self.__build_book()
       curr_page_content = self.__pages[self.__curr_page]
       print(self.__pages)
       while (True):
           print(curr_page_content)
           btn = input("[enter - read more, press q to quit]")
           if btn.strip() == 'q':
               break
           elif btn.strip() == "":
               self.__next_page()
           else:
               skip_page = int(btn)
               if skip_page-1 >= 0:
                   self.__skip_page(skip_page-1)
               elif skip_page == -1:
                   self.__prev_page()
 
           curr_page_content = self.__pages[self.__curr_page]
 
 
Book("book.txt").read()
