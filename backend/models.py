from sqlalchemy import Column, Integer, String, BigInteger
from database import Base
from sqlalchemy import DateTime
from sqlalchemy import Text

class YouTubeVideo(Base):

    __tablename__ = "youtube_videos"

    id = Column(Integer, primary_key=True)

    video_id = Column(String, unique=True)

    title = Column(String)

    channel_name = Column(String)

    niche = Column(String)

    published_at = Column(String)

    embedding = Column(Text)
    


class YouTubeMetric(Base):

    __tablename__ = "youtube_metrics"

    id = Column(Integer, primary_key=True)

    video_id = Column(String)

    views = Column(BigInteger)

    likes = Column(BigInteger)

    comments = Column(BigInteger)

    fetched_at = Column(DateTime)