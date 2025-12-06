# Language Translation Tool (HTML + CSS + JavaScript)

This is a simple web-based Language Translation Tool built using HTML, CSS, and JavaScript.  
It uses the free MyMemory Translation API to translate text between English, Hindi, and Telugu.

---

## Features
- Supports English, Hindi, and Telugu translation
- Uses MyMemory free translation API
- Clean UI with textarea input
- Copy translated text with one click
- 100% client-side (no backend needed)

---

## Project Structure

```
project_folder/
│── index.html
│── style.css
│── app.js
│── README.md
```

---

## Technologies Used
- HTML  
- CSS  
- JavaScript  
- MyMemory Translation API  

---

## Installation / How to Run
1. Download or clone the project.
2. Open `index.html` in any web browser.
3. Enter text, select languages, and click **Translate**.

No backend or server setup required.

---

## How It Works
- User enters a text string.
- User selects source and target languages.
- JavaScript sends a GET request to MyMemory API:
  ```
  https://api.mymemory.translated.net/get?q=TEXT&langpair=en|te
  ```
- API returns translated text.
- Output is displayed in UI.

---

## Core Logic (JavaScript)

```javascript
async function translate(text, source, target) {
  const url = "https://api.mymemory.translated.net/get?q=" 
              + encodeURIComponent(text) 
              + `&langpair=${source}|${target}`;
  const res = await fetch(url);
  const data = await res.json();
  return data.responseData.translatedText;
}
```

---

## Future Improvements
- Add more languages
- Add voice input
- Auto-detect source language
- Add dark mode UI
- Support document translation (PDF/TXT)

---

## Author
Medalli Yamini
