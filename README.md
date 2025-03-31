# Huffman-Data-Compression-Optimization

# Overview
This repository contains the code and documentation for the Huffman Data Optimization project completed as part of the University course.
The project focuses on implementing the Huffman coding algorithm to compress and decompress data efficiently. Huffman coding is a widely used technique in data compression,
where frequently occurring characters are assigned shorter codes to minimize the overall size of the data.

The main goal of this project was to gain a deeper understanding of data compression techniques, algorithms, and their implementation. The project includes both the 
implementation of the Huffman coding algorithm and a user-friendly interface for compressing and decompressing files.

# Features
Huffman coding implementation for efficient data compression.
User-friendly command-line interface for compression and decompression.
Detailed documentation explaining the Huffman coding algorithm and how to use the program.
Support for compressing text files, binary files, and more.

# Getting Started
## Prerequisites
Before running the project, make sure you have the following installed:

Python (version X.X)
Any additional libraries or dependencies

# Installation
Clone the repository:
git clone https://github.com/Harish-Arvind/huffman-compression-data-optimization.git

Navigate to the project directory:
cd huffman-optimization

Install any required dependencies:
pip install -r requirements.txt

# Usage

To compress a file:
python main.py compress input_file.txt

To decompress a file:
python main.py decompress input_file.txt.huffman

Replace input_file.txt with the name of the file you want to compress or decompress.

### Algorithm Explanation
The Huffman coding algorithm involves the following steps:

# Frequency Counting: 
Calculate the frequency of each character in the input data.

# Building the Huffman Tree: 
Create a priority queue (heap) of nodes, each representing a character and its frequency. Repeatedly merge the two nodes with the lowest frequencies to build a binary tree.

# Assigning Codes: 
Traverse the Huffman tree to assign unique binary codes to each character. The codes are assigned in such a way that no code is a prefix of another.

# Encoding: 
Replace each character in the input data with its corresponding Huffman code.

# Compression: 
Write the encoded data to an output file, along with the necessary information to reconstruct the Huffman tree during decompression.

# Decompression: 
Read the compressed file, reconstruct the Huffman tree using the information stored, and decode the encoded data to recover the original data.

Contributing
Contributions to this project are welcome! If you find any bugs or want to enhance the project, feel free to create a pull request. Please follow the existing coding style and guidelines.

