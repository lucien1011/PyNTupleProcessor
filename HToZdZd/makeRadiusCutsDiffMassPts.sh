#!/bin/bash
#####################################################################################################
## PURPOSE: 
## SYNTAX:  
## NOTES:   
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-02-20
#####################################################################################################

#____________________________________________________________________________________________________
# User Parameters
zdmasslist="15 30 50 60" 
#zdmasslist="15 30 50 60 " 
radcutstart=0.2       # GeV
radcutstop=5        # GeV
radcutinterv=0.2      # GeV

binwidth=0.05       # GeV
zoom=0.05           # as a fraction of the radius to better see the full circle: x2-x1=2r+2zoom

template="template_plot_DarkPhoton_signif_radiuscut_cfg.py"
deletefile="DELETEtemp_plot_DarkPhoton_signif_radiuscut_cfg.py"

#____________________________________________________________________________________________________
# Main
for zdmass in $zdmasslist; do

    #for radiuscut in {0..10}; do 
    for radcut in $(seq ${radcutstart} ${radcutinterv} ${radcutstop}); do 
        #radiuscut=$( bc -l <<< "scale=1; ${radiuscut}/2" )
        #echo "${radiuscut}"
        if [ -e  ]; then
            rm ${deletefile}
        fi

        echo 
        echo "Copying template for mZd${zdmass}, radius cut = ${radcut} GeV..."
        cp ${template} ${deletefile}

        sed -i "s|RADIUSCUT|${radcut}|g"    ${deletefile}
        sed -i "s|ZDMASS|${zdmass}|g"       ${deletefile}
        sed -i "s|BINWIDTH|${binwidth}|g"   ${deletefile}
        sed -i "s|ZOOM|${zoom}|g"           ${deletefile}

        echo "Running UFNTuple on plot_DarkPhoton_signif_radiuscut_cfg.py for mZd${zdmass}, radius cut = ${radcut} GeV..."
        echo
        #UFNTuple ${deletefile} > output_mZd${zdmass}_radiuscut${radcut}.txt
        UFNTuple ${deletefile}

        #rm ${deletefile}*
    done

done

