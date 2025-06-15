# 🎧 Lofybox

**Lofybox** is a minimalist productivity app that blends the **Pomodoro technique** with **lo-fi music** to help you stay focused and in flow.

With a single click, it starts a focus timer and automatically plays your favorite Spotify playlist.  
At the end of the session, Lofybox can also log your task in **Clockify** and alert you with a gentle sound.

Perfect for creatives, students, freelancers, and anyone who values focus, mood, and simplicity.

---

## ✨ Features

- 🕒 Focus timer (25 min default Pomodoro)
- 🎵 Auto-start/pause of Spotify playlist
- ⏱️ Clockify integration for time tracking
- 🔔 Optional end-of-session notification sound
- 💎 Minimalist black-and-white interface
- 🖥️ Windows executable packaging

---

## 🖼️ Interface Preview

> *(optional)* Add your app UI screenshot in `assets/screenshot.png`  
> Example:  
> ![Lofybox UI](assets/screenshot.png)

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone git@github.com:PitangaVigand/lofybox.git
cd lofybox
```

### 2. Create virtual environment

Using Poetry:

```bash
poetry install
poetry shell
```

Or using Conda:

```bash
conda create -n lofybox python=3.11 -y
conda activate lofybox
poetry install
```

### 3. Create `.env` file

```ini
# Spotify
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
SPOTIFY_PLAYLIST_URI=spotify:playlist:your_playlist_uri

# Clockify
CLOCKIFY_API_KEY=your_clockify_api_key
CLOCKIFY_WORKSPACE_ID=your_workspace_id
CLOCKIFY_USER_ID=your_user_id
CLOCKIFY_PROJECT_ID=your_project_id
```

---

## 🔐 How to Get Clockify IDs

1. Get your **API Key** from https://clockify.me/user/settings  
2. Open Clockify in browser, go to **Dev Tools** → **Network**, click em qualquer requisição e procure:
   - `workspaceId`
   - `X-Api-Key`
3. To list all projects and get your `projectId`:

```bash
curl -H "X-Api-Key: YOUR_API_KEY" \
  https://api.clockify.me/api/v1/workspaces/YOUR_WORKSPACE_ID/projects
```

4. To get your `userId`:

```bash
curl -H "X-Api-Key: YOUR_API_KEY" \
  https://api.clockify.me/api/v1/user
```

---

## 🧠 Usage

Run the app locally:

```bash
python src/main.py
```

Or if you're using Poetry:

```bash
poetry run python src/main.py
```

Press the ▶️ button to start the timer and music.  
Press ⏸️ to pause both Spotify and Clockify entry.  
When finished, the session auto-stops and logs your time.

---

## 🧪 Running Tests

```bash
poetry run pytest
```

---

## 📦 Building Windows Executable

You can use PyInstaller to generate a `.exe`:

```bash
poetry run pyinstaller src/main.py ^
  --name=lofybox ^
  --noconfirm ^
  --noconsole ^
  --onedir ^
  --windowed ^
  --distpath dist ^
  --workpath build ^
  --specpath build
```

Your `.exe` will be inside `dist/lofybox`.

---

## 🗺️ Roadmap

- [x] Spotify integration
- [x] Clockify time logging
- [x] App icon with retro turntable style
- [x] Play/pause synchronization
- [x] Environment variable setup
- [ ] System tray minimization
- [ ] Break sessions (short/long)
- [ ] UI themes (light/dark)
- [ ] Session history tracking

---

## 👤 About the Author

Created by [Pitanga Vigand](https://github.com/PitangaVigand)  
*Architectural computational designer focused on back-end development.*

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
