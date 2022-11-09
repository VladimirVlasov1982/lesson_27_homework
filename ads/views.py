import json
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ads


def main(request):
    return JsonResponse({"status": "Ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):

    def get(self, request):
        """Получаем все категории"""
        categories = Categories.objects.all()
        response = []

        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        """Добавляем категорию"""
        categories_data = json.loads(request.body)

        category = Categories()
        category.name = categories_data['name']

        try:
            category.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, 422)

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, json_dumps_params={"ensure_ascii": False})


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        """Получаем категорию по id"""
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):

    def get(self, request):
        """Получаем все объявления"""
        ads = Ads.objects.all()
        response = []

        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        """Добавляем объявление"""
        ads_data = json.loads(request.body)

        ad = Ads()
        ad.name = ads_data["name"]
        ad.author = ads_data["author"]
        ad.price = ads_data["price"]
        ad.description = ads_data["description"]
        ad.address = ads_data["address"]
        ad.is_published = ads_data["is_published"]

        try:
            ad.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, 422)

        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, json_dumps_params={"ensure_ascii": False})


class AdsDetaiView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        """Получаем объявление по id"""
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "address": self.object.address,
            "is_published": self.object.is_published,
        }, json_dumps_params={"ensure_ascii": False})
