from typing import List

from .models import Musician


def create_musician(
        first_name: str,
        last_name: str,
        instrument: str,
        age: int) -> Musician:
    musician = Musician.objects.create(
        first_name=first_name,
        last_name=last_name,
        instrument=instrument,
        age=age,
    )
    return musician


def get_all_musicians() -> List[Musician]:
    return Musician.objects.all()


def get_musician_by_id(musician_id: int) -> Musician:
    return Musician.objects.get(id=musician_id)


def update_musician(musician_id, **kwargs) -> Musician:
    musician = Musician.objects.get(id=musician_id)

    for field, value in kwargs.items():
        if hasattr(musician, field):
            setattr(musician, field, value)

        musician.save()
        return musician


def delete_musician(musician_id: int) -> None:
    musician = Musician.objects.get(id=musician_id)
    musician.delete()
