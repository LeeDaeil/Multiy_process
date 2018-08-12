from Process_1 import P_1
from Process_2 import P_2


class start_main:
    def __init__(self):
        # 공유되는 메모리 선언 -> 즉 글로벌 변수로 활용 가능
        self.mother_mem = [0, 0]


    def start_process(self):
        Pro_ = [P_1(self.mother_mem), P_2(self.mother_mem)]
        # Pro_.run()
        for agent in Pro_:
            agent.start()


if __name__ == '__main__':
    Test = start_main()
    Test.start_process()



