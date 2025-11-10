"""
도서 관리 프로그램
- 메뉴 : 도서 추가 / 도서 삭제(제목) / 도서 조회(제목) / 전체 도서 목록 / 종료
"""

# ----------------------------------------------------
# 1) Node 클래스 
# ----------------------------------------------------
# 단순연결구조를 위한 Node 클래스
class Node:
    def __init__(self,elem, link=None):
        self.data = elem # 데이터 필드
        self.link = link # 다음 노드을 가리키는 주소값을 저장(링크) 필드

    # 노드 기반 삽입 연산
    def append(self, new) :  # 현재 노드(self) 뒤에 새 노드(new)를 연결 연산
        if new is not None:
            new.link = self.link # new의 다음 노드는 현재 노드(self)의 다음 노드로 수정
            self.link = new      # 현재 노드(self)의 다음 노드를 new로 수정

    # 노드 기반 삭제 연산
    def popNext(self): # 현재 노드 (self)의 다음 노드를 삭제하고, 그 노드를 반환
        deleted = self.link # 삭제할 노드를 deleted에 저장
        if deleted is not None:
            self.link = deleted.link 
            deleted.link = None # 연결 해제
        return deleted
# ----------------------------------------------------
# 2) 단순 연결 리스트 클래스 ()
# ----------------------------------------------------
class LinkedList:
    def __init__ (self):
        self.head = None # 비어있는 리스트의 초기 상태
    
    # 주요 기본 연산
    def isEmpty(self):
        # 리스트의 빈 상태 검사
        return self.head == None
    
    def isFull(self):
        # 리스트의 포화 상태 검사
        return False    # 동적 노드 할당

    def getNode(self, pos):  # pos 기반 연산
        # pos 위치에 있는 노드를 반환
        # pos는 리스트의 인덱스 0부터 고려
        if pos < 0: return None # pos는 유효하지 않은 위치
        if self.head == None: # 리스트가 빈 상태
            return None
        else:
            ptr = self.head
            for _ in range(pos):
                if ptr == None: # pos가 리스트보다 클 경우
                    return None
                ptr = ptr.link
            return ptr  # 최종 노드 반환
    
    def getEntry(self, pos):
        # 리스트의 pos 위치에 있는 노드를 찾아 데이터값을 반환
        node = self.getNode(pos) # 1 . 해당 위치의 노드를 탐색
        if node == None: # 해당 노드가 없는 경우
            return None
        else:
            return node.data
        
    def insert(self, pos, elem):  # 인덱스 기반 연산
        # pos 위치에서 새 노드(elem) 삽입 연산
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        
        new = Node(elem) # 1 . 새 노드 생성
        before = self.getNode(pos - 1) # 2 . pos - 1 위치의 노드 탐색
        # 3 . before 노드의 위치에 따라 구분
        if before is None:
            if pos == 0: # 1) 머리 노드로 삽입
                new.link = self.head
                self.head = new
                return
            else:   # 2) pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else:   # 3) 중간 노드로 삽입
            before.append(new) 
        
    def delete(self, pos):  # 인덱스 기반 연산
        # pos 위치에서 해당 노드 삭제
        if pos < 0 :
            raise ValueError("잘못된 위치 값!")
        
        before = self.getNode(pos - 1) # 1 . 삭제 노드 이전의 노드 탐색
        # 2 . before 노드의 위치에 따라 구분
        if before == None:
            if pos == 0:    # 1) 머리 노드로 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted 
            else:  # 2) pos가 리스트 범위에서 벗어남
                raise IndexError("삭제할 위치가 유효하지 않음!")
        else:   # 3) 중간 노드로 삭제
            return before.popNext()
        
    def size(self):
        # 리스트의 전체 노드의 개수
        if self.head == None: # 현재 리스트가 공백이면
            return 0
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count
        
    def display(self, msg = "LinkedList: "):
        # 리스트의 내용을 출력
        print(msg, end = '')
        if self.head == None:  # 현재 리스트가 공백이면
            return None
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, end = " -> ")
                ptr = ptr.link
            print("None")

    def replace(self, pos, elem): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드의 데이터 필드를 수정
        node = self.getNode(pos)
        if node != None: # 해당 노드가 있는 경우
            node.data = elem
    
    # 메서드 추가(책 제목으로 도서 찾기 / 위치 찾기)
    def find_by_title(self, title):
        # 책 제목으로 도서(BOOK)를 찾아 반환, 없으면 None 반환
        ptr = self.head
        while ptr is not None:
            book = ptr.data
            if book.title == title:
                return book
            ptr = ptr.link
        return None
    
    def find_pos_by_title(self, title):
        # 책 제목으로 도서(BOOK)의 위치를 찾기, 없으면 -1 반환
        pos = 0
        ptr = self.head
        while ptr is not None:
            book = ptr.data
            if book.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return -1

# ----------------------------------------------------
# 3) Book 클래스
# ----------------------------------------------------
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id  # 도서 ID
        self.title = title      # 도서 제목
        self.author = author    # 저자
        self.year = year        # 출판 연도
    
    def __str__(self):
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"

# ----------------------------------------------------
# 4) BookManagement 클래스 : 메뉴/기능 구현
# ----------------------------------------------------
class BookManagement:
    def __init__(self):
        self.books = LinkedList()
    
    # 1 . 도서 추가 : 책 번호/제목 중복 방지
    def add_book(self, book_id, title, author, year):
        # 리스트 순회 -> 중복 검사 
        ptr = self.books.head
        while ptr is not None:
            b = ptr.data
            if b.book_id == book_id:
                print("오류: 이미 존재하는 책 번호입니다.")
                return False
            if b.title == title:
                print("오류: 이미 존재하는 책 제목입니다.")
                return False
            ptr = ptr.link
        
        # 중복이 아니면 도서 추가
        self.books.insert(self.books.size(), Book(book_id, title, author, year))
        print(f"도서 '{title}'가 추가되었습니다.")
        return True

    # 2 . 도서 삭제 (책 제목으로 삭제)
    def remove_book(self, title):
        pos = self.books.find_pos_by_title(title)
        if pos == -1:
            print("오류: 해당 제목의 도서를 찾을 수 없습니다.")
            return False
        else:
            self.books.delete(pos)
            print(f"도서 '{title}'가 삭제되었습니다.")
            return True
    
    # 3 . 도서 조회 (책 제목으로 조회)
    def search_book(self, title):
        b = self.books.find_by_title(title)
        if b is None:
            print("오류: 해당 제목의 도서를 찾을 수 없습니다.")
            return None
        else:
            print(f"책 번호: {b.book_id}, 제목: {b.title}, 저자: {b.author}, 출판 연도: {b.year}")
            return b
    
    # 4 . 전체 도서 목록 출력
    def display_books(self):
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        # 등록 순서대로 출력
        ptr = self.books.head
        print("현재 등록된 도서 목록:")
        while ptr is not None:
            b = ptr.data
            print(f"책 번호: {b.book_id}, 제목: {b.title}, 저자: {b.author}, 출판 연도: {b.year}")
            ptr = ptr.link
    
    # 5 . 메뉴 루프
    def run(self):
        print("=== 도서 관리 프로그램 ===")
        while True:
            # ✅ 변경: 우리 최소본은 루프 전체 try/except 없이 진행(입력 변환만 예외 처리)
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            menu = input("메뉴를 선택하세요: ").strip()

            if menu == '1':
                # book_id/year를 문자열로 받고 아래에서 정수 변환
                book_id_str = input("책 번호를 입력하세요: ").strip()   
                title = input("책 제목을 입력하세요: ").strip()
                author = input("저자를 입력하세요: ").strip()
                year_str = input("출판 연도를 입력하세요: ").strip()     

                # 숫자 변환/검사 (잘못되면 안내 후 메뉴로)
                try:
                    book_id = int(book_id_str)                           
                    year = int(year_str)                                 
                except ValueError:
                    print("오류: 책 번호와 출판 연도는 정수로 입력하세요.")  
                    print()
                    continue                                              

                self.add_book(book_id, title, author, year)

            elif menu == '2':
                title = input("삭제할 책 제목을 입력하세요: ").strip()
                self.remove_book(title)
            
            elif menu == '3':
                title = input("조회할 책 제목을 입력하세요: ").strip()
                self.search_book(title)
            
            elif menu == '4':
                self.display_books()
            
            elif menu == '5':
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 선택입니다. 1~5 중에서 선택하세요.")
            print()

# ----------------------------------------------------
# 5) 메인 실행부
# ----------------------------------------------------
if __name__ == "__main__":
    manager = BookManagement()
    manager.run()