# Closed Loop-Kompensation in der Schleifbearbeitung

## 1.1   Definition Profilkompensation und Closed Loop

Die **Profilkompensation** korrigiert geschliffene Formelemente (Walzwerkzeuge, Stechplattenprofile, Formfräserprofile, …) oder erzeugte Geometrieelemente (Nutsteigungsverläufe, …). In der Regel wird der Schlichtpfad kompensiert, welcher zuvor mit Punktkontakt zwischen Schleifscheibe und Werkstück geschliffen wurden.      
Die Profilkompensation beim Einstechschleifen mit Profilscheiben ist geometrisch nicht möglich, weil hier ein Linienkontakt vorliegt. Alternativ kann hier der Abrichtprozess kompensiert werden, sofern dieser mit Punktkontakt stattfindet.

![puntk_linienkontakt.png](puntk_linienkontakt.png)

Die Profilerfassung zur Kompensation erfolgt typischerweise immer auf einer Messmaschine, wäre aber prinzipiell auch auf der Schleifmaschine möglich. Der Begriff **Closed Loop** in der Systemtechnik bedeutet, dass in diesem Fall die Messung in einem geschlossenen Kreislauf zur Kompensation zurückgeführt wird.    
Adelbert Haas verwendet den Begriff Closed Loop ausschließlich im Falle der Profilkompensation und nicht für die Kompensation einzelner Werkstückparameter (Durchmesser, Steigung, Winkel, etc.). Im systemtechnischen Sinn ist dies auch als Closed Loop Kompensation zu sehen und wird von anderen Maschinenhersteller auch in diesem Sinne verwendet.     

## 1.2 Potentiale und Voraussetzungen

<Haas Intern>

## 2. Technische Realisierung der Profilkompensation

Der ClosedLoop zur Profilkompensation wird über einen File-basierten Austausch ermöglicht. Schleifmaschine (Schleifsoftware) und Messmaschine Schreiben für eine Kompensation ein *.Json-File welches nachfolgend erläutert wird.

Auf den Austauschordner greifen beide Schleif- und Messsoftware zu. Die Schleifsoftware schreibt die Nominalwerte. Und liest *sofern vorhanden* Actualwerte ein. Die Messmaschine liest die Nominalwerte und schreibt für jede erfolgreiche Messung die Actualwerte in das Json-File.

### 2.1 *.json-File

* Schleifsoftware Horizon schreibt Nominal/Solldaten zur Messung für nachfolgende Kompensation
* Messmaschine hängt bei Bedarf (Automation/Bediener fordert an) Actual/Messresultat an Sollfile an.
* Einheitliche Beschreibung des kompensierten Werkstücks im gleichen File. 
* File Flexibel für Metadaten und Für Nutzer interpretierbar -> **json** ist das Format der Wahl
* Das File kann initial durch die Schleifsoftware geschrieben werden. Alternativ wird es eingelesen (nur Einfachkompensation).
* Format muss erweiterbar (versioniert) sein.
* FileName entspricht dem Produktname > Leerzeichen und Umlaute sind möglich!

### 2.2 Messung

* Nominaldaten werden über Punkte und zugehörige Normalenvektoren in Werkstückkoordinaten definiert. 
  * i.d.R. über X/Y-Koordinate
  * i.d.R ist dabei ein Abstand von 0.02 mm vorgewählt.
  * wiederholte (doppelte) Eineindeutige Punkte  können vorkommen. (Info: Wird mit zukünftiger Version der Schleifsoftware vorausichtlich entfallen)
* Messwerte werden an jedem Punkt als Abweichung (Soll-Ist) in Normalenrichtung zurückgegeben.
  * i.d.R. muss dabei eine Einpassung stattfinden. 

### 2.3 Optionen

* Falls ein File im Ordner Existiert, und die Sollpunkte von den Istpunkten abweichen (z.B. weil Tesselation geändert/ kontur geändert) gibt die Schleifsoftware einen Fehler mit Option das File neu zu schreiben (vorhandene Korrekturen werden dann überschrieben (!) <> Die Nominaldaten müssen vor Jeder Messung Geschrieben werden.
* <Interrn>: wenn kein Nominal vorhanden, kann die Messmaschine auch Nominal über ein eingeladenes Messfile Interpolieren. Dann ist aber nur eine Korrektur möglich. alternativ kann hier das "einfache" 6/7-Spalten Format verwendet werden.
* Wenn 2d Konturen gehandhabt werden sollte das Profil diese Werte auswerten können. 3D geht auch, ich muss aber die Info immer mitziehen.

### 2.4 Designfragen: 

* Um Probleme mit Datenkonvertierung zu vermeiden ist eine Vergleichstoleranz von 7 Nachkommastellen sinnvoll. Gerechnet wird aber auf den Normalen.
* Auf Werte `Infinity` / `NaN` wird Verzichtet, obwohl es sinnvoll wäre. [[rfc4627](https://www.rfc-editor.org/rfc/rfc4627.txt)](https://www.rfc-editor.org/rfc/rfc4627.txt)
* `id` der Punkte wird mit angegeben, für Menschliche Lesbarkeit und Fehlersuche
* zusammengehörige Daten werden immer gewährleistet. Deshalb wurde das Konzept "wenn werte sich nicht ändern, müssen Listenelemente nicht geschrieben werden" verworfen (*referenz*: Json aus SinucomNC-Trace). 
* Größe der Dateien ist kein großes Problem, mein Python-Skrip (interpreter-Sprache) liest die Datei in 0.04s, schreiben dauert 0.04 -> Die Libs sind darauf optimiert. Auch Tests mit Schleifsoftware und 400 Profilmessung zeigt keine Probleme. 

### 2.5 Elemente: Objects/Arrays/Numbers/Strings

* Siehe json-Schema.

## 3. Altes Austauschformat

<Haas Intern>
