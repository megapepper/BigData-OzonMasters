add file projects/2/predict.py;
add file projects/2/model.py;
add file 2.joblib;
insert overwrite table hw2_pred
select  
    transform(*) using 'predict.py' 
from hw2_test
where if1 > 20 and if1 < 40;