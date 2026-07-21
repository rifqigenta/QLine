from flask_jwt_extended import create_access_token

from app.repositories.shop_repository import ShopRepository
from app.utils.password import verify_password


class AuthService:

    @staticmethod
    def login(username: str, password: str):
        shop = ShopRepository.get_by_username(username)

        if shop is None:
            return None

        if not verify_password(password, shop.password_hash):
            return None

        token = create_access_token(
            identity=str(shop.id),
            additional_claims={
                "shop_code": shop.public_code,
                "username": shop.username,
            },
        )

        return {
            "access_token": token,
            "shop": {
                "id": str(shop.id),
                "name": shop.name,
                "username": shop.username,
                "public_code": shop.public_code,
            },
        }