TA3 Disaster Response CBR System

What this project is about
--------------------------
This project implements a simple Case-Based Reasoning (CBR) system for a
Disaster Response Decision Support System. The program uses previous disaster
cases to solve a new disaster problem.

The program demonstrates the four CBR stages:

1. Case representation - disaster problems and solutions are stored as Python
   dictionaries.
2. Similarity assessment and retrieval - the new disaster is compared with
   stored cases using weighted similarity scores. The highest-scoring case is
   retrieved.
3. Case adaptation - the retrieved response plan is adjusted for the new
   population, severity, and road conditions.
4. Learning or retention - the new problem and adapted solution are saved as
   Case C004 in cases.json.

Files in this folder
--------------------

disaster_cbr.py
    The Python program.

cases.json
    The retained case base. It contains the original cases and the new case
    saved by the program.

TA3_Sabulao_Roces.pdf
    The submission document containing the code, short documentation,
    screenshots, and pair reflection.

images/
    Source screenshots used in the PDF.

How to run the program
----------------------

1. Open PowerShell.
2. Change to this folder:

   cd "C:\Users\Msi\Documents\School\CS elective\TA3"

3. Run the program:

   python disaster_cbr.py

   If that command does not work, use:

   py disaster_cbr.py

What the program displays
-------------------------

The output displays:

- The new disaster problem
- The retrieved similar case
- The similarity score
- The adapted evacuation solution
- Confirmation that the new case was retained
- The updated case base

Expected test scenario
----------------------

Disaster type: flood
Severity: 5
Affected population: 22000
Rainfall: 390 mm
Road access: blocked

Expected result
---------------

The program should retrieve Case C002, produce a similarity score of about
0.968, increase the response to 10 rescue teams and 5 water trucks, recommend
full emergency evacuation using alternate routes, and retain the new case as
Case C004.

Submission checklist
-------------------

[ ] disaster_cbr.py is included.
[ ] TA3_Sabulao_Roces.pdf is included.
[ ] The PDF contains the short documentation.
[ ] The PDF contains the program screenshots.
[ ] The PDF contains the pair reflection.
[ ] Both pair members' names are correct in the PDF.
[ ] cases.json may be included as supporting data.
