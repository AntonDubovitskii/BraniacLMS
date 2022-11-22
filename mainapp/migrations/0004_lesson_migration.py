from django.db import migrations


def forwards_func(apps, schema_editor):

    Lesson = apps.get_model("mainapp", "Lesson")

    Lesson.objects.create(
        num=1,
        title="Lesson 1",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=2,
        title="Lesson 2",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=3,
        title="Lesson 3",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=4,
        title="Lesson 4",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=5,
        title="Lesson 5",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=6,
        title="Lesson 6",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=7,
        title="Lesson 7",
        description="Описание урока",
        course_id=10,
    )

    Lesson.objects.create(
        num=1,
        title="Lesson 1",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=2,
        title="Lesson 2",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=3,
        title="Lesson 3",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=4,
        title="Lesson 4",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=5,
        title="Lesson 5",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=6,
        title="Lesson 6",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=7,
        title="Lesson 7",
        description="Описание урока",
        course_id=11,
    )

    Lesson.objects.create(
        num=1,
        title="Lesson 1",
        description="Описание урока",
        course_id=12,
    )

    Lesson.objects.create(
        num=2,
        title="Lesson 2",
        description="Описание урока",
        course_id=12,
    )

    Lesson.objects.create(
        num=3,
        title="Lesson 3",
        description="Описание урока",
        course_id=12,
    )

    Lesson.objects.create(
        num=4,
        title="Lesson 4",
        description="Описание урока",
        course_id=12,
    )

    Lesson.objects.create(
        num=5,
        title="Lesson 5",
        description="Описание урока",
        course_id=12,
    )

    Lesson.objects.create(
        num=6,
        title="Lesson 6",
        description="Описание урока",
        course_id=12,
    )

    Lesson.objects.create(
        num=7,
        title="Lesson 7",
        description="Описание урока",
        course_id=12,
    )


def reverse_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model("mainapp", "Lesson")
    # Delete objects
    Lesson.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_courses_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
