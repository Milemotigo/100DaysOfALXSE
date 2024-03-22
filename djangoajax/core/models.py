from django.db import models


SCHOOL_COURSES = (
    ('math', 'Mathematics'),
    ('sci', 'Science'),
    ('eng', 'English'),
    ('hist', 'History'),
    ('geo', 'Geography'),
    ('lang', 'Language Arts'),
    ('art', 'Art'),
    ('music', 'Music'),
    ('comp', 'Computer Science'),
    ('pe', 'Physical Education'),
)


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    course = models.CharField(max_length=50, choices=SCHOOL_COURSES)

    def __str__(self):
        return self.id
    def __str__(self):
        return self.name
