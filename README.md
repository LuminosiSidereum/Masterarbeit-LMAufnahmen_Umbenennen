# Bild-Umbenennungstool für Lichtmikroskop-Aufnahmen

## Funktionsweise
Dieses Skript passt die Dateinamen von **Lichtmikroskop-Aufnahmen** an, sodass sie einem festgelegten Namensstandard entsprechen.  
Die Umbenennung erfolgt auf Basis des ersten Blocks des ursprünglichen Dateinamens und einer fortlaufenden Nummerierung.  

Das Skript verarbeitet alle `.tif`-Dateien in den Verzeichnissen:  
- **aufnahmen/**  
- **aufnahmen/Plain/**  

## Nutzung des Skripts
### Eingabedaten
- Das Skript erwartet `.tif`-Dateien in den oben genannten Verzeichnissen.  
- Die ursprünglichen Namen enthalten Blöcke, die durch **"_"** getrennt sind.  
- Die neuen Namen setzen sich aus dem ersten Block des alten Namens und einer durchnummerierten ID zusammen.  

### Ausführung
1. Stelle sicher, dass sich die Bilder in den Verzeichnissen **"aufnahmen/"** oder **"aufnahmen/Plain/"** befinden.  
2. Starte das Skript `umbenennen.py`.  
3. Die Bilder werden nach folgendem Muster umbenannt:  
    Alter Name: ProbeA_12345.tif
    Neuer Name: ProbeA_0.tif
    (Die fortlaufende Nummerierung basiert auf der Reihenfolge im Verzeichnis.)  

### Ausgabe
- Die `.tif`-Dateien werden mit neuen Namen gespeichert.  
- Die ursprüngliche Struktur bleibt erhalten, nur die Nummerierung wird angepasst.  
