from Address import Address # type: ignore
from Mailing import Mailing # type: ignore

to_address = Address
from_address = Address
to_address = 236040, "г. Москва", "ул. Невская", 25, 15
from_address = 236404, "г. Волгоград", "ул. Черняховского", 44, 19

sending = Mailing
sending(to_address, from_address, 2000, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)