# API Reference

## Header files

- [test_comp/include/comp1.h](#file-test_compincludecomp1h)
- [test_comp/include/comp2.h](#file-test_compincludecomp2h)

## File test_comp/include/comp1.h

_This is a test file for_ [_**comp1**_](#struct-comp1)_._

To use this driver:

* include this file in your project
* [**print()**](#function-print) is a function that prints "Hello World!"

## Structures and Types

| Type | Name |
| ---: | :--- |
| struct | [**comp1**](#struct-comp1) <br>_struct comp_ |
| typedef int | [**comp1\_int**](#typedef-comp1_int)  <br>_typedef int for comp_ |
| union  | [**union\_comp1**](#union-union_comp1)  <br>_it's a union!!!_ |

## Functions

| Type | Name |
| ---: | :--- |
|  void | [**add**](#function-add) ([**comp1**](#struct-comp1) a, [**comp1**](#struct-comp1) b) <br>_print the added result_ |
|  void | [**print**](#function-print) (void) <br>_print function_ |

## Macros

| Type | Name |
| ---: | :--- |
| define  | [**TEST\_FOO**](#define-test_foo)  111;<br>_THIS IS TEST\_FOO VARIABLE!_ |

## Structures and Types Documentation

### struct `comp1`

_struct comp_

Variables:

-  int bar  

-  int foo  <br>_??? foo?_

### typedef `comp1_int`

_typedef int for comp_
```c
typedef int comp1_int;
```

### union `union_comp1`

_it's a union!!!_

Variables:

-  [**comp1**](#struct-comp1) a  

-  [**comp1**](#struct-comp1) b  


## Functions Documentation

### function `add`

_print the added result_
```c
void add (
    comp1 a,
    comp1 b
) 
```


**Parameters:**


* `a` aaa 
* `b` bbb
### function `print`

_print function_
```c
void print (
    void
) 
```


## Macros Documentation

### define `TEST_FOO`

_THIS IS TEST\_FOO VARIABLE!_
```c
#define TEST_FOO 111;
```


## File test_comp/include/comp2.h





## Structures and Types

| Type | Name |
| ---: | :--- |
| enum  | [**DAY**](#enum-day)  <br> |
| struct | [**comp2**](#struct-comp2) <br>_struct_ [_**comp2**_](#struct-comp2) |
| typedef int | [**comp2\_int**](#typedef-comp2_int)  <br>_typedef int for comp_ |

## Functions

| Type | Name |
| ---: | :--- |
|  void | [**add**](#function-add) (int a, int b) <br>_print the added result_ |
|  void | [**print**](#function-print) (void) <br>_print function_ |


## Structures and Types Documentation

### enum `DAY`

```c
enum DAY {
    MON = 1,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN
};
```

### struct `comp2`

_struct_ [_**comp2**_](#struct-comp2)

Variables:

-  int bar  

-  int foo  

### typedef `comp2_int`

_typedef int for comp_
```c
typedef int comp2_int;
```


## Functions Documentation

### function `add`

_print the added result_
```c
void add (
    int a,
    int b
) 
```


**Parameters:**


* `a` a 
* `b` b
### function `print`

_print function_
```c
void print (
    void
) 
```



