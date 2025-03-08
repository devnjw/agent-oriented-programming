from openai import OpenAI
from typing import Dict, Any, List

from . import prompts


class ResponseFormatter:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.model_name = model_name
        self.client = OpenAI()

    async def format_response(
        self, original_query: str, sql_query: str, data: List[Dict[str, Any]]
    ) -> str:
        """
        DB에서 가져온 데이터를 기반으로 사용자 친화적인 응답 생성
        """
        if not data:
            data_str = "데이터 없음"
        else:
            data_str = str(data)

        system_prompt = prompts.get_response_formatting_prompt()

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"질문: {original_query}\n\nSQL 쿼리: {sql_query}\n\n데이터: {data_str}",
                },
            ],
        )

        return response.choices[0].message.content.strip()
