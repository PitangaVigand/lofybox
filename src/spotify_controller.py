import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()  # Garante que .env seja carregado

_spotify_instance = None
_has_started = False


def get_spotify_client():
    global _spotify_instance
    if _spotify_instance is None:
        _spotify_instance = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                scope="user-modify-playback-state user-read-playback-state user-read-currently-playing",
            )
        )
    return _spotify_instance


def start_or_resume_playlist():
    global _has_started
    sp = get_spotify_client()
    playlist_uri = os.getenv("SPOTIFY_PLAYLIST_URI")

    devices = sp.devices()
    if not devices["devices"]:
        print("⚠️ Nenhum dispositivo ativo encontrado.")
        return

    device_id = devices["devices"][0]["id"]

    try:
        playback = sp.current_playback()
        if (
            playback
            # and playback["is_playing"] is True
            # and playback["context"]
            # and playback["context"]["uri"] == playlist_uri
        ):
            sp.start_playback(device_id=device_id)
            print("⏯️ Playlist retomada de onde parou.")
        else:
            sp.start_playback(device_id=device_id, context_uri=playlist_uri)
            print("🎵 Playlist iniciada do começo.")
    except Exception as e:
        print("❌ Erro ao iniciar/retomar playlist:", e)


def stop_playback():
    sp = get_spotify_client()
    try:
        sp.pause_playback()
        print("⏸️ Música pausada.")
    except Exception as e:
        print("❌ Erro ao pausar:", e)
