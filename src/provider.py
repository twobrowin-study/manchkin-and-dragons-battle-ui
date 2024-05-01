from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)
import dotenv, os

class Provider:
    """
    Класс, обеспечивающий работу
    """

    def __init__(self) -> None:
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.db_engine = create_async_engine(
                f"postgresql+asyncpg://{os.environ.get('PG_USER')}:{os.environ.get('PG_PASSWORD')}@{os.environ.get('PG_HOST')}:{os.environ.get('PG_PORT')}/{os.environ.get('PG_DB')}", 
                echo=False,
                pool_size=10,
                max_overflow=2,
                pool_recycle=300,
                pool_pre_ping=True,
                pool_use_lifo=True
            )
        self.db_session = async_sessionmaker(bind = self.db_engine)