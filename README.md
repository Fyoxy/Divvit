# Envy-Free Allocation Project - ITB8802 Täppismeetodid otsustuste vastuvõtmisel

## Introduction

This project implements an envy-free allocation system using Streamlit, a Python library for creating web applications. The goal is to distribute tasks among team members based on their preferences and task complexities, ensuring an envy-free assignment.

## Code Overview

The main functionality of the project is implemented in the `envy_free_allocation` function, which utilizes the Hungarian algorithm from the SciPy library. This function takes task preferences and complexities as input and returns an envy-free allocation.

```python
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
```

## How to Use

1. **Navigate to:** https://divvit.streamlit.app/
   
2. **Number of Tasks and Team Members:** Input the number of tasks and team members using the respective input fields.

3. **Task Details:** Enter the details for each task, including the task name. Tasks can be expanded for more details.

4. **Team Member Preferences:** For each team member, input their name and set task complexities using sliders.

5. **Distribute Tasks:** Click the "Distribute Tasks" button to calculate and display the envy-free allocation results.


## Getting Started with development

To run the application locally, ensure you have Streamlit installed:

```bash
pip install streamlit
```

Then, run the following command in your terminal:

```bash
streamlit run streamlit_app.py
```

Replace `streamlit_app.py` with the name of the file containing the Streamlit code.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [NumPy](https://numpy.org/)
- [SciPy](https://www.scipy.org/)

## Acknowledgments

This project was developed as part of the ITB8802 "Täppismeetodid otsustuste vastuvõtmisel" course at TalTech University.

Feel free to explore the code and adapt it to your needs!
