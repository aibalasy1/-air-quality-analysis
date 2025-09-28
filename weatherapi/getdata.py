import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

stations = {
    "k12": (51.18128712, 71.46580696),
    "k8": (51.18611299, 71.34372285),
    "k7": (51.1231206, 71.48337096),
    "k9": (51.15841381, 71.46746001)
}

base_url = "https://archive-api.open-meteo.com/v1/archive"
common_params = {
    "start_date": "2023-04-01",
    "end_date": "2024-04-01",
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "pressure_msl", "wind_speed_10m", "wind_direction_10m", "cloud_cover"],
    "wind_speed_unit": "ms",
    "timezone": "auto"
}

for station_id, (lat, lon) in stations.items():
    print(f"Получение данных для станции {station_id} ({lat}, {lon})...")

    params = common_params.copy()
    params["latitude"] = lat
    params["longitude"] = lon

    responses = openmeteo.weather_api(base_url, params=params)
    response = responses[0] 

    hourly = response.Hourly()
    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ),
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
        "relative_humidity_2m": hourly.Variables(1).ValuesAsNumpy(),
        "precipitation": hourly.Variables(2).ValuesAsNumpy(),
        "pressure_msl": hourly.Variables(3).ValuesAsNumpy(),
        "wind_speed_10m": hourly.Variables(4).ValuesAsNumpy(),
        "wind_direction_10m": hourly.Variables(5).ValuesAsNumpy(),
        "cloud_cover": hourly.Variables(6).ValuesAsNumpy(),
    }

    df = pd.DataFrame(hourly_data)

    filename = f"{station_id}.csv"
    df.to_csv(filename, index=False)
    print(f"Файл {filename} сохранен.")
