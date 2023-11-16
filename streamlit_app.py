# Add cost to every developer and 
# set how many hours predicted
# Calculate who may be the cheapest
# Complexity multiplier, if task is complex for user do complexity times hours or something


import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment

def envy_free_allocation(data):
    # Create a matrix of complexities for each person and task
    persons = sorted(set(entry['name'] for entry in data))
    tasks = sorted(set(entry['task'] for entry in data))
    matrix = np.zeros((len(persons), len(tasks)))

    for entry in data:
        person_index = persons.index(entry['name'])
        task_index = tasks.index(entry['task'])
        matrix[person_index, task_index] = entry['complexity']

    # Apply the Hungarian algorithm to find the envy-free allocation
    row_ind, col_ind = linear_sum_assignment(matrix)

    # Create the envy-free assignment dictionary
    assignment = {}
    for person_idx, task_idx in zip(row_ind, col_ind):
        person = persons[person_idx]
        task = tasks[task_idx]
        assignment[person] = task

    return assignment

st.title("Software Development Task Distribution")

# Input the number of team members
num_tasks = st.number_input("Number of Tasks:", min_value=1, value=1)

# Input the number of team members
num_members = st.number_input("Number of Team Members:", min_value=1, value=1)

st.header("Tasks")
tasks = []
for i in range(num_tasks):
    with st.expander(f"Expand Task {i + 1}"):
        task_name = st.text_input(f"Enter task name for Task {i + 1}")
        tasks.append({"name": task_name})  # Corrected indentation
    
team_members = []

# Input task details
st.header("Preferences")

for i in range(num_members):
    with st.expander(f"Team Member {i + 1} preferences"):
        team_member_name = st.text_input(f"Team member name", key=i)
        st.subheader("Choose task complexity for every task", divider = 'rainbow')
        st.text("(1 - Very simple, 5 - Very complex)")
        for j in range(num_tasks):
            task_complexity = st.slider(f"Task Complexity for {tasks[j]['name']}", 1, 5, 3, key=f"slider_{i}_{j}")
            team_members.append({"name":team_member_name, "task":tasks[j]['name'], "complexity":task_complexity})

if st.button("Distribute Tasks"):
    st.header("Results", divider = 'rainbow')
    allocation = envy_free_allocation(team_members)
    for person, task in allocation.items():
        st.write(f"{person.capitalize()} is assigned task: {task}.")
