# Aplicație Meteo

Această aplicație meteo permite utilizatorilor să introducă numele unui oraș și să vizualizeze informații despre temperatură, umiditate și condiții meteo curente. De asemenea, aplicația include elemente vizuale dinamice, precum schimbarea culorii fundalului și afișarea unei iconițe reprezentative pentru starea vremii.

## Funcționalități principale

1. Introducerea numelui orașului de către utilizator.
2. Afișarea temperaturii în grade Celsius.
3. Prezentarea umidității în procente.
4. Afișarea condițiilor meteo generale (soare, ploaie, nori etc.).
5. Modificarea fundalului în funcție de condițiile meteo.
6. Afișarea unei iconițe corespunzătoare vremii.
7. Afișarea unui mesaj de eroare dacă orașul nu este valid.

## Aspecte tehnice

Aplicația este dezvoltată în **Python** și utilizează mai multe biblioteci:

- **Tkinter**: pentru crearea interfeței grafice (GUI);
- **Requests**: pentru realizarea cererilor HTTP către API-ul OpenWeatherMap;
- **Pillow**: pentru manipularea și afișarea imaginilor.

### Funcții principale

1. **`get_weather(city)`**  
   Preia datele meteo din API-ul OpenWeatherMap pentru orașul specificat de utilizator și returnează un dicționar cu informațiile relevante (temperatură, umiditate, condiții meteo).

2. **`fetch_weather()`**  
   Apelează funcția `get_weather(city)`, preia datele și actualizează interfața utilizatorului cu noile informații.

3. **`update_icon(condition)`**  
   Modifică imaginea afișată în funcție de condițiile meteo primite. Selectează un fișier imagine corespunzător și îl afișează în interfață.

4. **`update_background(condition)`**  
   Schimbă culoarea fundalului aplicației în funcție de vremea curentă pentru a oferi o experiență vizuală mai dinamică.

