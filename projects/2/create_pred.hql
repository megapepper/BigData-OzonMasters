create table hw2_pred(
    id int,
    label int
)
row format delimited
fields terminated by '\t'
stored as textfile
location 'megapepper_hw2_pred';