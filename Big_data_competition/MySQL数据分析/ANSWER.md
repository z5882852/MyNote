# 答案
## 1.
环境中已经安装mysql8，用户名root，密码123456，开启数据库服务。
```bash
systemctl start mysqld
mysql -uroot -p123456
```
## 2.
创建数据库employee并使用此数据库
```mysql
create database employee;
use employee;
```
## 3.
在数据库employee下创建数据表employee并导入数据（数据类型参考步骤说明,数据路径`/root/mysql/employee`）；
```mysql
create table employee (
emp_id int primary key,
emp_sex char(40),
emp_email varchar(50),
emp_salary varchar(10),
emp_bonus varchar(10),
emp_job_id int,
emp_dept_id int,
emp_manager varchar(50),
emp_name char(10),
emp_date date
);

load data infile '/tmp/employee.csv' 
into table employee 
fields terminated by ',' 
optionally enclosed by '"' 
lines terminated by '\n'
ignore 1 lines;
```
注：导入的文件需要先复制到/tmp/目录下

## 4.
在数据库employee下创建数据表attendance并导入数据（数据类型参考步骤说明,数据路径`/root/mysql/employee`）；
```mysql
create table attendance (
id int primary key,
check_date date,
emp_id int,
clock_in timestamp,
clock_out timestamp
);

load data infile '/tmp/attendance.csv' 
into table attendance 
fields terminated by ',' 
optionally enclosed by '"' 
lines terminated by '\n'
ignore 1 lines;
```
注：导入的文件需要先复制到/tmp/目录下

## 5.
在数据库employee下创建数据表calendar并导入数据（数据类型参考步骤说明,数据路径`/root/mysql/employee`）；
```mysql
create table calendar (
id int primary key,
calendar_date date,
calendar_year int,
calendar_month int,
calendar_day int,
is_work_day varchar(1)
);

load data infile '/tmp/calendar.csv' 
into table calendar 
fields terminated by ',' 
optionally enclosed by '"' 
lines terminated by '\n'
ignore 1 lines;

```
注：导入的文件需要先复制到/tmp/目录下

## 6.
结合日历信息表，分析打卡记录表attendance中的检查日期(check_date)为工作日还是非工作日，结果存为视图table1。(字段：id check_date is_work_day)
```mysql
CREATE VIEW table1 as
SELECT a.id, a.check_date,c.is_work_day is_work_day FROM attendance a
INNER JOIN calendar c
ON a.check_date = c.calendar_date
WHERE a.check_date IS NOT NULL
order by id;
```
## 7.
查询2021年1月份应出勤的天数（不考虑节假日），将员工姓名和应出勤天数存为视图table2。(字段：emp_name att_days)
```mysql
CREATE VIEW table2 as
SELECT e.emp_name,count(a.emp_id) att_days
FROM attendance a
INNER JOIN employee e
ON a.emp_id = e.emp_id
GROUP BY a.emp_id;
```
## 8.
查询2021年1月所有迟到的人员信息（即早上打卡时间晚于09:00:00），结果存为视图table3。（字段：calendar_date、emp_name、clock_in）
```mysql
CREATE VIEW table3 as
SELECT a.check_date calendar_date, e.emp_name, a.clock_in
FROM attendance a
INNER JOIN employee e
ON a.emp_id = e.emp_id
WHERE HOUR(a.clock_in) >= 9;
```
## 9.
查询2021年1月所有早退的人员信息（即下午打卡时间早于18:00:00）,结果存入视图table4。(字段：calendar_date、emp_name、clock_out)
```mysql
CREATE VIEW table4 as
SELECT a.check_date calendar_date, e.emp_name, a.clock_out
FROM attendance a
INNER JOIN employee e
ON a.emp_id = e.emp_id
WHERE HOUR(a.clock_out) < 18;
```
## 10.
查询所有未打卡的人员信息（即clock_in或者clock_out为MULL），结果存入视图table5。(字段：calendar_date、emp_name、clock_in、clock_out)
```mysql
CREATE VIEW table5 as
SELECT
	t.calendar_date,
	e.emp_name,
	t.clock_in,
	t.clock_out 
FROM
	(
	SELECT
		t1.*,
		NULL AS clock_in,
		NULL AS clock_out 
	FROM
		( SELECT c.calendar_date, e.emp_id FROM calendar c JOIN employee e ON c.is_work_day = "Y" ) t1
		LEFT JOIN ( SELECT check_date, emp_id FROM attendance ) t2 ON t1.calendar_date = t2.check_date 
		AND t1.emp_id = t2.emp_id 
	WHERE
		t2.emp_id IS NULL UNION
	SELECT
		check_date AS calendar_date,
		emp_id,
		clock_in,
		clock_out 
	FROM
		attendance 
	WHERE
		clock_in IS NULL 
		OR clock_out IS NULL 
	) t
	INNER JOIN employee e ON t.emp_id = e.emp_id;
```