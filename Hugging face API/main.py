import requests
from config import HF_API_KEY

MODEL_ID = "facebook/bart-large-mnli"

API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

TOPICS = ["Sports", "Politics", "Technology", "Health", "Entertainment"]


def ask_hf(headline: str):
    payload = {
        "inputs": headline,
        "parameters": {
            "candidate_labels": TOPICS
        }
    }

    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)

    if not r.ok:
        raise RuntimeError(f"HF error {r.status_code}: {r.text}")

    data = r.json()

    # Convert HF response into your expected format
    preds = []
    for label, score in zip(data["labels"], data["scores"]):
        preds.append({
            "label": label,
            "score": score
        })

    return preds


def best_topic(preds: list):
    best = max(preds, key=lambda x: x["score"])
    return best["label"], best["score"]


def bar(score: float) -> str:
    bar_length = 20
    blocks = int(score * bar_length)
    return "█" * blocks + "-" * (bar_length - blocks)


def show(headline: str, preds: list):
    top_label, top_score = best_topic(preds)

    print("\n" + "=" * 60)
    print("News topic classification")
    print(f"Headline: {headline}")
    print(f"Best topic: {top_label}")
    print(f"Confidence: {round(top_score * 100, 1)}% {bar(top_score)}")

    print("\nAll predictions:")

    top3 = sorted(preds, key=lambda x: x["score"], reverse=True)[:3]

    for i, p in enumerate(top3):
        print(f"{i + 1}. {p['label']}: {round(p['score'] * 100, 1)}% {bar(p['score'])}")

    print("=" * 60 + "\n")


def main():
    print("Welcome! Type a news headline and I'll guess the topic.")
    print("Topics: " + ", ".join(TOPICS))
    print("Type 'exit' to quit.\n")

    while True:
        headline = input("Enter a news headline: ")

        if headline.lower() == "exit":
            break

        try:
            preds = ask_hf(headline)
            show(headline, preds)

        except Exception as e:
            print(f"Error: {e}")
            print("Please try again or check your API key and network connection.")


if __name__ == "__main__":
    main()