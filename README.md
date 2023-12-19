# PComp

# 1. Closed Loop-compensation in Profile Grinding

This repository describes the procedure and the exchange format for profile compensation (closed loop).
The Json format is documented via a Json schema and tested for validity. 

## 1.1 Definition of Profilcompensation and Closed Loop

Profile compensation corrects ground form elements (rolling tools, profiled inserts, form cutter profiles, ...) or generated geometry elements (flute profil shcape, ...). In general, the finishing path that was previously ground with point contact between the grinding wheel and the workpiece is compensated. 
Profile compensation for plunge-cut grinding with profile wheels is not geometrically possible. The present line contact prevents this. Alternatively, the dressing process can be compensated, assumed it takes place with point contact.


![punkt_linienkontakt.png](punkt_linienkontakt.png)

Profile acquisition for compensation is typically carried out on a measuring machine, but in principle would also be possible on the grinding machine. The term **closed loop** means that in this case the measurement is fed back to the compensation in a closed loop.
Adelbert Haas uses the term closed loop exclusively in the case of profile compensation and not for the compensation of individual workpiece parameters (diameter, pitch, angle, etc.). In terms of system technology, this can also be seen as closed loop compensation and is also used in this sense by other machine manufacturers.

## 1.2 Potential and prerequisites

<Haas Intern>

## 2. Technical realization of profile compensation

The closed loop for profile compensation is enabled by a file-based exchange. The grinding machine (grinding software) and measuring machine (measuring software) write a *.Json file for compensation, which is explained here.
Both software accesses an exchange folder on the customer server, grinding machine or measuring machine. The grinding software writes the nominal values and reads *if available* actual values. The measuring machine reads the nominal values and then measures accordingly. The actual values are written to the Json file for each successful measurement.

### 2.1 *.json-File

* Horizon grinding software writes the file and the NominalValues object for measurement for subsequent compensation.
* Measuring machine appends AcutalValues (result) to the Object if required (automation/operator requests).
* The objective is the uniform description of the compensated workpiece in the same file.
* **json** is the format of choice, because Data and Metadata can be stored and accessed by human and machine 
* The file can initially be written by the grinding software. Alternatively, it can be read in (single compensation only).
* Format is expandable (versioned).
* FileName corresponds to the product name > Spaces and German Umlauts are possible!

### 2.2 Measurment

* Nominal data is defined via points and associated normal vectors in workpiece coordinates. 
  * usually via X/Y coordinates
  * usually, an Euclidean distance of 0.02 mm is preselected.
  * Repeated (double) unique points can occur before Grinding Software version 1_39. 
* Measured values are returned at each point as a deviation (nominal/actual) in the normal direction.
  * usually, an fitting must be made. 

### 2.3 Options

* If a file exists in the folder and the nominal points deviate from the actual points, the grinding software issues an error with the option to rewrite the file. Existing corrections are then overwritten <> The nominal data must be written before each measurement.
<Intern>: if no nominal is available, the measuring machine can also interpolate nominally via a loaded measurement file. Alternatively, the "simple" 6/7-column format can be used here.
* If 2d contours are handled, the profile should be able to evaluate these values. 3D also works, but I always have to drag the info along.

### 2.4 Desing issues 

* To avoid problems with data conversion, a comparison tolerance of 7 decimal places is used. However, the calculation is based on the normal directions.
* Values `Infinity` / `NaN` are not used, although it would make sense. [[rfc4627](https://www.rfc-editor.org/rfc/rfc4627.txt)](https://www.rfc-editor.org/rfc/rfc4627.txt)
* `id` of the points is included, for human readability and troubleshooting
* Related data is always guaranteed. Therefore the concept "if values do not change, list elements do not have to be written" has been discarded (*reference*: Json from SinucomNC trace). 
* Size of the files is not a big problem, my Python script (interpreter language) reads the file in 0.04s, writing takes 0.04 -> the libs are optimized for this. Tests with grinding software and 400 profile measurement also show no problems.

### 2.5 Elements: Objects/Arrays/Numbers/Strings

* see on descriptions in json-Schema.

## 3. Old exchange format

<Haas Intern>
