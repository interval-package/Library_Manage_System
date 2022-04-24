# Library Manage System

# 一、需求分析

在本次课程设计中，基于任务要求，我们设计了一套图书馆管理系统

## （1）界面需求

对于我们的图书馆管理系统，我们对于用户的交互体验，总结出了一下几点基本需求：

## （2）功能需求

对于我们的系统，我们对于功能的需求可以基本分为以下大类：

### 基本功能要素

### 拓展功能要素

### 移植功能要素

### 安全功能要素

## （3）性能需求

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

表结构

表约束

### (2) 远程数据库结构

表结构

表约束

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