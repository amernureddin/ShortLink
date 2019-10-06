from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from shorter_link_app import models


def home(request):
    url_error = False
    url_input = ""
    shortened_url = ""

    if request.method == "POST":
        validator = URLValidator()
        try:
            url_input = request.POST.get("url", None)
            if not url_input:
                url_error = True
            else:
                validator(url_input)
        except ValidationError:
            url_error = True

        if not url_error:
            link_db, created = models.Link.objects.get_or_create(
                link=url_input)
            # link_db.link = url_input
            # link_db.save()
            shortened_url = request.build_absolute_uri(link_db.get_short_id())
            url_input = ""
            print(models.Link.objects.all().values())
            # shortened_url = "%s/%s"%(request.META["HTTP_HOST"], link_db.get_short_id())

    return render(request, "index.html",
                  {"error": url_error, "url": url_input, "shorturl": shortened_url})


def link(request, id):
    # print id
    db_id = models.Link.decode_id(id)
    # print db_id
    link_db = get_object_or_404(models.Link, id=db_id)
    return redirect(link_db.link)
