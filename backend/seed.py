from app import create_app
from app.repositories.shop_repository import ShopRepository
from app.utils.password import hash_password

app = create_app()


def seed():
    app.app_context().push()

    existing = ShopRepository.get_by_username("admin")

    if existing:
        print("Admin already exists.")
        return

    ShopRepository.create(
        display_code="QL000001",
        public_code="A7XK29P4",
        username="admin",
        password_hash=hash_password("admin123"),
        name="René Barbershop",
        is_open=True,
    )

    ShopRepository.commit()

    print("Seed completed.")


if __name__ == "__main__":
    seed()