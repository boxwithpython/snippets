from typing import NamedTuple


class Skills(NamedTuple):
    mining: int  # здесь будет 0
    woodcutting: int = 1  # можно задавать дефолтные значения

    def __str__(self) -> str:
        return f"Какой качок, уровень копания: {self.mining}\n" \
               f"уровень лесорубства: {self.woodcutting}"


AnotherSkills = NamedTuple(
    'AnotherSkills',
    [('breathtaking', int), ('googling', int)]
)
