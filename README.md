## Setup

```bash
pip install -r requirements.txt
python init_db.py
export OPENAI_API_KEY=sk-proj-xxxx
```

## Run

```bash
uvicorn app.main:app --reload
```

## Test

```bash
curl -X POST "http://localhost:8000/api/ask" -H "Content-Type: application/json" -d '{"query": "상영 시간이 가장 짧은 영화랑 가장 긴 영화 알려줘"}'

{"response":"가장 짧은 상영 시간을 가진 영화는 \"토이 스토리 4\"이며, 상영 시간은 100분입니다.\n\n가장 긴 상영 시간을 가진 영화는 \"아바타: 물의 길\"이며, 상영 시간은 192분입니다."}
```

```bash
curl -X POST "http://localhost:8000/api/ask" -H "Content-Type: application/json" -d '{"query": "크리스토퍼 놀란 감독의 영화 중 평점이 높은 영화 추천해줘"}'

{"response":"크리스토퍼 놀란 감독의 영화 중 추천드릴 영화는 \"다크 나이트\"입니다. 이 영화는 2008년 8월 6일에 개봉되었고, 액션, 범죄, 드라마 장르로 평점은 9.0으로 매우 높게 평가되었습니다. 꼭 한 번 시청해보세요!"}
```

```bash
curl -X POST "http://localhost:8000/api/ask" -H "Content-Type: application/json" -d '{"query": "상영관수가 가장 많은 영화관 알려줘"}'

{"response":"가장 상영관 수가 많은 영화관은 \"CGV 강남\"입니다. 해당 영화관은 207개의 상영관을 보유하고 있습니다."}
```
