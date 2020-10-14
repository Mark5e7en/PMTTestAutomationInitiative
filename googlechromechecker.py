'''launch tool
set ComplianceBaselineParameter value > installed version
perform a scan
verify check is failed'''


import os
protect_mytech_location = r'"C:\ProgramData\Accenture\ProtectMyTech\ProtectMyTech.exe"'
os.system(protect_mytech_location)


def update_compliancebaseline_value(pmtparameter, value):
    import json
    compliance_baseline_location = "C:\\Users\mark.steven.l.tagaro\AppData\Local\Accenture\ProtectMyTech\ComplianceBaselineParameter.json"

    with open(compliance_baseline_location, 'r+') as f:
        try:
            # read the JSON from compliance baseline file then put it in a variable named data
            data = json.load(f)

            for item in data:
                if item['pmtparameter'] == pmtparameter:
                    # replaces the value of the key
                    item['value'] = value

            file = open(compliance_baseline_location, "w")
            # puts the updated JSON to the compliance baseline file
            # separators will remove spaces within the JSON
            json.dump(data, file, separators=(',', ':'))
        except:
            print("Some error")


# update_compliancebaseline_value("Java12MinimumAllowedVersion", "86.0")

