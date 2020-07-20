# -*- coding: utf-8 -*-

from utils import exponential_generator
from queue import Queue, Full


# Model Initialization
def initialize(config):
    if config["queue_length"] == "inf":
        queue_max_size = float("inf")
    else:
        queue_max_size = config["queue_length"]

    return {
        "model": {
            # Config parameters
            "mean_interarrival": 1 / config["arrival_rate"],
            "mean_service": 1 / config["service_rate"],
            "num_delays_required": config["num_delays_required"],
            # Simulation clock
            "time": 0.0,
            # Queue
            "queue_length": queue_max_size,
            "time_arrival_queue": Queue(maxsize=0),
            # Statistical counters
            "num_customers_delayed": 0,
            "area_num_in_queue": 0.0,
            "area_server_status": 0.0,
            "total_of_delays": 0.0,
            # State variables
            "num_in_queue": 0,
            "clients_in_queue_absolute_freq": [0.0 for n in range(config["num_delays_required"])],
            "clients_in_system_absolute_freq": [0.0 for n in range(config["num_delays_required"])],
            "num_without_service": 0,
            "server_busy": False,
            "time_last_event": 0.0,
            # Event list
            "event_list": {
                "arrival": exponential_generator(1 / config["arrival_rate"]),
                "departure": float("inf"),
            },
        },
        "results_time": {
            "avg_delay_in_queue": {},
            "avg_num_in_queue": {},
            "avg_delay_in_system": {},
            "avg_num_in_system": {},
            "server_utilization": {},
            "clients_in_queue_absolute_freq": [],
        },
    }


# Determination of the next event's type and time
def timing(event_list):
    next_event_type = min(event_list, key=event_list.get)
    next_event_time = event_list[next_event_type]

    return (next_event_type, next_event_time)


# Update time-average statistical accumulators
def update_time_stats(model):
    time_since_last_event = model["time"] - model["time_last_event"]

    # N Clients in queue probabilities
    model["clients_in_queue_absolute_freq"][model["num_in_queue"]] += time_since_last_event
    # N Clients in system probabilities
    model["clients_in_system_absolute_freq"][
        model["num_in_queue"] + model["server_busy"]
    ] += time_since_last_event

    model["area_num_in_queue"] += time_since_last_event * model["num_in_queue"]
    model["area_server_status"] += time_since_last_event * int(model["server_busy"])
    model["time_last_event"] = model["time"]


# Arrival Event
def arrive(model):
    model["event_list"]["arrival"] = model["time"] + exponential_generator(
        model["mean_interarrival"]
    )
    if model["server_busy"]:
        if model["num_in_queue"] + 1 > model["queue_length"]:
            model["num_without_service"] += 1
        else:
            model["time_arrival_queue"].put_nowait(model["time"])
            model["num_in_queue"] += 1
    else:
        model["num_customers_delayed"] += 1
        model["server_busy"] = True
        model["event_list"]["departure"] = model["time"] + exponential_generator(
            model["mean_service"]
        )


# Departure Event
def depart(model):
    if model["num_in_queue"] == 0:
        model["server_busy"] = False
        model["event_list"]["departure"] = float("inf")
    else:
        model["num_in_queue"] -= 1
        delay = model["time"] - model["time_arrival_queue"].get_nowait()
        model["total_of_delays"] += delay
        model["num_customers_delayed"] += 1
        model["event_list"]["departure"] = model["time"] + exponential_generator(
            model["mean_service"]
        )


# Partial Report Generator
def event_report(results_time, model):
    # Average time in queue
    current_avg_delay_in_queue = model["total_of_delays"] / model["num_customers_delayed"]
    results_time["avg_delay_in_queue"][model["num_customers_delayed"]] = current_avg_delay_in_queue
    # Average quantity of costumers in queue
    current_avg_num_in_queue = model["area_num_in_queue"] / model["time"]
    results_time["avg_num_in_queue"][model["time"]] = current_avg_num_in_queue

    # Average time in the system
    current_avg_delay_in_system = current_avg_delay_in_queue + model["mean_service"]
    results_time["avg_delay_in_system"][
        model["num_customers_delayed"]
    ] = current_avg_delay_in_system

    # Average Average quantity of costumers in the system
    current_avg_num_in_system = (1 / model["mean_interarrival"]) * current_avg_delay_in_system
    results_time["avg_num_in_system"][model["time"]] = current_avg_num_in_system

    # Server utilization
    current_server_utilization = model["area_server_status"] / model["time"]
    results_time["server_utilization"][model["time"]] = current_server_utilization


# Final Report Generator
def final_report(results_time, model):
    n_clients_in_queue_probability_array = [
        time_n_clients / model["time"] for time_n_clients in model["clients_in_queue_absolute_freq"]
    ]
    n_clients_in_system_probability_array = [
        time_n_clients / model["time"]
        for time_n_clients in model["clients_in_system_absolute_freq"]
    ]
    client_not_getting_service_probability = (
        model["num_without_service"] / model["num_customers_delayed"]
    )

    return {
        "avg_delay_in_queue": results_time["avg_delay_in_queue"],
        "avg_delay_in_system": results_time["avg_delay_in_system"],
        "avg_num_in_queue": results_time["avg_num_in_queue"],
        "avg_num_in_system": results_time["avg_num_in_system"],
        "server_utilization": results_time["server_utilization"],
        "n_clients_in_queue_probability_array": n_clients_in_queue_probability_array,
        "n_clients_in_system_probability_array": n_clients_in_system_probability_array,
        "client_not_getting_service_probability": client_not_getting_service_probability,
        "total_time": model["time"],
    }
