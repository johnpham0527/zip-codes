# zip-codes
I have created Python scripts to obtain the ZIP code of a given list of public schools using the API for Google Maps.

Purpose:
The codes in this repository takes a name of a public school in Queens, NY and returns the ZIP code from the resulting JSON data

Known Bugs:
1. The following schools produce an "IndexError: list index out of range error" when querying Google Maps:
       A.C.E. Academy for Scholars at the Geraldine Ferra
       P.S. 173 Fresh Meadows
       P.S. 051
       M.S. 053 Brian Piccolo
       Goldie Maple Academy
       P.S. 144 Col Jeromus Remsen
       P.S. 228 Early Childhood Magnet School of the Arts
2. A ZIP code cannot be found for some schools.
3. The CSV Writer sometimes outputs an extra line break in the cell. When the CSV file is opened in Excel, it makes it look as if the cell is empty.
