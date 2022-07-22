evtool eventfiles="/home/idies/eventfiles/eFEDS/fm00_300007_020_EventList_c001.fits /home/idies/eventfiles/eFEDS/fm00_300008_020_EventList_c001.fits /home/idies/eventfiles/eFEDS/fm00_300009_020_EventList_c001.fits /home/idies/eventfiles/eFEDS/fm00_300010_020_EventList_c001.fits" outfile="/home/idies/eventfiles/filtered_events.fits" region="j2000;circle(137.7836456d,-1.906282902d,0.1d)"
echo "merged eventfiles"
radec2xy  /home/idies/eventfiles/filtered_events.fits 137.7836456 -1.906282902
echo "centered image"
evtool eventfiles="/home/idies/eventfiles/filtered_events.fits" outfile="/home/idies/eventfiles/image5376.fits" emin=0.2 emax=2.3 image=yes rebin=80 size=180  events=no
echo "generated image"
echo "DONE"
