'''
Created on Mar 16, 2017

@author: soufanom
'''

import sys
import numpy as np

def load_options(filename):
        """Parse input options file and store selections of the user in a dictionary options structure.

        Parameters
        ----------
        filename : string value (Default is 'options').
                Name of the file where relevant options to run the programs are listed.
                For example, 'InputType=AID', 'AID=644', 'Features=DWFS', 
                'Classifier=NBC', 'pid=1', etc. 

        Returns
        -------
        options : dictionary structure.
                The key is the name of the option and value is the selection input of the user.
        
        """

        try:
                lines = [lines.strip() for lines in open(filename)]
        except:
                print "\"options\" file is missing. Please create a file \"options\" which contains all needed parameters under the same path of the program."
                return -1 #exit(1)

        options = {}
        # Initialize options to empty. Although not necessary, it helps in other function to directly check
        # if the value is of an option is empty, then, just assume all related values to be selected.
        options['id'] = ''; options['CL_Name'] = ''; options['det_plate'] = '';
        options['det_well'] = ''; options['SM_Dose'] = ''; options['SM_LINCS_ID'] = '';
        options['SM_Name'] = ''; options['SM_Center_Compound_ID'] = ''; options['SM_Time'] = '';
        options['SM_Pert_Type'] = '';
        for l in lines:
                l = l.split('=')
                options[l[0]] = l[1]

        return options
    
def match_cur_field(options, optval, line):
    curlist = []
    print options, optval
    print options[optval]
    if(options[optval] != ''):
        vals = line.split('\t') #.gct is a tab delimited file
        for j in range(len(vals)):
            if(vals[j].find(options[optval]) != -1):
                curlist.append(j)
    return curlist

def find_optval(i):
    optval = ''
    if(i==3):
        optval = 'id'              
    elif(i==4):
        optval = 'CL_Name'
    elif(i==5):
        optval = 'det_plate'
    elif(i==6):
        optval = 'det_well'
    elif(i==7):
        optval = 'SM_Dose'
    elif(i==9):
        optval = 'SM_LINCS_ID'
    elif(i==10):
        optval = 'SM_Name'
    elif(i==11):
        optval = 'SM_Center_Compound_ID'
    elif(i==12):
        optval ='SM_Time'
    elif(i==14):
        optval = 'SM_Pert_Type'
    return optval
    
    
def match_columns(ifname, optfname='options'):
    """Parse header of the input data file and find indices of columns that match with the specified options.
    
    Parameters
    ----------
    ifname : string value.
            Name of the input data file to parse.
        
    optfname : string value (Default is 'options').
            Name of the file where relevant options to run the programs are listed.
            For example, 'CL_Name=MCF7' (i.e. cell line name), 'SM_Name=neratinib' (i.e. drug or chemical molecule name)
    

    Returns
    -------
    match_col_ids : list.
            Holds column ids that corresponds to the selected matched options in the .gct file.
    
    """
    # Checking the format of the input file. This parser is for inputs prepared in .gct format.
    # For more details about .gct format, please check 
    # http://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats
    if(ifname[-4:] != ".gct"):
        print "The input data file is not in .gct format. Please provide the file in the required format."
        exit(1)
    
    '''TO-DO'''
    '''TO-DO'''    
    '''TO-DO: check the file is not only a .gct but also coming from LINCS with specific fields definitions...
        For example, make sure the CL_Name for a cell name is found in the input data file!!!!'''
    '''TO-DO'''
    '''TO-DO''' 
    
    options = load_options(optfname)

    curlist = []
    origlist = []
    with open(ifname) as infile:
        for i, line in enumerate(infile):
            if(len(curlist) != 0):
                if(len(origlist) == 0):
                    origlist = np.asarray(curlist) # first time initialization
                else:
                    origlist = np.intersect1d(origlist, np.asarray(curlist))
            
            if(i>14):
                # Just parse the header
                break
            else:
                optval = find_optval(i)
                curlist = match_cur_field(options, optval, line)
                
    return origlist
                
if __name__=="__main__":

    ifname = "/home/soufanom/Postdoc/Projects/L1000/Data/GSE70138_Broad_LINCS_Level3_INF_mlr12k_n78980x22268_2015-06-30.gct"#sys.argv[0]
    origlist = match_columns(ifname, optfname='options_example')
    print origlist



''' 
For mapping SM_LINCS_ID to PubChem...
http://lincs-dcic.org/metadata/SmallMolecules/LincsID2FacilityID_LINCS_StandardizedCmpds_LSMIDs.txt
http://lincs-dcic.org/metadata/SmallMolecules/CompoundTable_LINCS_StandardizedCmpds_LSMIDs.txt
http://lincs-dcic.org/metadata/SmallMolecules/SampleTable_LincsID2FacilityID2CenterBatchID_LINCS_StandardizedCmpds_LSMIDs.txt
https://thinklab.com/discussion/unichem-mapping-to-lincs-small-molecules/51
'''

'''
bufsize = 65536
with open(path) as infile: 
    while True:
        lines = infile.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            process(line)
'''