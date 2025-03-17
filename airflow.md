# **MLOps**

- **MLOps**는 **Machine Learning Operations**의 약자로, 머신러닝(ML) 모델을 배포, 모니터링, 유지 관리하는 일련의 과정을 의미합니다. 이는 전통적인 소프트웨어 애플리케이션을 다루는 DevOps와 비슷합니다.
- **MLOps의 목표**: ML 모델의 개발 생명 주기를 **자동화**하고 **최적화**하는 것이 목표입니다. 이를 통해 기업이 머신러닝 모델을 **신뢰성 있게** 그리고 **효율적으로** 활용할 수 있게 됩니다.



## MLOps가 필요한 이유

1. **ML 모델의 복잡성**: 머신러닝 모델은 개발과 배포가 복잡할 수 있습니다. MLOps는 이러한 모델을 더 쉽게 관리할 수 있게 합니다.
2. **변하는 데이터**: ML 모델은 데이터를 기반으로 학습하는데, 시간이 지나면 데이터가 바뀔 수 있습니다(이를 "데이터 드리프트"라고 부릅니다). MLOps는 모델을 모니터링하고 데이터가 바뀔 때 모델을 업데이트할 수 있게 도와줍니다.
    
`Data drift` : 훈련시킨 모델과 실제 운영 환경에서의 데이터 사이에 발생하는 변화. 시간이 지남에 따라 실제 환경에서의 데이터 분포가 달라지며 발생할 수 있고 모델 성능 저하의 주요 요소 중 하나입니다.

3. **팀 간 협업**: 머신러닝은 데이터 과학자, 개발자, 운영팀이 함께 일하는 분야입니다. MLOps는 이들이 더 효과적으로 협력할 수 있도록 돕습니다.
4. **환경 재현이 가능**: 배포한 모델에 문제가 생기는 경우 빠르게 환경을 재현할 수 있게 됩니다.


## **MLOps의 장점**

1. **빠른 배포**: 머신러닝 모델의 배포 과정을 자동화하여, 프로덕션 환경까지의 시간을 단축.
2. **협업 효율성 향상**: 데이터 과학자, 개발자, 운영팀이 함께 더 원활하게 협업할 수 있음.
3. **모델 성능 향상**: 지속적으로 모델을 모니터링하고 필요 시 업데이트하여 성능을 최적 상태로 유지.



# 1. Airflow의 개념

### **Batch Process**

- 프로그래밍에서는 컴퓨터 프로그램 흐름에 따라 일회성(1회), 또는 주기마다 예약된 시간에 실행되는 프로세스를 `Batch Process`라고 부릅니다. Airflow는 `Batch Process` 에 최적화된 프레임워크입니다.
Airflow


- Airflow는 Flask 기반으로 작성된 여러가지 태스크들(데이터셋 생성, 모델 학습 등)을 일련의 그래프로 연결하고 스케줄링, 모니터링 등 파이프라인 관리를 위한 다양한 기능을 제공하고 있는 Workflow Management Platform입니다. 



- 워크플로는 DAG(Directed Acyclic Graph)로 표시되며, 종속성과 데이터 흐름을 고려하여 정렬된 Task라는 개별 작업을 포함합니다.



- DAG는 작업 간의 종속성과 Task를 실행하고 재시도를 실행하는 순서를 지정합니다. Airflow는 일반적으로 다음 구성 요소를 포함합니다.
    - Scheduler: 예약된 워크플로를 트리거하고 Task를 실행하도록 관리합니다.
    - Executor: 실행 중인 task를 처리합니다. 기본적으로 executor는 scheduler 내에 포함된 task를 관리하지만 운영 환경에 적합한 executor는 worker에 task를 푸시합니다.
    - Webserver: DAG 및 task의 동작을 검사, 트리거 및 디버그할 수 있는 사용자 인터페이스를 제공합니다.
    - Metadata Database: Scheduler, executor 및 webserver에서 상태를 저장하는 데 사용하는 메타데이터 데이터베이스입니다.



- Workloads DAG는 일련의 task를 통해 실행되며 다음과 같은 세 가지 일반적인 task 유형이 있습니다.
    - Operators: 개념적으로 DAG 내에서 미리 정의된 task에 대한 템플릿
    - Sensors: 한 가지 task를 수행하도록 설계된 특수한 유형의 operator
    - TaskFlow: Python 코드를 사용하여 DAG를 작성하는 경우, TaskFlow API를 사용하면 추가 상용구 없이 DAG를 쉽게 작성 가능




### Ubuntu 환경에서 Docker로 설치 및 실행

$ ubuntu

$ mkdir airflow

$ cd airflow

$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'

$ mkdir -p ./dags ./logs ./plugins ./config

$ echo AIRFLOW_UID=50000 > .env

$ docker compose up airflow-init

$ docker compose up


## 가. Airflow 코드의 기본 구조

1) DAG 대표하는 객체를 먼저 만들기

- DAG 이름, 실행주기, 실행날짜, 오너 등등

2) DAG를 구성하는 태스크 만들기

- 태스크별로 적합한 오퍼레이터를 선택
- 태스크 ID를 부여하고 해야할 작업의 세부사항 지정

3) 최종적으로 태스크들 간의 실행 순서를 결정

4) UI에서 실행과 확인
- DAG 파일을 저장하면, Airflow 웹 UI에서 확인할 수 있습니다.
- Airflow 웹 UI에서 해당 DAG을 ON으로 변경하면 DAG이 스케줄링되어 실행됩니다.
- DAG 세부 페이지에서 실행된 DAG Run의 결과를 볼 수 있습니다.

- Airflow는 DAG이라는 단위로 스케줄링을 관리합니다.
- 각 DAG은 Task로 구성되며,
- DAG 내 Task는 순차적으로 실행되거나, 동시에(병렬로) 실행할 수 있습니다.


크론식을 사용하면 특정 날짜로는 스케쥴을 정의할 수 있지만, 특정 빈도로는 스케쥴을 정의하기 어렵습니다. (3일마다, 2일마다 등등) 그래서 airflow는 스케쥴 간격에 대한 프리셋을 제공합니다. 
