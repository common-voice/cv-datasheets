import time
import json
import requests
import os
import http
from dotenv import load_dotenv

load_dotenv()

COMMON_VOICE_URL = "https://commonvoice.mozilla.org"
COMMON_VOICE_API_URL = COMMON_VOICE_URL + "/api/v1/{locale}/sentences?count={count}"
SCS_SENTENCES_PATH = "../metadata/scs-sentences.json"
SCS_DEMOGRAPHIC_PATH = "../metadata/cv-corpus-23.0-2025-09-05.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://commonvoice.mozilla.org/ca/speak",
    "Content-Type": "application/json; charset=utf-8",
    "sentry-trace": os.getenv("CV_SENTRY_TRACE"),
    "baggage": os.getenv("CV_BAGGAGE"),
    "Alt-Used": "commonvoice.mozilla.org",
    "Connection": "keep-alive",
    "Cookie": os.getenv("CV_COOKIE"),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=4",
    "TE": "trailers",
}


def read_json_file(file_name: str) -> dict:
    """Read json file from dist

    Parameters
    ----------
    file_name : str
        File name

    Returns
    -------
    dict
        json data as python dict
    """
    with open(file_name, "r") as f:
        data = json.load(f)
    return data


demographic_data = read_json_file(SCS_DEMOGRAPHIC_PATH).get("locales")


def fetch_sentences(locale: str, max_sentences: int = 5) -> list[str]:
    """Fetches sentences from the Common Voice API for a given locale.

    Parameters
    ----------
    locale : str
        Locale language code
    max_sentences : int, optional
        Number of sentences to fetch, default=5

    Returns
    -------
    List[str]
        List of sentences
    """
    url = COMMON_VOICE_API_URL.format(locale=locale, count=max_sentences)
    print(f"Requesting {locale} status_code=", end="")
    time.sleep(0.2)
    response = requests.get(url, headers=HEADERS)
    if response.status_code == http.HTTPStatus.OK:
        print("200")
        return [row["text"] for row in json.loads(response.content)]
    else:
        print(response.status_code)
        print(f"Error for {locale}: status_code={response.status_code}")
        return []


sentences = {}
for locale in demographic_data:
    sentences[locale] = fetch_sentences(locale, 5)
with open(SCS_SENTENCES_PATH, "w") as f:
    json.dump(sentences, f)
