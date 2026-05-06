import requests
import json
import sys
from datetime import datetime

# ================== CONFIG ==================
WEBHOOK_URL = "https://discord.com/api/webhooks/1501443463701598240/tt19SDxy8BpiIkTgvGPeZIctoKV-gqwxiRwRF5qfhezmJZeGnZpQ7UGR0Vldik9UAiwz"  # ← CHANGE THIS

# Embed settings
EMBED_TITLE = "New idiot has found"
EMBED_DESCRIPTION = "an idiot has turned on the toggle lol" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
EMBED_COLOR = 0x00ff00  # Green (you can change to hex like 0xff0000 for red)
# ===========================================

def send_discord_embed():
    if WEBHOOK_URL == "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL_HERE":
        print("❌ Please set your actual Discord Webhook URL in the script!")
        return False

    embed = {
        "title": EMBED_TITLE,
        "description": EMBED_DESCRIPTION,
        "color": EMBED_COLOR,
        "timestamp": datetime.utcnow().isoformat(),
        "footer": {
            "text": "Fast Crystal"
        }
    }

    data = {
        "username": "Fast Crystal",
        "embeds": [embed]
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 204 or response.status_code == 200:
            print("✅ Embed sent successfully to Discord!")
            return True
        else:
            print(f"❌ Failed to send. Status: {response.status_code}")
            print(response.text)
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Fast Crystal Test Script Started")
    send_discord_embed()