#  Příběhy dat: Výpočetní přístupy ke studiu kultury a společnosti

---
## Autor
* Vojtěch Kaše (kase@kfi.zcu.cz; [[website](https://vojtechkase.cz)]


## License
CC-BY-SA 4.0, see attached License.md

---
# Úvod

Právě jste se ocitli na domovské stránce projektu *Příběhy dat*. Jedná se o sestavu *elektronických, 
multimediálních a interaktivních studijních opor* vytvořených pro potřeby výuky výpočetních přístupů
ke studiu kultury a společnosti na Západočeské univerzitě v Plzni. Tyto studijní byly vytvořeny primárně pro studenty
humanitního či společensko-vědního zaměření v různých stádiích studia, ale mohou v určitém ohledu posloužit i studentům 
na technických obor.  

Výpočetní přístupy ke studiu kultury a společnosti se úzce pojí s výzkumnou oblastí, které se říká *digital humanities*, 
nebo - chcete-li - digitální humanitní vědy. My zde však budeme v použití tohoto označení spíše zdrženliví,
a to z několika důvodů. Zaprvé a především, pohlédneme-li do některých významných publikací z oblasti tzv.
digital humanities (např. [^1]), zjistíme, že toto označení je značně široké a skrývá se za ním podstatně větší šíře
činností než jen využití výpočetních metod ke studiu kultury a společnosti, které zde zajímají nás. 
Podle některých autorů pod digital humanities spadá i humanitně-vědná reflexe dopadu informačních technologií na současnou 
kulturní produkci atú.

Ústředním tématem digital humanities je nepochybně *digitalizace* kulturních děl a jejich zpřístupňování široké veřejnosti.
Zde máme na mysli např. vytváření různých digitálních archivů literárních děl či online galerií výtvarného umění. V této
oblasti bylo v posledních několika dekádách vykonáno neuvěřitelně mnoho (viz např. rozsáhlý korpus historických tisků 
od společnosti Google) a tento vývoj bude nepochybně pokračovat. 

Těmito digitalizačními projekty však digital humanities ani zdaleka nekončí. Naopak, s veřejně dostupnými 
digitalizovanými reprezentacemi kulturních artefaktů se před námi otevírá obrovské pole možností, jak s těmito daty 
dále nakládat. A zde je třeba si nejprve uvědomit, že například digitalizovaná kniha nemá pouze tu výhodu, 
že může být čtena odkudkoli na světě. Ale také tu, že může být v jistém smyslu "čtena" počítačem, neboli výpočetně
analyzována. Význam této skutečnosti vysvytne, když si uvědoméme, že takových digitalizovaných knih je dnes 
k dispozici nepřeberné množství, rozhodně více, než je v silách člověka za celý život přečíst. Oproti tomu, dnešní 
osobní počítač nemá problém během vteřin prohledat textové soubory čítající stamilióny slov. Obdobné platí pro 
rozsáhlé audiovizuální soubory či rozsáhlé datasety digitalizovaných výtvarných děl. 

Efektivní prohlédávání  je nejspíš tou nejběžnější činností, kterou si představíme, že můžeme jako 
humanitní vědci s rozsáhlými digitalizovanými a veřejně zpřístupněnými kulturními datasety za pomoci počítače dělat.
I to je však pouze začátek. Dalším krokem jsou různé kvantitativní analýzy těchto dat, například hledání určitých 
formálních či obsahových podobností mezi jednotlivými texty či zkoumání vývojových či prostorových trendů. 
Zde již není středobodem našeho zájmu samotná digitalizace a dostupnost příslušných datových souborů, ale potenciál 
výpočetních metod pro jejich analýzu. Namísto *digital humanities* proto v tomto kontextu někteří badatelé raději 
používají termíny jako jsou *computational humanities* či *cultural analytics*. Jelikož měřítko těchto analýz 
je často výrazně větší než v případě tradičních humanitních věd, které se často zaměřují na interprataci kulturního jednání 
jednotlivců, tyto přístupy se současně překrývají i s tzv. *computational social science*. 

Tím se již dostáváme ke stanovení hlavních cílů tohoto souboru interaktivních studijních opor. 
Je jím na jedné straně (1) *prohloubení badatelské imaginace* studenta humanitního zaměření o možnost využití 
výpočetních metod pro práci s kulturními data a (2) *praktické osvojení si* základních konceptů digitalizace těchto
dat. Tyto dva cíle jsou úzce provázané. Ukazuje se totiž, že právě nedostatek toho, co zde nazýváme
*badatelskou imaginací* v oblasti výpočetních metod, mezi tvůrci digitalizovaných kulturních dat je důvodem pro to, 
proč některé digitalizační projekty neumožňují tak široké využití jimi zpřístupněných dat, jaké by mohly. Problémem je, 
že bez představy o tom, jak by bylo možné daná data analyticky využít, jsou během digitalizace a zpřístupňování 
často učiněna  zdánlivě nevinná rozhodnutí, která následně badatelům využívajícím výpočetní metody značně stěžují 
práci - příklady těchto rozhodnutí si v jednotlivých studujních oporách opakovaně ukážeme.  
Jelikož tvůrci digitalizovaných dat působící například jako pracovníci v institucích péče o kulturní dědictví 
jsou typicky absolventy humanitních oborů, jsou studenti těchto oborů přirozenou
cílovou skupinou pro osvojování si těchto znalostí a dovedností.

Tento soubor učebních opor je nazván "Příběhy dat". Již mnoho historiků si povšimlo, že v jádru práce historika není pouze 
*zjistit*, co a jak se skutečně stalo ("Wie es eigentlich gewesen," jak pravil klasik), ale také to sdělit ostatním. 
Toto sdělení má formu vyprávění (na rozdíl od přírodních věd, kde je možné podat vysvětlení i prostřednictvím určitého 
formálního vyjádření). Má-li tedy humanitní badatel analyzující kulturní data za využití výpočetních metod
učinit za dost tomuto poslání, neměl by zapomenout podat své závěry ve formě vyprávění či příběhu. -> Datová žurnalistika.

Další důležitou lekcí, kterou si zde osvojíme, je, že v našem případě neexistuje nic takového jako "syrová data" 
("Raw data is an oxymoron", hlásá název jednoho známé studie [^]). Za každými daty se skrývá určitý model, soubor 
určitých teoretických předpokládů, které rozhodly o tom, že daný jev je zde reprezentován tímto a ne jiným způsobem.

Formát

Programování 

Kapitoly:
"Tušíme kdy, aneb časové nejistotě nazdory"
"Digitální edice"





[^1]: Debates in the digital humanities 2023. (2023). University of Minnesota Press. https://dhdebates.gc.cuny.edu/projects/debates-in-the-digital-humanities-2023
[^2]: Archiv Jana Patočky. https://archiv.janpatocka.cz/items/browse
