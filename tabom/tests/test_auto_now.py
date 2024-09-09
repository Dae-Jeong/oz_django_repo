from datetime import datetime

from django.db import connection
from django.test import TestCase

from tabom.models.user import User


class TestAutoNow(TestCase):
    def test_auto_now_field_not_set_when_raw_sql_update_executed(self) -> None:
        # Given
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tabom_user(id, name, updated_at, created_at) "
                "VALUES (1, 'hihi', '1999-01-01 10:10:10', '1999-01-01 10:10:10')"
            )

            # When
            cursor.execute("UPDATE tabom_user SET name='changed' WHERE id=1")

        # Then
        user = User.objects.filter(id=1).get()
        self.assertEqual(user.updated_at, datetime(year=1999, month=1, day=1, hour=10, minute=10, second=10))
