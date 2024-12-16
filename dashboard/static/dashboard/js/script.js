document.addEventListener("DOMContentLoaded", (e) => {
  setTimeout(() => {
    const message = document.querySelectorAll(".alert-message");
    message.forEach((items) => {
      items.style.opacity = 0;
      items.style.transition = 'opacity 1s ease'
      setTimeout(() => {
        items.style.display = "none";
      }, 1000);
    });
  }, 3000);
});
