import requests
from decouple import config
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_response(url, unit):
    payload = {
        "unitGroup": unit,
        "key": config("key"),
        "contentType": "json",
    }
    response = requests.get(url, params=payload)
    return response


@api_view()
def weather(request, location):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"
    unit = request.GET.get("unit", "metric")
    try:
        response = get_response(url, unit)
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
