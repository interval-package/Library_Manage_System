# Library Manage System

[TOC]



# 一、需求分析

移动互联网技术在图书馆数字化进程中应用广泛、效果显著，这不仅弥补了传统图书管理模式效率低下、难于管理的不足，还方便了众多读者用户，而图书馆全盘数字化也是未来的发展趋势。

图书馆信息管理系统数据库用以收集、存储书籍信息、人（读者、图书管理员）信息、图书借阅信息以及意外处理信息,及时记录存储各个环节信息的变更,以便管理、查询、显示、输出，节约大量人力物力把人们从繁杂的手工记录方式中解脱出来的同时,有力保障图书馆日常事务的高效运作。

图书管理系统可以极大地提高图书馆日常的运作效率，图书管理员和读者使用此系统进行图书管理、读者管理、图书借还、图书查找、查看借阅记录等功能，增强各方用户体验感，可以将用户从冗杂的数据处理中解放出来。

本文以图书馆管理实际需求出发，分析了具体的需求，设计了各个模块，实现图书借阅管理的人性化、智能化，使图书管理更加规范、方便、快捷，更贴近人们的生活。

本文运用4+1视图方法，针对不同需求进行架构设计。“4+1”视图模型是一个十分通用的模型，可以在每个视图里面定义体系结构的各种组成元素，对于不同的视图还可以选择不同的体系结构风格。

在本文中，“4+1”模型采用UML作为各视图的表达和解释环境, 统一各部分的建模描述语言, 有利于合作开发以及各层次、各环节开发人员之间的沟通, 建立切合实际的模型, 平衡软件质量与开发周期间的矛盾, 加速软件的开发和推广。“4+1”体系结构描述方法与统一建模语言UML的结合, 可以克服目前软件开发两难境地, 提高软件开发和构件重用的效率。

在本次课程设计中，基于任务要求，我们设计了一套图书馆管理系统，结合各个方面的考虑，我们认为我们的系统有以下基本需求：

## 界面需求

用户界面是人与计算机之间的媒介。用户通过用户界面来与计算机进行信息交换。因此，用户界面的质量，直接关系到应用系统的性能能否充分发挥，能否使用户准确、高效、轻松、愉快地工作。所以软件的友好性、易用性对于软件系统至关重要。

对于我们的图书馆管理系统，我们对于用户的交互体验，总结出了一下几点基本需求：

### 界面元素

通常一个用户界面的元素包括界面主颜色、字体颜色、字体大小、界面布局、界面交互方式、界面功能分布、界面输入输出模式。其中，对用户工作效率有显著影响的元素包括：输入输出方式、交互方式、功能分布。

软件界面作为一个整体，其中任何一个元素不符合用户习惯、不满足用户要求都将降低用户对软件系统的认可度，甚至影响用户的工作效率，而使用户最终放弃使用系统。

对于我们的图书馆管理系统：

- 界面应当精简而又能够覆盖所有的功能需求。
- 每个相应功能要进行分页管理。
- 页面转跳功能要全面。
- 用户能自由的对界面上的每一项做出选择，且所有选择都是可逆的。在用户做出危险的选择时有信息提示是减少用户错误的有效方法。

### 用户角色

想他们所想，做他们所做。用户总是按照他们自己的方法理解和使用。在界面设计中采用以用户为中心的设计方法（*User Centered Design*），让用户真正参与到界面设计当中来。在最终界面设计中体现用户的想法，是设计出让用户满意的用户界面的关键。

对于我们的图书管理系统，我们主要面对：

- 学生用户
- 教师用户
- 图书管理员用户
  - 对于管理员用户，我们要允许高级操作

![](.\DisplayPics\Process_pic\UserRole.png)

## 功能需求

对于我们的系统，我们对于功能的需求可以基本分为以下大类：

### 基本功能要素

主要包括管理图书的库存信息、每一本书的借阅信息以及每一个人的借书信息。

- 每一种图书的库存信息包括编号、书名、作者、出版社、出版日期、金额、类别、总入库数量、当前库存量、已借出本数等。
- 每一本被借阅的书都包括如下信息：编号、书名、金额、借书证号、借书日期、到期日期、罚款金额等。
- 每一个人的借书信息包括借书证号、姓名、班级、学号等。

#### 借阅资料管理 

要求把书籍、期刊、报刊分类管理，这样的话操作会更加灵活和方便，可以随时对其相 关资料进行添加、删除、修改、查询等操作。

#### 借阅管理

(1) 借出操作：用户能够通过界面对目标书籍进行检索，查询，选择目标的对象。

(2) 还书操作：用户可以在操作界面对于目标界面，进行选择的书本类型进行归还操作或者是金额补偿操作。

(3) 续借处理：对于已经到达期限的书籍，用户可以在界面内通过金额补偿进行续借。

#### 读者管理 

读者等级：对借阅读者进行分类处理，例如可分为教师和学生两类。并定义每类读者的可借书数量和相关的借阅时间等信息。

读者管理：对读者信息可以录入，并且可对读者进行挂失或注销、查询等服务的作业。

在本图书管理系统中，最终用户为图书馆管理员以及借书人，其中，借书人只能进行图书书目查询、图书管理员能进行全部操作，所以要求图书管理员能充分掌握该系统。读者通过图书证可以进行查询图书馆书目，查询自己的借阅信息。管理员可以通过此系统对书进行借出登记、增加/删除新书、查询书目信息 、查询借阅信息的功能。

#### 统计分析

随时可以进行统计分析，以便及时了解当前的借阅情况和相关的资料状态，统计分析包括借阅排行榜、资料状态统计和借阅统计、显示所有至当日内到期未还书信息 等功能分析。

#### 系统参数设置

可以设置相关的罚款金额，最多借阅天数等系统服务器参数。

### 拓展功能要素

#### 信息导出

对于超级用户，允许对数据进行直接的查寻，并且可以通过选择路径的方式，将查询结果的数据导出到excel表格。

### 移植功能要素

#### 本地与云端

应当设计可以多种数据库方式，可以连接到本地内置服务器，也应当可以通过地址连接到云端服务器。

<img src=".\DisplayPics\Process_pic\本地与云端.png" style="zoom:50%;" />

### 安全功能要素

保证只有超级用户可以进行数据的详细修改。

保证只有超级用户可以进入权限管理界面，或者对数据库进行直接的修改。

![](.\DisplayPics\Process_pic\Safety.png)

## 性能需求

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

## 逻辑流程设计

### 登录逻辑流程

![](.\DisplayPics\Process_pic\login_logic.png)

### 借阅流程逻辑

![](.\DisplayPics\Process_pic\rentting_logic.png)

### 管理员权限流程

![](.\DisplayPics\Process_pic\superpage_logic.png)



## 页面逻辑设计

在本次实践中，主要使用pyqt框架进行开发。

`PyQt`实现了一个Python模块集。它有超过300类，将近6000个函数和方法。它是一个多平台的工具包，可以运行在所有主要操作系统上，包括UNIX，Windows和Mac。 `PyQt`采用双许可证，开发人员可以选择GPL和商业许可。在此之前，GPL的版本只能用在Unix上，从`PyQt`的版本4开始，GPL许可证可用于所有支持的平台。

<img src=".\DisplayPics\Outter\qt.png" style="zoom: 50%;" />

### 用户界面逻辑流程

![](.\DisplayPics\Process_pic\user_page_logic.png)

## 对象设计

在本次实践中，我们基本分为了三大族类对象：

- 功能类对象
- 界面类对象
- 异常类对象

### 功能类对象：

主要负责数据的存储以及与数据库之间的数据交互。

![](.\DisplayPics\obj_pic\basic_util_class.png)

### 界面对象：

由于我们使用的是Qt框架，所以每个界面都是以类的形式定义。在不同的类与对象之间，存在着嵌套与继承的关系，基本关系如下图关系图所示。

![](.\DisplayPics\obj_pic\page_objs.png)

### 异常对象：

在程序设计的过程中，由于用户的不安全操作，或者是一部分正常的但是不满足要求以至于被拒绝的操作，会导致程序出现异常。

同时，我们通过异常来传递请求失败的信息，通过异常处理，来形成错误弹窗。主要使用qt原生错误族类，以及sql错误族类。

## 数据库设计

### 本地数据库结构

本项目源码中内置sqlite轻量型数据库，可以提供用户直接使用。

SQLite，是一款轻型的数据库，是遵守ACID的关系型数据库管理系统，它包含在一个相对小的C库中。它是`D.RichardHipp`建立的公有领域项目。它的设计目标是嵌入式的，而且已经在很多嵌入式产品中使用了它，它占用资源非常的低，在嵌入式设备中，可能只需要几百K的内存就够了。它能够支持Windows/Linux/Unix等等主流的操作系统，同时能够跟很多程序语言相结合，比如 `Tcl`、C#、PHP、Java等，还有ODBC接口，同样比起`Mysql`、PostgreSQL这两款开源的世界著名数据库管理系统来讲，它的处理速度比他们都快。SQLite第一个Alpha版本诞生于2000年5月。 至2021年已经接近有21个年头，SQLite也迎来了一个版本 SQLite 3已经发布。

![](.\DisplayPics\Outter\sqlite.png)

### 远程数据库结构

本系统同时支持SQL server数据库，并且支持远程连接。

SQL Server 是Microsoft 公司推出的关系型数据库管理系统。具有使用方便可伸缩性好与相关软件集成程度高等优点，可跨越从运行Microsoft Windows 98 的膝上型电脑到运行Microsoft Windows 2012 的大型多处理器的服务器等多种平台使用。

Microsoft SQL Server 是一个全面的数据库平台，使用集成的商业智能 (BI)工具提供了企业级的数据管理。Microsoft SQL Server 数据库引擎为关系型数据和结构化数据提供了更安全可靠的存储功能，使您可以构建和管理用于业务的高可用和高性能的数据应用程序。

![image-20220516095610379](.\DisplayPics\Outter\sql_server.png)

# 三、详细设计

## 基本对象

### 概览

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
```



### 详细介绍

#### 基本功能对象

##### `DataLoader`

初始化数据库，用于导入数据。封装数据库访问接口，适配云端与本地服务。

![](.\DisplayPics\obj_pic\dataloader.png)

##### `BasicUser`

用户对象模型：

| field             |                |
| ----------------- | -------------- |
| user info         | 基础的用户信息 |
| user rent history | 用户的借阅信息 |

#### 界面显示对象

对于每个界面，我们都有两个界面类，负责不同功能。

```
UI_Page
负责界面内容ui的绘制与初始化。

Page_Wrapper
时UI_Page的子类，在UI_Page初始化ui的前提下，实现逻辑功能与转跳。
```

##### 主界面

```python
class Ui_MainWindow(object)
class MainWindow(QMainWindow, Ui_MainWindow)
```

`def __init__(self)`

初始化函数，负责承接UI类的内容初始化。

| param   | type | description |
| ------- | ---- | ----------- |
| returns | none | 无返回      |

`def setIcon(self)`

设置标签函数，设置我们函数的标签

| param   | type | description |
| ------- | ---- | ----------- |
| returns | none | 无返回      |

`def switchPage(self, index)`

页面切换函数，进行一级主界面的转换与加载。

使用`class QStackedWidget(QFrame)`进行切换，所有的页面内容挂载其中。

| param   | type        | description        |
| ------- | ----------- | ------------------ |
| index   | int         | 需要切换的页面编号 |
| throws  | index error |                    |
| returns | none        |                    |

`def LoginPage_Login(self)`

登录界面主要逻辑。

调用`self.LoginPage.Login()`进行用户的登录逻辑。

传递参数到其他页面。

| param   | type | description                        |
| ------- | ---- | ---------------------------------- |
| returns | none | 通过图形化界面的文本框获得输入信息 |

`def SuperUserAction(self)`

当用户尝试访问超级控制，判断是否拥有权限进行管理页面的访问。

| param   | type | description            |
| ------- | ---- | ---------------------- |
| returns | none |                        |
| throws  | none | 当非法访问时，弹出弹窗 |

**报错函数**

`def Echo_Fail_Authority(self)`

回显函数，在尝试进行超级用户操作，被拒绝的时候，进行调用。

弹出错误弹窗，告知用户信息。

![image-20220513185458590](.\DisplayPics\pop up\super fail.png)

| param   | type     | description                        |
| ------- | -------- | ---------------------------------- |
| returns | none     |                                    |
| pop up  | error    |                                    |
| throws  | printing | no exception throws, but printing. |

`def SignUpPage_SignUpAction_Bind(self)`

绑定功能，在注册界面进行注册的操作。访问界面中的文本输入框，获取信息，访问数据库添加数据。

| param   | type | description                                  |
| ------- | ---- | -------------------------------------------- |
| returns | none | 将登录逻辑绑定到目标结构上，初始化登录逻辑。 |

##### 登录界面

```python
class Ui_LoginPage(object)
class LoginPage(QtWidgets.QWidget, Ui_LoginPage)
```

`def Login(self)`

`def LoginResult(self, user_id: str, password: str)`

**报错函数**

1. `def Echo_Login_Failed(self)`
2. `def Echo_Login_Empty(self)`

3. `def Echo_Login_Success(self)`
4. `def MultiUserErrorFind(self)`

| param   | type | description                            |
| ------- | ---- | -------------------------------------- |
| returns | none |                                        |
| pop up  |      | 调用标准错误提示窗口，显示当前错误信息 |

##### 注册界面

```python
class Ui_SignUpPage(object)
class SignUpPage(QtWidgets.QWidget, Ui_SignUpPage)
```

`def SignUp_Action(self)`

从文本框获取信息，进行注册访问。

| param   | type | description |
| ------- | ---- | ----------- |
| returns | none |             |

`def Echo_Empty_Input(self)`

当注册失败时调用，弹出注册失败的相关内容。

| param   | type | description                      |
| ------- | ---- | -------------------------------- |
| returns | none | 进行弹窗，显示错误，或者成功信息 |

##### 用户界面

```python
class Ui_Form(object)
class UserPage(QtWidgets.QWidget, Ui_Form)
```

`def SetUser(self, user)`

外部传参函数，用于初始化内部的用户对象。

`def updatePage(self)`

刷新页面函数，调用其他组件刷新函数，更新页面输入框图内容。

`def updateUserInfoList(self)`

更新页面中用户信息的显示，会调用以下函数

- `def updateRentedBookInfoList(self)`
- `def updateBookRankPage(self)`

- `def updateUserRankPage(self)`

对于所有函数有：

| param   | type | description              |
| ------- | ---- | ------------------------ |
| returns | none | 无返回，但是修改页面内容 |

`def CallPayPage(self)`

调用支付所有欠款的页面。

##### 借书界面

```python
class Ui_RentingPage(object)
class RentingPage(QtWidgets.QWidget, Ui_RentingPage)
```

`def setUser(self, User)`

外部传参函数，用于初始化内部的用户对象。

`def SetBookType(self)`

初始化选项框，提供书本类型名称与id的匹配。

`def updateRentedBookInfoList(self)`

根据查询结果，更新已经借阅了的书本信息。

**核心功能函数**

`def Query(self)`

`def Rent(self)`

| param   | type | description                                                |
| ------- | ---- | ---------------------------------------------------------- |
| returns | none | 进行弹窗，显示错误，或者成功信息，会对可视化界面进行修改。 |
| query   |      | 会对数据库进行访问                                         |

核心功能函数负责页面核心功能，即借阅功能的实现。

基本逻辑流程如下。

![](.\DisplayPics\obj_pic\rentAndQuery.png)

**报错函数**

`def Echo_Empty_Input(self, ms=None)`

`def Echo_Success_Not(self, flag)`

`def Echo_Fail_To_Rent(self)`

| param   | type | description                      |
| ------- | ---- | -------------------------------- |
| returns | none | 进行弹窗，显示错误，或者成功信息 |

##### 归还界面

```python
class Ui_ReturnPage(object)
class ReturnPage(QtWidgets.QWidget, Ui_ReturnPage)
```

`def SetUser(self, User)`

设置用户数据。

`def updatePage(self) -> None`

更新页面信息。

1. `def updateRentedBookInfoList(self) -> None`
   - 更新已经借阅信息表格。

`def ReturnBook(self)`

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| inputs  | none | 从表格中获取信息 |

##### 权限界面

```python
class Ui_SuperPage(object)
class SuperPage(QtWidgets.QWidget, Ui_SuperPage)
```

`def switchPage(self, index)`

进行挂载页面的切换。

![](.\DisplayPics\obj_pic\superpage.png)

##### 信息查询界面

```python
class Ui_CheckInfoPage(object)
class CheckInfoPage(QtWidgets.QWidget, Ui_CheckInfoPage)
```

`def SetTypeListDict(self)`

进行类型的绑定。将可选择进行的功能与目标函数进行绑定。

**页面刷新函数**

- `def RefreshPageInfo(self)`
  - 总刷新函数，刷新页面所有内容

- `def RefreshUserList(self)`
  - 刷新用户列表信息

- `def RefreshBookList(self)`
  - 刷新图书列表信息

- `def updateBookRankPage(self) -> None`
  - 刷新排名页

- `def SetBookType(self)`

此类函数负责页面的刷新内容

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| inputs  | none | 从表格中获取信息 |

`def MessageOfGettingPath(self, Filepath=None)`

调用内置功能模块，获取用户选择路径。

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | str  | 目标路径         |
| inputs  | none | 从表格中获取信息 |

<img src=".\DisplayPics\SuperUser\SaveBook.png" style="zoom:50%;" />



**核心功能函数**

`def SaveQuery(self)`

保存函数，调用pandas的data frame，将目标结构保存到目标地址。创建一个新的excel文件。

`def Query(self)`

查询函数

`def Query_User(self)`

<img src=".\DisplayPics\pages\checkinfo.png" alt="image-20220516104038630" style="zoom:50%;" />

##### 修改用户界面

```python
class Ui_UserEditPage(object)
class UserEditPage(QtWidgets.QWidget, Ui_UserEditPage)
```

`def CommandCommit(self)`

`def RefreshViews(self)`

**更新页面函数**

`def UpdateRoleView(self)`

`def UpdateUserView(self)`

`def SetBookType(self)`

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| inputs  | none | 从表格中获取信息 |
| action  |      | 刷新多个页面     |

**核心功能函数**

- `def ChangeUserInfoAction(self)`
  - 修改用户信息
- `def AddUserAction(self)`
  - 添加用户

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| inputs  | none | 从表格中获取信息 |

核心函数调用逻辑如下：

<img src=".\DisplayPics\Process_pic\edituser.png" style="zoom:67%;" />

**报错函数**

- `def Echo_Empty_Input(self, ms=None)`

- `def Echo_Fail(self, ms)`

- `def Echo_Success(self)`

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| inputs  | none | 从表格中获取信息 |

<img src=".\DisplayPics\pages\useredit.png" alt="image-20220516104141857" style="zoom:50%;" />

##### 修改书籍界面

```python
class Ui_BookEditPage(object)
class BookEditPage(QtWidgets.QWidget, Ui_BookEditPage)
```

**基本刷新函数**

- `def RefreshViews(self)`
- `def SetBookType(self)`

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| inputs  | none | 从表格中获取信息 |

**核心功能函数**

`def AddBookType(self)`

`def ChangeBookAction(self)`

`def AddBookAction(self)`

| param   | type | description          |
| ------- | ---- | -------------------- |
| returns | none |                      |
| inputs  | none | 从表格中获取信息     |
| action  |      | 访问数据库，修改信息 |

**报错函数**

1. `def Echo_Empty_Input(self, ms=None)`
2. `def Echo_Fail(self, ms)`
3. `def Echo_Success(self)`

| param   | type | description      |
| ------- | ---- | ---------------- |
| returns | none |                  |
| action  |      | 调用标准报错弹窗 |

<img src=".\DisplayPics\pages\bookedit.png" alt="image-20220516104222783" style="zoom:50%;" />

## 基本功能函数

### 概览

#### Query

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

#### 数据库访问函数

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

##### 按照条件查询

`def Query_UserRentingHis(user_id)`

该函数通过调用user_id，对数据库进行访问。会被User对象调用。

返回`Book.BookId, Book.BookName, BookType.TypeName, RentHistory.RentDay, RentHistory.ReturnDate`

每一条记录代表着某个用户的借阅历史记录。

| param   | type | description                                        |
| ------- | ---- | -------------------------------------------------- |
| user_id | str  | 用户的账号                                         |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况     |

`def Query_BookRank()`

该函数对数据库内容进行标准化访问。

返回查询结果结构：`Book.BookId, BookName, times, Stock, Price, TypeName`

按照借阅次数降序排序。

| param   | type | description                                        |
| ------- | ---- | -------------------------------------------------- |
| None    | None | 无传入参数                                         |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况     |

`def Query_UserRank()`

该函数对数据库内容进行标准化访问，与`Query_BookRank`类似。

返回查询结果结构：`UserName, User.UserId, times`

按照借阅次数降序排序。

| param   | type | description                                                  |
| ------- | ---- | ------------------------------------------------------------ |
| None    | None | 无传入参数                                                   |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况               |

`def Query_BookType()`

同族类似功能函数有：

1. `def Query_BookType_Id()`
2. `def FetchAllBookType()`

获取Type信息。

| param   | type | description                                                  |
| ------- | ---- | ------------------------------------------------------------ |
| None    | None | 无传入参数                                                   |
| returns | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行Dict封装。 |
| throws  | none | 不会抛出异常，但是当访问出错时，会打印异常状况               |

`def Query_Book(TypeName, BookInfo)`

该函数用于查询书本列表，按照书本的类型以及书本名称（可以不用完全相等）来查找书籍。

| param      | type | description                                                  |
| ---------- | ---- | ------------------------------------------------------------ |
| `TypeName` | str  | 书本类型名称                                                 |
| `BookInfo` | str  | 书本名称部分切片                                             |
| returns    | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws     | none | 不会抛出异常，但是当访问出错时，会打印异常状况。             |

`def Query_UnReturned_Book(UserId)`

按照`UserId`从数据库中查询用户尚未归还的书籍。

| param    | type | description                                                  |
| -------- | ---- | ------------------------------------------------------------ |
| `UserId` | str  | 读者号                                                       |
| returns  | list | 一个两层的list结构，第一层每个元素为一个数据元组。尚未进行`Dict`封装。 |
| throws   | none | 不会抛出异常，但是当访问出错时，会打印异常状况。             |

`def Query_Price_Remain(UserId, BookId=None, RentDate=None)`

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

`def Modify_Return(tar)`

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

`def RentCertification(UserId, BookId) -> bool`

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

##### 添加数据类

`def Add_RentHis(UserId, BookId)`

该函数实现借阅功能，会调用`RentCertification`进行借阅有效性的验证。

| param    | type                | description                |
| -------- | ------------------- | -------------------------- |
| `UserId` | str                 | 读者id                     |
| `BookId` | str                 | 书本id                     |
| returns  | none                |                            |
| throws   | `sql.DatabaseError` | 数据库访问异常，在外部抓取 |

`def Add_Book(BookId, BookName, stock, price, BookType)`

由超级用户使用，用于添加书本。

| param   | type                | description                |
| ------- | ------------------- | -------------------------- |
| `args`  | str                 | 一系列书本相关数据         |
| returns | none                |                            |
| throws  | `sql.DatabaseError` | 数据库访问异常，在外部抓取 |

`def Add_BookType(Id, Name)`

由超级用户使用，用于创建新的书本类型。

| param   | type                | description |
| ------- | ------------------- | ----------- |
| Id      | str                 | 书本id      |
| Name    | str                 | 书本名称    |
| returns | none                | none        |
| throws  | `sql.DatabaseError` | `           |

`def Add_User(UserId, UserName, Role, Password)`

可以被超级用户，或者是读者进行注册操作的时候调用。创建新用户。

为了保护数据库安全性，该方式调用时具有限定性，只能创建老师或者是学生用户，不能创建超级用户。

| param   | type                | description                  |
| ------- | ------------------- | ---------------------------- |
| `args`  | str                 | 读者的id，姓名，权限以及密码 |
| returns | none                |                              |
| throws  | `sql.DatabaseError` | `                            |

`def Update_UserInfo(pack)`

超级用户使用，用于修改已有的用户的属性。

```python
pack = dict()
for i, title in zip(self.UserView.selectionModel().selectedIndexes(), self.UserInfoHeader):
	pack[title] = i.data()
	Update_UserInfo(pack)
```

| param   | type                  | description                      |
| ------- | --------------------- | -------------------------------- |
| pack    | `dict`                | 数据包，装载格式化的传入数据参数 |
| returns | none                  |                                  |
| throws  | `RentRefuse(repr(e))` | 拒绝借阅异常                     |

对于打包内容需要有以下关键字：

```python
pack['name'], pack['password'], pack['role'], pack['id']
```

`def Update_RentDate(UserId, BookId, RentDate)`

通过传入参数，查询借阅记录。同时更新借阅记录的借阅日期为当前时间。

| param    | type | description |
| -------- | ---- | ----------- |
| UserId   | str  | 用户id      |
| BookId   | str  | 借阅书本id  |
| RentDate | str  | 借阅日期    |

`def Update_BookInfo(pack)`

```
pack['name'], pack['stock'], pack['price'], pack['type id'], pack['id']
```

| param   | type | description              |
| ------- | ---- | ------------------------ |
| pack    | dict | 字典包，字典结构如图所示 |
| returns | none |                          |

```python
update Book set BookName = '{}',
Stock = '{}',
Price = '{}',
TypeId = '{}'
where BookId = '{}' 
```

##### 直接获取类

`def FetchAllBooks()`

`def FetchAllRoleTypes()`

`def FetchAllUser()`

- 获取所有用户权限信息。
- 获取所有书本的信息。
- 用于获取用户数据，该方法下获取所有用户的数据。

| param   | type | description  |
| ------- | ---- | ------------ |
| input   | list | 输出查询结果 |
| returns | none | 无返回       |

## 数据库结构详解

### 内置数据库

#### 表结构

##### Book

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

| Name       | Data Type | PK   | FK                                               | Unique | Check    | Default |
| ---------- | --------- | ---- | ------------------------------------------------ | ------ | -------- | ------- |
| `BookId`   | char      | true |                                                  |        |          |         |
| `BookName` | char      |      |                                                  |        |          |         |
| `Stock`    | int       |      |                                                  |        |          | 0       |
| `Price`    | int       |      |                                                  |        |          | 0       |
| `TypeId`   | char      |      | `REFERENCES BookType (TypeId)`，参照`BookType表` |        | not null |         |

##### BookType

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

##### User

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

##### UserRole

```sql
CREATE TABLE UserRole (
    RoleId       NUMERIC PRIMARY KEY ASC,
    RoleName     CHAR    NOT NULL,
    Duration     TIME    NOT NULL,
    LendingTimes INT     NOT NULL
);
```

读者类型与权限记录表，记录读者权限。

| Name           | Data Type | PK   | FK   | Unique | Check          | Default |
| -------------- | --------- | ---- | ---- | ------ | -------------- | ------- |
| `RoleId`       | char      | true |      |        |                |         |
| `RoleName`     | char      |      |      | true   |                |         |
| `Duration`     | num       |      |      |        | check positive | 10      |
| `LendingTimes` | num       |      |      |        | check positive | 10      |

该表正常情况下，不允许添加新项目，固定信息如下：

| Role         | `RoleId` | Duration | `LendingTimes` |
| ------------ | -------- | -------- | -------------- |
| `Super User` | 0        | 365      | 100            |
| `Teacher`    | 1        | 30       | 10             |
| `Students`   | 2        | 10       | 5              |

系统借阅的基本参数，由该表决定，后续修改依照该表。

##### RentHistory

```sql
CREATE TABLE RentHistory (
    UserId              REFERENCES User (UserId) 
                        NOT NULL,
    BookId              REFERENCES Book (BookId) 
                        NOT NULL,
    RentDay    DATETIME NOT NULL,
    ReturnDate DATETIME,
    PRIMARY KEY (
        UserId,
        BookId,
        RentDay
    )
);
```

借阅记录表，该表负责记录所有的借阅与归还信息。

每次借阅都会插入一条数据，并且设置`ReturnDate`的初始值为null。

对于归还了的记录，`returnDate`将为非null，可以用于后续判断。

| Name         | Data Type | PK   | FK                              | Unique | Check    | Default     |
| ------------ | --------- | ---- | ------------------------------- | ------ | -------- | ----------- |
| `UserId`     | char      | true | true `REFERENCES User (UserId)` |        | not null |             |
| `BookId`     | char      | true | true `REFERENCES Book (BookId)` |        | not null |             |
| `RentDay`    | Date      |      |                                 |        | not null | `getdate()` |
| `ReturnDate` | Date      |      |                                 |        |          | null        |

#### 视图设计

为了方便编程，以及快速查询与修改，在设计设计库的时候，设计了一系列的视图，为后续的功能提供支持。

##### `BookRemain`

设计视图用于快速查询剩余的书本数量，用于限制借阅次数。

```sql
Select Book.BookId, Book.Stock-temp.num remain from Book
inner join
(
select BookId, count(*) num
from RentHistory
where ReturnDate is null
group by BookId
)as temp
on temp.BookId = Book.BookId
```



##### `UnreturnPrice`

统计所有用户目前所欠金额。

```sql
select User.UserId, Book.BookId,Book.BookName, Book.Price, RentHistory.RentDay
from Book, RentHistory, User, UserRole
where Book.BookId = RentHistory.BookId
and User.UserId = RentHistory.UserId
and USer.Role = UserRole.RoleId
and RentHistory.ReturnDate is null
and
date(RentHistory.RentDay, '+'||cast(UserRole.Duration as string)|| ' day') < date('now')
```

##### `UserUnReturn_Count`

统计所有用户目前未归还书本的数目。

```sql
select User.UserId, temp.times, UserRole.LendingTimes from User, UserRole,
(
select UserId, count(*) as times
from RentHistory
where ReturnDate is null
group by UserID
) as temp
where User.Role = UserRole.RoleId
and User.UserId = temp.UserId
```

#### 触发器设计

sqlite无法支持复杂的触发器结构，但是我们在云端部署的SQL server数据库中，使用触发器，对于我们图书馆管理系统的完整性进行约束。

##### 借阅有效性判断

判读是否还有剩余的书本，以及用户是否还有剩余的借阅限额。

```sql
USE [LibraryManageSystem]
GO
/****** Object:  Trigger [dbo].[UserRentConstrain]    Script Date: 2022/5/16 10:28:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER trigger [dbo].[UserRentConstrain]
on [dbo].[RentHistory] for insert
as
begin
declare @tempNum int
declare @boundNum int
select @tempNum = times, @boundNum = LendingTimes
from UserUnReturn_Count, inserted
where
UserUnReturn_Count.UserId = inserted.UserId
if @tempNum >= @boundNum
begin
rollback
end
end
```

### 远程链接数据库

同本地数据库结构。

# 四、程序运行结果测试与分析

## GUI展示

### 普通用户流程展示

#### 登录界面

<img src=".\DisplayPics\GeneralUser\LoginPage.png" style="zoom: 50%;" />

##### 登录成功

<img src=".\DisplayPics\GeneralUser\Login_Success.png" style="zoom: 50%;" />

##### 日历界面

<img src=".\DisplayPics\GeneralUser\LoginPage_2.png" style="zoom: 50%;" />

#### 注册界面

#### 用户界面

##### 基本用户信息界面

<img src=".\DisplayPics\GeneralUser\UserPage.png" style="zoom: 50%;" />

##### 用户排行榜

<img src=".\DisplayPics\GeneralUser\UserRank.png" style="zoom: 50%;" />

##### 图书排行榜

<img src=".\DisplayPics\GeneralUser\UserRank.png" style="zoom: 50%;" />

#### 借阅界面

<img src=".\DisplayPics\GeneralUser\RentPage.png" style="zoom: 50%;" />

#### 归还界面

##### 初始

<img src=".\DisplayPics\GeneralUser\ReturnPage.png" style="zoom: 50%;" />

##### 归还操作

<img src=".\DisplayPics\GeneralUser\ReturnAction.png" style="zoom: 50%;" />

#### 续借界面

##### 未有过期书目：

<img src=".\DisplayPics\GeneralUser\PayMoney.png" style="zoom:80%;" />

##### 有过期书目：

<img src=".\DisplayPics\GeneralUser\Debt.png" style="zoom:50%;" />

#### 尝试访问管理权限

<img src=".\DisplayPics\GeneralUser\FailOfSuper.png" style="zoom: 50%;" />

### 超级用户流程展示

#### 用户界面

<img src=".\DisplayPics\SuperUser\UserPage.png" style="zoom:50%;" />

#### 权限界面

<img src=".\DisplayPics\SuperUser\SuperPage.png" style="zoom:50%;" />

#### 查询信息界面

<img src=".\DisplayPics\SuperUser\CheckInfo_BookRanked.png" style="zoom:50%;" />

#### 修改读者信息界面

<img src=".\DisplayPics\SuperUser\ChangeUserInfoBefore.png" style="zoom:50%;" />

#### 修改书本信息界面

## 数据输出展示

<img src=".\DisplayPics\SuperUser\SaveBook.png" style="zoom: 33%;" />



![](.\DisplayPics\SuperUser\SaveUserRes.png)

# 五、结论与心得

## 任务负责

在本次的课程实践中，我负责该管理系统的全部的设计与实现工作。包括但不限于以下工作：

1. 数据库ER模型设计
2. 数据库模型编码实现
3. UI界面设计
4. UI界面前端绘制
5. 业务逻辑设计
6. 业务逻辑编码实现
7. 成果测试检验

## 收获

### 概念收获

在本次的程序设计课程设计中，我收获了许多。首先是更加了解了软件工程的实际含义，与在实际工程中所需要的思考方式与想法。

同时更加深入地了解数据库的设计与创建过程。

<img src="C:\Users\15191\AppData\Roaming\Typora\typora-user-images\image-20220516105240297.png" alt="image-20220516105240297" style="zoom:50%;" />

了解数据库各级的形成过程：

数据库各级模式的形成过程需求分析阶段：综合各个用户的应用需求。

概念设计阶段：形成独立于机器特点，独立于各个DBMS产品的概念模式(E-R图)。

逻辑设计阶段：首先将E-R图转换成具体DBMS支持的数据模型，如关系模型，形成数据库逻辑模式；然后根据用户处理的要求、安全性的考虑，在基本表的基础上再建立必要的视图(View)，形成数据的外模式。

物理设计阶段：根据DBMS特点和处理的需要，进行物理存储安排，建立索引，形成数据库内模式。

### 技术收获

在本次的项目中其实收获到的最大的好处就是，将之前学习到的很多内容，进行了一个梳理，同时也对知识点有了更深的印象。使得自己对于哪些python以及sql基础知识有了一个更好的理解，同时对其会产生的问题有了一个具体的了解，当我在遇到的时候就会懂得如何去修改，以及能及时发现其中的错误。

#### 前端技术收获

深入了解学习python qt前端的框架体系。了解了前端可视化界面的总体结构。

![](https://img-blog.csdnimg.cn/2018112115221670.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lqX2FuZHJvaWRfZGV2ZWxvcA==,size_16,color_FFFFFF,t_70)

#### 数据库技术收获

在学习数据库和数据表创建和修改时，了解到表是建立关系数据库的基本结构，用来存储数据具有已定义的属性，在表的操作过程中，有查看表信息、查看表属性、修改表中的数据、删除表中的数据及修改表和删除表的操作。

从实践中让我更明白一些知识，表是数据最重要的一个数据对象，表的创建好坏直接关系到数数据库的成败，表的内容是越具体越好，但是也不能太繁琐，对表的规划和理解更加深刻。

同时更加深刻地了解到了不同数据库之间的不同，以及对应工作环境下的区别。

## 遇到困难

### 技术困难

1. qt表格类的使用
   - qt整个框架是基于c++构建的，移植到python下实际上底层内核还是使用c++编译的，无法直接查看源代码。对于部分功能的理解会有一点障碍。
   - qt表格类较为复杂，是多个对象以及方法的嵌套，了解起来有点困难。
2. 数据库触发设计
   - sqlite作为轻量级数据库，实际上数据的管理功能是有限的。
   - 在内置的功能里，不支持复杂的触发结构，需要程序员自行设计。

## 未实现功能

### 用户交互层面

用户交互设计依旧不够友好，对于部分操作还是分开进行。

例如：

- 对于修改用户权限，需要用户手动输入。对于用户权限的选择是具有局限性的选择，应当使用下拉式进行修改。
- 查询与修改操作是分开的，在修改是不能查询，查询时不能修改。

对于用户的可视化界面还不够美观。

### 数据库信息存储层面

- 目前而言数据模型还没有完善，对于用户只存储了基本信息，对于对书籍内容只存储了基本信息，需要后续进行拓展。
- 数据库数据的修改具有局限性，只允许管理员进行数据的修改，而用户无法对于自己的信息，进行直接修改。使得操作有时不够人性化。

### 网络连接层面

目前远程数据库只是有个雏形，目前只使用了local服务端进行模拟，总体功能还有待提升。