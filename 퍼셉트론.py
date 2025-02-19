#파이썬으로 퍼셉트론 학습 알고리즘 구현

import numpy as np

# yhat = w1x1 + w2x2 + ..... wnxn + bias  - w들과 b는 모델이 스스로 변경하는 파라미터
# 파라미터를 변경하는 방법을 조율하기 위해 개발자가 넣어주는 파라미터 - 하이퍼파라미터 (eta, epoch, batch_size)
# 재사용 가능한 클래스로 뉴런에 필요한 속성, 기능들을 몰아넣을 겁니다. 

class Perceptron(object):
    # 최초로 생성될 때 하이퍼파라미터를 가지고 퍼셉트론이 생성되도록
    def __init__(self, eta, n_iter=50, batch_size=1, random_state=1):
            self.eta = eta
            self.n_iter = n_iter
            self.batch_size = batch_size
            self.random_state = random_state

    # 학습시키기 위한 함수
    # X - 독립변수(문제들) - 상수처럼 값을 집어넣기만 할 뿐이다  
    # y - 종속변수(예측되어야 하는 정답) - X의 영향을 받는다 y
    def fit(self, X, y): 
        rgen = np.random.RandomState(self.random_state) 
        
        #  b + w1x2 + w2x2 + ....  필드 개수를 유연하게 받고 
        # (4.2, 1.2, 1.4, 3.5) - 1
        # (0)   - 1
        # (23) - 400 
        self.w_ = rgen.normal(loc=0, scale=0.01, size=X.shape[1] +1 )# 들어오는 X의 컬럼수(특성수)만큼 가중치 w_ + bias의 초기 가중치인 1을 더합니다. 
        self.errors_ = [] # 1개의 bias를 변경하기 위해 학습할 때마다 오차를 list로 전달해서 확인
        print(self.errors_)

        # 실제 학습
        for _ in range(self.n_iter):
            errors = 0

            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi # w1x1 ~ wnxn 까지의 가중치에 오차를 학습률만큼 곱해서 반영
                self.w_[0] += update # b 에 오차를 학습률만큼 곱해서 반영 
                errors += int(update)

                self.errors_.append(errors)

            return self

    # 새 데이터를 추론하기 위한 함수 
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0] # yhat 

    # 추론의 결과 다음 뉴런에게 출력하는 함수 
    def predict(self, X): # 0.0000001 이상이면 클래스 1, 0보다 작으면 -1을 리턴하도록 하는 이진분류기 
        return np.where(self.net_input(X) > 0, 1, -1) 