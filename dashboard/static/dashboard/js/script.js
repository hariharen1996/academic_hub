document.addEventListener("DOMContentLoaded", (e) => {
  const profileBtn = document.querySelector(".create-profile");

  setTimeout(() => {
    const message = document.querySelectorAll(".alert-message");
    message.forEach((items) => {
      items.style.opacity = 0;
      items.style.transition = "opacity 1s ease";
      setTimeout(() => {
        items.style.display = "none";
      }, 1000);
    });
  }, 3000);
});

profileBtn.addEventListener("click", () => {
  let profileImg = document.querySelector(".profile-img");
  profileImg.classList.add("highlight-profile");

  const toggleNav = document.querySelector(".navbar-toggler");

  if (window.innerWidth < 992) {
    if (toggleNav.getAttribute("aria-expanded") === "false") {
      toggleNav.click();
    }
  }
  setTimeout(() => {
    profileImg.classList.remove("highlight-profile");
    toggleNav.getAttribute("aria-expanded") === "true";
  }, 5000);
});
