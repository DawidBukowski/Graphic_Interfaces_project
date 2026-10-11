#!/usr/bin/env python3
"""
Generator wireframe'ów dla projektu QuizMaster.
Tworzy proste mockupy pokazujące układ elementów UI.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY_LIGHT = (245, 245, 245)
GRAY = (224, 224, 224)
GRAY_DARK = (153, 153, 153)
BLUE_LIGHT = (179, 217, 255)
BLUE = (0, 102, 204)
YELLOW = (255, 243, 205)
YELLOW_BORDER = (255, 193, 7)
GREEN = (212, 237, 218)
GREEN_BORDER = (40, 167, 69)

# Kolory opcji (Kahoot style)
RED = (226, 27, 60)
BLUE_OPTION = (19, 104, 206)
YELLOW_OPTION = (216, 158, 0)
GREEN_OPTION = (38, 137, 13)

# Rozmiary
WIDTH = 900
HEIGHT = 700

def create_base(title):
    """Tworzy bazowy obraz z tytułem"""
    img = Image.new('RGB', (WIDTH, HEIGHT), GRAY_LIGHT)
    draw = ImageDraw.Draw(img)

    # Ramka
    draw.rectangle([20, 20, WIDTH-20, HEIGHT-20], outline=BLACK, width=3)

    # Tytuł wireframe'a
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 16)
    except:
        font_title = ImageFont.load_default()

    draw.rectangle([20, 0, 400, 25], fill=BLACK)
    draw.text((30, 5), title, fill=WHITE, font=font_title)

    return img, draw

def draw_button(draw, x, y, w, h, text, fill=GRAY, outline=GRAY_DARK, text_color=BLACK):
    """Rysuje przycisk"""
    draw.rectangle([x, y, x+w, y+h], fill=fill, outline=outline, width=2)
    try:
        font = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 18)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text((x + (w - text_w) // 2, y + (h - text_h) // 2), text, fill=text_color, font=font)

def draw_logo(draw, x, y, w, h, text):
    """Rysuje logo placeholder"""
    draw.rectangle([x, y, x+w, y+h], fill=GRAY, outline=GRAY_DARK, width=2)
    try:
        font = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 16)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text((x + (w - text_w) // 2, y + (h - text_h) // 2), text, fill=(102, 102, 102), font=font)

def draw_input(draw, x, y, w, h, label, placeholder=""):
    """Rysuje pole input"""
    try:
        font_label = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 14)
        font_input = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 16)
    except:
        font_label = ImageFont.load_default()
        font_input = ImageFont.load_default()

    draw.text((x, y), label, fill=BLACK, font=font_label)
    draw.rectangle([x, y+25, x+w, y+25+h], fill=WHITE, outline=GRAY_DARK, width=2)
    if placeholder:
        draw.text((x+15, y+25+(h-20)//2), placeholder, fill=GRAY_DARK, font=font_input)

def generate_01_landing():
    """01. Landing Page"""
    img, draw = create_base("01. Landing Page (index.html)")

    # Logo
    draw_logo(draw, 350, 80, 200, 60, "LOGO QuizMaster")

    # Przyciski
    draw_button(draw, 250, 250, 400, 80, "Jestem prowadzącym", BLUE_LIGHT, BLUE)
    draw_button(draw, 250, 350, 400, 80, "Jestem uczestnikiem", BLUE_LIGHT, BLUE)

    # Link
    try:
        font = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 14)
    except:
        font = ImageFont.load_default()
    text = "Pobierz przykładowe quizy"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    draw.text((WIDTH//2 - text_w//2, 480), text, fill=BLUE, font=font)
    draw.line([WIDTH//2 - text_w//2, 495, WIDTH//2 + text_w//2, 495], fill=BLUE, width=1)

    img.save("01-landing-page.png")
    print("✓ Created 01-landing-page.png")

def generate_02_host_import():
    """02. Host - Import"""
    img, draw = create_base("02. Prowadzący - Import quizu (host.html - widok 1)")

    # Logo
    draw_logo(draw, 300, 60, 300, 50, "QuizMaster - Prowadzący")

    # File input
    draw.rectangle([200, 150, 700, 280], fill=WHITE, outline=GRAY_DARK, width=2)
    # Icon
    draw.rectangle([420, 170, 480, 210], fill=GRAY, outline=GRAY_DARK, width=2)
    try:
        font_icon = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 30)
        font = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 16)
        font_small = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 12)
    except:
        font_icon = font = font_small = ImageFont.load_default()

    draw.text((440, 180), "📄", fill=BLACK, font=font_icon)
    draw.text((360, 230), "Wybierz plik JSON", fill=BLACK, font=font)
    draw.text((330, 255), "Kliknij lub przeciągnij plik quizu", fill=GRAY_DARK, font=font_small)

    # Info boxes
    y = 310
    for label, value in [("Wybrany plik:", "historia.json"),
                          ("Tytuł quizu:", "Historia Polski"),
                          ("Liczba pytań:", "10")]:
        draw.rectangle([200, y, 700, y+50], fill=(249, 249, 249), outline=(204, 204, 204), width=2)
        draw.text((210, y+10), label, fill=GRAY_DARK, font=font_small)
        draw.text((210, y+28), value, fill=BLACK, font=font)
        y += 60

    # Button
    draw_button(draw, 200, 550, 500, 60, "Utwórz sesję", BLUE_LIGHT, BLUE)

    img.save("02-host-import.png")
    print("✓ Created 02-host-import.png")

def generate_03_host_dashboard():
    """03. Host - Dashboard"""
    img, draw = create_base("03. Prowadzący - Dashboard sesji (host.html - widok 2)")

    # Logo
    draw_logo(draw, 300, 60, 300, 50, "Sesja: Historia Polski")

    # PIN display
    draw.rectangle([250, 140, 650, 210], fill=YELLOW, outline=YELLOW_BORDER, width=3)
    try:
        font_pin = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 48)
        font = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 14)
        font_regular = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 12)
    except:
        font_pin = font = font_regular = ImageFont.load_default()

    draw.text((380, 160), "123456", fill=BLACK, font=font_pin)

    # Status badge
    draw.rectangle([350, 230, 480, 260], fill=GREEN, outline=GREEN_BORDER, width=2)
    draw.text((370, 238), "✓ Sesja aktywna", fill=(21, 87, 36), font=font)

    # Copy button
    draw_button(draw, 500, 230, 150, 30, "📋 Kopiuj PIN", GRAY, GRAY_DARK, BLACK)

    # Table title
    draw.text((50, 280), "Uczestnicy:", fill=BLACK, font=font)

    # Table
    table_y = 310
    # Header
    draw.rectangle([50, table_y, 850, table_y+40], fill=GRAY, outline=BLACK, width=2)
    draw.text((70, table_y+12), "Imię", fill=BLACK, font=font)
    draw.text((450, table_y+12), "Postęp", fill=BLACK, font=font)
    draw.text((650, table_y+12), "Status", fill=BLACK, font=font)

    # Rows
    rows = [
        ("Jan Kowalski", "3/10", "⏳ W trakcie"),
        ("Anna Nowak", "10/10", "✅ Ukończył"),
        ("Piotr Wiśniewski", "7/10", "⏳ W trakcie")
    ]

    for i, (name, progress, status) in enumerate(rows):
        row_y = table_y + 40 + i*40
        draw.rectangle([50, row_y, 850, row_y+40], fill=WHITE if i % 2 == 0 else (250, 250, 250), outline=GRAY_DARK, width=1)
        draw.text((70, row_y+12), name, fill=BLACK, font=font_regular)
        draw.text((450, row_y+12), progress, fill=BLACK, font=font_regular)
        draw.text((650, row_y+12), status, fill=BLACK, font=font_regular)

    # Close button
    draw_button(draw, 250, 580, 400, 60, "Zamknij sesję", BLUE_LIGHT, BLUE)

    img.save("03-host-dashboard.png")
    print("✓ Created 03-host-dashboard.png")

def generate_04_host_results():
    """04. Host - Results"""
    img, draw = create_base("04. Prowadzący - Wyniki sesji (host.html - widok 3)")

    # Logo
    draw_logo(draw, 250, 60, 400, 50, "Wyniki sesji: Historia Polski")

    # Title
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 28)
        font_name = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 18)
        font_rank = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 24)
        font_score = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 18)
    except:
        font_title = font_name = font_rank = font_score = ImageFont.load_default()

    draw.text((370, 140), "🏆 Ranking", fill=BLACK, font=font_title)

    # Results
    results = [
        ("1.", "Anna Nowak", "95/100 pkt"),
        ("2.", "Piotr Wiśniewski", "80/100 pkt"),
        ("3.", "Jan Kowalski", "70/100 pkt")
    ]

    y = 210
    for rank, name, score in results:
        draw.rectangle([150, y, 750, y+60], fill=(240, 240, 240), outline=GRAY_DARK, width=2)
        draw.text((170, y+15), rank, fill=GRAY_DARK, font=font_rank)
        draw.text((230, y+20), name, fill=BLACK, font=font_name)
        draw.text((620, y+20), score, fill=(40, 167, 69), font=font_score)
        y += 75

    # New session button
    draw_button(draw, 250, 590, 400, 60, "Nowa sesja", BLUE_LIGHT, BLUE)

    img.save("04-host-results.png")
    print("✓ Created 04-host-results.png")

def generate_05_participant_join():
    """05. Participant - Join"""
    img, draw = create_base("05. Uczestnik - Dołączanie do sesji (participant.html - widok 1)")

    # Logo
    draw_logo(draw, 300, 60, 300, 50, "QuizMaster - Uczestnik")

    # Inputs
    draw_input(draw, 200, 180, 500, 70, "Wpisz PIN sesji:", "______")
    draw_input(draw, 200, 320, 500, 70, "Twoje imię:", "Jan Kowalski")

    # Join button
    draw_button(draw, 250, 520, 400, 80, "Dołącz", BLUE_LIGHT, BLUE)

    img.save("05-participant-join.png")
    print("✓ Created 05-participant-join.png")

def generate_06_participant_question():
    """06. Participant - Question"""
    img, draw = create_base("06. Uczestnik - Pytanie (participant.html - widok 2)")

    try:
        font_number = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 16)
        font_question = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 24)
        font_option = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 18)
    except:
        font_number = font_question = font_option = ImageFont.load_default()

    # Question card
    draw.rectangle([100, 80, 800, 240], fill=(240, 240, 240), outline=GRAY_DARK, width=2)
    draw.text((400, 100), "Pytanie 3/10", fill=GRAY_DARK, font=font_number, anchor="mm")

    # Question text box
    draw.rectangle([130, 140, 770, 210], fill=WHITE, outline=GRAY_DARK, width=2)
    question = "W którym roku Polska odzyskała niepodległość?"
    draw.text((450, 175), question, fill=BLACK, font=font_question, anchor="mm")

    # Options
    options = [
        ("A. 1914", RED, 280),
        ("B. 1918", BLUE_OPTION, 360),
        ("C. 1920", YELLOW_OPTION, 440),
        ("D. 1945", GREEN_OPTION, 520)
    ]

    for text, color, y in options:
        draw.rectangle([100, y, 800, y+60], fill=GRAY, outline=(102, 102, 102), width=3)
        draw.rectangle([100, y, 115, y+60], fill=color)
        draw.text((120, y+20), text, fill=BLACK, font=font_option)

    img.save("06-participant-question.png")
    print("✓ Created 06-participant-question.png")

def generate_07_participant_finish():
    """07. Participant - Finish"""
    img, draw = create_base("07. Uczestnik - Zakończenie (participant.html - widok 3)")

    # Logo
    draw_logo(draw, 350, 60, 200, 50, "QuizMaster")

    try:
        font_icon = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 72)
        font_title = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", 36)
        font_msg = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", 20)
    except:
        font_icon = font_title = font_msg = ImageFont.load_default()

    # Checkmark
    draw.text((420, 200), "✅", fill=BLACK, font=font_icon)

    # Title
    draw.text((450, 320), "Dziękujemy za udział!", fill=BLACK, font=font_title, anchor="mm")

    # Message box
    draw.rectangle([200, 400, 700, 480], fill=(209, 236, 241), outline=(12, 84, 96), width=2)
    draw.text((450, 440), "Wyniki ogłosi prowadzący", fill=BLACK, font=font_msg, anchor="mm")

    img.save("07-participant-finish.png")
    print("✓ Created 07-participant-finish.png")

if __name__ == "__main__":
    print("Generowanie wireframe'ów...")
    os.chdir("/home/dawidbukowski/WebstormProjects/Graphic_Interfaces_project/kahoot-clone/etap-1-zarys/mockups")

    generate_01_landing()
    generate_02_host_import()
    generate_03_host_dashboard()
    generate_04_host_results()
    generate_05_participant_join()
    generate_06_participant_question()
    generate_07_participant_finish()

    print("\n✓ Wszystkie wireframe'y zostały wygenerowane!")
