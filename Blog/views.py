from django.shortcuts import get_object_or_404, render, get_list_or_404, HttpResponse
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.db.models import Q
import pandas as pd
import json
import os


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "Blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 20


class UserPostListView(ListView):
    model = Post
    template_name = "Blog/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "werkstoffnummer", "werkstoffbezeichnung", "gruppe", "source",
        "Iron_Fe", "Carbon_C", "Cobalt_Co", "Nickel_Ni", "Copper_Cu", "Zinc_Zn", "Mananese_Mn", "Chromuium_Cr", "Vanadium_V", "Titaniun_Ti", "Cadmium_Cd",
        "Silver_Ag", "Palladium_Pb", "Rhodium_Rh", "Molydbenum_Mo", "Niobium_Nb", "Zirconium_Zr", "Yttrium_Y", "Tungesten_W", "Aluminium_Al",
        "Boron_B", "Gallium_Ga", "Indium_In", "Lead_Pb", "Silicon_Si", "Tin_Sn", "Nitrogen_N", "Phosphorus_P", "Sulfur_S",
        "Hardness_HV", "Hardness_HRC", "Hardness_HBW", "files_Hardness",
        "Tensile_Strength_Rm", "Streckgrenze_Rp", "Streckgrenze_ReH", "Streckgrenze_ReL", "Tensile_Stretch_A", "Gleichmaßdehnung_Ag", "files_Tensile",
        "Kerbschlagarbeit", 'Temperatur', "files_Charpy",
        "EModul", "files_Modulus",
        "Density", "files_Density",
        "Gefüge_Aufnhame", 'Probe', "Gefüge_Beschreibung", "Wärmebehandlung", 'Ätzung', "files_Metallo","Notes",

    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        "werkstoffnummer", "werkstoffbezeichnung", "gruppe", "source",
        "Iron_Fe", "Carbon_C", "Cobalt_Co", "Nickel_Ni", "Copper_Cu", "Zinc_Zn", "Mananese_Mn", "Chromuium_Cr", "Vanadium_V", "Titaniun_Ti", "Cadmium_Cd",
        "Silver_Ag", "Palladium_Pb", "Rhodium_Rh", "Molydbenum_Mo", "Niobium_Nb", "Zirconium_Zr", "Yttrium_Y", "Tungesten_W", "Aluminium_Al",
        "Boron_B", "Gallium_Ga", "Indium_In", "Lead_Pb", "Silicon_Si", "Tin_Sn", "Nitrogen_N", "Phosphorus_P", "Sulfur_S",
        "Hardness_HV", "Hardness_HRC", "Hardness_HBW", "files_Hardness",
        "Tensile_Strength_Rm", "Streckgrenze_Rp", "Streckgrenze_ReH", "Streckgrenze_ReL", "Tensile_Stretch_A", "Gleichmaßdehnung_Ag", "files_Tensile",
        "Kerbschlagarbeit", 'Temperatur', "files_Charpy",
        "EModul", "files_Modulus",
        "Density", "files_Density",
        "Gefüge_Aufnhame", 'Probe', "Gefüge_Beschreibung", "Wärmebehandlung", 'Ätzung', "files_Metallo","Notes",

    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def Periodic_Table(request):
    return render(request, "Blog/Periodic_Table.html")

def user_manual(request):
    return render(request, "Blog/user_manual.html")

def about(request):
    return render(request, "Blog/about.html", {"title": "About"})

def search_post(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        posts = Post.objects.filter(
            Q(werkstoffnummer=searched) | Q(werkstoffbezeichnung=searched) | Q(gruppe=searched)
        )

        return render(
            request, "Blog/search_post.html", {"searched": searched, "posts": posts}
        )
    else:
        return render(request, "Blog/search_post.html", {})




def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404