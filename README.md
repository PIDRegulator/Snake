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

### Hlavní cyklus pro opakování hry 
Vezme vstupy od uživatele pro rychlost hada a počet políček. Naviguje jak postupovat dál a čeká 5 sekund než se spustí hra.

`direction = (0,1)`
`old_direction = (0,1)`
Nastaví směr doprava

`clock = pygame.time.Clock()`
Nastaví proměnnou, aby se dále jednodušeji dalo nastavovat jak často se obrazovka bude obnovovat

`score = 0`
Vyresetuje score

`max_len = cells*cells`
Spočítá jak dlouhý musí být had, aby hráč danou hru vyhrál

`apple = [random.randint(0,cells-1),random.randint(0,cells-1)]`
Vygeneruje náhodnou pozici jablka pro začátek hry

`snake = [[1,1]]`
Nastaví první pozici hada doprava nahoru jedno políčko od obou stěn.

`cell_size = screen_size[0]/cells`
Spočítá jak velké bude každé políčko podle velikosti desky a počtu políček zadaným hráčem

`background = pygame.Surface(screen_size)`
`background.fill((6, 189, 36))`
Vybarví herní plochu

`for y in  range(cells):`
&nbsp;&nbsp;&nbsp;&nbsp;`for x in  range(cells):`
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if (x+y) % 2  ==  0:`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pygame.draw.rect(background,[17, 140, 37],			[x*cell_size,y*cell_size,cell_size,cell_size])`
Spočítá a vykreslí, kde mají být políčka jiné barvy pro vytvoření šachovnice

`f = open("highscore.txt","r")`
`highs = int(f.read().splitlines()[0])`
`if highs >  0:`
&nbsp;&nbsp;&nbsp;&nbsp;`highscore_str = f"highscore: {highs}"`
`else:`
&nbsp;&nbsp;&nbsp;&nbsp;`highscore_str = ""`
najde *highscore* v souboru a zjistí pokud je větší než nula.

`running = True`
`movecount = speed`
Nastaví další proměnné pro běh cyklu hry a rychlosti

### Cyklus jednotlivých pokusů

`clock.tick(120)`
Nastaví kolikrát za sekundu se obrazovka obnoví

`framerate = clock.get_fps()`
`for event in pygame.event.get():`
&nbsp;&nbsp;&nbsp;&nbsp;`if event.type == pygame.QUIT:`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
Zajistí aby se dalo ze hry odejít aniž by hra crashovala

`keys = pygame.key.get_pressed()`
`if keys[pygame.K_UP] or keys[pygame.K_w]:`
&nbsp;&nbsp;&nbsp;&nbsp;`direction = (-1,0)`

`if keys[pygame.K_DOWN] or keys[pygame.K_s]:`
&nbsp;&nbsp;&nbsp;&nbsp;`direction = (1,0)`

`if keys[pygame.K_LEFT] or keys[pygame.K_a]:`
&nbsp;&nbsp;&nbsp;&nbsp;`direction = (0,-1)`

`if keys[pygame.K_RIGHT] or keys[pygame.K_d]:`
&nbsp;&nbsp;&nbsp;&nbsp;`direction = (0,1)`
Bere vstup z klávesnice a mění podle toho směr jízdy hada.

`if old_direction != direction and old_direction[0] + direction[0] ==  0:`
&nbsp;&nbsp;&nbsp;&nbsp;`direction = old_direction`
Znemožní otočit hada o 180° na jednou.

`if movecount ==0:`
&nbsp;&nbsp;&nbsp;&nbsp;`old_direction = direction`
&nbsp;&nbsp;&nbsp;&nbsp;`new_y = snake[-1][0] + direction[0]`
&nbsp;&nbsp;&nbsp;&nbsp;`new_x = snake[-1][1] + direction[1]`
&nbsp;&nbsp;&nbsp;&nbsp;`new_body = [new_y,new_x]`
Posune hada po uběhlém čase nastaveném před zapnutím hry.

`if snake[-1][0] >= cells or snake[-1][1] >= cells:`
&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
&nbsp;&nbsp;&nbsp;&nbsp;`continue`

`if snake[-1][0] <  0  or snake[-1][1] <  0:`
&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
&nbsp;&nbsp;&nbsp;&nbsp;`continue`
Zjistí pokud had je mimo hrací plochu. Pokud ano hru přeruší.

`if apple == new_body:`
&nbsp;&nbsp;&nbsp;&nbsp;`score += 1`
&nbsp;&nbsp;&nbsp;&nbsp;`!if  len(snake)+1>=max_len:`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`win = True`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("you won")`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`continue`
&nbsp;&nbsp;&nbsp;&nbsp;`else:`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`while apple in snake+[new_body]:`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`apple = [random.randint(0,cells-1),random.randint(0,cells-1)]`
`else:`
&nbsp;&nbsp;&nbsp;&nbsp;`snake.pop(0)`
`if new_body in snake:`
&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
&nbsp;&nbsp;&nbsp;&nbsp;`continue`
&nbsp;&nbsp;&nbsp;&nbsp;`snake.append(new_body)`
&nbsp;&nbsp;&nbsp;&nbsp;`movecount = speed`
Připočte bod pokud had snědl jablko. 
Ukončí hru pokud had dosáhl maximální délky podle velikosti hracího pole a zaručí s´že se ukáže *win screen* místo *death screen*.
Přidá nové jablko pokud had nedosáhl maximální délky.
Zničí poslední políčko těla hada.
Zajistí že hra se vypne pokud had nabourá sám do sebe.

`else:`
&nbsp;&nbsp;&nbsp;&nbsp;`movecount -= 1`
Odečte jedna od počtu uběhlých snímků za poslední sekundu aby se cyklus opakoval správně.

`screen.blit(background,(0,0))`
`pygame.draw.rect(screen,[227, 7, 14],[apple[1]*cell_size,apple[0]*cell_size,cell_size,cell_size]`
`for i,body in  enumerate(snake[:-1]):`
&nbsp;&nbsp;&nbsp;&nbsp;`color = abs(255-(255/len(snake)*i))`
&nbsp;&nbsp;&nbsp;&nbsp;`pygame.draw.rect(screen,[0,0,color],&nbsp;&nbsp;&nbsp;&nbsp;[body[1]*cell_size,body[0]*cell_size,cell_size,cell_size])`
&nbsp;&nbsp;&nbsp;&nbsp;`pygame.draw.rect(screen,[0, 0, 0],[snake[-1][1]*cell_size,snake[-1][0]*cell_size,cell_size,cell_size])`
Vykreslí jablko a hada

`text = font.render(f'score: {score}; {highscore_str}', True, (255,255,255))`
`text_rect = text.get_rect()`
`screen.blit(text,((screen_size[0]-text_rect.width)/2,screen_size[1]+(y_offset-text_rect.height)/2))`
Vypíše na spodku okna *score* a *highscore*

`if keys[pygame.K_ESCAPE]:`
&nbsp;&nbsp;&nbsp;&nbsp;`pygame.quit()`
&nbsp;&nbsp;&nbsp;&nbsp;`exit()`
Dovolí hráčovi odejít jen pomocí *esc*

`pygame.display.flip()`
Načte znovu obrazovku aby se zobrazil aktuální snímek.

`print(f"your score is {score}")`
Vypíše skóre do konsole

`f = open("highscore.txt","r")`
`highs = int(f.read().splitlines()[0])`
`if score > highs:`
&nbsp;&nbsp;&nbsp;&nbsp;`f = open("highscore.txt","w")`
&nbsp;&nbsp;&nbsp;&nbsp;`f.write(str(score))`
&nbsp;&nbsp;&nbsp;&nbsp;`f.close()`
Přečte *highscore* z dokumentu a uloží nové pokud je větší než minulé.

<br>`screen.fill((255, 0, 0))`
<br>`if win:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`screen.fill((0, 255, 0))`
<br>`text = fontdied.render(f'YOU DIED', True, (255,255,255))`
<br>`if win:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`text = fontdied.render(f'YOU WON', True, (255,255,255))`
<br>Vybarví obrazovku červenou nebo zelenou podle toho jestli hráč vyhrál a zobrazý daný text.

<br>`text_rect = text.get_rect()`
<br>`screen.blit(text,((screen_size[0]-text_rect.width)/2,400))`
<br>`text = font.render(f'score: {score}; {highscore_str}', True, (255,255,255))`

<br>`text_rect = text.get_rect()`
<br>`screen.blit(text,((screen_size[0]-text_rect.width)/2,500))`
<br>`text = fontspace.render(f'Press Backspace to start new game', True, (255,255,255))`

<br>`text_rect = text.get_rect()`
<br>`screen.blit(text,((screen_size[0]-text_rect.width)/2,600))`
<br>`text = fontspace.render(f'or Press ESC to leave the game', True, (255,255,255))`

<br>`text_rect = text.get_rect()`
<br>`screen.blit(text,((screen_size[0]-text_rect.width)/2,700))`
<br>`pygame.display.flip()`
<br>Vypíše instrukce pro další pokračování ve hře.

<br>`while  True:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`pygame.event.pump()`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`keys = pygame.key.get_pressed()`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`if keys[pygame.K_BACKSPACE]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`break`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`if keys[pygame.K_ESCAPE]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pygame.quit()`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`exit()`
<br>Umožní pustit další hru pomocí *backspace*, nebo zavřít celé okno pomocí *esc*

## Credits
<br>František Václavek - pomoc s kódem
<br>Robert Hunter Shea - pomoc s kódem
