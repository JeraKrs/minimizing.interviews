# Minimizing Interviews

My final project for the master degree.

## Environments

* Python - 3.6.1 
* PyYAML - 3.13
* numpy - 1.14.5

## Files

* algorithms: the implementation of our models for minimizing the interviews.
* data_accessors: the layer for mocking the interview process.
* data_generators: the implementation of the preference sample models.
* tools: the basic functions and the checkunits.

## Programmes

There are four main scripts for the evaluation.

### Data generator

To examine the preference sample models. The file `config_generation.yaml` is the configurations, it has five parameters:

* length: the length of each preference list.
* sample: the number of sample preference lists.
* model: the sample models in which the valid values are `random`, `luce`, `bradley` and `mallows`.
* theta: the similarity of the preference lists.
* print: output the preference lists or not in which the valid values are `True` and `False`.


To run:

```
$ python data-generator.py  

length:10
sample:10
model:mallows
theta:0.5
print:False
average distance = [0.0, 0.0, 0.2, 0.0, 0.2, 0.6, 0.2, 0.8, 0.4, 0.4]
```

### Assess the random model

To examine the random model of the interview-schedule. The file `config_random_model.yaml` is the configurations, it has three parameters:

* length: the length of each preference list.
* case: the number of test group.
* theta: the similarity of the preference lists in the test data.

To run:

```
$ python assess-random-model.py 

length:10
case:10
theta:0.8
Ru =  [1.0, 0.905, 0.865, 0.6900000000000001, 0.615, 0.51, 0.3950000000000001, 0.24500000000000002, 0.225, 0.07, 0]
```

The `Ru` is a list which length 11, it indicates the unsatisfied rate when the interview rate is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] percentage.

### Assess the MUL-PP model

To examine the MUL-PP model of the interview-schedule. The file `config_mul_model.yaml` is the configurations, it has three parameters:

* length: the length of each preference list.
* case: the number of test group.
* theta: the similarity of the preference lists in the test data.

To run:

```
```	
