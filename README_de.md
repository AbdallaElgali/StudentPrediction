# Schülervorhersage

## Übersicht
Das Projekt verwendet ein lineares Regressionsmodell, um die Abschlussnoten von Schülern basierend auf verschiedenen Merkmalen vorherzusagen.

## Projektstruktur
Das Projekt besteht aus den folgenden Dateien:

main.py: Das Haupt-Python-Skript, das die Implementierung des Jobvermittler-Modells enthält.
student-mat.csv: Der Datensatz enthält Informationen zu Schülern, einschließlich Noten, Lernzeit, Fehlzeiten und Misserfolgen.
studentmodel.pickle: Eine serialisierte Version des trainierten linearen Regressionsmodells.


## Verwendung
  
1. Öffnen Sie ein Terminal oder eine Befehlszeile und navigieren Sie zum Projektverzeichnis.
2. Führen Sie den folgenden Befehl aus, um das Programm auszuführen:

python main.py
  
3. Das Programm lädt den Datensatz, trainiert das lineare Regressionsmodell und gibt die Genauigkeit des Modells auf den Testdaten aus.
4. Das trainierte Modell wird in der Datei studentmodel.pickle gespeichert.

## Abhängigkeiten
Das Projekt erfordert die folgenden Abhängigkeiten:

pandas
numpy
scikit-learn
matplotlib
  
## Daten
Der für das Training und die Testung des Modells verwendete Datensatz wird in der Datei student-mat.csv gespeichert. Er enthält die folgenden Spalten:

- G1: Note im ersten Zeitraum
- G2: Note im zweiten Zeitraum
- G3: Abschlussnote (Zielvariable)
- studytime: Wöchentliche Lernzeit (1-4)
- absences: Anzahl der Fehlzeiten
- failures: Anzahl der vorherigen Klassenausfälle
  
## Modellbewertung
Die Leistung des Modells wird anhand des Bestimmtheitsmaßes (R^2-Score) bewertet. Je näher der R^2-Score bei 1 liegt, desto besser passt das Modell zu den Daten.

## Mögliche Verbesserungen
Hier sind einige potenzielle Bereiche für zukünftige Verbesserungen:

Untersuchung verschiedener Machine Learning-Algorithmen und Vergleich ihrer Leistung.
Durchführung von Merkmalsextraktion, um zusätzliche aussagekräftige Merkmale zu generieren.
Durchführung einer Hyperparameteroptimierung, um die Leistung des Modells zu optimieren.
Verbesserung der Visualisierung der Ergebnisse.
