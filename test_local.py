from app import handle_task
import json

print("=== Testing Teacher Agent Locally ===\n")

test_input = {
    "user_question": "What is Bitcoin?",
    "intent": "explain bitcoin",
    "crypto_data": {
        "bitcoin": {
            "price_data": {"bitcoin": {"usd": 45000, "usd_24h_change": 2.5}},
            "details": {"name": "Bitcoin", "symbol": "BTC", "current_price": 45000, "market_cap": 850000000000}
        }
    }
}

result = handle_task(json.dumps(test_input))
print(f"Result:\n{result}")
