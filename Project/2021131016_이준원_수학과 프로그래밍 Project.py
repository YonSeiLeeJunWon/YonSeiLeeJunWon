import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sys

class RecurrenceRelation:
    def __init__(self): #변수 저장
        self.coefficients = [] # (e.g, Fn=2*F(n-1)+3*F(n-2) => self.coefficients = [2,3])
        self.initial_values = [] # (e.g, F1=1, F2=2 => self.initial_values = [1,2])
        self.char_eq_roots = [] # 특성방정식의 해를 저장하는 variable
        self.general_solution = None # 점화식의 일반항을 저장하는 variable

    def set_variables(self): #1번 변수 저장 함수 : 점화식 계산에 필요한 변수개수, 항의 계수, 점화식의 초기항 등을 입력하고 저장한다
      try:
        n = int(input("변수의 개수를 입력하세요 (ex. 2 => Fn=Fn-1+Fn-2): "))
        self.coefficients = [sp.Rational(input(f"계수 a{i+1}을(를) 입력하세요: ")) for i in range(n)]
        self.initial_values = [sp.Rational(input(f"F{i+1}을(를) 입력하세요: ")) for i in range(n)]
        print("변수가 성공적으로 지정되었습니다.")

      except ValueError:
        print("잘못된 입력입니다. 다시 시도해주세요.")

    def compute_characteristic_equation(self): #2번 특성방정식 및 해 계산 함수 : 1번 변수 저장 함수를 통해 저장한 변수를 이용해, 해당 점화식의 특성방정식을 구하고 이를 계산한다.
        if self.coefficients==[]:
            print("변수 지정을 먼저 해주세요.")
            return

        x = sp.symbols('x')
        n = len(self.coefficients)
        LHS = x**n - sum(self.coefficients[i] * x**(n-1-i) for i in range(n)) #특성방정식에서의 좌항(LHS) 계산
        equation = sp.Eq(LHS, 0) #좌항=LHS, 우항=0

        self.char_eq_roots = sp.roots(equation, x) #좌항=LHS, 우항=0 인 방정식의 해 계산 (이때, self.char_eq_roots는 해를 keys, 중복도를 values로 갖는 딕셔너리)

        print(f"특성방정식: \n{LHS} = 0")
        print(f"특성방정식의 해: {self.char_eq_roots}")

    def compute_general_term(self): #3번 점화식의 일반항 계산 함수 : 2번 특성방정식 및 해 계산  함수를 통해 나온 해(근)을 통해, 점화식의 일반항을 도출한다.
      if self.char_eq_roots==[]:
        print("특성방정식의 해를 먼저 계산해주세요.")
        return

      k = sp.symbols('n')
      terms=[] #일반항은 각각의 계수*terms의 원소 들의 합으로 표현할 수 있다. 이때, terms는 특성방정식의 해와 중복도를 이용함
      for a, b in self.char_eq_roots.items():
        if b==1: #중복도가 1인 경우, 해당 근에 n제곱한 뒤, terms에 추가한다.
          terms.append(a**k)
        elif b!=1: #중복도가 1보다 큰 경우, 해당 근에 n제곱한 뒤, b의 값만큼 n제곱을 한 뒤 각각을 terms에 추가한다.
          for j in range(b):
            terms.append(k**j * a**k)

      x = sp.symbols(f'x:{len(terms)}') 

      equation = sum(x[j] * terms[j] for j in range(len(terms))) #일반항은 각각의 계수*terms의 원소들의 합이다.
      equations = []

      for i in range(1, len(self.initial_values)+1):
        equations.append(sp.Eq(equation.subs(k,i),self.initial_values[i-1])) #위 equation에 각각의 초기항 대입하면 이들이 초기항의 데이터값과 같다. 이에 대한 연립방정식 

      constants=sp.solve(equations) #연립방정식을 풀면, 각각의 계수가 나온다. 이때, constants는 x0, x1,...,를 keys, 각 계수의 값을 values로 갖는 딕셔너리이다.
      general_solution_terms=[]
      for term, constant in zip(terms, constants.values()):
        general_solution_terms.append(constant * term)

      self.general_solution = sum(general_solution_terms)

      print("점화식의 일반항 계산 결과:")
      print(f"Fn = {self.general_solution}")

    def compute_specific_term(self): #4번 점화식의 값 대입 함수 : 3번에서 구한 점화식의 일반항을 통해, 점화식의 n번째 항에 해당하는 값을 계산한다.
      if not self.general_solution:
        print("점화식의 일반항을 먼저 계산해주세요.")
        return

      try:
        n = int(input("계산 결과를 구하고 싶은 항을 입력하세요: "))
        if n<=0:
          print("잘못된 입력입니다. 다시 시도해주세요")
          return
        else:
          specific_term = self.general_solution.subs(sp.symbols('n'),n).evalf(n=15) 
          print(f"F{n}의 값은 {specific_term}입니다.")

      except ValueError:
        print("잘못된 입력입니다. 다시 시도해주세요.")

    def plot_solution(self): # 3번에서 구한 점화식의 일반항을 그래프로 나타낸다.
        if not self.general_solution:
            print("점화식의 일반항을 먼저 계산해주세요.")
            return

        try:
            x = int(input("그래프로 항의 인덱스를 입력하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            return

        k = sp.symbols('n')
        general_solution_func = sp.lambdify(k, self.general_solution, 'numpy')
        n_values = np.arange(1, x + 1)
        general_solution_values = general_solution_func(n_values)

        plt.plot(n_values, general_solution_values, label='점화식')
        plt.xlabel('n')
        plt.ylabel('F(n)')
        plt.title('점화식의 특정 항의 값')
        plt.legend()
        plt.show()


def main(): # main 함수 : 1~6까지의 수를 입력하여 입력값에 해당하는 함수를 실행한다.
    rr = RecurrenceRelation()
    actions = {
        '1': rr.set_variables,
        '2': rr.compute_characteristic_equation,
        '3': rr.compute_general_term,
        '4': rr.compute_specific_term,
        '5': rr.plot_solution
    }

    while True:
        print("\n1. 변수 지정\n2. 점화식의 특성방정식 및 해 계산\n3. 점화식의 일반항 계산\n4. 점화식 대입\n5. 점화식의 그래프 시각화\n6. 종료")
        choice = input("실행할 함수를 선택하세요: ")
        if choice in actions:
            actions[choice]()
        elif choice=='6': #6번을 입력할 시, 코드를 종료한다.
          sys.exit("코드를 종료합니다")
        else:
            print("유효하지 않은 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
