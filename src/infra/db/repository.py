from sqlalchemy import select

from src.domain.models import User
from src.infra.db.db_mixin import DatabaseMixin


class UsersRepository(DatabaseMixin):

    async def save_user(self, user: User):
        async with self._cursor() as session:
            stmt = select(User).where(
                (User.app_bundle_id == user.app_bundle_id) or (User.apphud_user_id == user.apphud_user_id)
            )
            result = await session.execute(stmt)
            existing_user = result.scalar_one_or_none()

            if existing_user:
                return None

            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

