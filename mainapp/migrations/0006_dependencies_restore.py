from django.db import migrations

def forwards_func(apps, schema_editor):

    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    Courses = apps.get_model("mainapp", "Courses")

    t = CourseTeachers.objects.get(id=8)
    c = Courses.objects.get(id=10)

    t.course.add(c)

    t = CourseTeachers.objects.get(id=9)
    c = Courses.objects.get(id=11)

    t.course.add(c)

    t = CourseTeachers.objects.get(id=10)
    c = Courses.objects.get(id=12)

    t.course.add(c)

def reverse_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Delete objects
    CourseTeachers.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_teachers_migration'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
