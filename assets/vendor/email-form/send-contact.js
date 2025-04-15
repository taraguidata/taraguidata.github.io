document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");

  if (!form) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const thisForm = this;
    const formData = new FormData(thisForm);

    thisForm.querySelector(".loading").classList.add("d-block");
    thisForm.querySelector(".error-message").classList.remove("d-block");
    thisForm.querySelector(".sent-message").classList.remove("d-block");

    fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData).toString(),
    })
      .then((response) => {
        thisForm.querySelector(".loading").classList.remove("d-block");
        if (response.ok) {
          thisForm.querySelector(".sent-message").classList.add("d-block");
          thisForm.reset();
        } else {
          return response.text().then((text) => {
            throw new Error(text);
          });
        }
      })
      .catch((error) => {
        thisForm.querySelector(".error-message").innerHTML = error.message;
        thisForm.querySelector(".error-message").classList.add("d-block");
      });
  });
});
