from flask import Flask, request, send_file, jsonify, make_response
from flask_cors import CORS
import subprocess
import os
import uuid

app = Flask(__name__)
CORS(app, resources={r"/download": {"origins": "*"}})

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


@app.route("/download", methods=["POST", "OPTIONS"])
def download_video():

   
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response, 200

    
    data = request.get_json(silent=True)

    if not data or "url" not in data:
        return jsonify({"error": "URL não fornecida"}), 400

    url = data["url"]
    file_id = str(uuid.uuid4())
    output_template = os.path.join(DOWNLOAD_DIR, f"{file_id}.%(ext)s")

    command = [
        "yt-dlp",
        "-f", "bv*[height<=1080]+ba/best[height<=1080]",
        "--merge-output-format", "mp4",
        "-o", output_template,
        url
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        return jsonify({"error": "Falha ao baixar o vídeo"}), 500

    
    final_file = None
    for f in os.listdir(DOWNLOAD_DIR):
        if f.startswith(file_id) and f.endswith(".mp4"):
            final_file = os.path.join(DOWNLOAD_DIR, f)
            break

    if not final_file:
        return jsonify({"error": "Arquivo final não encontrado"}), 500

    return send_file(
        final_file,
        as_attachment=True,
        download_name="video.mp4",
        mimetype="video/mp4"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
