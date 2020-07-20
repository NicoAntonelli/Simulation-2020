# TP3.0 - Single-server Queuing System
M/M/1 Queue Model: Simulation and Analysis of common performance measures

## Models Comparison
Analytic Solutions

Python Simulation

AnyLogic Simulation

## Performance Measurements Analyzed
Average quantity of costumers in queue

Average delay time in queue

Average quantity of costumers in the system

Average delay time in queue

Server utilization

N customers in system probability

Denial of service probability

## Example in the Python Simulations
Simulation runs: 10, Total Customers Quantity: 10000, Arrival Rate: 1.5, Service Rate: 2

Graphics: Simulation results VS Expected values

![avg_num_in_queue](./graphs/graph_10runs_10000delays_config2_avg_num_in_queue.png)
![avg_delay_time_in_queue](./graphs/graph_10runs_10000delays_config2_avg_delay_time_in_queue.png)
![avg_num_in_the_system](./graphs/graph_10runs_10000delays_config2_avg_num_in_the_system.png)
![avg_delay_time_in_the_system](./graphs/graph_10runs_10000delays_config2_avg_delay_time_in_the_system.png)
![server_utilization](./graphs/graph_10runs_10000delays_config2_server_utilization.png)
![n_customers_probability](./graphs/graph_10runs_10000delays_config2_n_customers_in_queue_probability.png)

## Example in the AnyLogic Simulations
Simulation runs: 1, Total Customers Quantity: 30000, Arrival Rate: 1.5, Service Rate: 2

#### Model
![anylogic_general](./anylogic/model/anylogic_general.png)

#### Results
![anylogic_results](./anylogic/graphs/arrivalrate=1.5,servicerate=2.png)
