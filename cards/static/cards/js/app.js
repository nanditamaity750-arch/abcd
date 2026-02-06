const quotes = [
  "I love you more than yesterday, less than tomorrow.",
  "Every love story is beautiful, but ours is my favorite.",
  "You are my today and all of my tomorrows.",
  "I still get butterflies when I see you.",
  "You are the calm in my chaos and the light in my life.",
  "With you, everything feels like home.",
  "You are my once in a lifetime.",
  "I love you to the moon and back, and then some.",
  "You make my heart feel safe.",
  "In your smile, I see something more beautiful than the stars."
];

const quoteBox = document.getElementById("quote-box");
const newQuoteBtn = document.getElementById("new-quote");
if (newQuoteBtn && quoteBox) {
  newQuoteBtn.addEventListener("click", () => {
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    quoteBox.textContent = `"${randomQuote}"`;
  });
}

const audio = document.getElementById("bg-audio");
const playBtn = document.getElementById("play-music");
if (audio) {
  audio.volume = 0.35;
}
if (playBtn && audio) {
  playBtn.addEventListener("click", () => {
    audio.play().catch(() => {
      // Autoplay might be blocked until user interacts.
    });
  });
}

const themeBtn = document.getElementById("toggle-theme");
const themes = [
  { key: "rose", label: "Rose" },
  { key: "sunset", label: "Sunset" },
  { key: "ocean", label: "Ocean" }
];

function applyTheme(themeKey) {
  document.body.setAttribute("data-theme", themeKey);
  const theme = themes.find(item => item.key === themeKey) || themes[0];
  if (themeBtn) {
    themeBtn.textContent = `Theme: ${theme.label}`;
  }
}

const savedTheme = localStorage.getItem("valentine-theme") || "rose";
applyTheme(savedTheme);

if (themeBtn) {
  themeBtn.addEventListener("click", () => {
    const current = document.body.getAttribute("data-theme") || "rose";
    const currentIndex = themes.findIndex(item => item.key === current);
    const next = themes[(currentIndex + 1) % themes.length].key;
    localStorage.setItem("valentine-theme", next);
    applyTheme(next);
  });
}
