# 🔐 Adaptive CAPTCHA System

An intelligent, behavior-aware CAPTCHA generator that dynamically adjusts its difficulty based on how fast a user types the CAPTCHA. This system demonstrates real-world AI integration, adaptive UX, and a clean full-stack architecture.

---

## 📌 Features

- 🔄 5-Level Adaptive Difficulty (Very Easy → Very Hard)
- ⌛ Typing speed tracking using JavaScript stopwatch
- 🧠 Session-based CAPTCHA progression
- ✨ Real-time input feedback (correct so far / mismatch)
- 🎨 Dark-themed responsive UI with clean styling
- 📈 (Optional) Ready for ML-based behavior modeling

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **CAPTCHA Generator:** `captcha` Python library
- **Session Management:** Flask sessions
- **Fonts/Design:** Inter, Poppins, modern dark theme

---

## 🚀 Difficulty Levels

| Level | Name        | Characters Used                            | Length |
|-------|-------------|---------------------------------------------|--------|
| 1     | Very Easy   | `a-z` (lowercase only)                      | 4      |
| 2     | Easy        | `a-z` + digits                              | 5      |
| 3     | Medium      | `a-z + A-Z + 0-9`                           | 6      |
| 4     | Hard        | Letters + digits + `!@#`                   | 7      |
| 5     | Very Hard   | Letters + digits + `!@#$%^&*()`            | 8      |

---

## 🖼️ UI Preview

![CAPTCHA Demo](static/previews/demo.png)

---
