# Návrh aplikace pro snášenlivost zeleniny

## Problem statement

Uživatel chce jednoduchý program s webovým rozhraním, ve kterém si vybere jednu zeleninu a aplikace vypíše, která zelenina je na záhonu snášenlivá a která není. Seznam zeleniny má vycházet z běžných druhů vhodných pro pěstování v České republice.

## Chosen approach and rationale

Zvolena byla malá server-rendered webová aplikace ve Flasku. Repo je prázdné, takže tato varianta přidává nejmenší množství kódu, je snadno spustitelná lokálně a drží logiku kompatibility přehledně v Pythonu 3.11.

## Approved design details

- Aplikace bude mít jeden vstupní formulář s výběrem jedné zeleniny.
- Data o kompatibilitě budou uložena přímo v Python slovníku.
- Po odeslání formuláře server vrátí stejnou stránku doplněnou o:
  - seznam snášenlivé zeleniny
  - seznam nesnášenlivé zeleniny
- Zelenina bude zvolena z běžných druhů vhodných pro pěstování v ČR, například rajče, mrkev, cibule, salát, okurka, fazole, hrášek, česnek, zelí a brambory.
- Pokud uživatel nic nevybere nebo přijde neznámá hodnota, aplikace nevypíše výsledek a zobrazí jen formulář.

## Acceptance criteria

- Po spuštění aplikace se v prohlížeči zobrazí stránka s titulkem a formulářem.
- V seznamu je několik běžných druhů zeleniny vhodných pro pěstování v ČR.
- Po výběru zeleniny se zobrazí snášenlivé a nesnášenlivé druhy.
- Aplikace nespadne při prázdném nebo neznámém vstupu.
- Aplikace je spustitelná pomocí Pythonu 3.11.

## Remaining open questions

- Žádné blokující otázky nezůstaly. Vzhled bude jednoduchý, účelový a bez dalších funkcí.
