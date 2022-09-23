from django.db import models
import uuid #required for unique instances
from django.urls import reverse  #used to generate URLS by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date



# Create your models here.
class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre ')

    def __str__(self):
        """String for representing the model object"""
        return self.name

class Book(models.Model):
    """Model representing Books"""
    title = models.CharField(max_length=200)
    #foreign key used becuase books can have one author, but authors can have mutiple books
    #Author as a string rather than object beacuse it hasn't been declared in the file
    author=models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter Brief Description of thr book')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    #ManyTomanyField used becuase genre can contain many books. books can cover many genres.
    #Genre class has aready bben defined so we specify the object above
    genre = models.ManyToManyField(Genre, help_text='select a genre for this book')

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        #Returns the URL to access a detail record for this book
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """creating a string for the genre. to diplay genre in admin becuase 
        by deafault Django doesn't allow manyTomany filled to appear on admin site """

        return ','.join(genre.name for genre in self.genre.all()
        [:3])

    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    #model representing a specific copy of the book that can be borrowed from library
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique Id for this particular book acrooss whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a','Available'),
        ('r','Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    class Meta:
        ordering =['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    @property
    def is_overdue(self):
       """Determines if the book is overdue based on due date and current date."""
       return bool(self.due_back and date.today() > self.due_back)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank= True)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        #Returns the URL to access a particular author instance
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    


