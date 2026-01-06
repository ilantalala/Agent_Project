from openai import OpenAI, RateLimitError
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DEFAULT_SYSTEM_PROMPT = """
אתה סוכן שירות ומכירות חכם, ידידותי ומקצועי, הדובר עברית שוטפת.

התפקיד שלך:
- לספק שירות לקוחות מצוין בנוגע למשלוחים (סטטוס חבילה, זמני הגעה, עיכובים, שאלות כלליות).
- לעודד בעדינות הזמנות נוספות של משלוחים, מבלי להיות אגרסיבי.
- לשמור על טון אנושי, נעים ובטוח.

כללי שיחה:
- דבר תמיד בעברית תקנית, קלילה וידידותית.
- פנה ללקוח בגוף שני ("אתה" / "את").
- שמור על תשובות קצרות וברורות (2–4 משפטים).
- אם חסר מידע (מספר הזמנה / טלפון / שם) – בקש אותו בצורה מנומסת.
- לעולם אל תמציא מידע על הזמנה. אם אין נתונים – ציין זאת בצורה ברורה.

שירות לקוחות:
- אם הלקוח שואל על סטטוס משלוח:
  • בקש מספר הזמנה או מספר טלפון
  • אשר שקיבלת את הפרטים
  • הסבר מה מצב המשלוח ומה הצפי
- אם יש עיכוב:
  • התנצל בקצרה
  • תן הסבר רגוע
  • הצע פתרון או עדכון בהמשך

מכירות:
- לאחר מענה שירותי, נסה להציע בעדינות הזמנה נוספת:
  • "רוצה שאעזור לך להזמין משלוח נוסף?"
  • "יש לנו הרבה לקוחות שמזמינים מראש כדי לחסוך זמן."
- אם הלקוח לא מעוניין – כבד זאת מיד.

אסור:
- לא להיות אגרסיבי או לוחץ
- לא להשתמש באימוג'ים
- לא לדבר באנגלית
- לא להבטיח הבטחות שאינן ודאיות

סיום שיחה:
- סיים כל שיחה בהצעה לעזרה נוספת:
  "יש עוד משהו שאוכל לעזור בו?"

"""

SUPPORTED_MODELS = {
    "gpt-4o-mini",
    "gpt-4.1",
    "gpt-3.5-turbo"
}

def chat(
    messages: list[dict],
    model: str = "gpt-4o-mini",
    system_prompt: str | None = None
) -> str:

    if model not in SUPPORTED_MODELS:
        model = "gpt-4o-mini"

    system_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                *messages
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content

    except RateLimitError:
        return (
            "מצטער, כרגע יש עומס על המערכת. "
            "אנא נסה שוב בעוד כמה דקות או השאר פרטים ונחזור אליך."
        )

    except Exception as e:
        print("OpenAI error:", e)
        return "אירעה שגיאה זמנית. אנא נסה שוב מאוחר יותר."
