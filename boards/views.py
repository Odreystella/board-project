from django.shortcuts import render
from django.views.generic import ListView
from boards.models import Board


class BoardListView(ListView):

    model = Board
    template_name = "boards/board_list.html"
    context_object_name = "boards"
    ordering = "-created_at"
    paginate_by = 10
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Articles"
        return context