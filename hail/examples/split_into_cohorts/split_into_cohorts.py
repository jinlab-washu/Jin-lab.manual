import hail as hl

# Inputs:                                                                                                                                                                    
#    filename: A filename, contains a list of samples separated by line breaks                                                                                                # Outputs:                                                                                                                                                                    
#    Returns a list of samples                                                                                                                                                 
def generate_sample_lists(filename):
    samples = []
    with open(filename, "r") as cohort_file:
        for line in cohort_file:
            stripped_line = line.strip()
            samples.append(stripped_line)
    return samples

# Import the full table                                                                                                                                                        
mt = hl.read_matrix_table('aatd.mt')

# Generate a MatrixTable for SLD
ids = generate_sample_lists('sld.txt')
sld = mt.filter_cols(hl.literal(ids).contains(mt.s))
sld.write('sld.mt')

# Generate a MatrixTable for NLLD
ids = generate_sample_lists('nlld.txt')
nlld = mt.filter_cols(hl.literal(ids).contains(mt.s))
nlld.write('nlld.mt')
