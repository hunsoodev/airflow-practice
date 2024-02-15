import glob
import os
import pytest
# from airflow.models import DAG
from airflow.models.dagbag import DagBag

DAG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "dags/**/*.py")
DAG_FILES = glob.glob(DAG_PATH, recursive=True)

@pytest.mark.parametrize("dag_file", DAG_FILES)
def test_dag_integrity(dag_file):
    dag_bag = DagBag(dag_folder=os.path.dirname(dag_file), include_examples=False)
    # DAG 파일 로드
    dag_bag.process_file(dag_file, only_if_updated=True)
    # 로드된 DAG들을 검사
    for dag_id, dag in dag_bag.dags.items():
        print(f"DAG ID: {dag_id}, DAG Object: {dag}")
        # DagBag의 process_file 메소드가 순환 의존성을 포함한 여러 오류를 검사
        # 오류가 있는 경우, 해당 DAG는 dag_bag.dags에 포함되지 않음

        # DAG 객체 존재 여부 확인
        assert dag_id in dag_bag.dags

        # DagBag에서 오류 메시지를 확인하여 순환 의존성이나 기타 문제가 있는지 검사
        assert not dag_bag.import_errors

