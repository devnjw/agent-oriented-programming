from app.database import engine, SessionLocal
from app.models import Base, Movie, Theater, Screening
from datetime import datetime, timedelta
import random
import os

# 기존 데이터베이스 파일 삭제 (경로는 실제 DB 파일 위치에 맞게 수정)
db_file = "app.db"  # 또는 ".db" 확장자를 가진 실제 데이터베이스 파일 경로
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"기존 데이터베이스 파일 '{db_file}'을 삭제했습니다.")

# 데이터베이스 스키마 생성
Base.metadata.create_all(bind=engine)

# 샘플 데이터 추가
db = SessionLocal()

# 영화 데이터 추가 (쉼표로 구분된 다중 장르)
movies_data = [
    {
        "title": "어벤져스: 엔드게임",
        "genres": "액션,SF,모험",
        "director": "루소 형제",
        "release_date": datetime(2019, 4, 24),
        "duration": 181,
        "rating": 8.4,
    },
    {
        "title": "기생충",
        "genres": "드라마,스릴러,코미디",
        "director": "봉준호",
        "release_date": datetime(2019, 5, 30),
        "duration": 132,
        "rating": 8.6,
    },
    {
        "title": "존 윅 4",
        "genres": "액션,범죄,스릴러",
        "director": "채드 스타헬스키",
        "release_date": datetime(2023, 3, 24),
        "duration": 169,
        "rating": 7.8,
    },
    {
        "title": "인터스텔라",
        "genres": "SF,드라마,모험",
        "director": "크리스토퍼 놀란",
        "release_date": datetime(2014, 11, 6),
        "duration": 169,
        "rating": 8.6,
    },
    {
        "title": "라라랜드",
        "genres": "뮤지컬,로맨스,드라마",
        "director": "데이미언 셔젤",
        "release_date": datetime(2016, 12, 7),
        "duration": 128,
        "rating": 8.0,
    },
    {
        "title": "다크 나이트",
        "genres": "액션,범죄,드라마",
        "director": "크리스토퍼 놀란",
        "release_date": datetime(2008, 8, 6),
        "duration": 152,
        "rating": 9.0,
    },
    {
        "title": "미나리",
        "genres": "드라마",
        "director": "리 아이작 정",
        "release_date": datetime(2021, 3, 3),
        "duration": 115,
        "rating": 7.9,
    },
    {
        "title": "서울의 봄",
        "genres": "드라마,역사",
        "director": "김성수",
        "release_date": datetime(2023, 11, 22),
        "duration": 141,
        "rating": 9.1,
    },
    {
        "title": "아바타: 물의 길",
        "genres": "SF,액션,모험,판타지",
        "director": "제임스 카메론",
        "release_date": datetime(2022, 12, 14),
        "duration": 192,
        "rating": 7.6,
    },
    {
        "title": "범죄도시3",
        "genres": "액션,범죄,코미디",
        "director": "이상용",
        "release_date": datetime(2023, 5, 31),
        "duration": 105,
        "rating": 7.0,
    },
    {
        "title": "오펜하이머",
        "genres": "드라마,스릴러",
        "director": "크리스토퍼 놀란",
        "release_date": datetime(2023, 8, 15),
        "duration": 180,
        "rating": 8.8,
    },
    {
        "title": "토이 스토리 4",
        "genres": "애니메이션,가족",
        "director": "조시 쿨리",
        "release_date": datetime(2019, 6, 20),
        "duration": 100,
        "rating": 7.8,
    },
    {
        "title": "괴물",
        "genres": "드라마,스릴러",
        "director": "고레에다 히로카즈",
        "release_date": datetime(2023, 6, 28),
        "duration": 126,
        "rating": 8.2,
    },
    {
        "title": "듄",
        "genres": "SF,모험",
        "director": "드니 빌뇌브",
        "release_date": datetime(2021, 10, 20),
        "duration": 155,
        "rating": 8.1,
    },
    {
        "title": "웅남이",
        "genres": "코미디,드라마",
        "director": "박성광",
        "release_date": datetime(2024, 4, 17),
        "duration": 102,
        "rating": 6.9,
    },
    {
        "title": "엑시트",
        "genres": "코미디,액션",
        "director": "이상근",
        "release_date": datetime(2019, 7, 31),
        "duration": 103,
        "rating": 7.5,
    },
    {
        "title": "스즈메의 문단속",
        "genres": "애니메이션,드라마",
        "director": "신카이 마코토",
        "release_date": datetime(2023, 3, 8),
        "duration": 122,
        "rating": 7.7,
    },
    {
        "title": "극한직업",
        "genres": "코미디,액션,범죄",
        "director": "이병헌",
        "release_date": datetime(2019, 1, 23),
        "duration": 111,
        "rating": 7.8,
    },
    {
        "title": "해리 포터와 불사조 기사단",
        "genres": "판타지,모험,가족",
        "director": "데이비드 예이츠",
        "release_date": datetime(2007, 7, 11),
        "duration": 138,
        "rating": 7.5,
    },
    {
        "title": "킹메이커",
        "genres": "드라마,역사",
        "director": "변성현",
        "release_date": datetime(2022, 1, 26),
        "duration": 123,
        "rating": 7.3,
    },
]

# 영화 추가
for movie_data in movies_data:
    movie = Movie(**movie_data)
    db.add(movie)

db.commit()

# 극장 데이터 추가
theaters = [
    {"name": "CGV 강남", "location": "서울 강남구"},
    {"name": "메가박스 코엑스", "location": "서울 강남구"},
    {"name": "롯데시네마 월드타워", "location": "서울 송파구"},
    {"name": "CGV 센텀시티", "location": "부산 해운대구"},
    {"name": "메가박스 성수", "location": "서울 성동구"},
]

for theater_data in theaters:
    theater = Theater(**theater_data)
    db.add(theater)

db.commit()

# 상영 정보 추가 (오늘부터 7일간)
movies = db.query(Movie).all()
theaters = db.query(Theater).all()

screening_times = [
    datetime.now().replace(hour=10, minute=0, second=0, microsecond=0),
    datetime.now().replace(hour=13, minute=30, second=0, microsecond=0),
    datetime.now().replace(hour=16, minute=0, second=0, microsecond=0),
    datetime.now().replace(hour=19, minute=30, second=0, microsecond=0),
    datetime.now().replace(hour=22, minute=0, second=0, microsecond=0),
]

for day in range(7):  # 7일간의 상영 정보
    for movie in movies:
        for theater in theaters:
            # 모든 영화가 모든 극장에서 상영되지는 않도록 랜덤하게 선택
            if random.random() > 0.3:
                # 랜덤하게 1-3개의 상영 시간 선택
                selected_times = random.sample(screening_times, random.randint(1, 3))
                for time in selected_times:
                    # 해당 날짜의 상영 시간
                    screening_time = time + timedelta(days=day)
                    screening = Screening(
                        movie_id=movie.id,
                        theater_id=theater.id,
                        screening_time=screening_time,
                        available_seats=random.randint(20, 100),
                    )
                    db.add(screening)

db.commit()
db.close()

print("샘플 데이터가 성공적으로 추가되었습니다!")
