from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Dict, Any, List


class QueryExecutor:
    def __init__(self, db: Session):
        self.db = db

    def execute_sql(self, sql_query: str) -> List[Dict[str, Any]]:
        """
        SQL 쿼리를 실행하고 결과를 반환합니다.
        보안을 위해 파라미터화된 쿼리를 사용하는 것이 좋지만,
        예시에서는 간단히 직접 실행합니다.
        """
        try:
            result = self.db.execute(text(sql_query))
            columns = result.keys()

            # 결과를 딕셔너리 리스트로 변환
            rows = [dict(zip(columns, row)) for row in result]
            return rows
        except Exception as e:
            # 실제 구현에서는 더 세밀한 예외 처리 필요
            print(f"SQL 실행 오류: {e}")
            return []
