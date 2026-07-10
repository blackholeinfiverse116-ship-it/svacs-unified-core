import requests

BASE_URL = "https://showing-wizard-buffer.ngrok-free.dev"

ENDPOINT = "/api/comprehensive-news-analysis"


def fetch_intelligence(news_url):

    payload = {
        "url": news_url,
        "enable_video_search": True,
        "enable_video_prompts": True,
        "enable_random_video": True
    }

    response = requests.post(
        BASE_URL + ENDPOINT,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    return response.json()
