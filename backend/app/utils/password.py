import bcrypt


def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt(),
    )

    return hashed.decode()


def verify_password(
    password: str,
    password_hash: str,
) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode(),
    )