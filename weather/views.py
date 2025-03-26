import requests
from decouple import config
from rest_framework.decorators import api_view, throttle_classes
from django.views.decorators.cache import cache_page

# from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def get_response(url, unit, payload):
    response = requests.get(url, params=payload)
    return response


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "unit",
            openapi.IN_QUERY,
            description="Unit (metric)",
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={200: "weather data JSON"},
)
@cache_page(60 * 30)
@api_view()
@throttle_classes([AnonRateThrottle])
def weather(request, location):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"
    unit = request.GET.get("unit", "metric")
    payload = {
        "unitGroup": unit,
        "key": config("key"),
        "contentType": "json",
    }

    try:
        response = get_response(url, unit, payload)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as e:
        return Response(
            {
                "message": "Unable to fetch weather. Please check the location and try again.",
                "status code": response.status_code,
            },
            status=response.status_code,
        )
    except requests.exceptions.RequestException:
        return Response(
            {"message": "Weather service unavailable. Please try again later."},
            status=503,
        )
    if not data:
        return Response(
            {"message": "No weather data available for this location."}, status=204
        )
    return Response(data)
