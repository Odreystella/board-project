from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView
from django.http import Http404
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


class BoardDetailView(DeleteView):

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

    def get_object(self, queryset=None):   # return the object the view is displaying
        board = super().get_object(queryset=queryset)   
        if board.writer.pk != self.request.user.pk:   # 글의 작성자가 아닌 다른 유저가 수정하지 못하게끔 함
            raise Http404() 
        return board

@login_required
def delete_board(request, pk):
    user = request.user
    try:
        board = Board.objects.get(pk=pk)
        if board.writer == user:
            board.delete()
        else:
            raise Http404() 
        return redirect(reverse("home"))

    except Board.DoesNotExist:
        return redirect(reverse("home"))
