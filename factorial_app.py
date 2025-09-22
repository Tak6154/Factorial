import time     # 실행 시간 측정용

# 테스트 데이터 (메뉴 4번에서 실행)
TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# -----------------------------------------------------------------
# 반복문 기반 팩토리얼
# -----------------------------------------------------------------
def factorial_iter(n):
    # n이 정수이고 0 이상인지 확인
    if not isinstance(n, int) or n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result
# -----------------------------------------------------------------
# 재귀 기반 팩토리얼
# -----------------------------------------------------------------
def factorial_rec(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)
# -----------------------------------------------------------------
# 실행 결과와 경과 시간(초) 반환
# -----------------------------------------------------------------
def run_with_time(func, n):
    start = time.perf_counter()     # 시작 시각
    value = func(n)                 # 실행 결과
    end = time.perf_counter()       # 종료 시각
    diff = end - start              # 경과 시간(초)
    return value, diff
# -----------------------------------------------------------------
# 문자열을 0 이상의 정수로 변환
# -----------------------------------------------------------------
def change_into_int(text):
    text = text.strip()             # 공백 제거
    number = int(text)              # 문자열을 정수로 변환
    if number < 0:
        raise ValueError            # 음수면 허용 X
    return number
# -----------------------------------------------------------------
# 메뉴 화면 출력
# -----------------------------------------------------------------
def print_menu():
    print("\n================ Factorial Tester ================")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print("--------------------------------------------------")
# -----------------------------------------------------------------------------
# 옵션 1/2 : 반복문, 재귀 중 한 방식만 실행
# -----------------------------------------------------------------------------
def single(mode):
    try:
        text = input("n 값(정수, 0 이상)을 입력하세요: ")
        n = change_into_int(text)
    except Exception:
        print("정수(0 이상의 숫자)만 입력하세요.")
        return
    
    if mode == "iter":      # 반복문일 때
        value, _ = run_with_time(factorial_iter, n)
        print(f"[반복] {n}! = {value}")
    else:                   # 재귀일 때
        value, _ = run_with_time(factorial_rec, n)
        print(f"[재귀] {n}! = {value}")
# -----------------------------------------------------------------------------
# 옵션 3 : 두 방식 결과/실행 시간 비교
# -----------------------------------------------------------------------------
def compare_both():
    try:
        text = input("n 값(정수, 0 이상)을 입력하세요: ")
        n = change_into_int(text)
    except Exception:
        print("정수(0 이상의 숫자)만 입력하세요.")
        return

    iter_value, iter_time = run_with_time(factorial_iter, n)        # 반복 결과/시간
    rec_value, rec_time = run_with_time(factorial_rec, n)           # 재귀 결과/시간

    print(f"[반복] {n}! = {iter_value}")
    print(f"[재귀] {n}! = {rec_value}")
    print(f"결과 일치 여부 : {'일치' if (iter_value == rec_value) else '불일치'}")
    print(f"[반복] 시간 : {iter_time:.6f} s  |  [재귀] 시간 : {rec_time:.6f} s")
# -----------------------------------------------------------------------------
# 옵션 4 : 테스트 데이터 실행
# -----------------------------------------------------------------------------
def test():
    print("\n[테스트 데이터 실행]")
    for n in TEST_DATA:
        iter_value, iter_time = run_with_time(factorial_iter, n)
        rec_value, rec_time = run_with_time(factorial_rec, n)
        same = (iter_value == rec_value)
        print(f"n=  {n} | same={same} | iter={iter_time:.6f}s, rec={rec_time:.6f}s")
        print(f"  {n}! = {iter_value}")
# -----------------------------------------------------------------------------
# 메인 함수 선언
# -----------------------------------------------------------------------------
def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.")
    while True:
        print_menu()
        choice = input("선택: ").strip().lower()        # 공백 제거/소문자화
        if choice == "1":
            single("iter")
        elif choice == "2":
            single("rec")
        elif choice == "3":
            compare_both()
        elif choice == "4":
            test()
        elif choice == "q":
            print("종료합니다.")
            break
        else:
            print("메뉴에서 1/2/3/4 또는 q 를 입력하세요.")

if __name__ == "__main__":
    main()