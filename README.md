# Closed Loop-Kompensation in der Schleifbearbeitung

## 1.1   Definition Profilkompensation und Closed Loop

Die **Profilkompensation** korrigiert geschliffene Formelemente (Walzwerkzeuge, Stechplattenprofile, Formfräserprofile, …) oder erzeugte Geometrieelemente (Nutsteigungsverläufe, …). In der Regel wird der Schlichtpfad kompensiert, welcher zuvor mit Punktkontakt zwischen Schleifscheibe und Werkstück geschliffen wurden.      
Die Profilkompensation beim Einstechschleifen mit Profilscheiben ist geometrisch nicht möglich, weil hier ein Linienkontakt vorliegt. Alternativ kann hier der Abrichtprozess kompensiert werden, sofern dieser mit Punktkontakt stattfindet.

![puntk_linienkontakt.png](puntk_linienkontakt.png)

Die Profilerfassung zur Kompensation erfolgt typischerweise immer auf einer Messmaschine, wäre aber prinzipiell auch auf der Schleifmaschine möglich. Der Begriff **Closed Loop** in der Systemtechnik bedeutet, dass in diesem Fall die Messung in einem geschlossenen Kreislauf zur Kompensation zurückgeführt wird.    
Adelbert Haas verwendet den Begriff Closed Loop ausschließlich im Falle der Profilkompensation und nicht für die Kompensation einzelner Werkstückparameter (Durchmesser, Steigung, Winkel, etc.). Im systemtechnischen Sinn ist dies auch als Closed Loop Kompensation zu sehen und wird von anderen Maschinenhersteller auch in diesem Sinne verwendet.     

## Technische Realisierung der Profilkompensation

### *.json-File

* Schleifsoftware Horizon schreibt Nominal/Solldaten zur Messung für nachfolgende Kompensation
* Messmaschine hängt bei Bedarf (Automation/Bediener fordert an) Actual/Messresultat an Sollfile an.
* Einheitliche Beschreibung des kompensierten Werkstücks im gleichen File. 
* File Flexibel für Metadaten und Für Nutzer interpretierbar -> **json** ist das Format der Wahl
* Das File kann initial durch die Schleifsoftware geschrieben werden. Alternativ wird es eingelesen (nur Einfachkompensation). 
* Format muss erweiterbar (versioniert) sein.

### Messung

* Nominaldaten werden über Punkte und zugehörige Normalenvektoren in Werkstückkoordinaten definiert. 
  * i.d.R. über X/Y-Koordinate
  * i.d.R ist dabei ein Abstand von 0.02 mm vorgewählt.
  * wiederholte (doppelte) Eineindeutige Punkte  können vorkommen
* Messwerte werden an jedem Punkt als Abweichung (Soll-Ist) in Normalenrichtung zurückgegeben.
  * i.d.R. muss dabei eine Einpassung stattfinden. 

