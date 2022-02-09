# FMTeach   
This is a repository of exercises for the Formal Methods part of the Security course given on Aalborg University in the Spring of 2022. 




All exercises are accessed by, from the root, running

```
PYTHONPATH=./ python bin/fmteach programs/programname.while EXERCISENAME
```

where `EXERCISENAME` may be one of the following:  
|-------------------|------------------------------------------------------------|--------------------|
| Exercisename      | Information                                                | Ready              |
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
