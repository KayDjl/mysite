from django.contrib import admin
from .models import Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    #Отображение записей
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    #Поле сортировки по выбраным полям
    list_filter = ['status', 'created', 'publish', 'author']
    #Поле поиска по выбраным полям
    search_fields = ['title', 'body']
    #Автозаполнение поля slug на основе заполненого поля title
    prepopulated_fields = {'slug': ('title',)}
    #Изменение выпадающего списка на удобный поиск по записям
    raw_id_fields = ['author']
    #Навигация по иерархии дат
    date_hierarchy = 'publish'
    #Сортировка записей по выбраным полям
    ordering = ['status', 'publish']
    #Фильтр количесва фасетов
    show_facets = admin.ShowFacets.ALWAYS