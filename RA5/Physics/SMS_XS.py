
class CrossSection(object):
    def __init__(self,value,error):
        self.value = value
        self.error = error

br      = 0.04 
xs_dict = {
            "SMS-T1qqqqL_1000": CrossSection(0.325388,0.16758),
            "SMS-T1qqqqL_1500": CrossSection(0.0141903,0.227296),
            "SMS-T1qqqqL_1600": CrossSection(0.00810078,0.242679),
            "SMS-T1qqqqL_1700": CrossSection(0.00470323,0.261021),
            "SMS-T1qqqqL_1800": CrossSection(0.00276133,0.28108),
            "SMS-T1qqqqL_1900": CrossSection(0.00163547,0.299045),
            "SMS-T1qqqqL_2000": CrossSection(0.000981077,0.318422),
            
            "SMS-T1tbs_1000": CrossSection(br*0.325388,0.16758),
            "SMS-T1tbs_1500": CrossSection(br*0.0141903,0.227296),
            "SMS-T1tbs_1600": CrossSection(br*0.00810078,0.242679),
            "SMS-T1tbs_1700": CrossSection(br*0.00470323,0.261021),
            "SMS-T1tbs_1800": CrossSection(br*0.00276133,0.28108),
            "SMS-T1tbs_1900": CrossSection(br*0.00163547,0.299045),
            "SMS-T1tbs_2000": CrossSection(br*0.000981077,0.318422),
}
