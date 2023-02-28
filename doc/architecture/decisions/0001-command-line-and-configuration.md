# 1. Command Line and Configuration

Date: 2023-02-28

## Status

Proposed

## Context

Our current implementation for solving the maze involves hardcoding the parameters in the main file. This approach limits the user's ability to modify the maze's settings, making it less user-friendly. Additionally, we received feedback from teachers who expressed discomfort in writing Python commands to run the maze. Therefore, we need to implement a solution that allows users to set the maze's main settings through either a configuration file or a command line.

## Decision

To address this issue, we will use the argparse library to parse the command-line arguments and the configparser library to read and write configuration files. We will define a set of parameters that the user can modify, including the number of rows, number of columns, margin size, screen size, cell size, and random seed. We will define the default values for each parameter and allow the user to overwrite these values through either a configuration file or a command line.

## Consequences

The implementation of argparse and configparser libraries will make our maze-solving application more user-friendly, allowing users to set the maze's main settings without needing to modify the code. The use of command-line arguments and configuration files will also make it easier to automate running the maze and allow users to save specific configurations for future use. However, implementing this solution will require additional development time, as we will need to modify the existing code to use the argparse and configparser libraries.
