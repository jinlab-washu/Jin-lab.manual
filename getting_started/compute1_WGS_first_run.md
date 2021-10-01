# First run on Compute1 cluster

### Outline:



### Pre-request:

1. Compute1 Access - Using your WUSTL KEY to login!

    ```
    $ ssh {Your_WUSTL _KEY}@compute1-client-3.ris.wustl.edu
    ```

2. Setting your `~/.bashrc`:

    Follow the step below:

    ```
    $ cp /storage1/fs1/jin810/Active/demo/bashrc_demo > ~/.bashrc
    ```

3. Having your data on Storage1

### Running your first variant calling - [Parabricks Germline pipeline](https://docs.nvidia.com/clara/parabricks/v3.5/text/germline_pipeline.html)

1. Copy the demo script (`/storage1/fs1/jin810/Active/demo/pbrun_germline_v3.5.0.1_Demo.sh`) to your $HOME

    ```
    $ cp /storage1/fs1/jin810/Active/demo/pbrun_germline_v3.5.0.1_Demo.sh ~

    ```

2. Open the copied demo script in your $HOME, modify the TEST_NAME and WUSTL_KEY

    ```bash
    // modify pbrun_germline_v3.5.0.1_Demo.sh in your $HOME
    $ vim ~/pbrun_germline_v3.5.0.1_Demo.sh

    // In the pbrun_germline_v3.5.0.1_Demo.sh, find this two variable, and modify it.
    // (If you don't know how to do it, Google "VIM editer")
    TEST_NAME="demo_v1" <- need to modify
    WUSTL_KEY="fup" <- need to modify
    ```

3. Simply RUN the script

    ```
    $ /bin/bash ~/pbrun_germline_v3.5.0.1_Demo.sh
    ```

4. Check `bjobs` to see the job you sent

    ```
    $ bjobs
    ```

### (Advance, optional) Change the demo data set to your project's data set

1. Make a copy of bash script:

    ```
    $ cp ~/pbrun_germline_v3.5.0.1_Demo.sh ~/pbrun_germline_v3.5.0.1_YOUR_PROJECT_NAME.sh
    ```

2. Modify the IN_DIR and other necessary change

    Please make sure your folder structure is same as the demo script, otherwise you need to re-write the loop!

    ```
    $ vim ~/pbrun_germline_v3.5.0.1_Demo.sh
    ...
    IN_DIR=$DEMO_DIR/fastqs/NA12878_WES. <- modify this
    ...
    ```

    If you had any questions, please ask people who familiar with your dataset.
