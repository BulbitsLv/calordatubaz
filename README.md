# Calorie Tracker (Kaloriju skaitītājs)

Konsoles un grafiskā lietojumprogramma Python valodā, kas izstrādāta ar SQLite datubāzi, lai sekotu līdzi ikdienas kalorijām, uzturvērtībai, fiziskajām aktivitātēm un svara izmaiņām.

## Galvenās iespējas
- Lietotāju pārvaldība: Lietotāju reģistrācija un individuālo dienas kaloriju mērķu uzstādīšana.
- Uztura uzskaite: Ēdienu kataloga un maltīšu žurnāla pārvaldība (meals, meal_items).
- Aktivitāšu reģistrs: Fizisko vingrojumu uzskaite un kaloriju patēriņa kontrole (exercise_logs, exercises).
- Svara kontrole: Svara dinamikas fiksēšana laika gaitā (weight_logs).

## Tehnoloģijas
- Python 3.x - programmēšanas valoda.
- SQLite3 - datubāzes dzinējs (iebūvētā Python bibliotēka, nav nepieciešams instalēt papildu ārējās pakotnes).
- Tkinter - grafiskās saskarnes bibliotēka (iebūvēta Python).

## Kā palaist programmu
1. Pārliecinies, ka tavā datorā ir instalēts Python 3.
2. Saglabā failus database.py un main.py vienā mapē.
3. Atver termināli šajā mapē un palaid programmu ar komandu:
   ```bash
   python main.py
