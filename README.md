# 🛠️ Python Automation Toolkit

A collection of Python scripts that automate boring, repetitive tasks — built as part of my developer portfolio to showcase Python scripting and CLI tool development.

---

## 📦 Scripts

### 1. File Renamer
Bulk rename files inside a folder using different modes.

**Modes:**
- `number` — renames files in alphabetical order with a number prefix (001, 002, 003...)
- `date` — adds today's date as a prefix to every file
- `oldest` — orders files by oldest modification date and numbers them accordingly

**Usage:**
```bash
python file_renamer/renamer.py <folder_path> --mode number
python file_renamer/renamer.py <folder_path> --mode date
python file_renamer/renamer.py <folder_path> --mode oldest
```

**Example:**
```
cat.jpg → 001_cat.jpg
dog.jpg → 002_dog.jpg
bird.jpg → 003_bird.jpg
```

---

### 2. Folder Organizer
Automatically sorts all files in a messy folder into subfolders by file type.

**Categories it sorts into:**
| Folder | File Types |
|--------|-----------|
| Images | .jpg, .jpeg, .png, .gif, .webp, .svg |
| Videos | .mp4, .mov, .avi, .mkv |
| Music | .mp3, .wav, .flac, .aac |
| Documents | .pdf, .docx, .txt, .xlsx, .csv |
| Programs | .exe, .msi, .apk |
| Code | .py, .js, .html, .css, .java |
| Archives | .zip, .rar, .tar, .gz |
| Others | anything else |

**Usage:**
```bash
python folder_organizer/organizer.py <folder_path>
```

**Example:**
```
Before:
  downloads/cat.jpg, report.pdf, song.mp3, setup.exe

After:
  downloads/Images/cat.jpg
  downloads/Documents/report.pdf
  downloads/Music/song.mp3
  downloads/Programs/setup.exe
```

---

### 3. Web Scraper
Scrapes quotes from [quotes.toscrape.com](http://quotes.toscrape.com) and saves them to a JSON file.

**Usage:**
```bash
python web_scraper/scraper.py --pages 3 --output quotes.json
```

**Options:**
- `--pages` — number of pages to scrape (default: 3)
- `--output` — output filename (default: quotes.json)

**Output format:**
```json
[
  {
    "quote": "The world as we have created it...",
    "author": "Albert Einstein",
    "tags": ["change", "deep-thoughts", "thinking"]
  }
]
```

---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/YOURUSERNAME/python-automation-toolkit
cd python-automation-toolkit
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run any script**
```bash
python file_renamer/renamer.py <folder_path> --mode oldest
python folder_organizer/organizer.py <folder_path>
python web_scraper/scraper.py --pages 5 --output results.json
```

---

## 🧰 Tech Stack

- **Python 3**
- **os / shutil / argparse** — built-in Python libraries
- **requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing

---

## 👤 Author

Made by **Rangga Joshua Maindra** — First grade SMK student building a developer portfolio.

- GitHub: [https://github.com/jojoisstudying)
- Portfolio: https://jojoisstudying.github.io/
