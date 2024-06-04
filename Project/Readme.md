# 주제 : 선형점화식의 일반항 유도 및 그래프 계산 프로젝트

                                                            2021131016 이준원

## 1. 모티베이션(프로젝트를 하게 된 동기)

   : 수학과 프로그래밍 수업 진행간, Recursion(점화식)의 코딩 방식(Memorization, Bottom up)에 대해서 배울 수 있었다. 해당 방식을 통해, 기존 점화식 작성 코드보다 더욱 빠르고 적은 용량으로 점화식의 값을 구할 수 있었다. 하지만, 해당 코딩 방식에서는 "매우 큰 항에 대해서는 값을 구하는 것이 다소 어렵다는 점, 점화식을 일반화하기 어렵다는 점(항이 3개, 4개, ...등 인 경우, 내가 원하는 설정(점화식의 계수, 초기항의 값)으로 점화식을 구하기 어렵다는 점 등"이 문제점으로 느껴졌다. 이산수학 과목에서 배운 내용에 따르면, 특성방정식을 만들고 해당 방정식의 근을 구함으로써, 선형점화식의 일반항을 계산할 수 있다는 것을 배웠다. 이를 접목하면, 선형점화식을 일반화하고 매우 큰 항의 값도 빠른 시간내에 구할 수 있을 것이라 판단하여 해당 주제로 프로젝트를 진행하였다.

## 2. 이론적 배경

  1) 선형 점화식 및 특성 방정식
     : 수열 ${a_n}$에 대하여 $a_{n+k}+c_1a_{n+k-1}+...+c_ka_n=f(n)$의 형태로 나타내는 점화식을 선형 점화식이라고 한다. 이때, r에 대한 방정식 $r^{n+k}+c_1r^{n+k-1}+...+c_kr{n}=0$을 이 점화식의 특성방정식이라 한다. 

  2) 선형점화식의 일반항 유도
     : 1)의 특성방정식에서, $α_{1}, α_{2}, ..., α_{n}$을 특성방정식의 근이라 하자. 이때, 점화식의 일반항은 $α_{1}^n, α_{2}^n, ..., α_{n}^n$의 일차결합으로 표현된다.
     <br/>(1) 만약 특성방정식의 근에서 중복된 근이 존재하지 않으면, ${a_n}=A_1α_{1}^n, A_2α_{2}^n, ..., A_nα_{n}^n$으로 나타낼 수 있으며, 초기항($a_1, a_2, ...$)의 값을 대입하여, $A_1, A_2, ..., A_n$을 구할 수 있다.
    <br/>(2) 만약 특성벙장석의 근에서 어떤 근 β가 k번 중복된다면, 중복되는 근은 $β^n, nβ^n, ... , n^{k-1}β^n$으로 표현해야 한다. 이후, 중복되지 않은 근과의 일차결합을 통해 특성방정식의 일반항을 표현할 수 있다.

## 3. 코드 작성방법 및 설명

  ### 1) import
```
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sys
```
1. numpy : 점화식의 일반항을 유도하고, 이를 그래프로 옮기는 코드를 작성하는 과정에서, np.arange을 이용해 x축에 변수를 추가해주었다.

2. matplotlib.pyplot : 점화식의 일반항을 그래프로 그리는 과정에서 matplotlib 모듈을 사용하였다.

3. sympy : 변수를 지정하고, 방정식을 설정하고, 방정식의 해를 구하기 위해 해당 모듈을 사용하였다.
   
   (a) `x = sp.symbols('n')` : x를 기호변수 n으로 선언해준다. 해당 기호변수를 통해, 수식을 나타내고 이에 대한 근을 구하거나, 기호변수에 특정한 값을 대입할 수 있다.
   
   (b) `sp.Eq(LHS, RHS)` : 좌변에는 LHS, 우변에는 RHS으로 이루어진 등식을 만들어준다. (ex. `E = sp.Eq(x**2, 1)` => `E`: `x**2 = 1` (`E`라는 변수에 `x**2 = 1`을 대입한다.)
   
   (c) `sp.Rational(a, b)` : 유리수를 분수 {a/b}로 나타낸다. `sp.Rational(a)`는 `a`로 출력된다.
   
   (d) `sp.solve(Eqn, x)`, `sp.roots(Eqn, x)` : `Eqn`이라는 방정식에 대하여 `x`에 관한 해를 구한다. `sp.solve(Eqn, x)`는 `x`에 관한 해만 출력하는 반면, `sp.roots(Eqn, x)`는 다항식의 해를 keys, 각 해의 중복도를 values로 갖는 dictionary를 반환한다.
   
   (e) `sp.lambdify(x, fct, 'numpy')` : `x`라는 변수를 갖는 `fct` 표현식을 실제 계산에 사용할 수 있도록 파이썬 함수로 변환할 수 있다. (Ex. `f = sp.lambdify(x, sp.sin(x), 'numpy')`로 지정한다면, `f(np.pi/2)`는 1이라는 값을 갖는다.

   (f) eqn.subs(x, 1) : 기호변수에 특정한 값을 대입하거나, 다른 기호변수로 대체할 수 있는 메소드이다.
   <br/> (ex. eqn=$x^2+5$ => eqn.subs(x,2)=$2^2+5=9$ / eqn.subs(x,t)=$t^2+5$

5. sys : `sys.exit()`코드를 이용해, 프로젝트의 코드를 종료하게 만들었다.

본격적인 설명에 앞서, 정의한 메소드, 함수들은 RecurrenceRelation 클래스 안에 있다.
  ### 2) __init__
  ```
    def __init__(self): #변수 저장
        self.coefficients = [] # (e.g, Fn=2*F(n-1)+3*F(n-2) => self.coefficients = [2,3])
        self.initial_values = [] # (e.g, F1=1, F2=2 => self.initial_values = [1,2])
        self.char_eq_roots = [] # 특성방정식의 해를 저장하는 variable
        self.general_solution = None # 점화식의 일반항을 저장하는 variab
```

이후 후술할 메소드들에서 구한 데이터들을 각 변수들에 반환한다.

self.coefficients : 선형점화식에서 이루어진 계수들을 저장하는 변수이다.
<br/>(Ex. $F_n=2F_{n-1}+3F_{n-2}$의 구조로 이루어진 선형점화식을 데이터로 갖는다면, self.coefficients = [2, 3]이 된다.)

self.initial_values : 선형점화식에서 정해진 초기항들의 값들을 저장하는 변수이다.
<br/>(Ex, $F_n=2F_{n-1}+3F_{n-2}$ / F1=2, F2=5 라면, self.initial_values=[2, 5]이다.

self.char_eq_roots : 특성방정식의 근과 중복도를 각각 keys, values로 갖는 dictionary를 저장한다.
<br/>(Ex, $F_n=-2F_{n-1}-1F_{n-2}$에서, 특성방정식의 근은 -1, 중복도는 2이다. 이때, self.char_eq_roots={-1 : 2}가 된다.

self.general_solution : 점화식의 일반항을 유도한 뒤, 해당 일반항을 저장한다.

  ### 3) set_variables
  ```
    def set_variables(self): #1번 변수 저장 함수 : 점화식 계산에 필요한 변수개수, 항의 계수, 점화식의 초기항 등을 입력하고 저장한다
      try:
        n = int(input("변수의 개수를 입력하세요 (ex. 2 => Fn=Fn-1+Fn-2): "))
        self.coefficients = [sp.Rational(input(f"계수 a{i+1}을(를) 입력하세요: ")) for i in range(n)]
        self.initial_values = [sp.Rational(input(f"F{i+1}을(를) 입력하세요: ")) for i in range(n)]
        print("변수가 성공적으로 지정되었습니다.")
```

main 함수에서의 1번 함수이다. (코드 실행 후, 1을 입력 시 해당 함수가 실행된다.)

위 함수에서, 점화식을 설정하고 각 데이터들을 변수에 반환하는 기능을 한다.

처음 n은 항의 개수이다. 구하고자 하는 선형점화식의 항의 개수를 입력하면 된다. 
<br/>(ex. n=3이면, $F_n=a_1F_{n-1}+a_2F{n-2}+a_3F{n_3}$꼴의 선형점화식을 가짐. n=2이면, $F_n=a_1F_{n-1}+a_2F{n-2}$꼴의 선형점화식을 가짐.)

이후, 각 점화식의 계수와 초기항의 값들을 입력한다.
<br/>(ex. $n=2, a_1=1, a_2=1, F_1=1, F_2=1$으로 설정하면, $F_n=F_{n-1}+F_{n-2} / F_1=1, F_2=1$(피보나치 수열)의 선형점화식으로 설정 가능)

  ### 4) compute_characteristic_equation
  ```
    def compute_characteristic_equation(self): #2번 특성방정식 및 해 계산 함수 : 1번 변수 저장 함수를 통해 저장한 변수를 이용해, 해당 점화식의 특성방정식을 구하고 이를 계산한다.
        if self.coefficients==[]:
            print("변수 지정을 먼저 해주세요.")
            return

        x = sp.symbols('x')
        n = len(self.coefficients)
        LHS = x**n - sum(self.coefficients[i] * x**(n-1-i) for i in range(n))
        equation = sp.Eq(LHS, 0)

        self.char_eq_roots = sp.roots(equation, x)

        print(f"특성방정식: \n{LHS} = 0")
        print(f"특성방정식의 해: {self.char_eq_roots}")
```

main 함수에서의 2번 함수이다. (코드 실행 후, 2를 입력 시 해당 함수가 실행된다.)

1번 함수에서 지정한 선형점화식 변수들을 이용해서 특성방정식을 유도하고 특성방정식의 해 및 중복도를 계산하는 함수이이다.

만약 1번 함수를 실행하지 않고, 2번 함수를 실행할 시, 설정한 선형점화식이 없기 때문에 "변수 지정을 먼저 해주세요."라는 문구와 함께 return된다.

위 코드에서, x는 기호변수 x로 작동한다. LHS는 특성방정식의 좌항으로, 설정한 선형점화식을 변수 x에 관한 식으로 변환한 뒤, 이들을 전부 좌항으로 이항한 값이다.
<br/>(ex. $F_n=F_{n-1}+F_{n-2} (피보나치 수열)$이라면, $x^n=x^{n-1}+x^{n-2}$가 되고, LHS는 이들을 전부 좌항으로 이항한 $x^n-x^{n-1}-x^{n-2}$가 된다.)

따라서, 위와 같은 식으로 LHS 변수를 지정했다.

이에 따라, 우항은 0이 되므로 특성방정식은 sp.Eq(LHS,0)이 된다.

이후, sp.roots를 통해 해당 방정식을 계산하고 특성방정식의 해와 중복도를 각각 keys와 values로 갖는 dictionary를 self.char_eq_roots에 저장하고 특성방정식과 해당 dictionary를 출력하였다.

  ### 5) compute_general_term
```
    def compute_general_term(self): #3번 점화식의 일반항 계산 함수 : 2번 특성방정식 및 해 계산  함수를 통해 나온 해(근)을 통해, 점화식의 일반항을 도출한다.
      if self.char_eq_roots==[]:
        print("특성방정식의 해를 먼저 계산해주세요.")
        return

      n = len(self.char_eq_roots)
      k = sp.symbols('n')
      terms=[]
      for a, b in self.char_eq_roots.items():
        if b==1:
          terms.append(a**k)
        elif b!=1:
          for j in range(b):
            terms.append(k**j * a**k)

      x = sp.symbols(f'x:{len(terms)}')

      equation = sum(x[j] * terms[j] for j in range(len(terms)))
      equations = []

      for i in range(1, len(self.initial_values)+1):
        equations.append(sp.Eq(equation.subs(k,i),self.initial_values[i-1]))

      constants=sp.solve(equations)

      general_solution_terms=[]
      for term, constant in zip(terms, constants.values()):
        general_solution_terms.append(constant * term)

      self.general_solution = sum(general_solution_terms)

      print("점화식의 일반항 계산 결과:")
      print(f"Fn = {self.general_solution}")
```

main 함수에서의 3번 함수이다. (코드 실행 후, 3을 입력 시 해당 함수가 실행된다.)

2번 함수에서 얻은 특성방정식의 근과 중복도, 1번 함수에서 얻은 점화식의 초기항의 값을 이용하여 점화식의 일반항을 유도하는 함수이다.

만약 2번 함수를 실행하지 않고, 3번 함수를 실행할 시, 특성방정식의 해와 중복도에 대한 데이터가 없기 때문에 "특성방정식의 해를 먼저 계산해주세요."라는 문구와 함께 return된다.

우선, 특성방정식의 해의 n제곱에 관한 일차결합으로 나타내기 전에, terms라는 list에 각 특성방정식의 해의 n제곱에 해당하는 데이터들을 넣어주었다.

이론적 배경에 의하면, 중복수이다.

만약 3번 함수를 실행하지 않고, 4번 함수를 실행할 시, 점화식의 일반항에 대한 데이터가 없기 때문에 "점화식의 일반항을 먼저 계산해주세요."라는 문구와 함께 return된다.

계산 결과를 구하고 싶은 항을 입력하면, subs()매소드를 통해, n에 관한 점화식의 일반항에 해당 값을 직접 대입하고 이를 specific_term에 저장한다. 이때, evalf(n=15) 메소드를 이용해, 해당 항의 계산 결과 값을 15자리로 계산해준다.

이후, 해당 데이터값을 직접 출력하게된다.

  ### 6) plot_solution
  ```
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
        n_values = np.arange( x + 1 )
        general_solution_values = general_solution_func(n_values)

        plt.plot(n_values, general_solution_values, label='General Solution')
        plt.xlabel('n')
        plt.ylabel('F(n)')
        plt.title('Comparison of General Solution and Actual Recurrence')
        plt.legend()
        plt.show()
```
main 함수에서의 5번 함수이다. (코드 실행 후, 5를 입력 시 해당 함수가 실행된다.)

3번 함수에서 얻은 점화식의 일반항을 그래프로 시각화하는 함수이다.

만약 3번 함수를 실행하지 않고, 5번 함수를 실행할 시, 점화식의 일반항에 대한 데이터가 없기 때문에 "점화식의 일반항을 먼저 계산해주세요."라는 문구와 함께 return된다.






