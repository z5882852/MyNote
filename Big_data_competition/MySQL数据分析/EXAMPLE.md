# 警务出勤数据分析

### 项目背景
**数据以公安部门警务人员考勤管理为背景，对警务考勤信息进行分析，为后续考勤管理解决方案提供依据，以便能够提高警务人员的出勤及时性和工作效率，提升警务服务质量。**

### 数据说明
- 数据路径：/root/mysql/employee
- 数据库：employee

### 员工表：employee
|字段名称|数据类型|说明|示例数据|
|-|-|-|-|
emp_id|int类型，索引ID，可用于主键。|员工ID|1|
emp_sex	char类型，长度40|	员工性别|	男|
emp_email|	varchar类型，长度50|	员工邮箱|	liubei@shuguo.com|
emp_salary|	varchar类型，长度10|	薪水|	30000|
emp_bonus|	varchar类型，长度10|	奖金|	10000|
emp_job_id|	int类型|	工作ID|	1|
emp_dept_id|	int类型|	部门ID|	1|
emp_manager|	varchar类型，长度50|	员工经理|	NULL|
emp_name|	char类型，长度10|	姓名|	刘备|
emp_date|	date类型|	日期|	2000-01-01|

### 打卡记录表：attendance
|字段名称	|数据类型	|说明	|示例数据|
|-|-|-|-|
|id	|int类型，索引ID，可用于主键。	|记录ID	|1|
|check_date	|date类型	|检查日期	|2021-01-04|
|emp_id	|int类型	|员工ID	|1|
|clock_in	|timestamp类型	|上班打卡	|2021-01-04 08:34:02|
|clock_out	|timestamp类型	|下班打卡	|2021-01-04 18:33:12|

### 日历信息表：calendar
|字段名称	|数据类型	|说明	|示例数据|
|-|-|-|-|
|id	|int类型，索引ID，可用于主键。	|记录ID	|1|
|calendar_date	|date类型	|日期	|2021/1/1|
|calendar_year	|int类型	|年	|2021|
|calendar_month	|int类型	|月	|1|
|calendar_day	|int类型	|日	|1|
|is_work_day	|varchar类型，长度1	|是否工作日	|N|

### 数据清洗
数据字段，给出的数据集中已经给出对应的字段，这里无需再做修改。
重复值，数据中已经添加索引作为唯一值，这里无需在做修改。
点击下方按钮，查看题目清单


### 考核条件如下 :
- 1.
环境中已经安装mysql8，用户名root，密码123456，开启数据库服务。
(30/ 30分)

操作环境：
qingjiao
- 2.
创建数据库employee并使用此数据库
(30/ 30分)

操作环境：
qingjiao
- 3.
在数据库employee下创建数据表employee并导入数据（数据类型参考步骤说明,数据路径`/root/mysql/employee`）；
(30/ 30分)

操作环境：
qingjiao
- 4.
在数据库employee下创建数据表attendance并导入数据（数据类型参考步骤说明,数据路径`/root/mysql/employee`）；
(30/ 30分)

操作环境：
qingjiao
- 5.
在数据库employee下创建数据表calendar并导入数据（数据类型参考步骤说明,数据路径`/root/mysql/employee`）；
(30/ 30分)

操作环境：
qingjiao
- 6.
结合日历信息表，分析打卡记录表attendance中的检查日期(check_date)为工作日还是非工作日，结果存为视图table1。(字段：id check_date is_work_day)
(30/ 30分)

操作环境：
qingjiao
- 7.
查询2021年1月份应出勤的天数（不考虑节假日），将员工姓名和应出勤天数存为视图table2。(字段：emp_name att_days)
(30/ 30分)

操作环境：
qingjiao
- 8.
查询2021年1月所有迟到的人员信息（即早上打卡时间晚于09:00:00），结果存为视图table3。（字段：calendar_date、emp_name、clock_in）
(30/ 30分)

操作环境：
qingjiao
- 9.
查询2021年1月所有早退的人员信息（即下午打卡时间早于18:00:00）,结果存入视图table4。(字段：calendar_date、emp_name、clock_out)
(30/ 30分)

操作环境：
qingjiao
- 10.
查询所有未打卡的人员信息（即clock_in或者clock_out为MULL），结果存入视图table5。(字段：calendar_date、emp_name、clock_in、clock_out)
(30/ 30分)

操作环境：
qingjiao