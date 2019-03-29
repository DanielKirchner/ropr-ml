Dieses Repository enthält die Scripts und Rohdaten zur Arbeit:

*Projekt Robotik - Machine Learning basierte Authentifizierung mit Hilfe einer Microsoft Kinect*

## Verwendung
### 0. Kinect-Daten
Die Rohdaten der Kinect können mit einem auf Anfrage an daniel97k@gmail.com herausgegebenen Python Skript in die in **1.** verwendete Struktur gebracht werden.
### 1. Rohdaten
Rohdaten im Verzeichnis `raw_data/` in folgender Struktur ablegen:
```
raw_data/
  person1/
    position1/
      output.txt
    position2/
      output.txt
  person2/
    ...
```
### 2. Ausführen
- Für ein SVM-gestütztes Modell: `python svm.py`
- Für ein Decision-Tree-gestütztes Modell: `python tree.py`
- Zur visuellen Darstellung der Rohdaten: `python draw_person.py` (Anpassen des Pfades in Zeile 5 beachten)
