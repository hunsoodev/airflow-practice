# Airflow Docker Local Setup

- Docker, Git이 기본적으로 설치되어 있어야 함

## 설치 및 실행 방법
1. 리포지토리 복제
    ```
    git clone https://github.com/hunsoodev/airflow-practice.git
    cd airflow-practice
    ```


2. 환경 설정 파일 생성  
airflow를 실행하기 전에 현재 사용자의 UID를 .env파일에 설정함  
이 작업은 Docker 컨테이너와 호스트 시스템 간의 파일 권한 문제를 해결하기 위해 필요(권장)
    ```
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```

3. Airflow 서비스 시작
    ```
    docker compose up -d
    ```

4. Airflow 웹 인터페이스 접근  
    airflow 웹 인터페이스는 http://localhost:8080 에서 접근할 수 있음. 추가 세부사항은 docker-compose.yaml 파일 참고


5. 종료 및 정리
airflow를 종료하고 모든 컨테이너를 정리하려면 다음과 같은 명령어 사용
    ```
    docker compose down
    ```

