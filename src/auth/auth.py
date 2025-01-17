from fastapi_users.authentication import JWTStrategy, AuthenticationBackend

from fastapi_users.authentication import CookieTransport

from src.config import setting

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="message")


SECRET = setting.SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
