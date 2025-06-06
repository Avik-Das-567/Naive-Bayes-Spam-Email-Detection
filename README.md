# Naive Bayes with Streamlit - Spam Email Detection
### App Link
- https://naive-bayes-spam-email-detection.streamlit.app/
---
### What is Naive Bayes?
- Naive Bayes is a **machine learning algorithm** that uses **probability** to **predict categories** (like **Yes/No** or **Spam/Not Spam**).
- **Example:** Just like we say, "Most emails with **'Buy Now'** are spam", Naive Bayes looks at **words in text** and uses chances to decide whether it’s spam or not."
- Naive Bayes works **best on text data**. It's very fast and simple.
- It is used in **Gmail**, **SMS apps**, and **comment filters**.
---
### Required Python Packages
- **`scikit-learn`** - To build machine learning models
- **`streamlit`** - To build data apps
- **`pandas`** - To work with the dataset
---
### Example Problem
- Detecting Spam Email Based on Message Text

| Message Text               | Is\_Spam |
| -------------------------- | -------- |
| Win money now              | Yes      |
| Buy 1 Get 1 Free           | Yes      |
| Meeting at 3 PM            | No       |
| Your invoice is attached   | No       |
| Claim your free gift today | Yes      |

---
### How the code works
- It converts **text into numbers** using **`CountVectorizer`**.
- Then it calculates **probability** of a message being spam.
- Naive Bayes is called "naive" because it **assumes each word is independent**, even though they’re not.
---
