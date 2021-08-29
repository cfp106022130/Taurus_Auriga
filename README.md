# Taurus_Auriga
###### Python scripts and observe scripts prepared for SMA project, 2021A-A010. 
The observations purpose is to constrain the spectral indices of 47 Class II protoplanetary disks in Taurus-Auriga star forming region. 
The science targets were selected from Andrews & Williams (2005) by their flux densities to achieve > 10-sigma significance in < 2 hours observing time. 
In the observing script, we want to minimize the path of observing 47 science targets and group them into 15 mins blocks with gain calibrator in the beginning and in the end. 
In a 1.5 hrs observing loop, we allocated 1.5 hrs to each target source according to the propotions of their estimated observing time in the proposal and converted the allocated time into number of scans with 15 secs in each scan.
The icrs celestial coordinate is obtained from Gaia Archive.  <br /> <br />
File 'Target.txt' lists the target name, flux density at 0.85 mm, its uncertainty, flux density at 1.3 mm, its uncertainty. All of them are measured by Andrews & Williams (2005). <br />
Python script 'plot.py' reads these flux density measurements and does 1.3 mm - 0.85 mm flux density scatter plot and their distributions. <br /> <br />
File 'Target_a.txt' lists the submillimeter spectral index (alpha), its uncertainty of the selected targets fit by Andrews & Williams (2005). <br />
Python script 'plot1.py' reads spectral index and plot cummulative distribution of alpha for the 47 science targets. <br /> <br />
File 'targetname_1.txt' lists the target name, RA, Dec, number of scans at 400 GHz, number of scans at 230 GHz in a 1.5 hrs loop. File 'targetname_2.txt' is used for naming the plot regarding 230 GHz observations. <br />
Jupyter notebook 'Coordinate.ipynb' contains 11 cells: <br /> 
1. The first cell reads the RA, Dec and plots the positions of 47 science targets using WCS coordinate generated by FT_Tau fits file from HHLI of Herschel Science Archive. <br /> 
2. The second cell is for 400 GHz observation and the third cell is for 230 GHz. 
We first divided the targets into 6 groups considering their relative positions in the first plot. 
This process was done by our personal judgement, and we wrote the target names and numbers of scans of each group in a1-a6 and s1-s6, respectively. 
Again, the cell plots the positions of targets but with different colors corresponding to different groups and the transparency corresponding to numbers of scans. <br />
3. In the fourth to seventh cell, we used the KD-tree algorithm to construct the minimun spanning tree of the 47 targets by the seperation of their celestial coordinates. 
The tree is constructed by the following steps: <br />
- First, choose a target with index **u** as the first vertex to add in the tree. <br />
- Next, use _KDTree.query_ to list the targets in ascending order of distance to the first vertex. The first element in the list (the nearest target) will be the next vertex **a** to add in the tree. <br />
- The program will draw a line on the first plot between the first vertex **u** and the next vertex **a**, which is the branch of the tree. <br />
- Add the next vertex **a** in the tree, let the variable **u** be **a** and end the first loop. The process of finding the nearest target will iterate to add vertices and branches. <br />
- When the variable **u** is iterating, if the distance between the last vertex and its nearest target is smaller than that between **u** and its nearest target, it will choose the nearest target of last vertex to be the next vertex **a** instead of the nearest target of **u**. <br />
4. Besides finding the shortest path, the scripts also group the targets such that each group has 48 scans in total in order to put them into 15 mins block. 
The loop counts the total scans that targets in the tree needs. When the total scans exceed 48, there are three kinds of condition expression in the fourth to sixth cell: <br />
- In the fourth cell, when the total scans exceed, the line plot will change color and put the next vertex in the next group. Moreover, if the target **u** in the loop is the first vertex in the group, the program will not refer to the last vertex to get another target with smaller distance branch. <br />
- In the fifth cell, when the total scans exceed, the line plot will change color but put the next vertex in the present group. The program will refer to the last two vertices to see if it can find a smaller distance branch than that of the present vertex **u**. <br />
- In the sixth cell, when the total scans exceed, the program will find the next nearest vertices to see if the scans it needs can be added into 48 scans. Then, this vertex will be the next vertex to add in the present group. When the total scans exceed and no vertex with small enough scans can be found, the line plot will change color and put the next vertex in the next group. Moreover, if the target **u** in the loop is the first vertex in the group, the program will not refer to the last vertex to get another target with smaller distance branch. <br />
5. In order to arrange the target in each 48 scans group more efficiently, the seventh cell splits > 3 scans targets into several 3 scans and their scans modulo 3. With this spliting, each target may contributes several vertices with 3 or less scans in the tree. The tree building and condition expression to seperate each group follow the sixth cell. In this spanning tree, if the scans of the next target will lead to an excess in total scans of group, its scans can be divided into two in the present group and the next group. 
6. The eighth cell is for 400 GHz observation and the nineth cell is for 230 GHz. 
We looked at the results from the seventh cell and rearranged the targets and their scans in a1-a6 and s1-s6, respectively. 
We still slightly modified the first and last target in each group to make the targets in a group more spatially compact and avoid division of a target's scans as we can. 
Again, the cell plots the positions of targets with different colors representing different groups and the transparency corresponding to numbers of scans. 
We mark the scanning order of the group beside the target with its group color and derived the geometric center of each group targets labeled with a dot. 
This time, we also considered the positions of two gain calibrators, 0510+180 and 3c111. We want the calibrator to be close enough to the geometric center (within 10 deg) and to form a cycle with the group targets in each 15 mins block. <br />
7. The tenth cell is for 400 GHz observation and the eleventh cell is for 230 GHz. 
These cells reads the groups array and the targetname file and generates the target list and observe loop written in the observing scripts. 
While, there are still some things to by ourselves: The first thing is to revise the scan time of the target with divided scans in two different groups. The second thing is to put the corrected number of scans of those divided scans targets into the observe loop. The third thing is to add calibrators between different groups when changing the calibrators in the observing loop. <br /> <br />
File 'observing_script_230GHz.txt' and 'observing_script_400GHz.txt' are the complete observing scripts generated by the SMA projects page on the website. 
