"""Сервисные миксины проекта."""


class CreationLogMixin:
    """
    Печатает в stdout сведения о созданном объекте.
    Вызывается из dataclass-метода __post_init__() наследника.
    """

    def __post_init__(self):
        pairs = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        print(f"{self.__class__.__name__}({pairs}) создан")  # noqa: T201
