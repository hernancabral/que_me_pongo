from typing import Dict, Any


class WeatherService:

    @classmethod
    def get_weather(cls) -> Dict[str, Any]:
        return {'temperature': 10, 'rain': False}
