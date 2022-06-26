INSERT OVERWRITE DIRECTORY 'megapepper_hiveout' 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
SELECT id, case when p.label is null then 0 else p.label end label from hw2_pred p;