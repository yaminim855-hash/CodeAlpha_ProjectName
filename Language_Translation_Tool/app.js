async function translate(text, source, target) {
  // Free demo API (MyMemory) – ok for internship project
  const url =
    "https://api.mymemory.translated.net/get?q=" +
    encodeURIComponent(text) +
    `&langpair=${source}|${target}`;

  const res = await fetch(url);
  const data = await res.json();
  return data.responseData.translatedText;
}

document.getElementById("translateBtn").onclick = async () => {
  const text = document.getElementById("inputText").value;
  const source = document.getElementById("sourceLang").value;
  const target = document.getElementById("targetLang").value;

  if (!text.trim()) {
    alert("Please enter some text");
    return;
  }

  document.getElementById("output").innerText = "Translating...";

  try {
    const translated = await translate(text, source, target);
    document.getElementById("output").innerText = translated;
  } catch (e) {
    document.getElementById("output").innerText = "Error while translating.";
    console.error(e);
  }
};

document.getElementById("copyBtn").onclick = () => {
  const out = document.getElementById("output").innerText;
  navigator.clipboard.writeText(out || "");
  alert("Copied!");
};
