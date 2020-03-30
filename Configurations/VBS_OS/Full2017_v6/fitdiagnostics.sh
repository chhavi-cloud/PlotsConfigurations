#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/m/mlizzo/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workdir=/afs/cern.ch/work/m/mlizzo/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2017/nAODv5_v6
workspaceDir=workspaces

cd $workdir

echo "events:" "" > ${workspaceDir}/diagnostics_mjj_vs_mTi.txt
combine -M FitDiagnostics ${workspaceDir}/mjj_vs_mTi.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/diagnostics_mjj_vs_mTi.txt
