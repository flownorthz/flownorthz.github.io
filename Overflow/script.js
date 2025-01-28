// ตั้งค่า Repository ของคุณ
const repoOwner = "flownorthz"; // แทนที่ด้วยชื่อ GitHub ของคุณ
const repoName = "my-songs"; // ชื่อ Repository
const branch = "main"; // ชื่อ branch ที่ใช้ (ส่วนใหญ่คือ main)

// โฟลเดอร์สำหรับเก็บเพลงและเนื้อเพลง
const songsFolder = `https://raw.githubusercontent.com/${repoOwner}/${repoName}/${branch}/songs/`;
const lyricsFolder = `https://raw.githubusercontent.com/${repoOwner}/${repoName}/${branch}/lyrics/`;

let songs = [];

function fetchSongsAndLyrics() {
    // ดึงรายชื่อไฟล์ในโฟลเดอร์เพลงจาก GitHub API
    fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contents/songs?ref=${branch}`)
        .then(response => response.json())
        .then(data => {
            songs = data
                .filter(file => file.name.endsWith(".mp3"))
                .map(file => {
                    const title = file.name.replace(".mp3", "");
                    return {
                        title: title,
                        file: `${songsFolder}${file.name}`,
                        lyrics: `${lyricsFolder}${title}.txt`
                    };
                });
            displaySongList();
        })
        .catch(error => console.error("Error fetching songs:", error));
}

function displaySongList() {
    const songList = document.getElementById("song-list");
    songList.innerHTML = "";
    songs.forEach((song, index) => {
        const li = document.createElement("li");
        li.textContent = song.title;
        li.onclick = () => showSongDetail(index);
        songList.appendChild(li);
    });
}

function showSongDetail(index) {
    const song = songs[index];
    document.getElementById("song-title").textContent = song.title;
    document.getElementById("song-audio").src = song.file;

    // ดึงเนื้อเพลง
    fetch(song.lyrics)
        .then(response => response.text())
        .then(text => {
            document.getElementById("song-lyrics").textContent = text;
        })
        .catch(error => {
            document.getElementById("song-lyrics").textContent = "Lyrics not found.";
            console.error("Error fetching lyrics:", error);
        });

    document.getElementById("song-list").style.display = "none";
    document.getElementById("song-detail").style.display = "block";
}

function backToList() {
    document.getElementById("song-detail").style.display = "none";
    document.getElementById("song-list").style.display = "block";
}

document.addEventListener("DOMContentLoaded", fetchSongsAndLyrics);
