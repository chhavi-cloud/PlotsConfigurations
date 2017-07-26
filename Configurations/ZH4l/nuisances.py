# nuisances

#nuisances = {}

eleWP='mva_90p_Iso2016'
#'cut_WP_Tight80X'
#'cut_WP_Tight80X_SS'
#'mva_80p_Iso2015'
#'mva_80p_Iso2016'
#'mva_90p_Iso2015'
#'mva_90p_Iso2016'
muWP='cut_Tight80x'

upDownPath = "/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_summer16/"


# name of samples here must match keys in samples.py
#

nuisances['lumi']  = {
        'name'  : 'lumi_13TeV',
        'samples'  : {
            'WH_hww'    : '1.023',
            'ZH_hww'    : '1.023',
            'ggZH_hww'  : '1.023',
            'WH_htt'    : '1.023',
            'ZH_htt'    : '1.023',
            'ggH_hzz'   : '1.023',
            'WWW'       : '1.023',
            'VVZ'       : '1.023',
            'ZZ'        : '1.023',
            'ggZZ'      : '1.023',
            'WZ'        : '1.023',
            'WW'        : '1.023',
            'ggWW'      : '1.023',
            'Vg'        : '1.023',
            'DY'        : '1.023',
            'ttW'       : '1.023',
            'ttZ'       : '1.023',
            'Top'       : '1.023',
            },
        'type'  : 'lnN',
        }


nuisances['lumi2016']  = {
               'name'  : 'lumi_13TeV_2016', 
               'samples'  : {
                   'ggH_hww'  : '1.058',
                   'qqH_hww'  : '1.058',
                   'WH_hww'   : '1.058',
                   'ZH_hww'   : '1.058',
                   'ZH_htt'   : '1.058',
                   'H_htt'    : '1.058',
                   'H_hww'    : '1.058',
                   'WH_hww'   : '1.058',
                   'ggZH_hww'   : '1.058',
                   'VVZ'      : '1.058',
                   'WWW'      : '1.058',
                   'WZ'       : '1.058',
                   'WW'       : '1.058',
                   'ttW'       : '1.058',
                   'ttZ'       : '1.058',
                   'ggWW'     : '1.058',
                   'Vg'       : '1.058',
                   'VgS'      : '1.058',
                   #'DY'       : '1.058',    # --> datadriven
                   #'WW'       : '1.058',    # --> datadriven
                   #'top'      : '1.058',    # --> datadriven
                   },
               'type'  : 'lnN',
              }




# Theoritical Systematics

from LatinoAnalysis.Tools.HiggsXSection import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_ZH_zh4l']  = {
        'name' : 'QCDscale_ZH',
        'samples' : {
            'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.0','scale','sm'),
            },
        'type' : 'lnN',
        }

nuisances['QCDscale_ggZH_zh4l']  = {
        'name' : 'QCDscale_ggZH',
        'samples'  : {
            'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','scale','sm'),
            },
        'type' : 'lnN',
        }

# pdf uncertainty

nuisances['pdf_gg_zh4l']  = {
        'name' : 'pdf_gg',
        'samples' : {
            'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','pdf','sm'),
            },
        'type' : 'lnN',
        }

nuisances['pdf_qqbar_zh4l']  = {
        'name'  : 'pdf_qqbar',
        'type'  : 'lnN',
        'samples'  : {
            'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH' ,'125.0','pdf','sm'),
            },
        }

## PS/UE
#
## PS
#
nuisances['PS_zh4l']  = {
        'name'  : 'PS_zh4l',
        #               'kind'  : 'tree',
        'type'  : 'lnN',
        'samples'  : {
            'ZH_hww'   : '1.037',
            'ZH_htt'   : '1.037',
            'ggH_hzz'  : '1.037',
            },
        }

nuisances['UE_zh4l']  = {
        'name'  : 'UE_zh4l',
        'type'  : 'lnN',
        'samples'  : {
            'ZH_hww'   : '1.010',
            'ZH_htt'   : '1.010',
            'ggH_hzz'  : '1.010',
            },
        }


nuisances['ZZ4lnorm']  = {
        'name'  : 'ZZ4lnorm',
        'samples'  : {
            'ZZ' : '1.00',
            },
        'type'  : 'rateParam',
        'cuts'  : [
            'zh4l_ZZ_13TeV',
            'zh4l_XSF_13TeV',
            'zh4l_XDF_13TeV',
            ]
        }
# Other Systematics


nuisances['btagbc']  = {
        'name'  : 'ICHEP_btag_bc',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  : {
            'ggH_hww' : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'qqH_hww' : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'WH_hww'  : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ZH_hww'  : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ZH_htt'  : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggZH_hww': ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'H_htt'   : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'H_hww'   : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggH_hzz' : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'DY'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ttZ'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ttW'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'WWW'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'VVZ'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'VZ'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ZZ'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggZZ'    : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'WW'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggWW'    : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'top'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'Vg'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'VgS'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            }
        }

nuisances['btagudsg']  = {
        'name'  : 'ICHEP_btag_udsg',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  : {
            'ggH_hww' : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'qqH_hww' : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WH_hww'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ZH_hww'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ZH_htt'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggZH_hww': ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'H_htt'   : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'H_hww'   : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WH_hww'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggH_hzz' : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'DY'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ttZ'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ttW'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WWW'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'VVZ'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'VZ'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ZZ'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggZZ'    : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WW'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggWW'    : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'top'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'Vg'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'VgS'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            }
        }


nuisances['trigg_zh4l']  = {
        'name'  : 'trigger',
        'kind'  : 'weight',
        #'kind'  : 'tree', #'weight',
        'type'  : 'shape',
        'samples'  : {
            'WH_hww'   : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ZH_hww'   : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ZH_htt'   : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ggZH_hww' : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'WH_htt'   : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ggH_hzz'  : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'WWW'      : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'VVZ'      : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'WZ'       : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'DY'       : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ttW'      : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ttZ'      : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ZZ'       : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'ggZZ'     : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'WW'       : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'Vg'       : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            'top'      : ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)'],
            },
        }

# electronIdIso = '(1+(abs(std_vector_lepton_flavour[0])==11)*(std_vector_electron_idisoW_'+eleWP+'_Up[0])/(std_vector_electron_idisoW_'+eleWP+'[0]-1))*(1+(abs(std_vector_lepton_flavour[1])==11)*(std_vector_electron_idisoW_'+eleWP+'_Up[1])/(std_vector_electron_idisoW_'+eleWP+'[1]-1))*(1+(abs(std_vector_lepton_flavour[2])==11)*(std_vector_electron_idisoW_'+eleWP+'_Up[2])/(std_vector_electron_idisoW_'+eleWP+'[2]-1))*(1+(abs(std_vector_lepton_flavour[3])==11)*(std_vector_electron_idisoW_'+eleWP+'_Up[3])/(std_vector_electron_idisoW_'+eleWP+'[3]-1))','(1+(abs(std_vector_lepton_flavour[0])==11)*(std_vector_electron_idisoW_'+eleWP+'_Down[0])/(std_vector_electron_idisoW_'+eleWP+'[0]-1))*(1+(abs(std_vector_lepton_flavour[1])==11)*(std_vector_electron_idisoW_'+eleWP+'_Down[1])/(std_vector_electron_idisoW_'+eleWP+'[1]-1))*(1+(abs(std_vector_lepton_flavour[2])==11)*(std_vector_electron_idisoW_'+eleWP+'_Down[2])/(std_vector_electron_idisoW_'+eleWP+'[2]-1))*(1+(abs(std_vector_lepton_flavour[3])==11)*(std_vector_electron_idisoW_'+eleWP+'_Down[3])/(std_vector_electron_idisoW_'+eleWP+'[3]-1))'

# muonIdIso = '(1+(abs(std_vector_lepton_flavour[0])==13)*(std_vector_muon_idisoW_'+muWP+'_Up[0])/(std_vector_muon_idisoW_'+muWP+'[0]-1))*(1+(abs(std_vector_lepton_flavour[1])==13)*(std_vector_muon_idisoW_'+muWP+'_Up[1])/(std_vector_muon_idisoW_'+muWP+'[1]-1))*(1+(abs(std_vector_lepton_flavour[2])==13)*(std_vector_muon_idisoW_'+muWP+'_Up[2])/(std_vector_muon_idisoW_'+muWP+'[2]-1))*(1+(abs(std_vector_lepton_flavour[3])==13)*(std_vector_muon_idisoW_'+muWP+'_Up[3])/(std_vector_muon_idisoW_'+muWP+'[3]-1))','(1+(abs(std_vector_lepton_flavour[0])==13)*(std_vector_muon_idisoW_'+muWP+'_Down[0])/(std_vector_muon_idisoW_'+muWP+'[0]-1))*(1+(abs(std_vector_lepton_flavour[1])==13)*(std_vector_muon_idisoW_'+muWP+'_Down[1])/(std_vector_muon_idisoW_'+muWP+'[1]-1))*(1+(abs(std_vector_lepton_flavour[2])==13)*(std_vector_muon_idisoW_'+muWP+'_Down[2])/(std_vector_muon_idisoW_'+muWP+'[2]-1))*(1+(abs(std_vector_lepton_flavour[3])==13)*(std_vector_muon_idisoW_'+muWP+'_Down[3])/(std_vector_muon_idisoW_'+muWP+'[3]-1))'



# nuisances['idiso_ele_wh3l']  = {
#         'name'  : 'idiso_ele',
#         'kind'  : 'weight',
#         #'kind'  : 'tree', #'weight',
#         'type'  : 'shape',
#         'samples'  : {
#               'WH_hww'   : [electronIdIso],
#               'ZH_hww'   : [electronIdIso],
#               'ggZH_hww' : [electronIdIso],
#               'WH_htt'   : [electronIdIso],
#               'WW'       : [electronIdIso],
#               'Vg'       : [electronIdIso],
#               'WZ'       : [electronIdIso],
#               'ZZ'       : [electronIdIso],
#               'ggZZ'     : [electronIdIso],
#               'WWW'      : [electronIdIso],
#               'VVZ'      : [electronIdIso],
#               'ttZ'      : [electronIdIso],
#               'ttW'      : [electronIdIso],
#             },
#         #'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel__TrigEff/',    # uncertainties fixed!
#         #'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel__TrigEff/'
#         }


# nuisances['idiso_mu_wh3l']  = {
#         'name'  : 'idiso_mu',
#         'kind'  : 'weight',
#         #'kind'  : 'tree', #'weight',
#         'type'  : 'shape',
#         'samples'  : {
#               'WH_hww'   : [muonIdIso],
#               'ZH_hww'   : [muonIdIso],
#               'ggZH_hww' : [muonIdIso],
#               'WH_htt'   : [muonIdIso],
#               'WW'       : [muonIdIso],
#               'Vg'       : [muonIdIso],
#               'WZ'       : [muonIdIso],
#               'ZZ'       : [muonIdIso],
#               'ggZZ'     : [muonIdIso],
#               'WWW'      : [muonIdIso],
#               'VVZ'      : [muonIdIso],
#               'ttZ'      : [muonIdIso],
#               'ttW'      : [muonIdIso],
#             },
#         }

# # # nuisances handled by means of a different set of trees


nuisances['jes_zh4l']  = {
        'name'  : 'scale_j',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESup',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESdo'

        }

nuisances['electronpt_zh4l']  = {
        'name'  : 'scale_e',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepElepTup',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepElepTdo'
        }

nuisances['muonpt_zh4l']  = {
        'name'  : 'scale_m',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepMupTup',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepMupTdo'
        }

nuisances['met_zh4l']  = {
        'name'  : 'scale_met',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__METup',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__METdo'
        }

# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
nuisances['stat']  = {
        # apply to the following samples: name of samples here must match keys in samples.py
        'samples'  : {
            'ttW': {
                'typeStat' : 'bbb',
                },
            'ttZ': {
                'typeStat' : 'bbb',
                },
            'DY': {
                'typeStat' : 'bbb',
                },

            'WW': {
                'typeStat' : 'bbb',
                },

            'ZZ': {
                'typeStat' : 'bbb',
                },

            'ggZZ': {
                'typeStat' : 'bbb',
                },

            'WZ': {
                'typeStat' : 'bbb',
                },

            'WWW': {
                'typeStat' : 'bbb',
                },

            'VVZ': {
                'typeStat' : 'bbb',
                },

            'WH_hww': {
                'typeStat' : 'bbb',
                },

            'ZH_hww': {
                'typeStat' : 'bbb',
                },

            'ggZH_hww': {
                'typeStat' : 'bbb',
                },

            'WH_htt': {
                'typeStat' : 'bbb',
                },

            'ZH_htt': {
                'typeStat' : 'bbb',
                },
            'ggH_hzz': {
                'typeStat' : 'bbb',
                },
            'Top': {
                'typeStat' : 'bbb',
                },
            'Fake': {
                'typeStat' : 'bbb',
                },
            'Vg': {
                    'typeStat' : 'bbb',
                    },
            },
               'type'  : 'shape'
                 }