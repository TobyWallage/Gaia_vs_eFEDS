from astropy.table import Table

# dat_path = '../matching_tables/five_and_half_arcmin_match.dat'
dat_path = 'matching_tables/five_and_half_arcmin_match.dat'
cluster_table = Table.read(dat_path, format='ascii')

i = 0
current_cluster = None
for row in cluster_table:
    if row['clus_ID_SRC'] == current_cluster:
        continue
    current_cluster = row['clus_ID_SRC']
    ra, dec = row['clus_RA'], row['clust_DEC']
    # print(current_cluster, ra, dec)
    merge_event_string = 'evtool eventfiles="/home/idies/eventfiles/eFEDS/fm00_300007_020_EventList_c001.fits /home/idies/eventfiles/eFEDS/fm00_300008_020_EventList_c001.fits /home/idies/eventfiles/eFEDS/fm00_300009_020_EventList_c001.fits /home/idies/eventfiles/eFEDS/fm00_300010_020_EventList_c001.fits" outfile="/home/idies/eventfiles/filtered_events.fits" '
    region_string = 'region="j2000;circle({RA:.10}d,{DEC:.10}d,0.1d)"'.format(
        RA=ra, DEC=dec)
    center_image_string = 'radec2xy  /home/idies/eventfiles/filtered_events.fits {RA:.10} {DEC:.10}'.format(
        RA=ra, DEC=dec)
    gen_image_string = 'evtool eventfiles="/home/idies/eventfiles/filtered_events.fits" outfile="/home/idies/eventfiles/image{NAME}.fits" emin=0.2 emax=2.3 image=yes rebin=80 size=180  events=no'.format(
        NAME=current_cluster)
    with open("make_bash_script/bash_scripts/generate_image_"+str(current_cluster)+".sh", 'w') as file:
        file.write(merge_event_string+region_string+'\n')
        file.write('echo "merged eventfiles"\n')
        file.write(center_image_string+'\n')
        file.write('echo "centered image"\n')
        file.write(gen_image_string+'\n')
        file.write('echo "generated image"\n')
        file.write('echo "DONE"\n')
