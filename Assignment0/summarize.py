import argparse
from trafilatura import fetch_url, extract, baseline
from google import genai


parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, required=True)

url = parser.parse_args().url

while True:
    downloaded = fetch_url(url)

    if downloaded is None:
        continue
    else:
        break

text = baseline(downloaded)


client = genai.Client()


response = client.models.generate_content(
    model="gemini-1.5-flash", 
    contents=text[1] + "\n Respond only in valid JSON output. Write a 3 sentence summary of this text and choose 5 keywords. Also, return the provided URL as a Reference. " + url,
    config={
        "response_mime_type": "application/json",
        "temperature": 0.2,
        "topP": 0.9,
        "topK": 40,
        "maxOutputTokens": 512,
    }

)

with open("output.json", "w") as f:
    f.write(response.text)
