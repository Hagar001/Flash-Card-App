# Flash Card App 📚💡  

A capstone project from the 100 Days of Code: The Complete Python Bootcamp by Angela Yu.
This project is a **language learning flash card application** built with Python and Tkinter. It helps users practice vocabulary by showing words in one language and their translations when you click directly on the card to flip it.  

---

## 🚀 Features  

- 🎴 Flash card system that displays a random word in the learning language.  
- 🖱️ Click on the card itself to flip and reveal the translation.  
- ✅ "Known" button to remove learned words from the learning list.  
- 🔁 Persistent progress tracking — words you already know won’t appear again.  
- 🖼️ Clean graphical interface made with **Tkinter**.  

---

## 🛠️ Tech Stack  

- **Python 3**  
- **Tkinter** – for GUI  
- **Pandas** – for data handling (CSV word lists)  

---

## 📂 Project Structure  

flash-card-app/
│── main.py                # Main application code
│── words\_to\_learn.csv     # Progress file (auto-generated after using app)
│── data/
│   └── french\_words.csv   # Starter dataset with French–English vocabulary
│── images/
│   ├── card\_front.png     # Flashcard front design
│   ├── card\_back.png      # Flashcard back design
│   └── right.png          # "Known" button image
│   └── wrong.png          # "Unknown" button image
│── README.md              # Project documentation

---

## ▶️ How to Run  

1. Clone this repository:  
   ```bash
   git clone https://github.com/Hagar001/Flash-Card-App.git
   cd Flash-Card-App
   
2. Install required dependencies:

   ```bash
   pip install pandas
   ```
3. Run the program:

   ```bash
   python main.py
   ```
---

## 🎯 How It Works

1. The app shows a **random French word** from the dataset.
2. Click on the **card itself** to flip and reveal the **English translation**.
3. If you **knew the word**, click ✅ → it’s removed from the learning list.
4. If not, click ❌ → it stays in the list for future practice.
5. Progress is saved in **`words_to_learn.csv`** automatically.

---

## 📖 Learning Outcome

This project demonstrates how to:

* Work with **Tkinter** to build GUIs.
* Handle **click events on images/widgets** for interactions.
* Manage data with **Pandas**.
* Save and load progress for user-friendly applications.

---

## 📸 Demo (Screenshot Example)
<img width="1023" height="726" alt="Capture-eau-water0" src="https://github.com/user-attachments/assets/5f8bdc5d-ede1-4bd0-ae84-630579b3623a" />

<img width="1023" height="728" alt="Capture-eau-water1" src="https://github.com/user-attachments/assets/4aef4193-100b-466e-89a0-b4e1264903db" />

---

## 🏆 Credits

* Project idea from the 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu.
* Dataset: Provided in course (French–English word list).
