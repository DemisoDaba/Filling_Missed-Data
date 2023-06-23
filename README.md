![image](https://github.com/DemisoDaba/Filling_Missed_RF-Data/assets/125874545/4473a5d8-c3b5-462f-b750-dd92db06cdb9)

# Filling_Missed_RF-Data

## Two methods
1. **Arithmetic Mean method**
2. **Inverse Distance.W-Method**


- [This --> Arithmetic_Mean.py](./Arithmetic_Mean.py) is A python script that creates a graphical user interface (GUI) for filling missing values in a Rainfall dataset using the Arithmetic Mean method.
- [This is](./Arithmetic_IDW-Method.py) A python script that creates a graphical user interface (GUI) for filling missing values in a Rainfall dataset using the Arithmetic Mean method.

**Important notes**:
- Your data (**txt & csv only**) must be arranged vertically (column wise)
    - The first row of your data is considered as the name of the station **default**
    - Any Missed and non-filled cells below the first row is considered as *missed value*.
    - After filled, the script aouthomatically create the folder named as "*filled*",
    - And save the result in the *same destination of loaded file*.
