from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'tt012j_Vcb_NLO_CP5_FXFX_Summer20UL18'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'run_crab_UL_LHEGEN.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'tt012j_Vcb_NLO_CP5_FXFX_Summer20UL18'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000 # num. of jobs to submit
NJOBS = 600  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/shin/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer20UL18wmLHEGEN'

config.Site.storageSite = 'T3_KR_KNU'
