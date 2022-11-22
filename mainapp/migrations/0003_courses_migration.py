from django.db import migrations

def forwards_func(apps, schema_editor):

    Courses = apps.get_model("mainapp", "Courses")

    Courses.objects.create(
        id = 10,
        name = "Основы С#",
        description = "На курсе вы получите крепкие основы языка C#, которые помогут старту вашей карьеры",
        description_as_markdown = True,
        cost = 7999.9,
        cover = "img/no_image.svg",
    )

    Courses.objects.create(
        id = 11,
        name = "Продвинутый С#",
        description = "На курсе вы научитесь писать продвинутые приложения на языке C#",
        description_as_markdown = True,
        cost = 9999.9,
        cover = "img/no_image.svg",
     )

    Courses.objects.create(
        id = 12,
         name = "HTML/CSS",
         description = "На курсе вы получите знание основных технологий, необходимых веб-разработчику",
        description_as_markdown = False,
        cost = 6999.9,
        cover = "img/no_image.svg",
    )
def reverse_func(apps, schema_editor):
    
    Courses = apps.get_model("mainapp", "Courses")
    
    Courses.objects.all().delete()
    

class Migration(migrations.Migration):
   
    dependencies = [
        ('mainapp', '0002_data_migration'),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]