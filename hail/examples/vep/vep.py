import hail as hl

# Read in the MatrixTable
mt = hl.read_matrix_table('table.mt')

# Apply VEP
vep = hl.vep(mt, "vep85-loftee-ruddle-b38.json")

# Write the MatrixTable (you don't want to re-apply VEP every time, it takes ~1 hour)
vep.write('vep_matrixtable.mt')

# Get SNVs
snvs = mt.filter_rows(mt.vep.variant_class == "SNV")

# Filter for specific consequence_terms
snvs.filter_rows(snvs.vep.transcript_consequences.consequence_terms.contains(["missense_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["splice_acceptor_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["splice_donor_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["splice_region_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["start_lost"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["stop_gained"])| snvs.vep.transcript_consequences.consequence_terms.contains(["stop_lost"])).show()

# Filter for rows that do NOT have those consequence_terms
snvs.filter_rows(~(snvs.vep.transcript_consequences.consequence_terms.contains(["missense_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["splice_acceptor_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["splice_donor_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["splice_region_variant"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["start_lost"]) | snvs.vep.transcript_consequences.consequence_terms.contains(["stop_gained"])| snvs.vep.transcript_consequences.consequence_terms.contains(["stop_lost"]))).show()

# Filter for a most_severe_consequence
snvs.filter_rows(snvs.vep.most_severe_consequence == "missense_variant").show()

# Filter for multiple most_severe_consequences
snvs.filter_rows((snvs.vep.most_severe_consequence == "missense_variant") | (snvs.vep.most_severe_consequence == "splice_acceptor_variant")  | (snvs.vep.most_severe_consequence == "splice_donor_variant") | (snvs.vep.most_severe_consequence == "splice_region_variant") | (snvs.vep.most_severe_consequence == "start_lost") | (snvs.vep.most_severe_consequence == "stop_gained") | (snvs.vep.most_severe_consequence == "stop_lost")).show()
