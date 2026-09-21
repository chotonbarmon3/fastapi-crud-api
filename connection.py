from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from config import setting
from model import base


url = setting.url

if url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql+asyncpg://", 1)
elif url.startswith("postgresql://"):
    url = url.replace("postgresql://", "postgresql+asyncpg://", 1)

engine=create_async_engine(url , echo=False)

session_local=async_sessionmaker(bind=engine,class_=AsyncSession,autoflush=False,autocommit=False,expire_on_commit=False)

# base.metadata.create_all(bind=engine)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)




async def get_db():
    async with session_local() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise



    
