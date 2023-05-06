# Snake Projekt
## Obsah
	1. Cíl Projektu
	2. Použité technologie
	3. Jak hru nainstalovat
	4. Jak hru používat
	5. Vysvětlení kódu
	6. Credits
## Cíl Projektu
Cílem projektu je vytvořit známou hru Snake s náhodným generováním potravy pro hada
## Použité technologie
Pro vytvoření hry je použita knihovna pygame pro Python
## Jak hru nainstalovat
### Co budete potřebovat
	- Visual Studio Code
	- Python
	- pygame
### Jak jednotlivé prvky získat
**Visual Studio Code**
Pro Windows, Linux, Mac běžte na:
[Visual Studio Code Download](https://code.visualstudio.com/download)
Stáhněte verzi pro váš operační systém.

*Linux Download*
Pro Linux budete potřebovat ještě tento [Návod](https://code.visualstudio.com/docs/setup/linux)

**Python**
Pokud Python ještě nemáte nainstalovaný běžte na:
[Python Download](https://www.python.org/downloads/)
Stáhněte verzi pro váš operační systém

*Linux Download*
Pro Linux se bude hodit [Návod](https://www.scaler.com/topics/python/install-python-on-linux/)

**Pygame**
*Windows Instalace*
Do příkazového řádku napište `pip install pygame`
Pokud něco nefunguje jděte na:
[Windows instalace](https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/)

*Linux Instalace*
Do příkazového řádku napište `pip install pygame`
Pokud něco nefunguje jděte na:
[Linux instalace](https://www.geeksforgeeks.org/install-pygame-in-linux/)

*Mac Instalace*
Do příkazového řádku napište `pip3 install pygame` 
Pokud něco nefunguje jděte na:
[Mac instalace](https://www.geeksforgeeks.org/install-pygame-in-macos/)

### Otevření projektu ve Visual Studio Code 
1. Stáhněte .zip soubor z githubu a uložte do složky
2. Soubor do složky rozbalte
3. Zapněte Visual Studio Code a vlevo nahoře klikněte na kolonku *File* nebo zmáčkněte *Ctrl+K Ctrl+O*
4. Klikněte na Open Folder a vyberte složku do které jste uložili soubor z githubu a potvrďte
## Jak hru používat
### Seznam bodů 
	- Kontrola highscore
	- Nastavení velikosti okna
	- Nastavení parametrů hry
	- Ovládání hry
	- Ukončení hry
**Kontrola highscore**
1. Otevřete soubor *highscore.txt*
2. Zkontrolujte že jediné co v souboru je napsané je jedno číslo (pokud hru hrajete poprvé mělo by být 0).

**Nastavení velikosti okna**
3. Otevřete soubor *main.py* 
4. Na řádku 7 nastavte *screen_size_pixels*  menší nebo vetší podle rozlišení vašeho displeje

**Nastavení parametrů hry**
5.  Spusťte soubor *main.py* pomocí šipky napravo nahoře
6. Po spuštění vyskočí okno. Zmáčkněte *alt+Tab*, nebo se překlikněte zpátky do Visual Studio Code
7. V terminálu by se mělo objevit kolonka *speed* zadejte rychlost jakou chcete aby se had po herní ploše pohyboval. Obrazovka se obnoví 120x za sekundu to znamená že se dá spočítat jak často se bude pohybovat. Je zde tabulka s pár příklady kolikrát se za sekundu posune, při nastavené rychlosti.
| 120  |  60 | 30  |20   |1   |
|---|---|---|---|---|
|  1x | 2x  | 4x  | 6x  | 120x  |
8. Po potvrzení rychlosti vyskočí další kolonka "*size*". Určuje kolik políček chcete aby bylo na jednom řádku/sloupci.
9. Po potvrzení velikosti okna se spustí odpočet 5 sekund. Znovu zmáčkněte *alt+Tab* nebo překlikněte zpět do okna, které vám na začátku vyskočilo. Po uběhlých 5 sekundách se hra spustí.

**Ovládání hry** 
- Po zapnutí hry se had automaticky rozjede doprava. 
- Ovládat  se dá dvěma způsoby.
	- W, S, A, D
		- W - Nahoru
		- S - Dolu
		- A - Doleva
		- D - Doprava
	- Šipky
		- Podle směru šipky
- Kdykoli v průběhu hry se dá odejít pomocí zmáčknutí klávesy *esc*
- Po prohrání/vyhrání se pokus opakuje po zmáčknutí *Backspace*

**Ukončení hry**
- Po ukončení hry se highscore ukládá pro další pokusy.
- Pokud chcete highscore smazat/upravit v souboru *highscore.txt*


## Vysvětlení kódu
### Nastavení hlavních parametrů
`screen_size_pixels = 900` 
Nastavení velikosti obrazu hry v pixelech

`font_multiplier = screen_size_pixels/1000`
Vydělí velikost okna, tak aby se velikost písma poupravila

`screen_size = (screen_size_pixels, screen_size_pixels)`
Nastaví velikost okna, aby to vždy byl čtverec a stačilo zadat rozměr jen jednou

`y_offset = 100*font_multiplier`
Nastaví spodní odrážku pro výpis *score* podle velikosti okna

`screen = pygame.display.set_mode((screen_size[0],screen_size[1]+y_offset))`
Dopočítá velikost okna i s odrážkou

`font = pygame.font.Font('MINECRAFT.otf', int(70*font_multiplier))`
`fontdied = pygame.font.Font('MINECRAFT.otf', int(100*font_multiplier))`
`fontspace = pygame.font.Font('MINECRAFT.otf', int(40*font_multiplier))`
Spočítá všechny velikosti fontů, tak aby se při *Death screenu* velikosti mohli lišit

`speed = int(input("speed: ")) `
`cells = int(input("cells: "))`
`print("Press 'alt + tab'")` 
`time.sleep(5)`
Vezme vstupy od uživatele pro rychlost hada a počet políček. Naviguje jak postupovat dál a čeká 5 sekund než se spustí hra.


