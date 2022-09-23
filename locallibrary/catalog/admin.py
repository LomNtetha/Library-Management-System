from re import A
from django.contrib import admin

# Register your models here.
from.models import Author, Genre,Book, BookInstance

#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)
#admin.site.register(Genre)
class AuthorAdmin(admin.ModelAdmin):
    
    list_filter = ('first_name','last_name','date_of_birth','date_of_death')
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    #display objects from models including manyToMay filled by calling its Method
    list_display = ('title','author','display_genre')
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    search = ('book')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

