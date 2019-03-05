# zip-codes
I have created Python scripts to obtain the ZIP code of a given list of schools or libraries using the API for Google Maps.

Purpose:
The codes in this repository takes a name of a public school or library in Queens, NY and returns the ZIP code from the resulting JSON data

Known Bugs:
1. The following schools produce an "IndexError: list index out of range error" when querying Google Maps:
       A.C.E. Academy for Scholars at the Geraldine Ferra
       P.S. 173 Fresh Meadows
       P.S. 051
       M.S. 053 Brian Piccolo
       Goldie Maple Academy
       P.S. 144 Col Jeromus Remsen
       P.S. 228 Early Childhood Magnet School of the Arts
2. A ZIP code cannot be found for some schools
3. The CSV Writer sometimes outputs a blank in place of a school name
The reason for this error is because Google Maps can't find the school name as it is spelled or written
