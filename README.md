![image](https://github.com/DemisoDaba/Filling_Missed_RF-Data/assets/125874545/4473a5d8-c3b5-462f-b750-dd92db06cdb9)

# Filling_Missed_RF-Data

## Two methods
1. **Arithmetic Mean method**
2. **Inverse Distance.W-Method**

#|File_Names|Descriptions
---|:---:|---
*|[Arithmetic_Mean](./Arithmetic_Mean.py)| This is A python script that creates a graphical user interface (GUI) for filling missing values in a Rainfall dataset using the Arithmetic Mean method.
1|[Arithmetic_IDW](./Arithmetic_IDW-Method.py)| This is A python script that creates a graphical user interface (GUI) for filling missing values in a Rainfall dataset using the Arithmetic Mean and IDW method.

**Important notes**:

This code can work for ``any temporal``, and you can have ``many stations as you want.``
- Your data (**txt & csv only**) must be arranged vertically (column wise)
    - All the first row of your data is considered as the name of the station **default**
    - Any Missed and non-filled cells below the first row is considered as *missed value*.
    - After filled, the script aouthomatically create the folder named as "*filled*",
    - And save the result in the *same destination of loaded file*.
- **In IDW-Method:**
    - The coordinates of each station should be arranged as follows:
        - The Data you loaded and the coordinate you loaded must have the same station name
            - Otherwise, the first cell is considered as the first station name.
        - The first column must be station name
        - The second and third columns must be X and Y coordinate respectivly.
- Examples of data and cordinate arrangment:
  Station_Name|X-cordinate|Y-cordinate
  :---:|---:|---
  Station-A|38.123|7.523
  Station-B|37.235|8.838
  Station-C|36.425|6.987
  Station-D|38.257|7.854

  Station-A|Station-B|Station-C|Station-D
  :---|:---:|---:|---
  0.53|0.35|3.25|0.87
  0.62||0.25|0.36
  0.80|0.98|0.35|0.28
  5.50||4.25|0.68
  0.25|0.35|0.87|0.35

  **Getting Started**

  To use the code, you'll need to:
   - Clone this repository to your local machine.
   
    ```
   git clone https://github.com/DemisoDaba/Filling_Missed_RF-Data.git
    ```
##### © 2023 **Demiso Daba - All rights reserved**
