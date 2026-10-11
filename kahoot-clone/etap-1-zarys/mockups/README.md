# Mockupy / Wireframe'y - QuizMaster

Ten katalog zawiera wireframe'y (szkice interfejsu) projektu QuizMaster.

## Pliki

### Obrazki PNG (wireframe'y):
1. `01-landing-page.png` - Ekran startowy (wybór roli)
2. `02-host-import.png` - Prowadzący: import quizu z JSON
3. `03-host-dashboard.png` - Prowadzący: dashboard sesji z PIN-em i uczestnikami
4. `04-host-results.png` - Prowadzący: ranking wyników
5. `05-participant-join.png` - Uczestnik: dołączanie do sesji
6. `06-participant-question.png` - Uczestnik: ekran pytania
7. `07-participant-finish.png` - Uczestnik: zakończenie quizu

### Pliki źródłowe HTML (opcjonalne):
- `01-landing-page.html` do `07-participant-finish.html` - Interaktywne wireframe'y do podglądu w przeglądarce
- `wireframe-style.css` - Wspólne style dla wszystkich wireframe'ów HTML

### Generator:
- `generate_wireframes.py` - Skrypt Python (PIL/Pillow) do automatycznego generowania obrazków PNG

## Jak wygenerować wireframe'y od nowa?

```bash
cd mockups/
python3 generate_wireframes.py
```

Wymaga: Python 3 + biblioteka Pillow (PIL)

## Uwagi

Wireframe'y są celowo uproszczone - pokazują **układ elementów** i **hierarchię informacji**, nie finalne detale wizualne (kolory, cienie, gradienty itp.). Finalna wersja interfejsu będzie bardziej dopracowana wizualnie.

**Format:** 900x700px, PNG, paleta kolorów inspirowana Kahoot (żywe kolory, czytelne kontrasty)
