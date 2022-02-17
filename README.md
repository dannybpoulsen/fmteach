# FMTeach   
This is a repository of exercises for the Formal Methods part of the Security course given on Aalborg University in the Spring of 2022. All  of the exercises requires students to add some specific files in the repository. Running

```
python fmteachbin programs/programname.while EXERCISENAME 
```

without having solved the exercise will display which files has to be modified. A description is available by running 
```
python fmteachbin programs/programname.while EXERCISENAME --readme 
```





#Exercises   

|-------------------|------------------------------------------------------------|--------------------|
| Exercisename      | Information                                                | Ready  for solving |
|-------------------|------------------------------------------------------------|--------------------|
| CFAGraph          | [Information](fmteach/exercises/cfa_graph/README.md)       | :heavy_check_mark: |
| ExplicitGraph     | [Information](fmteach/exercises/explicit_graph/README.md)  | :heavy_check_mark: |
| EnumerateExplicit | [Information](fmteach/exercises/enum_explicit/README.md)   | :heavy_check_mark: |
| GenericVM         | [Information](fmteach/exercises/generic_vm/README.md)      | :x:                |
| StateGenerator    | [Information](fmteach/exercises/state_generator/README.md) | :x:                |
|-------------------|------------------------------------------------------------|--------------------|



# Requirements  

colorama==0.4.4  
commonmark==0.9.1  
graphviz==0.19.1  
numpy==1.22.2  
Pygments==2.11.2  
pyparsing==3.0.7  
rich==11.2.0  


The requirements can conveniently be installed with `pip install -r requirements.txt`.


# Solutions  
Solutions to all exercises are available in the repository. Generally files students need to modify are mirrored by an `sol.py`/`_sol.py` file which contains the solution. The solutions can be run with 

```
python fmteachbin programs/programname.while EXERCISENAME --solution
```



