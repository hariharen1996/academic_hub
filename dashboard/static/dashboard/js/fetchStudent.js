const container = document.querySelector(".student-lists-container");

const url = "http://127.0.0.1:8000/api/students/";

function displayStudents(data) {
  //console.log(data)
  let dom = "";

  data.forEach((student) => {
    dom += `<a href="students/${
      student.id
    }" class="navigate-details text-decoration-none text-black">
                <div class="student-card">
                    <div class="image-container">
                        ${
                          student.student_image
                            ? `<img src="${student.student_image}" alt="${student.name}" class="student-profile-img" />`
                            : `<img src="../../../media/default_pic.png" alt="${student.name}" class="student-profile-img" />`
                        }
                    </div>
                    <div class="card-content">
                        <h1 class="text-black">${student.name}</h1>
                        <p class="text-black">${student.roll_no}</p>
                    </div>
                </div>
            </a>`;
  });

  //console.log(dom)
  container.innerHTML = dom;
}

async function fetchStudents() {
  try {
    const response = await fetch(url);
    const data = await response.json();

    if (!data || !Array.isArray(data)) return;

    displayStudents(data);

    //console.log(data)
  } catch (err) {
    console.log(err.message);
  }
}

window.addEventListener("DOMContentLoaded", fetchStudents);
