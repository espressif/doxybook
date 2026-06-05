# API Reference

## Header files

- [src/animal.h](#file-srcanimalh)
- [src/animal_interface.h](#file-srcanimal_interfaceh)
- [src/bird.h](#file-srcbirdh)
- [src/config.h](#file-srcconfigh)
- [src/example.h](#file-srcexampleh)
- [src/special_bird.h](#file-srcspecial_birdh)
- [src/utils/exception.h](#file-srcutilsexceptionh)

## File src/animal.h





## Namespaces

| Type | Name |
| ---: | :--- |
| namespace  | [**example**](#namespace-example)  <br> |
| namespace  | [**inner\_namespace**](#namespace-exampleinner_namespace)  <br> |

## Classes

| Type | Name |
| ---: | :--- |
| class  | [**Animal**](#class-exampleanimal)  <br>_Base class for all animals from which_ [_**Bird**_](#class-examplebird)_ derives._ |
| class  | [**Animal**](#class-exampleanimal)  <br>_Base class for all animals from which_ [_**Bird**_](#class-examplebird)_ derives._ |
| struct | [**Result**](#struct-exampleanimalresult) <br>_Some random inner class of_ [_**Animal**_](#class-exampleanimal)_._ |
| class  | [**Vector**](#class-exampleinner_namespacevector)  <br> |


## Types

| Type | Name |
| ---: | :--- |
| enum  | [**Type**](#enum-type)  <br>_The 6 classes of animal kingdom._ |

## Functions

| Type | Name |
| ---: | :--- |
|  void | [**some\_global\_function**](#function-some_global_function) ([**example::Animal**](#class-exampleanimal) \*animal) <br>_Some random global function that modifies Animal._ |
|  void | [**some\_namespace\_function**](#function-some_namespace_function) (Animal \*animal) <br>_Some random namespace function that modifies_ [_**Animal**_](#class-exampleanimal)_._ |

## Namespaces Documentation

### namespace `example`

### namespace `example::inner_namespace`


## Classes Documentation

### class `example::Animal`

_Base class for all animals from which_ [_**Bird**_](#class-examplebird)_ derives._

Lorem Ipsum Donor. Some [Random link with **bold** and_italics_](http://github.com) And the following is a`typewritter` font.

Example code:


````cpp
Animal animal = Animal("Hello World", nullptr, nullptr);
std::cout << animal.get_name() << std::endl;
````



**See also:** [**Bird**](#class-examplebird)

**Bug**

Some random bug 



**Note:**

Some random note 



**Warning:**

Some random warning 



**Test**

Some random test description 



**Todo**

Some random todo 



**Template parameters:**


* `T` Some random template paramater description which actually does not exist in the code! 


**Precondition:**

First initialize the system. 



**Date:**

2017-2018 



**Author:**

Matus Novak 



**Author:**

Hello World

Variables:

-  [**Animal**](#class-exampleanimal) \* father  <br>_The pointer to the father._<br>Can be null!

-  [**Animal**](#class-exampleanimal) \* mother  <br>_The pointer to the mother._<br>Can be null!

-  std::string name  

### class `example::Animal`

_Base class for all animals from which_ [_**Bird**_](#class-examplebird)_ derives._

Lorem Ipsum Donor. Some [Random link with **bold** and_italics_](http://github.com) And the following is a`typewritter` font.

Example code:


````cpp
Animal animal = Animal("Hello World", nullptr, nullptr);
std::cout << animal.get_name() << std::endl;
````



**See also:** [**Bird**](#class-examplebird)

**Bug**

Some random bug 



**Note:**

Some random note 



**Warning:**

Some random warning 



**Test**

Some random test description 



**Todo**

Some random todo 



**Template parameters:**


* `T` Some random template paramater description which actually does not exist in the code! 


**Precondition:**

First initialize the system. 



**Date:**

2017-2018 



**Author:**

Matus Novak 



**Author:**

Hello World

Variables:

-  [**Animal**](#class-exampleanimal) \* father  <br>_The pointer to the father._<br>Can be null!

-  [**Animal**](#class-exampleanimal) \* mother  <br>_The pointer to the mother._<br>Can be null!

-  std::string name  

### struct `example::Animal::Result`

_Some random inner class of_ [_**Animal**_](#class-exampleanimal)_._

Variables:

-  const [**Animal**](#class-exampleanimal) \* father   = = nullptr

-  const [**Animal**](#class-exampleanimal) \* mother   = = nullptr

-  const std::string name  

-  const [**Type**](#enum-type) type   = = Type::NONE

### class `example::inner_namespace::Vector`


Variables:

-  int x  

-  int y  

-  int z  



## Types Documentation

### enum `Type`

_The 6 classes of animal kingdom._
```c
enum Type {
    NONE = 0,
    INSECT = 1,
    AMPHIBIAN = 2,
    BIRD = 3,
    FISH = 4,
    REPTILE = 5,
    MAMMAL = 6
};
```


Lorem Ipsum Donor.

## Functions Documentation

### function `some_global_function`

_Some random global function that modifies Animal._
```c
void some_global_function (
    example::Animal *animal
) 
```


**See also:** Animal 

**Parameters:**


* `animal` The pointer to the animal instance
### function `some_namespace_function`

_Some random namespace function that modifies_ [_**Animal**_](#class-exampleanimal)_._
```c
void some_namespace_function (
    Animal *animal
) 
```


**See also:** [**Animal**](#class-exampleanimal)

**Parameters:**


* `animal` The pointer to the animal instance

## File src/animal_interface.h





## Namespaces

| Type | Name |
| ---: | :--- |
| namespace  | [**example**](#namespace-example)  <br> |

## Classes

| Type | Name |
| ---: | :--- |
| interface  | [**AnimalInterface**](#interface-exampleanimalinterface)  <br> |
| interface  | [**AnimalInterface**](#interface-exampleanimalinterface)  <br> |




## Namespaces Documentation

### namespace `example`


## Classes Documentation

### interface `example::AnimalInterface`

### interface `example::AnimalInterface`





## File src/bird.h





## Namespaces

| Type | Name |
| ---: | :--- |
| namespace  | [**example**](#namespace-example)  <br> |

## Classes

| Type | Name |
| ---: | :--- |
| class  | [**Bird**](#class-examplebird)  <br> |
| class  | [**Bird**](#class-examplebird)  <br> |




## Namespaces Documentation

### namespace `example`


## Classes Documentation

### class `example::Bird`

### class `example::Bird`





## File src/config.h

_This is a config file._

This is a detailed description



## Macros

| Type | Name |
| ---: | :--- |
| define  | [**CONFIG\_HELLO**](#define-config_hello)  (123)<br> |
| define  | [**CONFIG\_WORLD**](#define-config_world)  ("abx")<br> |
| define  | [**PI**](#define-pi)  3.14159265358979323846<br> |
| define  | [**PRINT\_PRETTY**](#define-print_pretty) (MSG, ...) printf(MSG, \_\_VA\_ARGS\_\_)<br> |





## Macros Documentation

### define `CONFIG_HELLO`

```c
#define CONFIG_HELLO (123)
```

### define `CONFIG_WORLD`

```c
#define CONFIG_WORLD ("abx")
```

### define `PI`

```c
#define PI 3.14159265358979323846
```

### define `PRINT_PRETTY`

```c
#define PRINT_PRETTY (
    MSG,
    ...
) printf(MSG, __VA_ARGS__)
```




## File src/example.h















## File src/special_bird.h





## Namespaces

| Type | Name |
| ---: | :--- |
| namespace  | [**example**](#namespace-example)  <br> |

## Classes

| Type | Name |
| ---: | :--- |
| class  | [**SpecialBird**](#class-examplespecialbird)  <br> |
| class  | [**SpecialBird**](#class-examplespecialbird)  <br> |




## Namespaces Documentation

### namespace `example`


## Classes Documentation

### class `example::SpecialBird`

### class `example::SpecialBird`





## File src/utils/exception.h





## Namespaces

| Type | Name |
| ---: | :--- |
| namespace  | [**example**](#namespace-example)  <br> |

## Classes

| Type | Name |
| ---: | :--- |
| class  | [**CustomException**](#class-examplecustomexception)  <br> |
| class  | [**CustomException**](#class-examplecustomexception)  <br> |
| class  | [**NumericException**](#class-examplenumericexception)  <br> |
| class  | [**NumericException**](#class-examplenumericexception)  <br> |




## Namespaces Documentation

### namespace `example`


## Classes Documentation

### class `example::CustomException`


Variables:

-  std::string msg  

### class `example::CustomException`


Variables:

-  std::string msg  

### class `example::NumericException`


Variables:

-  std::string msg  

### class `example::NumericException`


Variables:

-  std::string msg  





