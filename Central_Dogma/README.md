# Gene Regulatory Network Simulator

## Overview

A Python-based bioinformatics application that models and simulates the Central Dogma of molecular biology using graph theory. This project demonstrates how genetic information flows from DNA through transcription and translation to produce proteins, with the ability to simulate epigenetic regulation states that affect gene expression.

## What This Project Does

The simulator represents biological pathways as directed graphs, where molecular entities (Transcription Factors, Promoters, Genes, mRNA) are vertices and biochemical transitions are edges. Using a custom Breadth-First Search (BFS) algorithm, it traverses the network to simulate protein synthesis pathways. A key feature is **Epigenetic Regulation Control**, allowing users to toggle between:

- **Acetylation (Gene ON)** – Active gene expression with complete pathway traversal
- **Methylation (Gene OFF)** – Gene silencing that terminates the synthesis pathway

## Features

- **Graph-Based Molecular Modeling** – Represents biological pathways as directed acyclic graphs
- **BFS Path Traversal** – Simulates protein synthesis through manual breadth-first search algorithm
- **Epigenetic Regulation** – Toggle between gene ON/OFF states to observe impact on pathways
- **Visual Pathway Representation** – High-fidelity matplotlib visualizations with active paths highlighted in red
- **Network Metrics Analysis** – Displays node degree tables showing in-degree and out-degree for each biological component

## Prerequisites & Installation

### Requirements
- Python 3.x
- `networkx` – Directed graph construction and analysis
- `matplotlib` – Pathway visualization
- `collections` (standard library) – Queue management for BFS

### Setup

```bash
pip install networkx matplotlib
```

## Usage Guide

### Running the Simulation

```bash
python Central_Dogma.py.py
```

### Step-by-Step Instructions

1. **Enter Target Protein** – When prompted, specify a protein (e.g., Insulin, Actin, Tubulin)
2. **Select Regulation State:**
   - Enter `1` for **Acetylation** (Gene ON – full synthesis)
   - Enter `2` for **Methylation** (Gene OFF – synthesis blocked)
3. **View Results:**
   - **Visual Graph** – Displays the regulatory network with active pathways highlighted in red
   - **Node Degree Table** – Terminal output showing in-degree and out-degree metrics
   - **Pathway Outcome** – Under methylation, visualization shows where synthesis terminates

## Technical Architecture

| Component | Purpose |
|-----------|---------|
| Graph Construction | Built using `networkx` Digraph to represent molecular entities and transitions |
| BFS Algorithm | Custom implementation using `collections.deque` for queue management |
| Epigenetic States | Toggle mechanism to enable/disable gene expression |
| Visualization Engine | Matplotlib-powered rendering of network topology and active paths |
| Metrics Calculation | Degree analysis for network connectivity assessment |

## Key Concepts

- **Central Dogma** – DNA → mRNA → Protein information flow
- **Epigenetic Regulation** – Reversible gene silencing without DNA sequence changes
- **Graph Theory** – Vertex-edge representation for biological networks
- **Breadth-First Search** – Algorithm for simulating sequential biological processes