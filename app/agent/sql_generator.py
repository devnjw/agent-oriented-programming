from openai import OpenAI
from typing import Dict, Any
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from . import prompts


class SQLGenerator:
    def __init__(self, db: Session, model_name: str = "gpt-4o-mini"):
        self.db = db
        self.model_name = model_name
        self.engine = db.get_bind()
        self.client = OpenAI()

    def get_db_schema(self) -> str:
        """데이터베이스 스키마 정보를 문자열로 반환"""
        schema_info = []
        inspector = inspect(self.engine)

        for table_name in inspector.get_table_names():
            columns = inspector.get_columns(table_name)
            schema_info.append(f"테이블: {table_name}")
            for column in columns:
                schema_info.append(f"  - {column['name']}: {column['type']}")

        return "\n".join(schema_info)

    async def generate_sql(self, query: str, current_time: str) -> Dict[str, Any]:
        """자연어 쿼리를 SQL로 변환"""
        db_schema = self.get_db_schema()
        system_prompt = prompts.get_sql_generation_prompt(db_schema, current_time)

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
            ],
            temperature=0.1,  # 정확한 SQL 생성을 위해 낮은 temperature 사용
        )

        sql_query = response.choices[0].message.content.strip()

        return sql_query
