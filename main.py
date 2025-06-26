import streamlit as st
from ytmusicapi import YTMusic
from yt_dlp import YoutubeDL

ytmusic = YTMusic()

st.title("🎵 YouTube Music Player (In-App)")
query = st.text_input("Enter song name")


def get_audio_url(video_id):
    with YoutubeDL({"format": "bestaudio"}) as ydl:
        info = ydl.extract_info(
            f"https://www.youtube.com/watch?v={video_id}", download=False
        )
        for f in info["formats"]:
            if f["ext"] == "m4a":
                return f["url"]
        return info["url"]  # fallback


if query:
    results = ytmusic.search(query, filter="songs")
    if results:
        song = results[0]
        title = song["title"]
        artist = song["artists"][0]["name"]
        video_id = song["videoId"]
        audio_url = get_audio_url(video_id)

        st.markdown(f"### 🎧 {title} - {artist}")
        st.audio(audio_url, format="audio/mp4")
    else:
        st.warning("No songs found.")
