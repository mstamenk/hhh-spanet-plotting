# HHH SPANET plotting
Small example on how to plot one variable from TTree using RDataFrame from ROOT

# Installation to be done once
In a terminal connected on lxplus via `ssh`:

```
mkdir workspace
cd workspace
cmsrel CMSSW_12_5_2
cd CMSSW_12_5_2/src
cmsenv
git clone git@github.com:mstamenk/hhh-spanet-plotting.git
```

Each time you open a new terminal and go to CMSSW, you need to do:
```
cd workspace/CMSSW_12_5_2/src
cmsenv
```

This sets up the working environment with the correct `python` and `ROOT` version.

# Running the script
```
cd hhh-spanet-plotting.git
python3 plot_variables.py 
```

