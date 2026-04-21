# Zelenina Snášenlivost Implementation Plan

**Goal:** Vytvořit jednoduchou lokální webovou aplikaci, kde uživatel vybere jednu zeleninu a zobrazí se snášenlivé a nesnášenlivé druhy.

**Architecture:** Aplikace bude mít jeden Flask server v `app.py` a jednu HTML šablonu v `templates/index.html`. Data o kompatibilitě budou uložena v Python slovníku a stránka bude po odeslání formuláře znovu vykreslena s výsledkem.

**Tech Stack:** Python 3.11, Flask, Jinja2, HTML, CSS

---

### Task 1: Založit kostru aplikace

**Files:**
- Create: `app.py`
- Create: `templates/index.html`
- Create: `requirements.txt`
- Create: `README.md`

**Step 1: Přidat závislost**

Do `requirements.txt` zapsat `Flask`.

**Step 2: Vytvořit Flask aplikaci**

V `app.py` definovat:
- Flask app
- seznam zeleniny
- mapu kompatibility
- route `/` pro `GET` i `POST`

**Step 3: Vytvořit šablonu stránky**

V `templates/index.html` přidat:
- nadpis
- formulář se selectem
- výpis snášenlivé zeleniny
- výpis nesnášenlivé zeleniny

**Step 4: Dopsat spuštění**

Do `README.md` přidat stručný návod na instalaci a spuštění.

### Task 2: Ověřit základní funkčnost

**Files:**
- Test: `app.py`

**Step 1: Ověřit syntaxi**

Run: `python3.11 -m py_compile app.py`
Expected: bez chyby

**Step 2: Ověřit vykreslení routy**

Run: `python3.11 -c "from app import app; client = app.test_client(); response = client.get('/'); print(response.status_code)"`
Expected: `200`

**Step 3: Ověřit POST s výběrem**

Run: `python3.11 -c "from app import app; client = app.test_client(); response = client.post('/', data={'vegetable': 'rajce'}); print(response.status_code)"`
Expected: `200`
