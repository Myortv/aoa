import asyncpg
from asyncpg.pool import Pool

from utils.utils import raise_exception


class DatabaseManager():
    class Config:
        POOL: Pool = None
        PSQL_DATABASE: str = None
        PSQL_USER: str = 'postgres'
        PSQL_PASSWORD: str = 'hf0128mnr'
        PSQL_HOST: str = '82.118.245.233'

    @classmethod
    async def start(
        cls,
        database: str,
        user: str = None, 
        password: str = None,
        host: str = None,
    ) -> None:
        """
            Firstly, try loads from envirement, then from function arguments,
            then from plugun defaults.

            see plugins.AbsctractPlugin.loads_secrets for more
        """
        database, user, password, host = cls.loads_secrets(
            PSQL_DATABASE=database,
            PSQL_USER=user,
            PSQL_PASSWORD=password,
            PSQL_HOST=host,
        )
        cls.Config.POOL = await asyncpg.create_pool(
            database=database,
            user=user,
            password=password,
            host=host
        )

    @classmethod
    def make_async(cls):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                async with  cls.Config.POOL.acquire() as conn:
                    try:
                        result = await func(*args, conn=conn, **kwargs)
                    except Exception as e:
                        raise_exception(e)
                return result

                return await func(*args, **kwargs)
            return wrapper
        return decorator 

