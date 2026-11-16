# Calorie Tracker – Kaloriju uzskaites programma

## 1. Projekta apraksts

Calorie Tracker ir vienkārša programma, kas palīdz uzskaitīt kalorijas un saglabāt informāciju par lietotāju, produktiem un svaru.

Ar šo programmu var:
- Pievienot jaunus lietotājus.
- Saglabāt pārtikas produktus un to kaloriju daudzumu.
- Apskatīt dažādas datubāzes tabulas.
- Reģistrēt lietotāja svaru.
- Apskatīt informāciju par maltītēm un vingrojumiem.

Programma ir paredzēta cilvēkiem, kuri vēlas ērti saglabāt un apskatīt savu informāciju vienuviet.

## 2. Nepieciešamās lietas

Lai izmantotu programmu, nepieciešams:
- Dators ar Windows operētājsistēmu.
- Instalēta Python programma.
- Projekta faili.
- Datubāzes fails, kurā tiek glabāta informācija.

## 3. Instalēšana

Lai sāktu izmantot programmu:

1. Lejupielādē vai saglabā projekta failus datorā.
2. Pārliecinies, ka datorā ir instalēts Python.
3. Pārliecinies, ka visi projekta faili atrodas vienā mapē.
4. Atver projekta mapi programmā Visual Studio Code.
5. Atver termināli.

Papildu bibliotēkas nav nepieciešams instalēt, jo programma izmanto Python iebūvētās bibliotēkas.

## 4. Programmas palaišana

Lai palaistu programmu:

1. Atver projekta mapi.
2. Atver termināli.
3. Ieraksti komandu:

```bash
python main.py
```

Pēc palaišanas atvērsies programmas galvenais logs.

## 5. Kā lietot programmu?

Programmas galvenajā logā ir vairākas pogas:

- **Skatīt lietotājus** – parāda reģistrētos lietotājus un viņu informāciju.
- **Pievienot lietotāju** – ļauj ievadīt e-pastu, vārdu un ikdienas kaloriju mērķi.
- **Skatīt produktus** – parāda saglabātos pārtikas produktus.
- **Pievienot produktu** – ļauj pievienot jaunu produktu un norādīt tā kaloriju daudzumu uz 100 gramiem.
- **Skatīt vingrojumus** – parāda informāciju par vingrojumiem.
- **Skatīt svara žurnālu** – parāda iepriekš reģistrēto svaru.
- **Reģistrēt svaru** – ļauj ievadīt lietotāja ID un svaru kilogramos.
- **Skatīt maltītes** – parāda saglabātās maltītes.
- **Skatīt citas tabulas** – ļauj apskatīt arī pārējās datubāzes tabulas.
- **Iziet** – aizver programmu.

## 6. Datubāze

Programmā tiek izmantota SQLite datubāze.

Datubāzes faila nosaukums ir `calorie_tracker.db`.

Tajā tiek saglabāta informācija par:
- Lietotājiem.
- Produktiem.
- Produktu kategorijām.
- Vingrojumiem.
- Lietotāju mērķiem.
- Svara ierakstiem.
- Maltītēm.

Ievadītā informācija tiek saglabāta datubāzē, tāpēc, aizverot programmu, iepriekš saglabātajiem datiem vajadzētu palikt pieejamiem.

## 7. Izmantotās tehnoloģijas

Projektā izmantotas šādas tehnoloģijas:

- **Python** – programmēšanas valoda, kurā izveidota programma.
- **Tkinter** – izmantots, lai izveidotu programmas logus, pogas un ievades laukus.
- **SQLite** – izmantots datu saglabāšanai un uzglabāšanai.
- **SQL** – izmantots, lai pievienotu un apskatītu informāciju datubāzē.

## 8. Projekta mērķis

Projekta mērķis ir izveidot vienkāršu un saprotamu kaloriju uzskaites programmu, kurā lietotājs var pievienot, saglabāt un apskatīt dažādu informāciju.

Programmas galvenā priekšrocība ir tā, ka visa informācija ir pieejama vienā vietā un to var ērti apskatīt, izmantojot vienkāršas pogas.

## 9. Licence

Visas tiesības uz šo projektu un tā pirmkodu pieder projekta autoram. Projekta izmantošana, kopēšana vai izplatīšana bez autora atļaujas nav atļauta.