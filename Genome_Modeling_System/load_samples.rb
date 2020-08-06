# Inputs:
#	name: The name of the input sample (not the name of a genome sample object) 
# Outputs:
#	Returns the name of the created individual
def create_individual(name)
  individual = name + '_ind'
  cmd = 'genome individual create --taxon "human" --name=' + individual
  $file.puts(cmd)
  return individual
end

# Inputs:
#	name: The name of the input sample (not the name of a genome sample object) 
#	individual: The name of the individual
# Ouputs:
#	Returns the name of the created sample
def create_sample(name, individual)
  sample = name + '_sample'
  cmd = 'genome sample create --description=' + name + ' --name=' + sample + ' --source=' + individual
  $file.puts(cmd)
  return sample
end

# Inputs:
#	name: The name of the input sample (not the name of a genome sample object)
#	sample: The name of the sample
# Outputs:
#	Returns the name of the created library
def create_library(name, sample)
  library = name + '_library'
  cmd = 'genome library create --sample=' + sample + ' --name=' + library
  $file.puts(cmd)
  return library 
end

# Inputs:
#	path: The directory containing the flagstat file
# Outputs:
#	Returns the read count
def get_read_count(path)
  # TODO: This is not at all portable, assumes the existence of a flagstat file
  count = 0
  Dir.glob(path + '/*.flagstat') do |stats|
    line = File.open(stats) {|f| f.readline}
    line = line.split
    count = line[0]
  end
  return count
end

# Inputs:
#	path: The directory from which to load data
#	project: The name of the analysis project
#	library: The name of the library
#	format: The format of the samples (bam, fastq, etc.)
#	read_count: The number of reads
# Outputs:
#	None
def import_data(path, project, library, format, read_count)
  # TODO: Make the source name an input
  cmd = 'genome instrument-data import trusted-data --analysis-project=' + project + ' --import-source-name="Perlmutter_AATD" --library=' + library + ' --source-directory=' + path + ' --import-format=' + format + ' --read-count=' + read_count.to_s
  $file.puts(cmd)
end

def main
  # TODO: Don't hardcode this
  path = '/gscmnt/gc2738/locke/ITSD-10052'

  proj_name = 'AATD_Project'

  $file = File.open(proj_name + "_commands.txt", "a")

  cmd = 'genome analysis-project create --name "' + proj_name + '" --environment prod-builder'
  $file.puts(cmd)

  Dir.foreach(path) do |filename|
    next if filename == '.' or filename == '..'

    fullpath = path + '/' + filename

    read_count = get_read_count(fullpath)

    individual = create_individual(filename)
    sample = create_sample(filename, individual)
    library = create_library(filename, sample) 

    # TODO: Pass in format, don't assume bam
    import_data(fullpath, proj_name, library, 'bam', read_count)

    $file.puts('')
  end

  $file.close

end

main
