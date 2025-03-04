async function loadSongs() {
    const response = await fetch("songs.json");
    const songs = await response.json();
    const songList = document.getElementById("song-list");

    songs.forEach(songName => {
        const songDiv = document.createElement("div");
        songDiv.innerHTML = `
            <h2>${songName}</h2>
            <audio controls>
                <source src="songs/${songName}/1.mp3" type="audio/mpeg">
            </audio>
            <pre id="lyrics-${songName}">Loading lyrics...</pre>
        `;
        songList.appendChild(songDiv);
        loadLyrics(songName);
    });
}

async function loadLyrics(songName) {
    const response = await fetch(`songs/${songName}/lyrics.txt`);
    if (response.ok) {
        document.getElementById(`lyrics-${songName}`).textContent = await response.text();
    } else {
        document.getElementById(`lyrics-${songName}`).textContent = "ไม่มีเนื้อเพลง";
    }
}

loadSongs();
