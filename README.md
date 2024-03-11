This Python script generates a dynamic list of workers with unique IDs, names, genders, and salaries. It then produces a pay slip for each worker based on their salary and gender, applying certain conditions.

Code Overview
Step 1: Generating Worker List
A list of workers is dynamically created using a loop. Each worker dictionary contains the following information:

ID: Unique identifier for the worker.
Name: Name of the worker.
Gender: Gender of the worker, determined based on the ID.
Salary: Calculated salary based on a formula using the worker's ID.
Step 2: Producing Pay Slips
For each worker in the list, a pay slip is generated. The script applies certain conditions to determine the worker's level based on their salary and gender. The conditions are as follows:

If the salary falls between $10,000 and $20,000, the worker's level is set to "A1".
If the salary falls between $7,500 and $30,000 and the worker is female, the level is set to "A5-F".
Otherwise, the worker's level is set to "Regular".
The pay slip includes the worker's name, level, and salary.
