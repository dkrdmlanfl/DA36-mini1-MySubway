from repository.admin_repo import AdminRepo

class AdminService:

#순수익 #총매출만 구현하자. 총매출을 날자별로 확인해서 적립할 수 있도록.
    def __init__(self) :
        self.admin_repo = AdminRepo()
        self.sales_data = []
        self.total_price = []

        #순매출
    def total_sales(self):

        total_sales = self.total_price*0.3
        


        # def add_sale(self, allsales):
        #     """매출을 추가하는 메소드"""
        #
        #     if allsales <= 0:
        #         print("매출 금액은 0보다 커야 합니다.")
        #         return
        #     self.sales_data.append(allsales)
        #     print(f"{allsales}원이 추가되었습니다.")
        #
        # def total_sales(self):
        #     """총 매출을 계산하는 메소드"""
        #     total = sum(self.sales_data)
        #     print(f"총 매출은{total}원 입니다.")
        #     return total
        #
        # def show_sales(self):
        #     """모든 매출을 보여주는 메소드"""
        #     if not self.sales_data:
        #         print("매출 데이터가 없습니다.")
        #     else:
        #         print("현재 매출 데이터:")
        #         for i, sale in enumerate(self.sales_data, start=1):
        #             print(f"{i}. {sale}원")

            # def pureearn(self): #순수익
            #     pureearns = sum(sales_data) *.3
            #     print(f'총 순익은 {pureearns}원 입니다.')
            #
            # def purespand(self):#순지출
            #     purespands =sum(sales_data) *.15
            #     print(f"총 지출은 {purespands}원 입니다.")
            # # 메인 프로그램

        def main():
            pass
        # sales_manager = Sales()  # Sales 클래스의 인스턴스 생성
        # while True:
        #     print("\n매출 관리 시스템")
        #     print("1. 매출 추가")
        #     print("2. 총 매출 조회")
        #     print("3. 매출 목록 조회")
        #     print("0. 종료")
        #     choice = input("선택: ")
        #
        #     match choice:
        #         case '1':
        #             amount = float(input("추가할 매출 금액을 입력하세요: "))
        #             sales_manager.add_sale(amount)
        #         case '2':
        #             total = sales_manager.total_sales()
        #             print(f"총 매출: {total}원")
        #         case '3':
        #             sales_manager.show_sales()
        #         case '0':
        #             print("프로그램을 종료합니다.")
        #             break
        #         case _:
        #             print("잘못된 선택입니다.")

    # if __name__ == "__main__":
    #     main()

    # #def weeksales(self):#주간 총 매출
    #     weeksales =weeksales()
    #     print(f"금 주의 총 매출은 {weeksales}원 입니다.")
    #
    # def compareweeksales(self): # 주간 판매금 비교하기
    #     weeksales = {
    #         user_repo.weeksale()
    #     }
    #
    #     # 딕셔너리 항목 출력
    #     print("다음 항목 중에서 2개를 선택하세요:")
    #     for key, value in dict.items():
    #         print(f"{key}: {value}")
    #
    #     choice1 = int(input("첫 번째 주간을 선택해주세요 : "))
    #     choice2 = int(input("두 번째 주간을 선택해주세요 : "))
    #     # max_sales= max(choice1, choice2) - 두개 중 어느 것이 더 큰지.
    #     if choice1 in dict and choice2 in dict:
    #         print(f"첫 번째 선택: {dict[choice1]}")
    #         print(f"두 번째 선택: {dict[choice2]}")
    #         print(f"양 주간의 매출금 격차는 {dict[choice1]}-{dict[choice2]} 원 입니다.")
    #     else:
    #         print("잘못된 선택입니다. 유효한 번호를 입력하세요.")
