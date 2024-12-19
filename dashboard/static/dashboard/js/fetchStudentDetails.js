const studDetailsContainer = document.querySelector(".student-details");

const id = window.location.pathname.split("/")[2];
console.log(id);
const u = `http://127.0.0.1:8000/api/students/${id}/`;

function displayStudentDetails(data) {
  if (!data) {
    studDetailsContainer.innerHTML = "<p>No student data found.</p>";
    return;
  }
  //console.log(data)

  const defaultImage = "../../../media/default_pic.png";
  const studentImage = data.student_image || defaultImage;

  studDetailsContainer.innerHTML = `
        <h2 class="mb-4">Student Details</h2>
        <div class="table-responsive">
            <table class="table table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Field</th>
                        <th scope="col">Details</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Student Image</strong></td>
                        <td><img src="${studentImage}" alt="Student Image" width="100"></td>
                    </tr>
                    <tr>
                        <td><strong>Name</strong></td>
                        <td>${data.name}</td>
                    </tr>
                    <tr>
                        <td><strong>Roll No</strong></td>
                        <td>${data.roll_no}</td>
                    </tr>
                    <tr>
                        <td><strong>Course</strong></td>
                        <td>${data.course}</td>
                    </tr>
                    <tr>
                        <td><strong>Email</strong></td>
                        <td>${data.email}</td>
                    </tr>
                    <tr>
                        <td><strong>Address</strong></td>
                        <td>${data.address}</td>
                    </tr>
                    <tr>
                        <td><strong>Phone</strong></td>
                        <td>${data.phone}</td>
                    </tr>
                    <tr>
                        <td><strong>Marks</strong></td>
                        <td>${data.marks}</td>
                    </tr>
                    <tr>
                        <td><strong>Subjects</strong></td>
                        <td>
                            <ul>
                                ${data.subjects
                                  .map((subject) => `<li>${subject}</li>`)
                                  .join("")}
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td><strong>Bookmarked</strong></td>
                        <td>${data.bookmarked ? "Yes" : "No"}</td>
                    </tr>
                    <tr>
                        <td><strong>Date</strong></td>
                        <td>${data.date}</td>
                    </tr>
                    <tr>
                        <td><strong>Time</strong></td>
                        <td>${data.time}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    `;
}

async function fetchStudentDetails() {
  try {
    const response = await fetch(u);
    const data = await response.json();

    if (!data) return;

    console.log(data);

    displayStudentDetails(data);
  } catch (err) {
    console.log(err.message);
  }
}

window.addEventListener("DOMContentLoaded", fetchStudentDetails);
