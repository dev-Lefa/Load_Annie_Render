import requests
import os

def download_model():
    url = "https://drive.google.com/file/d/1hYYCT5Wec4RhmFx5_NGmRfX-sJxLd93P/view?usp=sharing"
    local_filename = "Annie-Ai.zip"
    if not os.path.exists(local_filename):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
