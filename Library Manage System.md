# Library Manage System

# 一、需求分析

在本次课程设计中，基于任务要求，我们设计了一套图书馆管理系统，结合各个方面的考虑，我们认为我们的系统有以下基本需求：

## 1.界面需求

对于我们的图书馆管理系统，我们对于用户的交互体验，总结出了一下几点基本需求：

## 2.功能需求

对于我们的系统，我们对于功能的需求可以基本分为以下大类：

### （1）基本功能要素

主要包括管理图书的库存信息、每一本书的借阅信息以及每一个人的借书信息。

- 每一种图书的库存信息包括编号、书名、作者、出版社、出版日期、金额、类别、总入库数量、当前库存量、已借出本数等。
- 每一本被借阅的书都包括如下信息：编号、书名、金额、借书证号、借书日期、到期日期、罚款金额等。
- 每一个人的借书信息包括借书证号、姓名、班级、学号等。

#### A、借阅资料管理 

要求把书籍、期刊、报刊分类管理，这样的话操作会更加灵活和方便，可以随时对其相 关资料进行添加、删除、修改、查询等操作。

#### B、借阅管理

(1) 借出操作：用户能够通过界面对目标书籍进行检索，查询，选择目标的对象。

(2) 还书操作：用户可以在操作界面对于目标界面，进行选择的书本类型进行归还操作或者是金额补偿操作。

(3) 续借处理：对于已经到达期限的书籍，用户可以在界面内通过金额补偿进行续借。

#### C、读者管理 

读者等级：对借阅读者进行分类处理，例如可分为教师和学生两类。并定义每类读者的可借书数量和相关的借阅时间等信息。

读者管理：对读者信息可以录入，并且可对读者进行挂失或注销、查询等服务的作业。

#### D、统计分析

随时可以进行统计分析，以便及时了解当前的借阅情况和相关的资料状态，统计分析包括借阅排行榜、资料状态统计和借阅统计、显示所有至当日内到期未还书信息 等功能分析。

#### E、系统参数设置

可以设置相关的罚款金额，最多借阅天数等系统服务器参数。

### （2）拓展功能要素

#### 1.信息导出

### （3）移植功能要素

#### 1.本地与云端

### （4）安全功能要素

## 3.性能需求

# 二、总体设计

## 1.逻辑流程设计

## 2.页面逻辑设计

## 3.对象设计

在本次实践中，我们基本分为了三大族类对象：

功能类对象：

界面对象：

异常对象：

## 3.数据库设计

### (1) 本地数据库结构

#### 1）表结构



#### 2）表约束

### (2) 远程数据库结构

#### 1）表结构

#### 2）表约束

# 三、详细设计

## 1.基本对象

### 1.概览

```python

## 基本功能对象

class DataLoader(object)

class LoginUserDataLoader(DataLoader):
    def __init__(self, user, password)

class BasicUser(object):
    def __init__(self, user_id, user_name, role, password)

## 界面显示对象

# 主界面
class Ui_MainWindow(object)
class MainWindow(QMainWindow, Ui_MainWindow)

# 登录界面
class Ui_LoginPage(object)
class LoginPage(QtWidgets.QWidget, Ui_LoginPage)

# 注册界面
class Ui_SignUpPage(object)
class SignUpPage(QtWidgets.QWidget, Ui_SignUpPage)

# 用户界面
class Ui_Form(object)
class UserPage(QtWidgets.QWidget, Ui_Form)

# 借书界面
class Ui_RentingPage(object)
class RentingPage(QtWidgets.QWidget, Ui_RentingPage)

# 归还界面
class Ui_ReturnPage(object)
class ReturnPage(QtWidgets.QWidget, Ui_ReturnPage)

## 异常处理对象
```



### 2.详细介绍

## 2.基本功能函数

### 1.概览



### 2.详细介绍

## 3.数据库结构详解

### (1) 内置数据库

#### 1.表结构

##### 1.Book

```sql
CREATE TABLE Book (
    BookId   CHAR    PRIMARY KEY
                     NOT NULL,
    BookName CHAR,
    Stock    INTEGER DEFAULT (0) 
                     CHECK (Stock >= 0) 
                     NOT NULL,
    Price    INTEGER DEFAULT (0) 
                     CHECK (Price > 0) 
                     NOT NULL,
    TypeId           REFERENCES BookType (TypeId) 
);
```



| Name | Data Type | PK   | FK   | Unique | Check | Default |
| ---- | --------- | ---- | ---- | ------ | ----- | ------- |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |

##### 2.BookType

```sql
CREATE TABLE BookType (
    TypeId   CHAR PRIMARY KEY
                  NOT NULL,
    TypeName CHAR
);
```



| Name | Data Type | PK   | FK   | Unique | Check | Default |
| ---- | --------- | ---- | ---- | ------ | ----- | ------- |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |

##### 3.User

| Name | Data Type | PK   | FK   | Unique | Check | Default |
| ---- | --------- | ---- | ---- | ------ | ----- | ------- |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |

##### 4.UserRole

| Name | Data Type | PK   | FK   | Unique | Check | Default |
| ---- | --------- | ---- | ---- | ------ | ----- | ------- |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |

##### 5.RentHistory

| Name | Data Type | PK   | FK   | Unique | Check | Default |
| ---- | --------- | ---- | ---- | ------ | ----- | ------- |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |
|      |           |      |      |        |       |         |

#### 2.表约束

#### 3.视图设计

#### 4.触发器设计

### (2) 远程链接数据库

#### 1.表结构

#### 2.表约束

#### 3.视图设计

#### 4.触发器设计

#### 5.存储过程设计

# 四、程序运行结果测试与分析

## 1.GUI展示

### （1）普通用户流程展示

#### 1.登录界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\LoginPage.png" style="zoom:25%;" />

##### 1）登录成功

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\Login_Success.png" style="zoom:25%;" />

##### 2）日历界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\LoginPage_2.png" style="zoom:25%;" />

#### 2.注册界面

#### 3.用户界面

##### 1）基本用户信息界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\UserPage.png" style="zoom:25%;" />

##### 2）用户排行榜

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\UserRank.png" style="zoom:25%;" />

##### 3）图书排行榜

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\UserRank.png" style="zoom:25%;" />

#### 4.借阅界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\RentPage.png" style="zoom:25%;" />

#### 5.归还界面

##### 1）初始

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\ReturnPage.png" style="zoom:25%;" />

##### 2）归还操作

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\ReturnAction.png" style="zoom:25%;" />

#### 6.续借界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\PayMoney.png" style="zoom:25%;" />

#### 7.尝试访问管理权限

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\FailOfSuper.png" style="zoom:25%;" />

### （2）超级用户流程展示

## 2.数据输出展示

## 3.数据库内容展示

## 4.软件性能展示

# 五、结论与心得

## 1.任务负责

## 2.收获

### 1) 概念收获

### 2) 技术收获

## 3.遇到困难

## 4.未实现功能