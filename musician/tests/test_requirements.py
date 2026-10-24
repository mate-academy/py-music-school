from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from musician.models import Musician


class MusicianRequirementsTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.payload = {
            "first_name": "Alice",
            "last_name": "Green",
            "instrument": "piano",
            "age": 14,
        }

    def test_minimum_age_and_application_date(self) -> None:
        response = self.client.post(
            reverse("musician:manage-list"), self.payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        musician = Musician.objects.get(pk=response.data["id"])
        self.assertEqual(musician.age, 14)
        self.assertEqual(musician.date_of_applying, timezone.localdate())
        self.assertFalse(response.data["is_adult"])

    def test_model_age_validation(self) -> None:
        musician = Musician(**{**self.payload, "age": 13})
        with self.assertRaises(ValidationError):
            musician.full_clean()
        musician.age = 14
        musician.full_clean()

    def test_adulthood_boundary(self) -> None:
        for age, expected in ((14, False), (20, False), (21, True), (22, True)):
            with self.subTest(age=age):
                musician = Musician(**{**self.payload, "age": age})
                self.assertEqual(musician.is_adult, expected)

    def test_updates_reject_underage_musicians(self) -> None:
        musician = Musician.objects.create(**self.payload)
        url = reverse("musician:manage-detail", args=[musician.pk])
        for method in (self.client.put, self.client.patch):
            response = method(url, {**self.payload, "age": 13})
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            musician.refresh_from_db()
            self.assertEqual(musician.age, 14)

    def test_computed_fields_are_read_only(self) -> None:
        response = self.client.post(
            reverse("musician:manage-list"),
            {
                **self.payload,
                "is_adult": True,
                "date_of_applying": "2000-01-01",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data["is_adult"])
        self.assertEqual(
            response.data["date_of_applying"], timezone.localdate().isoformat()
        )
        url = reverse("musician:manage-detail", args=[response.data["id"]])
        response = self.client.patch(
            url, {"age": 21, "is_adult": False,
                  "date_of_applying": "2000-01-01"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_adult"])
        self.assertEqual(
            response.data["date_of_applying"], timezone.localdate().isoformat()
        )
