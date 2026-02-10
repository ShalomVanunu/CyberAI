# AI AGent Scan Files on my folder and send me Email Summerize

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from google import genai
from google.genai import types

# טעינת משתני הסביבה מקובץ .env
load_dotenv()

# שליפת המשתנים
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


# אתחול הקליינט של גוגל
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_ID = "gemini-2.5-flash"



# --- הגדרת הכלים (Tools) ---

def list_files_in_directory() -> str:
    """סורק את התיקייה הנוכחית ומחזיר רשימת קבצים."""
    try:
        files = os.listdir('.')
        print(files)
        return f"נמצאו הקבצים הבאים בתיקייה: {', '.join(files)}"
    except Exception as e:
        return f"שגיאה בסריקת התיקייה: {str(e)}"




def send_actual_gmail(recipient: str, subject: str, body: str) -> str:
    """שולח אימייל דרך Gmail. דורש נמען, נושא ותוכן."""
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = GMAIL_USER
        msg['To'] = recipient

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)

        return "הודעה: המייל נשלח בהצלחה."
    except Exception as e:
        return f"שגיאה בשליחת המייל: {str(e)}"






# --- הרצת הסוכן ---

def run_ai_agent(prompt: str):
    print(f"--- הסוכן מתחיל לעבוד ---")

    # הגדרת הכלים וההנחיות לסוכן
    chat = client.chats.create(
        model=MODEL_ID,
        config=types.GenerateContentConfig(
            tools=[list_files_in_directory, send_actual_gmail],
            system_instruction="אתה סוכן אוטומציה מבוסס פייתון. תפקידך לסרוק קבצים ולדווח במייל.רשום לכל קובץ איזו אפלקציה מומלצת להרצה"
        )
    )

    # ביצוע המשימה
    response = chat.send_message(prompt)

    print("\nתגובה סופית:")
    print(response.text)


if __name__ == "__main__":
    user_request = f"סרוק את התיקייה ושלח לי סיכום למייל של הקבצים ורשימה של הסיומות שלהם עם התוכנה שמריצה אותם {GMAIL_USER}"
    run_ai_agent(user_request)
