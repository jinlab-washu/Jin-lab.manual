### Convert hg38 variant coordinates to b37 coordinates using GATK LiftoverVCF

*The default WES pipeline used in the jinlab on the WashU clusters uses hg38 for alignment*

> If you are converting hg19 to hg38, replace the following lines in the code below:

> replace `-C /gscmnt/gc2698/jin810/references/Hg38Tob37.over.chain` with `-C /gscmnt/gc2698/jin810/references/hg19ToHg38.over.chain.gz` 

> replace `-R /gscmnt/gc2698/jin810/references/Homo_sapiens_assemblyb37_gatk.fasta` with `-R /gscmnt/gc2698/jin810/references/hg19.fa`

Docker Protocol on Compute0

1. Load the broad institute gatk4 docker image 

    ```bsub -Is -q research-hpc -a 'docker(broadinstitute/gatk:4.1.8.1)' -R "select[mem>30000] rusage[mem=30000]" /bin/bash```
    
2. Run the LiftoverVcf command with your vcf, the Hg38Tob37.over.chain file, and the b37 reference fasta. *Note, the `.fasta` file must accompanied by a `.dict file` in the same directory. The chain file and b37 reference files have already been downloaded to compute0 under `/gscmnt/gc2698/jin810/references`  
        
      Generic Example:
        
        /gatk/gatk LiftoverVcf \
        -C /gscmnt/gc2698/jin810/references/Hg38Tob37.over.chain \
        -I $InputVCF \
        -R /gscmnt/gc2698/jin810/references/Homo_sapiens_assemblyb37_gatk.fasta \
        -O $InputVCF_hg38_liftover_to_b37.vcf.gz \
        --REJECT $InputVCF_hg38_to_b37_rejected.vcf.gz
        
      Where `$InputVCF` is the vcf to be converted. This will produced a "REJECT" file of the records that were unable to be converted to b37.
      
      Specific Example: 
      
        /gatk/gatk LiftoverVcf \
        -C /gscmnt/gc2698/jin810/references/Hg38Tob37.over.chain \
        -I /gscmnt/gc2698/jin810/jointcalling/4c2a1cef13954e8c99ee6edb48a21139/cromwell-executions/JointGenotyping/8c3337c8-7c90-4df8-b2cb-0b0f072ae7a3/call-FinalGatherVcf/execution/IDT_WES_hg38.vcf.gz \
        -R /gscmnt/gc2698/jin810/references/Homo_sapiens_assemblyb37_gatk.fasta \
        -O /gscmnt/gc2698/jin810/jointcalling/4c2a1cef13954e8c99ee6edb48a21139/cromwell-executions/JointGenotyping/8c3337c8-7c90-4df8-b2cb-0b0f072ae7a3/call-FinalGatherVcf/execution/IDT_WES_hg38_liftover_to_b37.vcf.gz \
        --REJECT /gscmnt/gc2698/jin810/jointcalling/4c2a1cef13954e8c99ee6edb48a21139/cromwell-executions/JointGenotyping/8c3337c8-7c90-4df8-b2cb-0b0f072ae7a3/call-FinalGatherVcf/execution/hg38_to_b37_rejected.vcf.gz
