import streamlit as st
from ytmusicapi import YTMusic

ytmusic = YTMusic()

st.title("🎵 YouTube Music Player (Embed Version)")
query = st.text_input("Enter song name")


if query:
    results = ytmusic.search(query, filter="songs")
    if results:
        song = results[0]
        title = song["title"]
        artist = song["artists"][0]["name"]
        video_id = song["videoId"]
        video_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1"

        st.markdown(f"### 🎧 {title} - {artist}")
        st.components.v1.iframe(video_url, height=80)
    else:
        st.warning("No songs found.")

