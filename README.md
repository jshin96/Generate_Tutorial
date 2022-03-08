# Generate_Tutorial

### Gridpack
```
 First make input cards 
    XXX_proc_card.dat
    XXX_run_card.dat
    XXX_madspin_card.dat (optional to set specific decay path)
    XXX_customizecards.dat (customize parameters like top mass)
    XXX_extramodels.dat (for non-SM Lagrangian)
 proc_card and run card can be made by running MadGraph
 Then submit through submit_gridpack_generation.sh in genproductions
   which is available by git clone https://github.com/cms-sw/genproductions.git
 ./gridpack_genrateion.sh <XXX> <directory containing cards relative to current location>
 This will generate gridpack tarball which should be moved to lxplus:eos/user/s/shin/Gridpacks which is available for the public to access to run generation later
check cernbox.cern.ch
```
### Generation Step
```
 initial setup
  
cmsrel CMSSW_XX_YY_ZZ 
 (CMSSW version that is appropriate for the MC, which is available at DAS if you are getting the generation from there)
cd CMSSW_/src
cmsenv

git cms-init
git cms-addpkg GeneratorInterface/LHEInterface
cd GeneratorInterface/LHEInterface/data
wget https://raw.githubusercontent.com/cms-sw/cmssw/master/GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh
chmod 755 run_generic_tarball_xrootd.sh
cd $CMSSW_BASE/src
scram b -j 6

 now clone the repository
mkdir Configuration && cd Configuration
mkdir GenProduction && cd GenProduction
mkdir python && cd python

Now you need the configuration file. Look at TOP-RunIISummer19UL18_No_decay.py as a sample (you can produce using cmsDriver.py command) 
https://cms-pdmv.cern.ch/mcm to find a sample similar to yours and use their command and fragment file.

check that the config uses proper "run_generic_tarball_XXXX/sh"
then put the configuration file in here
go back to src
scram b

 

This will give a file that can be used in crab, but you need a crab submit file to submit the file that was just produced. 
look at submit_crab_gen_py

Now submit 
crab submit <submit_crab_file>
crab status <crab_project/process name>
crab resubmit <crab_project/process name>
```

### SKFlatMaker
```


First SKFlatMaker and source setup.sh.


To run SKFlatMaker, KNU I already set the directory needed for UL and PreLegacy. 
Before you run MakeCrab.py to make the crab file, make sure you have the correct input DAS of sample you want to make.
You can search DAS name in SKFlatMaker?SKFlatMaker/scripts/CRAB3 using 

EX)  dasgoclient --query "/ttZJets*/RunIISummer*UL*/MINIAODSIM"

This will give you the list of DAS names that match what you put in.
where the "" denotes the name of sample you want to look for, the example is looking for ttZJets sample for UL MiniAOD
After that, you also need to make sure you have the right weight for the sample. 
Go to SKFlatMaker?SKFlatMaker/scripts/Weight and run

python getLog.py /ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1/MINIAODSIM

Where the example DAS name was directly copied and pasted from dasgoclient 
This will make a log file containing all the weights that needs to be applied to the sample. 
You then need to run 

python parseLog.py logs/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8__RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1.log 

Which will look for the factors that needs to be applied for the sample and make a txt file in Weight/data/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8__RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1.log 
(This could fail, which case needs to be manually made. The necessary values are Scale, PDF, AlphaS, AlphaSScale)
After the weight txt file is made, edit the corresponding year txt file eg) 2018_MC.txt, inserting the name of DAS file you want to run is in the file unstashed. and then run MakeCrab.py in CRAB3. 
This will turn in the command line and make crab python file in Run2UltraLegacy_v2 directory. 
```
