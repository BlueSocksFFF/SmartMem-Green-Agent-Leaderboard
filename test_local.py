"""Simple test client for SmartMem agents"""
import asyncio
import json
import httpx

GREEN_URL = "http://127.0.0.1:9010"
PURPLE_URL = "http://127.0.0.1:9011"

async def send_eval_request():
    """Send evaluation request to Green Agent"""
    
    eval_request = {
        "participants": {
            "purple": PURPLE_URL
        },
        "config": {
            "max_test_rounds": 1,
            "targeted_per_weakness": 1,
            "convergence_threshold": 0.05,
            "weakness_num": 1,
            "max_turns": 5  # Limit to 5 turns for quick testing
        }
    }
    
    message = {
        "jsonrpc": "2.0",
        "method": "message/send",
        "params": {
            "message": {
                "messageId": "eval-001",
                "role": "user",
                "parts": [
                    {
                        "kind": "text",
                        "text": json.dumps(eval_request)
                    }
                ]
            }
        },
        "id": "1"
    }
    
    print("Sending evaluation request to Green Agent...")
    print(f"Config: {json.dumps(eval_request['config'], indent=2)}")
    print("-" * 50)
    
    async with httpx.AsyncClient(timeout=600.0) as client:
        response = await client.post(
            f"{GREEN_URL}/",
            json=message,
            headers={"Content-Type": "application/json"}
        )
        
        result = response.json()
        print("\nResponse received!")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        
        return result

if __name__ == "__main__":
    asyncio.run(send_eval_request())
