# Project Title: Gene Regulatory Network Modeling (Biological Graph Models)

## Description
This project is a component of the Discrete Mathematics Spring 2026 course. It utilizes Graph Theory to model and simulate biological pathways, specifically the "Central Dogma" of molecular biology—the flow of genetic information from DNA to protein. The program represents molecular entities (Transcription Factors, Promoters, Genes, mRNA) as vertices and biochemical transitions as directed edges. It implements a manual Breadth-First Search (BFS) algorithm to traverse the network and simulate protein synthesis. A key feature of this simulation is the inclusion of Epigenetic Regulation, allowing the user to toggle between "Gene ON" (Acetylation) and "Gene OFF" (Methylation) states to see how gene silencing affects graph connectivity and path traversal.

## Tools Used
* Language: Python 3.x.
* Graph Management: networkx library for directed graph (Digraph) construction and metric analysis.
* Visualization: matplotlib for generating high-fidelity visual representations of the pathway.
* Data Structures: collections.deque for efficient queue management during the BFS process.
* Collaboration: GitHub for codebase version control.

## Instructions on How to Run Your Code

### 1. Prerequisites
Ensure you have Python installed on your system. You will also need to install the required libraries using pip:
```Bash
pip install networkx matplotlib
```

### 2. Running the Simulation
Download the provided script file. Execute the script through your terminal or IDE:
```Bash
python project_script.py
```
Provide Input: When prompted, enter the name of a target protein (e.g., Insulin, Actin, or Tubulin). 
Select Regulation State: Choose 1 for Acetylation (Gene ON) or 2 for Methylation (Gene OFF).

### 3. Interpreting Results
The program will display a visual graph where the Active Path is highlighted in red. 
A Node Degree Table will be printed in the terminal, showing the in-degree and out-degree of every biological component in the network. 
If "Methylation" is selected, the visualization will demonstrate an aborted synthesis where the path terminates at the Target Gene.