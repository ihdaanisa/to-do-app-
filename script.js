// Data saved via localStorage
const taskList = JSON.parse(localStorage.getItem('taskList')) || [];

// Function to add task
function addTask(task) {
    taskList.push(task);
    localStorage.setItem('taskList', JSON.stringify(taskList));
    updateTaskList();
}

// Function to update task list
function updateTaskList() {
    const taskListElement = document.getElementById('task-list');
    taskListElement.innerHTML = '';
    taskList.forEach((task, index) => {
        const taskElement = document.createElement('li');
        taskElement.textContent = task;
        taskListElement.appendChild(taskElement);
    });
}

// Function to delete task
function deleteTask(index) {
    taskList.splice(index, 1);
    localStorage.setItem('taskList', JSON.stringify(taskList));
    updateTaskList();
}

// Function to update task
function updateTask(index, task) {
    taskList[index] = task;
    localStorage.setItem('taskList', JSON.stringify(taskList));
    updateTaskList();
}

// Event listener for add task button
document.getElementById('add-task-btn').addEventListener('click', (e) => {
    e.preventDefault();
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value.trim();
    if (task) {
        addTask(task);
        taskInput.value = '';
    }
});

// Event listener for task list
document.getElementById('task-list').addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        const index = Array.prototype.indexOf.call(e.target.parentNode.children, e.target);
        deleteTask(index);
    }
});

// Event listener for task update
document.getElementById('task-list').addEventListener('dblclick', (e) => {
    if (e.target.tagName === 'LI') {
        const index = Array.prototype.indexOf.call(e.target.parentNode.children, e.target);
        const task = prompt('Masukkan tugas baru:', e.target.textContent);
        if (task) {
            updateTask(index, task);
        }
    }
});

// Initialize task list
updateTaskList();
