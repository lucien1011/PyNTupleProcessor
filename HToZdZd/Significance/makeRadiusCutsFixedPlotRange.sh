#!/bin/bash
#####################################################################################################
## PURPOSE: Produce loads of histograms, each with a certain radius cut applied in the Z2vsZ1 plane.
## SYNTAX:  ./<script.sh> <template_plot_DarkPhoton_script.py>
## NOTES:   Calls on a plot_DarkPhoton template, replaces many values, like mZd, radius cut, etc.
##          Then does UFNTuple on the template. Move on to next radius cut, make more histos.
##          Have a look inside the template file below and make sure it looks good.
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-02-20
## UPDATED: 2019-03-14
#####################################################################################################

#____________________________________________________________________________________________________
# User Parameters
zdmasslist="5" 
#zdmasslist="4 5 6 7 8 9 10 15 20 25 30 35 40 45 50 55 60" 
radcutstart=2.9       # GeV
radcutstop=2.9        # GeV
radcutinterv=0.1     # GeV
binwidth=0.05       # Z2vsZ1 binwidth [GeV]
zoom=0.05           # as a fraction of the radius to better see the full circle: x2-x1=2r+2zoom

outpath="DarkPhotonSR/DataMCDistributions/RadiusCuts/SignifRadiusCut_0p1to3p0in0p1GeVsteps/SignifRadiusCut_mZdZDMASS_radcut0p1to3p0in0p1GeVsteps/"
stdoutfile="output_mZd${zdmass}_radiuscut${radcut}.txt"
#____________________________________________________________________________________________________
# Processes
SAVEOUTPUT=0 # Gets stored in stdoutfile. Optional.
#____________________________________________________________________________________________________
# Main
template="$1"
deletefile="DELETE$template"

for zdmass in $zdmasslist; do

    for radcut in $(seq -w ${radcutstart} ${radcutinterv} ${radcutstop}); do 
        if [ -e ${deletefile} ]; then
            rm ${deletefile}
        fi

        echo 
        echo "Copying template for mZd${zdmass}, radius cut = ${radcut} GeV..."
        cp ${template} ${deletefile}

        sed -i "s|RADIUSCUT|${radcut}|g"        ${deletefile}
        sed -i "s|RADIUSMAX|${radcutstop}|g"    ${deletefile}
        sed -i "s|OUTPATH|${outpath}|g"         ${deletefile} # must come before ZDMASS sed!
        sed -i "s|BINWIDTH|${binwidth}|g"       ${deletefile}
        sed -i "s|ZOOM|${zoom}|g"               ${deletefile}
        sed -i "s|ZDMASS|${zdmass}|g"           ${deletefile}

        echo "Running UFNTuple on ${deletefile} for mZd${zdmass}, radius cut = ${radcut} GeV..."
        echo
        if [ ${SAVEOUTPUT} -eq 1 ]; then 
            UFNTuple ${deletefile} > stdoutfile
        else
            UFNTuple ${deletefile}
        fi

        rm ${deletefile}*
    done

done

