# Script to plot variables from ROOT TTree (processed with NanoAOD tools)

# import section
import os,ROOT

# ROOT.gROOT.SetBatch(ROOT.kTRUE) - uncomment to run batch for many plots
ROOT.ROOT.EnableImplicitMT() # Enable multi threading to go faster

# path to samples
path = '/afs/cern.ch/work/m/mstamenk/public/forPKU/v21/mva-inputs-HLT-selection-v21-inclusive-loose-wp-0ptag-2017/'

# Get signal sample
f_in = 'GluGluToHHHTo6B_SM'

# open the file using a data frame
df = ROOT.RDataFrame('Events', path+'/' + f_in + '.root')

# Potentially apply a selection 
selection = 'jet1Pt > 20 && jet1Eta < 2.5'
df_selection = df.Filter(selection)

# get report on selection efficiency
report = df_selection.Report()
report.Print()

# Get histograms
variable = 'jet1Pt' # momentum of the jet with highest b-tag score
bins = 50 # 50 bins
xmin = 0. # from 0 GeV
xmax = 500. # to 500 GeV

# book the rdataframe to get the histogram once it loops
# get jet1Pt variables, with histogram name Jet1 and title Jet1, with the eventWeight applied
h = df_selection.Histo1D(('Jet1','Jet1',bins,xmin,xmax),variables,'eventWeight') 

# Run loop
h.Draw()

# Draw histogram
c = ROOT.TCanvas() # canvas on which to draw the histograms
h.Draw("hist e") # draw histogram with error band (use "hist e same" to draw a second histogram on the same canvas
c.Print('C_%s.pdf'%variable)







