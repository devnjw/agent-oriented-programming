from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    genres = Column(String, index=True)  # "액션,드라마,SF" 형식으로 저장
    director = Column(String)
    release_date = Column(DateTime)
    duration = Column(Integer)  # 분 단위
    rating = Column(Float)  # 평점

    screenings = relationship("Screening", back_populates="movie")


class Theater(Base):
    __tablename__ = "theaters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    screenings = relationship("Screening", back_populates="theater")


class Screening(Base):
    __tablename__ = "screenings"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    theater_id = Column(Integer, ForeignKey("theaters.id"))
    screening_time = Column(DateTime, nullable=False)
    available_seats = Column(Integer, default=100)

    movie = relationship("Movie", back_populates="screenings")
    theater = relationship("Theater", back_populates="screenings")
