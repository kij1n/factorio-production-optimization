Okay, let’s ditch that idea, it actually made things worse. 
The factory class will know what it needs to output and what will be on input. The whole idea is to construct a master matrix and solve for recipes completed per second 

Factory class
initialization:
- desired output with values 
- provided materials 
- machines, same arguments
- force usage of specific recipes

Workflow
1. Find recipes that will be needed
    1. For supplied ingredients create a dummy recipe that will just have one value and zero as its target
    2. create production instances 
2. create master matrix to find recipes per second
    1. find unique items that will be produced/used
    2. assign an item a column 
    3. prepare each recipe so that coefficients align with ones set in previous step 
    4. also make note which recipe is which row 
    5. transpose the matrix 
    6. since columns are now rows, which means rows are values values to be produced
    7. prepare an output vector, align each item with their corresponding value
3. solve for recipe per second
4. feed value to production instances to find number of machines 


Production class:
initialization:
- calculate actual recipe values, include productivity 
workflow
1. get recipe per second
2. calculate number of machines needed taking speed into account


recipes may have inherent productivity from research but that will be in a recipe class
