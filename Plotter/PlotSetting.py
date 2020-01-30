labelDict = {
        "ht40"     : "H_{T}",
        "alphaT"   : "#alpha_{T}",
        "mht40_pt" : "H^{miss}_{T}",
        "met"   : "E^{miss}_{T}",
        "met_pt"   : "E^{miss}_{T}",
        "mht40_pt/met_pt": "H^{miss}_{T}/E^{miss}_{T}",
        "nVert"        : "n_{vtx}",
        "nJet40"       : "n_{Jet}",
        "nBJet": "n_{bJet}",
        "nBJet25": "n_{bJet}",
        "nBJet40": "n_{bJet}",
        "jet_pt[0]": "Leading Jet p_{T}",
        "jetPt1": "Leading Jet p_{T}",
        "jet_pt[1]": "Second Jet p_{T}",
        "jetPt2": "Second Jet p_{T}",
        "jet_pt[2]": "Third Jet p_{T}",
        "jet_eta[0]": "Leading Jet #eta",
        "jet_eta[1]": "Second Jet #eta",
        "jet_eta[2]": "Third Jet #eta",
        "jet_phi[0]": "Leading Jet #phi",
        "jet_phi[1]": "Second Jet #eta",
        "jet_phi[2]": "Third Jet #phi",
        "biasedDPhi": "#Delta#Phi*",
        "biasedDPhi20": "#Delta#Phi* (jet p_{T} > 20)",
        "metNoMu_pt"  :  "E^{miss}_{T,No #mu}",
        "mht40_pt/metNoMu_pt": "H^{miss}_{T}/E^{miss}_{T,No #mu}",
        "muon_pt[0]" : "Muon p_{T}",
        "muonPt1" : "Leading Muon p_{T}",
        "muonPt2" : "Second Muon p_{T}",
        "muon_eta[0]": "Muon #eta",
        "muon_phi[0]": "Muon #phi",
        "muon_relIso03[0]"  : "Muon I^{rel}_{0.3}",
        "muon_relIso04[0]"  : "Muon I^{rel}_{0.4}",
        "muon_miniRelIso[0]": "Muon I^{mini}",
        "mll": "m_{ll}",
        "mtw": "m_{T}",
        "minDelRJetMu": "min #DeltaR_{Jet,#mu}",
        "metNoEle_pt":  "E^{miss}_{T,No e}",
        "mht40_pt/metNoEle_pt": "H^{miss}_{T}/E^{miss}_{T,No e}",
        "ele_pt[0]" : "Electron p_{T}",
        "elePt1" : "Leading Electron p_{T}",
        "elePt2" : "Second Electron p_{T}",
        "ele_eta[0]": "Electron #eta",
        "ele_phi[0]": "Electron #phi",
        "ele_relIso03[0]"  : "Electron I^{rel}_{0.3}",
        "ele_relIso04[0]"  : "Electron I^{rel}_{0.4}",
        "ele_miniRelIso[0]": "Electron I^{mini}",
        "minDelRJetEle": "min #DeltaR_{jet,e}",
        "mht40_pt/metNoPhoton_pt":  "H^{miss}_{T}/E^{miss}_{T,No #gamma}",
        "gamma_pt[0]" : "#gamma p_{T}",
        "gamma_eta[0]": "#gamma #eta",
        "gamma_phi[0]": "#gamma #phi",
        "minDelRJetPhoton": "min #DeltaR_{jet,#gamma}",
        "nJet40Eta2p4" : "n_{Jet}",
        "nBJet40Eta2p4": "n_{bJet}",
        "minDelRJetZ": "min #DeltaR_{Z,Jet}",
        "njetInc": "n_{jet} (p_{T} > 25)",
        "biasedDPhiInc": "#Delta#Phi* (jet p_{T} > 25)",
        "biasedDPhi25": "#Delta#Phi* (jet p_{T} > 25)",
        "softDMass" : "m_{top}",
        "sdMass": "m_{W}",
        "nSubjets" : "n_{subjets}",
        "tau3tau2": "#tau_{3}/#tau_{2}",
        "tau2tau1": "#tau_{2}/#tau_{1}",
        "mht40_pt/metNoX_pt":  "H^{miss}_{T}/E^{miss}_{T}",
        "minjet40_chi": "min(#chi)",
        "subjetBtag": "subjet b-disc",
        "nfatjets": "n_{jet} (AK8)",
        "ptTopTag": "p_{T}^{top}",
        "ptWTag": "p_{T}^{W}",
        "fatjets_pt": "AK8 jet p_{T}",
        }

class PlotSetting(object):
    def __init__(self,
            divideByBinWidth=False,
            x_axis_title=None,x_axis_labels=None,
            y_axis_title=None,y_axis_labels=None,
            defaultLabelDict=labelDict,
            sf_x_pos=0.11,
            sf_y_pos=0.92,
            sf_text_font=42,
            sf_text_size=0.05,
            leg_name_dict={},
            log_x=False,
            linear_max_factor=1.5,
            log_max_factor=5,
            log_min=0.1,
            line_style_dict={},
            line_width_dict={},
            line_color_dict={},
            bin_width_label="",
            leg_pos=[],
            leg_column=None,
            leg_text_size=0.03,
            minimum=None,
            marker_size=0.5,
            marker_style=5,
            marker_style_dict={},
            marker_color_dict={},
            marker_size_dict={},
            scatter_density=1.0,
            tdr_style=False,
            cms_lumi=False,
            cms_lumi_number=4,
            ratio_range=[],
            ):
        self.divideByBinWidth = divideByBinWidth
        self.x_axis_title = x_axis_title
        self.y_axis_title = y_axis_title
        self.defaultLabelDict = defaultLabelDict
        self.x_axis_labels = x_axis_labels
        self.y_axis_labels = y_axis_labels
        self.sf_x_pos = sf_x_pos
        self.sf_y_pos = sf_y_pos
        self.sf_text_font = sf_text_font
        self.sf_text_size = sf_text_size
        self.leg_name_dict=leg_name_dict
        self.log_x = log_x
        self.linear_max_factor = linear_max_factor
        self.log_max_factor = log_max_factor
        self.log_min = log_min
        self.line_style_dict = line_style_dict
        self.line_width_dict = line_width_dict
        self.line_color_dict = line_color_dict
        self.bin_width_label = bin_width_label
        self.leg_pos = leg_pos
        self.leg_column = leg_column
        self.minimum = minimum
        self.marker_size = marker_size
        self.marker_style = marker_style
        self.marker_style_dict = marker_style_dict
        self.marker_color_dict = marker_color_dict
        self.marker_size_dict = marker_size_dict
        self.scatter_density = scatter_density
        self.tdr_style = tdr_style
        self.cms_lumi = cms_lumi
        self.cms_lumi_number = cms_lumi_number
        self.ratio_range = ratio_range
        self.leg_text_size = leg_text_size
