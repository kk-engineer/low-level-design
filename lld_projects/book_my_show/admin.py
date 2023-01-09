from django.contrib import admin

# Register your models here.
from book_my_show.models.City import City
from book_my_show.models.Language import Language
from book_my_show.models.Movie import Movie
from book_my_show.models.MovieTicket import MovieTicket
from book_my_show.models.Payment import Payment
from book_my_show.models.Screen import Screen
from book_my_show.models.Seat import Seat
from book_my_show.models.Show import Show
from book_my_show.models.ShowSeat import ShowSeat
from book_my_show.models.Theatre import Theatre
from book_my_show.models.Transaction import Transaction
from book_my_show.models.User import User
from book_my_show.models.Visual import Visual


class ShowAdmin(admin.ModelAdmin):
    list_display = ['movie', 'start_time', 'language', 'screen', 'theatre', 'link']
    list_editable = ['movie', 'start_time', 'language', 'screen', 'theatre', ]
    list_display_links = ['link']
    # list_filter = ['vehicle_type', 'spot_status', 'floor', 'lot_name', ]


admin.site.register(City)
admin.site.register(Theatre)
admin.site.register(Language)
admin.site.register(Visual)
admin.site.register(Movie)
admin.site.register(Screen)
admin.site.register(Show, ShowAdmin)
admin.site.register(ShowSeat)
admin.site.register(Seat)
admin.site.register(MovieTicket)
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Transaction)
