# 🎬 ClipGrabber-API

ClipGrabber-API is a **local Python API** for downloading videos from **YouTube**.

⚠️ **Important notice**: When this API is hosted online (VPS, cloud, etc.), YouTube detects it as a bot and blocks downloads. For this reason, **ClipGrabber-API currently works only on localhost**.

---

## 📌 Features

* Download YouTube videos locally
* Uses `yt-dlp` for reliable downloads
* Supports audio + video merge using **FFmpeg**
* Designed to be used as a backend for a frontend project

---

## 🧠 How it works

* The API runs locally using Python
* Requests are made from a frontend (such as ClipGrabber)
* Downloads are processed on the local machine
* Hosting the API publicly will cause YouTube to block requests

---

## 📂 Project structure

```
ClipGrabber-API/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🛠️ Requirements

Before running the project, make sure you have:

* **Python 3.6+**
* **pip**
* **FFmpeg** (mandatory, otherwise videos will be downloaded without audio)

---

## 🔽 Clone the repository

```bash
git clone https://github.com/gabrielrodriguesYT/ClipGrabber-API.git
cd ClipGrabber-API
```

---

## 🐍 Create a virtual environment (recommended)

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows (CMD)

```bat
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

## 📦 Install dependencies

### Linux / macOS / Windows

```bash
pip install -r requirements.txt
```

---

## 🎞️ Install FFmpeg

### Linux (Ubuntu / Pop!_OS)

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
```

---

### Windows

1. Download FFmpeg from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract it
3. Add the `bin` folder to **System PATH**
4. Restart the terminal

Verify:

```bat
ffmpeg -version
```

---

### macOS

```bash
brew install ffmpeg
```

---

## ▶️ Running the API

With the virtual environment activated:

```bash
python main.py
```

The API will start running on **localhost**.

---

## 🌐 Using with the frontend (ClipGrabber)

Clone the frontend repository:

```bash
git clone https://github.com/gabrielrodriguesYT/ClipGrabber.git
```

### Important

* Open the frontend project
* Locate the backend API URL configuration
* Change the backend URL to:

```
http://localhost:PORT
```

(Replace `PORT` with the port used in `main.py`)

Then run the frontend normally.

---

## ⚠️ Known limitations

* ❌ Does NOT work when hosted online
* ❌ YouTube blocks cloud/VPS IPs
* ✅ Works correctly on localhost

---

## 🔒 Security

* Never commit `venv/`
* Never expose API publicly
* `.gitignore` is required

---

## 📄 License

This project is for **educational purposes only**.

---

## 👤 Author

**Gabriel Rodrigues**
GitHub: https://github.com/gabrielrodriguesYT

---

If you like this project, consider giving it a ⭐ on GitHub!
