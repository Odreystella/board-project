from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView
from boards.models import Board
from .forms import  BoardCreationForm
from users.mixins import LoggedInOnlyView, LoggedOutOnlyView


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


class BoardCreateView(LoggedInOnlyView,FormView):
  
    model  = Board
    form_class = BoardCreationForm
    template_name="boards/board_create.html"
    context_object_name = "board"

    def form_valid(self, form):
        board = form.save()
        board.writer = self.request.user
        board.save()
        return redirect(reverse("home"))


class BoardDetailView(LoggedInOnlyView, DeleteView):

    model = Board
    template_name = "boards/board_detail.html"


class BoardUpdateView(LoggedInOnlyView, UpdateView):

    model = Board
    template_name = "boards/board_edit.html"
    pk_url_kwarg = "pk"
    fields = ("title", "content",)

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("boards:detail", kwargs={"pk": pk})