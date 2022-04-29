# Library Manage System

# 一、需求分析

移动互联网技术在图书馆数字化进程中应用广泛、效果显著，这不仅弥补了传统图书管理模式效率低下、难于管理的不足，还方便了众多读者用户，而图书馆全盘数字化也是未来的发展趋势。

图书馆信息管理系统数据库用以收集、存储书籍信息、人（读者、图书管理员）信息、图书借阅信息以及意外处理信息,及时记录存储各个环节信息的变更,以便管理、查询、显示、输出，节约大量人力物力把人们从繁杂的手工记录方式中解脱出来的同时,有力保障图书馆日常事务的高效运作。

图书管理系统可以极大地提高图书馆日常的运作效率，图书管理员和读者使用此系统进行图书管理、读者管理、图书借还、图书查找、查看借阅记录等功能，增强各方用户体验感，可以将用户从冗杂的数据处理中解放出来。

本文以图书馆管理实际需求出发，分析了具体的需求，设计了各个模块，实现图书借阅管理的人性化、智能化，使图书管理更加规范、方便、快捷，更贴近人们的生活。

本文运用4+1视图方法，针对不同需求进行架构设计。“4+1”视图模型是一个十分通用的模型，可以在每个视图里面定义体系结构的各种组成元素，对于不同的视图还可以选择不同的体系结构风格。

在本文中，“4+1”模型采用UML作为各视图的表达和解释环境, 统一各部分的建模描述语言, 有利于合作开发以及各层次、各环节开发人员之间的沟通, 建立切合实际的模型, 平衡软件质量与开发周期间的矛盾, 加速软件的开发和推广。“4+1”体系结构描述方法与统一建模语言UML的结合, 可以克服目前软件开发两难境地, 提高软件开发和构件重用的效率。

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

在本图书管理系统中，最终用户为图书馆管理员以及借书人，其中，借书人只能进行图书书目查询、图书管理员能进行全部操作，所以要求图书管理员能充分掌握该系统。读者通过图书证可以进行查询图书馆书目，查询自己的借阅信息。管理员可以通过此系统对书进行借出登记、增加/删除新书、查询书目信息 、查询借阅信息的功能。

#### D、统计分析

随时可以进行统计分析，以便及时了解当前的借阅情况和相关的资料状态，统计分析包括借阅排行榜、资料状态统计和借阅统计、显示所有至当日内到期未还书信息 等功能分析。

#### E、系统参数设置

可以设置相关的罚款金额，最多借阅天数等系统服务器参数。

### （2）拓展功能要素

#### 1.信息导出

对于超级用户，允许对数据进行直接的查寻，并且可以通过选择路径的方式，将查询结果的数据导出到excel表格。

### （3）移植功能要素

#### 1.本地与云端

应当设计可以多种数据库方式，可以连接到本地内置服务器，也应当可以通过地址连接到云端服务器。

### （4）安全功能要素

保证只有超级用户可以进行数据的详细修改。

## 3.性能需求

### 数据精确度 

保证查询的查全率和查准率为100%，所有在相应域中包含查询关键字的记录都能查到，所有在相应域中不包含查询关键字的记录都不能查到。 

### 系统响应时间

- n  单个记录查询时间少于3秒

- n  多个记录查询时间少于6秒

- n  更新/保存记录时间少于2秒


### 适应性

满足运行环境在允许操作系统之间的安全转换和与其他应用软件的独立运行要求

### 运行需求

| 需求     |                                                              |
| -------- | ------------------------------------------------------------ |
| 用户界面 | 使用浏览器界面结构，采用导航栏界面方式，尽力带给操作用户便利，对用户友好；对鼠标和键盘单独支持。 |
| 硬件接口 | 本软件需要能够互联网的支撑，用户的硬件平台应该能够与互联网连接。 |
| 软件接口 | 运行于Windows98及更高版本的Windows操作系统之上，或者其他系统。 |
| 故障处理 | 正常使用时不应出错，若运行时遇到不可恢复的系统错误，也必须保证数据库完好无损 |

# 二、总体设计

## 1.逻辑流程设计

## 2.页面逻辑设计

在本次实践中，主要使用pyqt框架进行开发。

`PyQt`实现了一个Python模块集。它有超过300类，将近6000个函数和方法。它是一个多平台的工具包，可以运行在所有主要操作系统上，包括UNIX，Windows和Mac。 `PyQt`采用双许可证，开发人员可以选择GPL和商业许可。在此之前，GPL的版本只能用在Unix上，从`PyQt`的版本4开始，GPL许可证可用于所有支持的平台。

## 3.对象设计

在本次实践中，我们基本分为了三大族类对象：

功能类对象：

界面对象：

异常对象：

## 3.数据库设计

### (1) 本地数据库结构

本项目源码中内置sqlite轻量型数据库，可以提供用户直接使用。

SQLite，是一款轻型的数据库，是遵守ACID的关系型数据库管理系统，它包含在一个相对小的C库中。它是`D.RichardHipp`建立的公有领域项目。它的设计目标是嵌入式的，而且已经在很多嵌入式产品中使用了它，它占用资源非常的低，在嵌入式设备中，可能只需要几百K的内存就够了。它能够支持Windows/Linux/Unix等等主流的操作系统，同时能够跟很多程序语言相结合，比如 `Tcl`、C#、PHP、Java等，还有ODBC接口，同样比起`Mysql`、PostgreSQL这两款开源的世界著名数据库管理系统来讲，它的处理速度比他们都快。SQLite第一个Alpha版本诞生于2000年5月。 至2021年已经接近有21个年头，SQLite也迎来了一个版本 SQLite 3已经发布。

#### 1）表结构

#### 2）表约束

### (2) 远程数据库结构

本系统同时支持SQL server数据库，并且支持远程连接。

SQL Server 是Microsoft 公司推出的关系型数据库管理系统。具有使用方便可伸缩性好与相关软件集成程度高等优点，可跨越从运行Microsoft Windows 98 的膝上型电脑到运行Microsoft Windows 2012 的大型多处理器的服务器等多种平台使用。

Microsoft SQL Server 是一个全面的数据库平台，使用集成的商业智能 (BI)工具提供了企业级的数据管理。Microsoft SQL Server 数据库引擎为关系型数据和结构化数据提供了更安全可靠的存储功能，使您可以构建和管理用于业务的高可用和高性能的数据应用程序。

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

#### 1)Query

```python
def Query_UserRentingHis(user_id)

def Query_BookRank()

def Query_UserRank()

def Query_BookType()

def Query_BookType_Id()

def Query_Book(TypeName, BookInfo)

def Query_UnReturned_Book(UserId)

def Query_Price_Remain(UserId, BookId=None, RentDate=None)

def Modify_Return(tar)

def RentCertification(UserId, BookId) -> bool

def Add_RentHis(UserId, BookId)

def Add_Book(BookId, BookName, stock, price, BookType)

def Add_BookType(Id, Name)

def Add_User(UserId, UserName, Role, Password)

def Update_UserInfo(pack)

def Update_RentDate(UserId, BookId, RentDate)

def Update_BookInfo(pack)

def FetchAllBooks()

def FetchAllBookType()

def FetchAllRoleTypes()

def FetchAllUser()
```



### 2.详细介绍

#### (1)数据库访问函数

数据库访问函数状态控制：

```python
QueryMethod = 'sqlite'
# QueryMethod = 'sql_server'

if QueryMethod == 'sqlite':
    from kernel.QueryInfoSite.QueryInfo_sqlite import *
elif QueryMethod == 'sql_server':
    from kernel.QueryInfoSite.QueryInfo_MsSql import *
```

双内核处理方式，支持多种数据库类型访问。在修改参数后，会修改数据库访问函数的细节调用。

##### `def Query_UserRentingHis(user_id)`

该函数通过调用user_id，对数据库进行访问。会被User对象调用。

返回`Book.BookId, Book.BookName, BookType.TypeName, RentHistory.RentDay, RentHistory.ReturnDate`

每一条记录代表着某个用户的借阅历史记录。

| param   | type | description                                        |
| ------- | ---- | -------------------------------------------------- |
| user_id | str  | 用户的账号                                         |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况     |

##### `def Query_BookRank()`

该函数对数据库内容进行标准化访问。

返回查询结果结构：`Book.BookId, BookName, times, Stock, Price, TypeName`

按照借阅次数降序排序。

| param   | type | description                                        |
| ------- | ---- | -------------------------------------------------- |
| None    | None | 无传入参数                                         |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况     |

##### `def Query_UserRank()`

该函数对数据库内容进行标准化访问，与`Query_BookRank`类似。

返回查询结果结构：`UserName, User.UserId, times`

按照借阅次数降序排序。

| param   | type | description                                                  |
| ------- | ---- | ------------------------------------------------------------ |
| None    | None | 无传入参数                                                   |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况               |

##### `def Query_BookType()`

同族类似功能函数有：

1. `def Query_BookType_Id()`
2. `def FetchAllBookType()`

获取Type信息。

| param   | type | description                                                  |
| ------- | ---- | ------------------------------------------------------------ |
| None    | None | 无传入参数                                                   |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行Dict封装。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况               |

##### `def Query_Book(TypeName, BookInfo)`

该函数用于查询书本列表，按照书本的类型以及书本名称（可以不用完全相等）来查找书籍。

| param      | type | description                                                  |
| ---------- | ---- | ------------------------------------------------------------ |
| `TypeName` | str  | 书本类型名称                                                 |
| `BookInfo` | str  | 书本名称部分切片                                             |
| returns    | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws     | none | 不会抛出异常，但是当访问出错时，会打印异常状况。             |

##### `def Query_UnReturned_Book(UserId)`

按照`UserId`从数据库中查询用户尚未归还的书籍。

| param    | type | description                                                  |
| -------- | ---- | ------------------------------------------------------------ |
| `UserId` | str  | 读者号                                                       |
| returns  | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws   | none | 不会抛出异常，但是当访问出错时，会打印异常状况。             |

##### `def Query_Price_Remain(UserId, BookId=None, RentDate=None)`

借阅的记录由`UserId`，`BookId`以及借阅日期决定。

该函数有可选性功能，当未传入`BookId`时，会搜索数据库中该用户所有的未归还记录，并且获得欠款数据。

当传入了`BookId`数据，则指定了目标条目所带来的数据欠款数据。

```python
    req = """
        select * from UnreturnPrice
        where UserId = {}
        """.format(str(UserId))

    if BookId is not None:
        req += " and BookId = '{}".format(str(BookId))

    if RentDate is not None:
        req += " and RentDay = '{}'".format(str(RentDate))
```

| param      | type                                | description                                                  |
| ---------- | ----------------------------------- | ------------------------------------------------------------ |
| `UserId`   | str                                 | 读者的id                                                     |
| `BookId`   | str，default：none                  | 对应的图书id                                                 |
| `RentDate` | str，在数据库中会自动转换为date类型 | 借阅日期                                                     |
| returns    | list                                | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws     | none                                | 打印发生的异常状态                                           |

##### `def Modify_Return(tar)`

```python
    UserId, BookId, RentDate = tar
```

该函数通过

| param   | type                | description                                                  |
| ------- | ------------------- | ------------------------------------------------------------ |
| tar     | tuple 或者list      | 输入参数，必须为三元组或者是长度为3的列表，内容分别为`UserId`, `BookId`, `RentDate` |
| returns | none                | 打印借阅成功信息                                             |
| throws  | ReturnRefuse        | 异常，表示传入数据包不符合要求                               |
| throws  | `sql.DatabaseError` | 数据库访问异常，需要在外部捕获，表示访问失败                 |

##### `def RentCertification(UserId, BookId) -> bool`

本地数据库使用，由于sqlite不支持复杂的触发器操作，则使用函数进行详细约束。

该函数进行借阅验证，测试当前用户是否还有借阅量剩余，是否有过期图书。

两次验证失败时均会抛出拒绝借阅异常。

| param    | type                           | description                      |
| -------- | ------------------------------ | -------------------------------- |
| `UserId` | str                            | 读者id                           |
| `BookId` | str                            | 书本id                           |
| returns  | bool                           | 是否有效                         |
| throws   | `RentRefuse("too many books")` | 借阅验证失败，超出借阅额度       |
| throws   | `RentRefuse("no book remain")` | 借阅验证失败，图书馆没有剩余书目 |
| throws   | `sql.DatabaseError`            | 数据库访问异常，在外部抓取       |

##### `def Add_RentHis(UserId, BookId)`

该函数实现借阅功能，会调用`RentCertification`进行借阅有效性的验证。

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def Add_Book(BookId, BookName, stock, price, BookType)`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def Add_BookType(Id, Name)`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def Add_User(UserId, UserName, Role, Password)`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def Update_UserInfo(pack)`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def Update_RentDate(UserId, BookId, RentDate)`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def Update_BookInfo(pack)`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def FetchAllBooks()`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def FetchAllRoleTypes()`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

##### `def FetchAllUser()`

| param | type | description |
| ----- | ---- | ----------- |
|       |      |             |
|       |      |             |
|       |      |             |

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

书本表，存储书本的基本数据。每一本书对应一条唯一的书本id，同时对应一条该表内的记录。

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

书本类型，将书本按照不同类型分类的表，存放书本的类型。每一条记录记录一种书本类型。

| Name       | Data Type | PK   | FK   | Unique | Check    | Default |
| ---------- | --------- | ---- | ---- | ------ | -------- | ------- |
| `TypeId`   | CHAR      | true |      |        | not null |         |
| `TypeName` | CHAR      |      |      |        |          |         |

##### 3.User

```sql
CREATE TABLE User (
    UserId   CHAR PRIMARY KEY
                  NOT NULL,
    UserName CHAR,
    Role          REFERENCES UserRole (RoleId) 
                  NOT NULL,
    Password CHAR NOT NULL
                  DEFAULT (0) 
);
```

User表存储所有的读者与管理人员信息。

| Name       | Data Type | PK   | FK                               | Unique | Check    | Default |
| ---------- | --------- | ---- | -------------------------------- | ------ | -------- | ------- |
| `UserId`   | CHAR      | true |                                  |        |          |         |
| `UserName` | CHAR      |      |                                  |        | not null |         |
| `Role`     |           |      | REFERENCES `UserRole` (`RoleId`) |        | not null |         |
| `Password` | CHAR      |      |                                  |        | not null |         |

##### 4.UserRole

```sql
CREATE TABLE UserRole (
    RoleId       NUMERIC PRIMARY KEY ASC,
    RoleName     CHAR    NOT NULL,
    Duration     TIME    NOT NULL,
    LendingTimes INT     NOT NULL
);
```



| Name           | Data Type | PK   | FK   | Unique | Check | Default |
| -------------- | --------- | ---- | ---- | ------ | ----- | ------- |
| `RoleId`       |           |      |      |        |       |         |
| `RoleName`     |           |      |      |        |       |         |
| `Duration`     |           |      |      |        |       |         |
| `LendingTimes` |           |      |      |        |       |         |

该表正常情况下，不允许添加新项目，固定信息如下：

| Role       |      |      |
| ---------- | ---- | ---- |
| Super User |      |      |
| Teacher    |      |      |
| Students   |      |      |

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

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\LoginPage.png" style="zoom: 50%;" />

##### 1）登录成功

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\Login_Success.png" style="zoom: 50%;" />

##### 2）日历界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\LoginPage_2.png" style="zoom: 50%;" />

#### 2.注册界面

#### 3.用户界面

##### 1）基本用户信息界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\UserPage.png" style="zoom: 50%;" />

##### 2）用户排行榜

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\UserRank.png" style="zoom: 50%;" />

##### 3）图书排行榜

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\UserRank.png" style="zoom: 50%;" />

#### 4.借阅界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\RentPage.png" style="zoom: 50%;" />

#### 5.归还界面

##### 1）初始

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\ReturnPage.png" style="zoom: 50%;" />

##### 2）归还操作

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\ReturnAction.png" style="zoom: 50%;" />

#### 6.续借界面

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\PayMoney.png" style="zoom:80%;" />

#### 7.尝试访问管理权限

<img src="D:\Coding\PythonProjects\Library_Manage_System\DisplayPics\GeneralUser\FailOfSuper.png" style="zoom: 50%;" />

### （2）超级用户流程展示

## 2.数据输出展示

## 3.数据库内容展示

## 4.软件性能展示

# 五、结论与心得

## 1.任务负责

在本次的课程实践中，我负责该管理系统的全部的设计与实现工作。包括但不限于以下工作：

1. 数据库ER模型设计
2. 数据库模型编码实现
3. UI界面设计
4. UI界面前端绘制
5. 业务逻辑设计
6. 业务逻辑编码实现
7. 成果测试检验

## 2.收获

### 1) 概念收获

在本次的程序设计课程设计中，我收获了许多。首先是

### 2) 技术收获

## 3.遇到困难

## 4.未实现功能