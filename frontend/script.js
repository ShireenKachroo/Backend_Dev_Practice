const API_URL = "http://127.0.0.1:8000";

let currentUser = null;


async function login() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    });

    const data = await response.json();

    if (!response.ok) {
        document.getElementById("login-message").textContent =
            data.detail || "Login failed";

        return;
    }

    localStorage.setItem("access_token", data.access_token);

    await loadCurrentUser();
}


async function loadCurrentUser() {

    const token = localStorage.getItem("access_token");

    const response = await fetch(`${API_URL}/auth/me`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (!response.ok) {
        logout();
        return;
    }

    currentUser = await response.json();

    document.getElementById("login-section")
        .classList.add("hidden");

    document.getElementById("dashboard-section")
        .classList.remove("hidden");

    document.getElementById("welcome-message").textContent =
        `Logged in as ${currentUser.username} (${currentUser.role})`;

    if (currentUser.role === "admin") {
        document.getElementById("admin-section")
            .classList.remove("hidden");
    }

    loadStudents();
}


async function loadStudents() {

    const token = localStorage.getItem("access_token");

    const response = await fetch(`${API_URL}/students/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (!response.ok) {
        return;
    }

    const students = await response.json();

    const table = document.getElementById("student-table");

    table.innerHTML = "";

    students.forEach(student => {

        const row = document.createElement("tr");

        let actions = "";

        if (currentUser.role === "admin") {
            actions = `
                <button
                    class="delete-button"
                    onclick="deleteStudent(${student.id})"
                >
                    Delete
                </button>
            `;
        }

        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.department_id}</td>
            <td>${actions}</td>
        `;

        table.appendChild(row);
    });
}


async function addStudent() {

    const token = localStorage.getItem("access_token");

    const id = Number(
        document.getElementById("student-id").value
    );

    const name =
        document.getElementById("student-name").value;

    const department_id = Number(
        document.getElementById("department-id").value
    );

    const response = await fetch(`${API_URL}/students/`, {
        method: "POST",

        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },

        body: JSON.stringify({
            id: id,
            name: name,
            department_id: department_id
        })
    });

    const data = await response.json();

    if (!response.ok) {

        document.getElementById("student-message").textContent =
            data.detail || "Failed to add student";

        return;
    }

    document.getElementById("student-message").textContent =
        "Student added successfully.";

    document.getElementById("student-id").value = "";
    document.getElementById("student-name").value = "";
    document.getElementById("department-id").value = "";

    loadStudents();
}


async function deleteStudent(studentId) {

    const token = localStorage.getItem("access_token");

    const response = await fetch(
        `${API_URL}/students/${studentId}`,
        {
            method: "DELETE",

            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    );

    if (!response.ok) {
        const data = await response.json();

        alert(data.detail || "Failed to delete student");

        return;
    }

    loadStudents();
}


function logout() {

    localStorage.removeItem("access_token");

    currentUser = null;

    document.getElementById("dashboard-section")
        .classList.add("hidden");

    document.getElementById("login-section")
        .classList.remove("hidden");

    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
}


window.onload = function () {

    const token = localStorage.getItem("access_token");

    if (token) {
        loadCurrentUser();
    }
};