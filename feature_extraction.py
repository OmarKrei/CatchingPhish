# feature_extraction.py

import pandas as pd
from urllib.parse import urlparse
import re

def extract_features(url):
    url_length = len(url)
    has_https = int(url.startswith("https"))
    count_at = url.count("@")
    count_dot = url.count(".")
    count_hyphen = url.count("-")
    count_slash = url.count("/")
    count_equal = url.count("=")
    count_question = url.count("?")
    count_percent = url.count("%")
    count_digits = sum(c.isdigit() for c in url)
    parsed = urlparse(url)
    domain_length = len(parsed.netloc)
    path_length = len(parsed.path)

    features = {
        'url_length': [url_length],
        'has_https': [has_https],
        'count_at': [count_at],
        'count_dot': [count_dot],
        'count_hyphen': [count_hyphen],
        'count_slash': [count_slash],
        'count_equal': [count_equal],
        'count_question': [count_question],
        'count_percent': [count_percent],
        'count_digits': [count_digits],
        'domain_length': [domain_length],
        'path_length': [path_length]
        # ⚠️ Add or remove fields based on your actual model’s training features!
    }

    return pd.DataFrame(features)