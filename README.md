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
<br>`screen_size_pixels = 900` 
<br>Nastavení velikosti obrazu hry v pixelech

<br>`font_multiplier = screen_size_pixels/1000`
<br>Vydělí velikost okna, tak aby se velikost písma poupravila

<br>`screen_size = (screen_size_pixels, screen_size_pixels)`
<br>Nastaví velikost okna, aby to vždy byl čtverec a stačilo zadat rozměr jen jednou

<br>`y_offset = 100*font_multiplier`
<br>Nastaví spodní odrážku pro výpis *score* podle velikosti okna

<br>`screen = pygame.display.set_mode((screen_size[0],screen_size[1]+y_offset))`
<br>Dopočítá velikost okna i s odrážkou

<br>`font = pygame.font.Font('MINECRAFT.otf', int(70*font_multiplier))`
<br>`fontdied = pygame.font.Font('MINECRAFT.otf', int(100*font_multiplier))`
<br>`fontspace = pygame.font.Font('MINECRAFT.otf', int(40*font_multiplier))`
<br>Spočítá všechny velikosti fontů, tak aby se při *Death screenu* velikosti mohli lišit

<br>`speed = int(input("speed: ")) `
<br>`cells = int(input("cells: "))`
<br>`print("Press 'alt + tab'")` 
<br>`time.sleep(5)`

### Hlavní cyklus pro opakování hry 
Vezme vstupy od uživatele pro rychlost hada a počet políček. Naviguje jak postupovat dál a čeká 5 sekund než se spustí hra.

<br>`direction = (0,1)`
<br>`old_direction = (0,1)`
<br>Nastaví směr doprava

<br>`clock = pygame.time.Clock()`
<br>Nastaví proměnnou, aby se dále jednodušeji dalo nastavovat jak často se obrazovka bude obnovovat

<br>`score = 0`
<br>Vyresetuje score

<br>`max_len = cells*cells`
<br>Spočítá jak dlouhý musí být had, aby hráč danou hru vyhrál

<br>`apple = [random.randint(0,cells-1),random.randint(0,cells-1)]`
<br>Vygeneruje náhodnou pozici jablka pro začátek hry

<br>`snake = [[1,1]]`
<br>Nastaví první pozici hada doprava nahoru jedno políčko od obou stěn.

<br>`cell_size = screen_size[0]/cells`
<br>Spočítá jak velké bude každé políčko podle velikosti desky a počtu políček zadaným hráčem

<br>`background = pygame.Surface(screen_size)`
<br>`background.fill((6, 189, 36))`
<br>Vybarví herní plochu

<br>`for y in  range(cells):`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`for x in  range(cells):`
<br>	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if (x+y) % 2  ==  0:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pygame.draw.rect(background,[17, 140, 37],			[x*cell_size,y*cell_size,cell_size,cell_size])`
<br>Spočítá a vykreslí, kde mají být políčka jiné barvy pro vytvoření šachovnice

<br>`f = open("highscore.txt","r")`
<br>`highs = int(f.read().splitlines()[0])`
<br>`if highs >  0:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`highscore_str = f"highscore: {highs}"`
<br>`else:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`highscore_str = ""`
<br>najde *highscore* v souboru a zjistí pokud je větší než nula.

<br>`running = True`
<br>`movecount = speed`
<br>Nastaví další proměnné pro běh cyklu hry a rychlosti

### Cyklus jednotlivých pokusů

<br>`clock.tick(120)`
<br>Nastaví kolikrát za sekundu se obrazovka obnoví

<br>`framerate = clock.get_fps()`
<br>`for event in pygame.event.get():`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`if event.type == pygame.QUIT:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
<br>Zajistí aby se dalo ze hry odejít aniž by hra crashovala

<br>`keys = pygame.key.get_pressed()`
<br>`if keys[pygame.K_UP] or keys[pygame.K_w]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`direction = (-1,0)`

<br>`if keys[pygame.K_DOWN] or keys[pygame.K_s]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`direction = (1,0)`

<br>`if keys[pygame.K_LEFT] or keys[pygame.K_a]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`direction = (0,-1)`

<br>`if keys[pygame.K_RIGHT] or keys[pygame.K_d]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`direction = (0,1)`
<br>Bere vstup z klávesnice a mění podle toho směr jízdy hada.

<br>`if old_direction != direction and old_direction[0] + direction[0] ==  0:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`direction = old_direction`
<br>Znemožní otočit hada o 180° na jednou.

<br>`if movecount ==0:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`old_direction = direction`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`new_y = snake[-1][0] + direction[0]`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`new_x = snake[-1][1] + direction[1]`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`new_body = [new_y,new_x]`
<br>Posune hada po uběhlém čase nastaveném před zapnutím hry.

<br>`if snake[-1][0] >= cells or snake[-1][1] >= cells:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`continue`

<br>`if snake[-1][0] <  0  or snake[-1][1] <  0:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`continue`
<br>Zjistí pokud had je mimo hrací plochu. Pokud ano hru přeruší.

<br>`if apple == new_body:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`score += 1`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`!if  len(snake)+1>=max_len:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`win = True`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("you won")`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`continue`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`else:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`while apple in snake+[new_body]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`apple = [random.randint(0,cells-<br>1),random.randint(0,cells-1)]`
<br>`else:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`snake.pop(0)`
<br>`if new_body in snake:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`running = False`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`continue`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`snake.append(new_body)`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`movecount = speed`
<br>Připočte bod pokud had snědl jablko. 
<br>Ukončí hru pokud had dosáhl maximální délky podle velikosti hracího pole a zaručí s´že se ukáže <br>*win screen* místo *death screen*.
<br>Přidá nové jablko pokud had nedosáhl maximální délky.
<br>Zničí poslední políčko těla hada.
<br>Zajistí že hra se vypne pokud had nabourá sám do sebe.

<br>`else:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`movecount -= 1`
<br>Odečte jedna od počtu uběhlých snímků za poslední sekundu aby se cyklus opakoval správně.

<br>`screen.blit(background,(0,0))`
<br>`pygame.draw.rect(screen,[227, 7, 14],[apple[1]*cell_size,apple[0]*cell_size,cell_size,cell_size]`
<br>`for i,body in  enumerate(snake[:-1]):`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`color = abs(255-(255/len(snake)*i))`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`pygame.draw.rect(screen,[0,0,color],&nbsp;&nbsp;&nbsp;&nbsp;[body[1]*cell_size,body[0]*cell_size,cell_size,cell_size])`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`pygame.draw.rect(screen,[0, 0, 0],[snake[-1][1]*cell_size,snake[-1][0]*cell_size,cell_size,cell_size])`
<br>Vykreslí jablko a hada

<br>`text = font.render(f'score: {score}; {highscore_str}', True, (255,255,255))`
<br>`text_rect = text.get_rect()`
<br>`screen.blit(text,((screen_size[0]-text_rect.width)/2,screen_size[1]+(y_offset-text_rect.height)/2))`
<br>Vypíše na spodku okna *score* a *highscore*

<br>`if keys[pygame.K_ESCAPE]:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`pygame.quit()`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`exit()`
<br>Dovolí hráčovi odejít jen pomocí *esc*

<br>`pygame.display.flip()`
<br>Načte znovu obrazovku aby se zobrazil aktuální snímek.

<br>`print(f"your score is {score}")`
<br>Vypíše skóre do konsole

<br>`f = open("highscore.txt","r")`
<br>`highs = int(f.read().splitlines()[0])`
<br>`if score > highs:`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`f = open("highscore.txt","w")`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`f.write(str(score))`
<br>&nbsp;&nbsp;&nbsp;&nbsp;`f.close()`
<br>Přečte *highscore* z dokumentu a uloží nové pokud je větší než minulé.

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
