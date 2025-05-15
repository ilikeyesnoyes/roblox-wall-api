from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

GROUP_ID = 6339168

@app.route('/get_wall_posts')
def get_wall_posts():
    url = f"https://groups.roblox.com/v2/groups/{GROUP_ID}/wall/posts?limit=10&sortOrder=Desc"
    headers = {
        "User-Agent": "RobloxWallFetcher/1.0"
    }
    response = requests.get(url, headers=headers)
    print("Roblox API status code:", response.status_code)
    print("Roblox API response:", response.text)
    try:
        return jsonify(response.json().get('data', []))
    except Exception as e:
        print("JSON decode error:", e)
        return jsonify({"error": "Failed to parse response"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Railway's assigned port
    app.run(host='0.0.0.0', port=port)
