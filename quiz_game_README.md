<div align="center">

# ❓ Quiz Game

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #8 — 5 questions. How many can you get right? 🖤**

</div>

---

## 💡 What It Does

```
5 questions appear one by one
You type your answer
Correct? Score goes up! ✅
Wrong? Try next one 😢
Final score shown at end!
```

---

## 🎮 Demo

```bash
Welcome to the QUIZ GAME^_^
WHAT IS THE CAPITAL OF FRANCE? : PARIS
WHAT IS THE LARGEST PLANET IN OUR SOLAR SYSTEM? : JUPITER
WHO WROTE THE PLAY 'ROMEO AND JULIET'? : WILLIAM SHAKESPEARE
WHAT IS THE CAPITAL OF JAPAN? : TOKYO
WHO INVENTED PYTHON : GUIDO VAN ROSSUM
Your score is: 5 /5 🎉
```

---

## ▶️ Run It

```bash
python QUIZ_GAME.PY
```

---

## ❓ Questions

| # | Question | Answer |
|---|----------|--------|
| 1 | Capital of France? | PARIS |
| 2 | Largest planet? | JUPITER |
| 3 | Who wrote Romeo & Juliet? | WILLIAM SHAKESPEARE |
| 4 | Capital of Japan? | TOKYO |
| 5 | Who invented Python? | GUIDO VAN ROSSUM |

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `dictionary {}` | Store questions & answers |
| `for question in questions` | Loop through all questions |
| `input()` | Get user's answer |
| `.upper()` | Convert answer to CAPS for comparison |
| `if / else` | Check if answer is correct |
| `score += 1` | Add point for correct answer |
| `print()` | Show final score |

---

## 💻 Source Code

```python
questions = {
    "WHAT IS THE CAPITAL OF FRANCE?"                  : "PARIS",
    "WHAT IS THE LARGEST PLANET IN OUR SOLAR SYSTEM?" : "JUPITER",
    "WHO WROTE THE PLAY 'ROMEO AND JULIET'?"          : "WILLIAM SHAKESPEARE",
    "WHAT IS THE CAPITAL OF JAPAN?"                   : "TOKYO",
    "WHO INVENTED PYTHON"                             : "GUIDO VAN ROSSUM",
}

score = 0
print("Welcome to the QUIZ GAME^_^")

for question in questions:
    answer = input(question + " : ").upper()
    if answer == questions[question]:
        score = score + 1
    else:
        print("WRONG ANSWER, TRY AGAIN 😊")

print("Your score is:", score, "/5")
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
