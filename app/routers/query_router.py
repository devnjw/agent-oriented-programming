from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from ..database import get_db
from ..agent.sql_generator import SQLGenerator
from ..agent.response_formatter import ResponseFormatter
from ..agent.query_executor import QueryExecutor

router = APIRouter(
    prefix="/api",
    tags=["queries"],
)


class NaturalLanguageQuery(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str


@router.post("/ask", response_model=QueryResponse)
async def process_query(request: NaturalLanguageQuery, db: Session = Depends(get_db)):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    """
    자연어 질의를 처리하고 데이터베이스에서 결과를 반환합니다.
    """
    print("--------------------------------")
    print(f"User Request:\n{request.query}")
    print("--------------------------------")

    # 1. SQL 생성
    sql_generator = SQLGenerator(db)
    sql_query = await sql_generator.generate_sql(request.query, current_time)

    print("--------------------------------")
    print(f"Generated SQL Query:\n{sql_query}")
    print("--------------------------------")

    # 2. 쿼리 실행
    executor = QueryExecutor(db)
    data = executor.execute_sql(sql_query)

    print("--------------------------------")
    print(f"Executed SQL Data:\n{data}")
    print("--------------------------------")

    # 3. 응답 포맷팅
    formatter = ResponseFormatter()
    formatted_response = await formatter.format_response(request.query, sql_query, data)

    print("--------------------------------")
    print(f"Formatted Response:\n{formatted_response}")
    print("--------------------------------")

    return {"response": formatted_response}
