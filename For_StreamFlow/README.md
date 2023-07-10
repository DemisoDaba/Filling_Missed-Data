![image](https://github.com/DemisoDaba/Filling_Missed-Data/assets/125874545/1d335119-c2c4-450f-8d0c-2ac529fb51c8)

# Filling_Missed_SF-Data

#|File_Names|Descriptions
---|:---:|---
*|[Stream Flow](./Fill_Stream_Flow.py)| This is A python script that creates a graphical user interface (GUI) for filling missing values in a steramflow dataset using regression method.

**Important notes**:

This code can work for ``any temporal``
- Your data (**csv only**) must be arranged vertically (column wise)
    - All the first row of your data is considered as the year of the data **default**
    - Any Missed and non-filled cells below the first row is considered as *missed value*.
    - After filled, the script aouthomatically create the file named as "*Sheet_filled.csv*",
    - And save the result in the *same destination of loaded file*.
      
- Examples of data and cordinate arrangment:

  Year-1|Year-2|Year-3|Year-4
  :---|:---:|---:|---
  0.53|0.35|3.25|0.87
  0.62||0.25|0.36
  0.80|0.98|0.35|0.28
  5.50||4.25|0.68
  0.25|0.35|0.87|0.35

  **Getting Started**

  To use the code, you'll need to:
   - Clone this repository to your local machine.

##### © 2023 **Demiso Daba - All rights reserved**
