let songs = [];
let currentIndex = 0;

async function loadSongs() {
    const response = await fetch("songs.json");
    songs = await response.json();
    if (songs.length > 0) {
        updateSongDisplay();
    }
}

function updateSongDisplay() {
    const songName = songs[currentIndex];
    document.getElementById("song-title").textContent = songName;
    document.getElementById("audio-source").src = `songs/${songName}/1.mp3`;
    document.getElementById("audio-player").load(); // โหลดไฟล์ใหม่
    loadLyrics(songName);
}

async function loadLyrics(songName) {
    const response = await fetch(`songs/${songName}/lyrics.txt`);
    const lyricsElement = document.getElementById("lyrics");
    if (response.ok) {
        lyricsElement.textContent = await response.text();
    } else {
        lyricsElement.textContent = "ไม่มีเนื้อเพลง";
    }
}

// เปลี่ยนเพลงไปข้างหน้า
document.getElementById("next-song").addEventListener("click", () => {
    if (currentIndex < songs.length - 1) {
        currentIndex++;
        updateSongDisplay();
    }
});

// เปลี่ยนเพลงไปข้างหลัง
document.getElementById("prev-song").addEventListener("click", () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateSongDisplay();
    }
});

// โหลดเพลงเมื่อหน้าเว็บเปิด
loadSongs();
