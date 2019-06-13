# Installation
>"Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous shape systematics, or to take arms against a sea of bins, and by uncorrelating, end them?"

Framework for running on root ntuples for various CMS physics analysis

```bash
git clone git@github.com:lucien1011/UF-PyNTupleRunner.git
```

If you are on UF IHEPA, you can set up the framework by doing:
```bash
cd UF-PyNTupleRunner
source setup_ihepa.sh
```
There are other setup.sh specific to each user's laptop.

# Structure
This framework supports multiple analysis so it is important to keep each analysis code in a separate folder.
* Common: stores various class and tools that can be used by various analysis, for example, TreeProducer (which produces ntuples), CSVFileProducer (which produces CSV files from ntuples).
* Core: stores the major classes for the framework. 
* DataMC: stores data or MC information, e.g. btagging working points, trigger efficiencies etc.
* DarkZ, HToZdZd, HZZ4l, LJMet, RA5, RPV and Zprime: stores analysis codes for each analysis
* Utils: stores useful functions and classes for cosmetics, tables, pickle files, or even kinematic calculation such as deltaR.
* Example: stores a simple example code to run the framework
* Plotter: a very useful and flexible set of classes that are used by multiple analysis codes to make data/MC plots.

# Usage
To run the framework, you have to first define your ntuple in your code. You can see various examples of this in the folder "Dataset" in each analysis folder. 
The name "Dataset" is just a convention. Then you have to create a new configuration file (your_cfg.py). In this file, you have 
to define the following variable:
* outputInfo: defines the output directory by setting outputInfo.outputDir, and defines the file name by setting outputInfo.TFileName
* nCores: defines how many computing threads you want to use
* disableProgressBar: set to True if you do not want the real-time progress bar to be shown, this is useful when you are debugging your codes.
* sequence: defines what you want to do for each event, the sequence should contain various modules and each module will 
carry out user-defined actions on each events.
* endSequence: defines what you want to do after you have run over all events.
* componentList: defines a list of dataset you have defined, e.g. instances you defined under the folder "Dataset" as mentioned above.

```bash
UFNTuple your_cfg.py
```
For a specific example, please refer to the Example folder and try running on the configuration file plot_example_cfg.py.

# Support
Direct **ALL** questions to kin.ho.lo@cern.ch
